import requests
import json
import time
import logging
class LLaMAService:
    def __init__(self, base_url="http://llama:8000"):
        self.base_url = base_url
    def generate(self, prompt, temperature=0.7, max_tokens=1024):
        try:
            payload = {
                "prompt": prompt,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            response = requests.post(f"{self.base_url}/generate", json=payload)
            if response.status_code == 200:
                result = response.json()
                return result["response"]
            else:
                raise Exception(f"LLaMA API error: {response.status_code}")
        except Exception as e:
            logging.error(f"Error calling LLaMA service: {str(e)}")
            raise
