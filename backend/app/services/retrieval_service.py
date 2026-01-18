from typing import List, Any, Dict, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timezone
from sqlalchemy.orm import selectinload
from app.models.document import Chunk
from app.services.vector_store import vector_store

class RetrievalService:
    async def search_memories(
        self, 
        query: str, 
        user_id: int, 
        db: AsyncSession, 
        top_k: int = 5,
        view: str = "auto"
    ) -> List[Dict[str, Any]]:
        """
        Search for relevant artifacts using the specified View.
        Views:
        - semantic: Vector Search (Default)
        - state: Fact Store Lookup (Current Truth)
        - episodic: Time-based Memory Log
        - auto: Hybrid (Logic to select best view, currently defaults to semantic+state)
        """
        if view == "state":
            return await self._search_state(query, user_id, db, top_k)
        elif view == "episodic":
            return await self._search_episodic(query, user_id, db, top_k)
        elif view == "semantic":
            return await self._search_semantic(query, user_id, db, top_k)
        else:
            # Auto: Run Semantic + small State check
            # For now, let's just do Semantic mixed with State
            state_results = await self._search_state(query, user_id, db, top_k=3)
            semantic_results = await self._search_semantic(query, user_id, db, top_k=top_k)
            
            # Meritocratic Merge? Or State on top?
            # Proposition 5: "State beats similarity"
            # So we prepend State results.
            return state_results + semantic_results

    async def _search_state(self, query: str, user_id: int, db: AsyncSession, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Search for current truths (Facts) using Hybrid Strategy:
        1. Semantic Search (Vector Store) -> Finds "parade" from "procession"
        2. Keyword Search (SQL) -> Finds exact matches
        3. Merge & Rank (Semantic + Recency)
        """
        from app.models.fact import Fact
        from sqlalchemy import or_
        import re

        semantic_fact_ids = []
        fact_score_map = {} # Map ID -> Vector Distance/Score

        try:
             # 1. Semantic Search (Vector Store) - Primary Matcher
             # Fetch more candidates to allow for filtering
             vector_results = await vector_store.query(
                 query_texts=query, # Fixed typo from query_text
                 n_results=top_k * 4, 
                 where={"user_id": str(user_id), "type": "fact"} 
             )
             
             if vector_results and vector_results.get("ids"):
                 for i, rid in enumerate(vector_results["ids"][0]):
                     # rid format: "fact_123"
                     if rid.startswith("fact_"):
                         try:
                             fid = int(rid.split("_")[1])
                             semantic_fact_ids.append(fid)
                             # Store distance/score if needed for ranking
                             # pinecone returns similarity (higher = better? or distance?)
                             # Assuming score from vector_store wrapper is useful
                             dist = vector_results["distances"][0][i] if vector_results.get("distances") else 0
                             fact_score_map[fid] = dist
                         except:
                             pass
        except Exception as e:
             # Soft fail if vector search unavailable
             print(f"Vector search for facts failed: {e}")
             return []

        if not semantic_fact_ids:
            return []

        # 2. SQL Hydration (Get actual Fact objects)
        # We ONLY fetch what Vector Store found. No fuzzy keyword search.
        filters = [
            Fact.user_id == user_id, 
            Fact.valid_until == None,
            Fact.is_superseded == False,
            Fact.id.in_(semantic_fact_ids)
        ]
        
        # Fetch Facts with Eager Loading of Chunk for context
        stmt = select(Fact).options(selectinload(Fact.chunk)).where(*filters)
        result = await db.execute(stmt)
        facts = result.scalars().all()
        
        # 3. Ranking
        ranked_facts = []
        for f in facts:
            score = f.confidence or 1.0
            
            # Vector Score Boost
            # Use the score from Vector Store if available, or rank index
            if f.id in fact_score_map:
                # Map vector score directly? 
                # Or use rank-based boost as before (more stable)
                rank_idx = semantic_fact_ids.index(f.id)
                score += 2.0 - (rank_idx * 0.1)
                
                # Optional: Add raw vector score?
                # score += fact_score_map[f.id] * 0.5 
 
            
            # Recency Boost (User Request: "recent one should be given more score")
            # Logic: Add up to +0.5 score for facts within last 30 days.
            # Decay: +0.1 for facts within last year.
            # Formula: 1 / (1 + log(days + 1))? 
            # Simple Linear Bonus:
            if f.valid_from:
                # Ensure timezone awareness (valid_from is usually tz-aware in model, but verify)
                vf = f.valid_from
                if vf.tzinfo is None:
                    vf = vf.replace(tzinfo=timezone.utc)
                
                # Compare to Now (UTC)
                now = datetime.now(timezone.utc)
                age_delta = now - vf
                days_old = max(0, age_delta.days)
                
                # Bonus for very recent (Active Memory context)
                if days_old < 30:
                    score += 0.5
                elif days_old < 90:
                    score += 0.3
                elif days_old < 365:
                    score += 0.1
                
                # Tie-breaker logic mainly, but here it's additive.
                # Also slight penalty for VERY old facts? 
                # No, just bonus for recent.

            ranked_facts.append((f, score))
            
        # Sort: Score DESC, ValidFrom DESC, ID DESC
        ranked_facts.sort(key=lambda x: (x[1], x[0].valid_from or datetime.min, x[0].id), reverse=True)
        
        # Format Results with Deduplication and Cleanup
        from difflib import SequenceMatcher
        from app.models.fact import Fact
        from sqlalchemy import update

        results = []
        seen_facts = [] # List of {'text': str, 'valid_from': datetime}
        facts_to_supersede = []
        
        for f, score in ranked_facts[:top_k * 2]:
            date_str = ""
            if f.valid_from:
                local_dt = f.valid_from.astimezone()
                date_str = f"[{local_dt.strftime('%Y-%m-%d')}] "
            
            text = f"{date_str}{f.subject} {f.predicate} {f.object}"
            norm_text = f"{f.subject} {f.predicate} {f.object}".lower().strip()
            
            # Fuzzy Deduplication Check
            is_duplicate = False
            for seen in seen_facts:
                # Check 1: Exact Date Match (as requested)
                if seen['valid_from'] == f.valid_from:
                    # Check 2: Content Match > 90%
                    similarity = SequenceMatcher(None, norm_text, seen['norm_text']).ratio()
                    if similarity > 0.9:
                        is_duplicate = True
                        facts_to_supersede.append(f.id)
                        break
            
            if is_duplicate:
                continue
                
            seen_facts.append({
                'text': text, 
                'norm_text': norm_text,
                'valid_from': f.valid_from
            })
            
            if len(results) >= top_k:
                # If we filled the quota, subsequent items are just dropped, NOT superseded (we haven't compared them fully)
                # Actually, duplicate detection relies on seeing the "better" one first.
                # Since we sorted by Score, we kept the best.
                # Remaining items in ranked_facts (beyond loop) are ignored.
                break

            results.append({
                "text": text,
                "score": score,
                "metadata": {
                    "type": "fact",
                    "fact_id": f.id,
                    "confidence": f.confidence,
                    "valid_from": str(f.valid_from),
                    "semantic_match": f.id in semantic_fact_ids
                },
                "chunk": f.chunk
            })
            
        # Passive Cleanup: Mark duplicates as superseded
        if facts_to_supersede:
             print(f"Retrieval Cleanup: Marking {len(facts_to_supersede)} redundant facts as superseded.")
             try:
                 stmt = update(Fact).where(Fact.id.in_(facts_to_supersede)).values(is_superseded=True)
                 await db.execute(stmt)
                 await db.commit()
             except Exception as e:
                 print(f"Cleanup Failed: {e}")

        return results

    async def _search_episodic(self, query: str, user_id: int, db: AsyncSession, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Search Memories primarily by time/recency matching query constraints?
        For now: Keyword search on Memories, sorted by created_at DESC.
        """
        from app.models.memory import Memory
        from sqlalchemy import text # For full text if available or simple like
        
        # Naive: Just simple LIKE query
        stmt = select(Memory).where(
            Memory.user_id == user_id, 
            Memory.content.ilike(f"%{query}%")
        ).order_by(Memory.created_at.desc()).limit(top_k)
        
        result = await db.execute(stmt)
        memories = result.scalars().all()
        
        results = []
        for m in memories:
            results.append({
                "text": m.content,
                "score": 1.0, # Valid hit
                "metadata": {
                    "type": "memory",
                    "memory_id": m.id,
                    "created_at": str(m.created_at),
                    "title": m.title
                },
                "chunk": None
            })
        return results

    async def _search_semantic(self, query: str, user_id: int, db: AsyncSession, top_k: int = 5) -> List[Dict[str, Any]]:
        # 1. MMR Fetch: Get more candidates than needed (4x)
        fetch_k = top_k * 10
        
        # 2. Vector Search (with embeddings for MMR)
        results = await vector_store.query(
            query, 
            n_results=fetch_k, 
            where={"user_id": user_id},
            include_values=True # Required for MMR
        )
        
        if not results["ids"] or not results["ids"][0]:
            return []
            
        # Extract candidates
        candidate_ids = results["ids"][0]
        candidate_embeddings = results["embeddings"][0]
        candidate_metadatas = results["metadatas"][0]
        candidate_distances = results["distances"][0] if results["distances"] else [0.0] * len(candidate_ids)
        candidate_docs = results["documents"][0]
        
        # MMR Logic
        import numpy as np
        
        def cosine_similarity(a, b):
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

        selected_indices = []
        candidate_indices = list(range(len(candidate_ids)))
        
        lambda_mult = 0.3 # 0.3 = Favor Diversity (Suppress Duplicates)
        
        seen_texts = set()
        
        # Greedy Selection loop
        for _ in range(min(top_k, len(candidate_ids))):
            best_score = -float("inf")
            best_idx = -1
            
            for i in candidate_indices:
                if i in selected_indices:
                    continue
                
                # Hard Dedupe: Check Text Similarity
                text_content = candidate_docs[i].strip() if candidate_docs[i] else ""
                
                # Fuzzy Match Check (sim > 0.9)
                is_duplicate = False
                for seen in seen_texts:
                    # Quick length check optimization
                    if abs(len(text_content) - len(seen)) > len(text_content) * 0.2:
                        continue
                        
                    # Calculate similarity (Jaccard or simple word overlap for speed?)
                    # Let's use simple token overlap for speed
                    s1 = set(text_content.lower().split())
                    s2 = set(seen.lower().split())
                    if not s1 or not s2: continue
                    overlap = len(s1.intersection(s2)) / len(s1.union(s2))
                    
                    if overlap > 0.85: # 85% word overlap = duplicate
                        # print(f"Skipping duplicate: {text_content[:30]}... (Overlap: {overlap:.2f})")
                        is_duplicate = True
                        break
                
                if is_duplicate:
                    continue

                # Relevance (Sim(Di, Q))
                relevance = candidate_distances[i] 
                
                # Diversity (max Sim(Di, Dk) for all k in selected)
                max_sim_to_selected = 0.0
                if selected_indices:
                    vec_i = np.array(candidate_embeddings[i])
                    sims = []
                    for j in selected_indices:
                        vec_j = np.array(candidate_embeddings[j])
                        sims.append(cosine_similarity(vec_i, vec_j))
                    max_sim_to_selected = max(sims) if sims else 0.0
                
                mmr_score = (lambda_mult * relevance) - ((1 - lambda_mult) * max_sim_to_selected)
                
                if mmr_score > best_score:
                    best_score = mmr_score
                    best_idx = i
            
            if best_idx != -1:
                selected_indices.append(best_idx)
                # Add to seen
                best_text = candidate_docs[best_idx].strip() if candidate_docs[best_idx] else ""
                seen_texts.add(best_text)

        # Filter candidates to selected ones
        top_ids = [candidate_ids[i] for i in selected_indices]
        # Re-map metadatas/docs for the next steps
        
        # 3. Fetch Rich Metadata from DB (Chunks)
        # Use top_ids (which are now MMR selected)
        
        # Async fetch with Eager Loading for Recency Calculation
        query_stmt = (
            select(Chunk)
            .options(selectinload(Chunk.memory), selectinload(Chunk.document))
            .where(Chunk.embedding_id.in_(top_ids))
        )
        db_res = await db.execute(query_stmt)
        chunks = db_res.scalars().all()
        chunk_map = {c.embedding_id: c for c in chunks}
        
        formatted_results = []
        
        for i, idx_in_original in enumerate(selected_indices):
            emb_id = candidate_ids[idx_in_original]
            distance = candidate_distances[idx_in_original] # This is relevance score
            base_score = distance # Already cosine similarity
            
            chunk = chunk_map.get(emb_id)
            
            if chunk:
                # 3. Apply Re-ranking modifiers
                feedback_mod = 1 + (chunk.feedback_score or 0.0)
                trust_mod = chunk.trust_score or 0.5
                
                # Recency Logic
                recency_mod = 1.0
                created_at = None
                if chunk.memory:
                    created_at = chunk.memory.created_at
                elif chunk.document:
                    created_at = chunk.document.created_at
                
                if created_at:
                    # ensure timezone awareness
                    if created_at.tzinfo is None:
                        created_at = created_at.replace(tzinfo=timezone.utc)
                    
                    now = datetime.now(timezone.utc)
                    days_diff = (now - created_at).days
                    # Boost: +10% for today/yesterday, decays to ~0% after a month
                    # Formula: 1 + (0.1 / max(1, days_diff))
                    recency_mod = 1 + (0.1 / max(1, days_diff))
                
                final_score = base_score * feedback_mod * (0.5 + trust_mod) * recency_mod
                
                # Enrich response
                # Fetch meta from original results using index
                meta = candidate_metadatas[idx_in_original]
                meta["summary"] = chunk.summary
                meta["generated_qas"] = chunk.generated_qas
                meta["trust_score"] = chunk.trust_score
                meta["memory_id"] = chunk.id # Add DB ID for reference
                meta["recency_boost"] = round(recency_mod, 2)
                
                # Prepend Date if available
                # date_prefix = ""
                # if created_at:
                #      date_prefix = f"[{created_at.strftime('%Y-%m-%d')}] "

                formatted_results.append({
                    "text": chunk.text, # Return DB text which is reliable
                    "score": final_score,
                    "metadata": meta,
                    "chunk": chunk # Return actual chunk object if needed
                })
            else:
                # Fallback if DB sync issue
                meta = candidate_metadatas[idx_in_original]
                formatted_results.append({
                    "text": candidate_docs[idx_in_original],
                    "score": base_score,
                    "metadata": meta,
                    "chunk": None
                })
                
        # Sort by final score desc
        formatted_results.sort(key=lambda x: x["score"], reverse=True)
        
        return formatted_results

retrieval_service = RetrievalService()
