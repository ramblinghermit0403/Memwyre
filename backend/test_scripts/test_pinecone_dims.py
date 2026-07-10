"""Check Pinecone index dimensions."""
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.core.config import settings
from pinecone import Pinecone

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

# Describe main index
idx = pc.Index(host=settings.PINECONE_HOST)
stats = idx.describe_index_stats()
print(f"Main index (PINECONE_HOST): dimension={stats.dimension}, total_vectors={stats.total_vector_count}")

# Describe sparse index if available
if settings.PINECONE_SPARSE_HOST:
    idx2 = pc.Index(host=settings.PINECONE_SPARSE_HOST)
    stats2 = idx2.describe_index_stats()
    print(f"Sparse index (PINECONE_SPARSE_HOST): dimension={stats2.dimension}, total_vectors={stats2.total_vector_count}")
