from src.memory.chroma_client import ChromaClient
import logging
class MemoryAgent:
    def __init__(self):
        self.chroma_client = ChromaClient()
        self.status = "idle"
    def store(self, evaluation):
        try:
            # Store learning in ChromaDB
            document = f"Hypothesis: [H]. Variant: [V]. Result: [R]. Learning: [L]."
            metadata = {
                "experiment_id": "exp_123",
                "metric": "signup_conversion",
                "lift_pct": evaluation["lift_pct"],
                "confidence": evaluation["confidence_pct"],
                "date": "2026-01-01"
            }
            self.chroma_client.add_document(document, metadata)
            self.status = "stored"
            logging.info("Learning stored in memory")
        except Exception as e:
            logging.error(f"Error in memory agent: {str(e)}")
            raise
    def get_status(self):
        return self.status
