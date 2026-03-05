import requests
from src.services.llama import LLaMAService
from src.models import Hypothesis
import json
import logging
class HypothesisAgent:
    def __init__(self):
        self.llama_service = LLaMAService()
        self.status = "idle"
    def reason(self, metrics):
        try:
            prompt = f"You are a growth engineer. Current metrics: Signup conversion: {metrics['signup_conversion']}% (was {metrics['previous_week_rate']}% last week, delta: {metrics['delta']}%). Top drop-off point: {metrics['conversion_dropoff']}. Page: {metrics['page']}. Past experiments that worked: [MEMORY_RESULTS] Generate 3 ranked A/B test hypotheses. Return JSON: {{\"hypotheses\":[{{\"rank\":1,\"hypothesis\":\"...\",\"rationale\":\"...\",\"predicted_lift_pct\":0,\"test_element\":\"headline|cta|hero|pricing|social_proof\"}}]}}"
            response = self.llama_service.generate(prompt, temperature=0.7, max_tokens=1024)
            hypotheses_data = json.loads(response)
            hypotheses = [Hypothesis(**h) for h in hypotheses_data["hypotheses"]]
            self.status = "reasoned"
            logging.info(f"Generated hypotheses: {len(hypotheses)}")
            return hypotheses
        except Exception as e:
            logging.error(f"Error in hypothesis agent: {str(e)}")
            raise
    def get_status(self):
        return self.status
