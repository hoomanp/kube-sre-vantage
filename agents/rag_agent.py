import chromadb
from litellm import embedding

class RAGAgent:
    """
    RAG Agent to index and retrieve context for SLO/SLA calculations.
    It indexes SLA documentation and historical incident reports.
    """
    def __init__(self, collection_name="sre_knowledge_base"):
        self.client = chromadb.Client() # In-memory for demo, can be persistent
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_knowledge(self, documents, metadatas, ids):
        """Adds SLA docs or incident history to the vector DB."""
        # Simple implementation using ChromaDB's default embedding function
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def retrieve_context(self, query, n_results=3):
        """Retrieves the most relevant SRE/SLA context for a given query."""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []

# Example usage (commented out for actual implementation)
# agent = RAGAgent()
# agent.add_knowledge(["Availability SLA for Tier-0 services is 99.9% per month.", 
#                    "Previous incident INC-102 showed high latency due to DB shard 4."],
#                    [{"type": "SLA"}, {"type": "Incident"}], ["doc1", "doc2"])
