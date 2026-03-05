import requests
from src.services.llama import LLaMAService
from src.models import Variant
import json
import logging
class CopywriterAgent:
    def __init__(self):
        self.llama_service = LLaMAService()
        self.status = "idle"
    def reason(self, hypotheses):
        try:
            variants = []
            for i, hypothesis in enumerate(hypotheses):
                prompt = f"Write A/B test copy for: {hypothesis.test_element} on {hypothesis.page}. Hypothesis: {hypothesis.hypothesis}. Product: [PRODUCT_DESC]. Audience: [ICP]. Current copy: [CURRENT]. Return JSON: {{\"control\":{{\"text\":\"...\",\"rationale\":\"...\"}},\"variant_a\":{{\"text\":\"...\",\"rationale\":\"...\"}},\"variant_b\":{{\"text\":\"...\",\"rationale\":\"...\"}}}}"
                response = self.llama_service.generate(prompt, temperature=0.85, max_tokens=1024)
                variant_data = json.loads(response)
                variant = Variant(
                    experiment_id=hypothesis.id,
                    control_text=variant_data["control"]["text"],
                    variant_a_text=variant_data["variant_a"]["text"],
                    variant_b_text=variant_data["variant_b"]["text"]
                )
                variants.append(variant)
            self.status = "reasoned"
            logging.info(f"Generated variants: {len(variants)}")
            return variants
        except Exception as e:
            logging.error(f"Error in copywriter agent: {str(e)}")
            raise
    def get_status(self):
        return self.status
