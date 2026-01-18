import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.vector_store import vector_store

def delete_all_pinecone_records():
    """Delete all records from Pinecone index"""
    try:
        # Get index stats to confirm what we're about to delete
        stats = vector_store.index.describe_index_stats()
        total_vectors = stats.get('total_vector_count', 0)
        
        print(f"Current Pinecone index contains {total_vectors} vectors.")
        
        if total_vectors == 0:
            print("No vectors found in the index.")
            return
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete ALL {total_vectors} vectors from Pinecone? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return
        
        # Delete all vectors by deleting everything in the namespace
        # If you don't use namespaces, pass delete_all=True
        vector_store.index.delete(delete_all=True)
        
        print(f"Successfully deleted all vectors from Pinecone index.")
        
        # Verify deletion
        stats_after = vector_store.index.describe_index_stats()
        remaining = stats_after.get('total_vector_count', 0)
        print(f"Remaining vectors: {remaining}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_all_pinecone_records()
