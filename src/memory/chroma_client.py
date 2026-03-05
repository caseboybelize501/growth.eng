import chromadb
from chromadb.config import Settings
import logging
class ChromaClient:
    def __init__(self):
        self.client = chromadb.Client(Settings(persist_directory="./chroma_data"))
        try:
            self.collection = self.client.get_collection(name="growth_learnings")
        except:
            self.collection = self.client.create_collection(name="growth_learnings")
    def add_document(self, document, metadata):
        try:
            self.collection.add(
                documents=[document],
                metadatas=[metadata],
                ids=[f"doc_{len(self.collection.get())}"]
            )
        except Exception as e:
            logging.error(f"Error adding document to Chroma: {str(e)}")
    def get_documents(self):
        try:
            return self.collection.get()
        except Exception as e:
            logging.error(f"Error retrieving documents from Chroma: {str(e)}")
