import math
from scipy import stats
import json
import logging
class EvaluatorAgent:
    def __init__(self):
        self.status = "idle"
    def evaluate(self, results):
        try:
            # Two-proportion z-test for statistical significance
            control_rate = results["control"]["conversion_rate"] / 100
            variant_a_rate = results["variant_a"]["conversion_rate"] / 100
            control_n = results["control"]["sample_size"]
            variant_a_n = results["variant_a"]["sample_size"]
            # Calculate z-score and p-value
            pooled_p = (control_rate * control_n + variant_a_rate * variant_a_n) / (control_n + variant_a_n)
            se = math.sqrt(pooled_p * (1 - pooled_p) * (1/control_n + 1/variant_a_n))
            z_score = (variant_a_rate - control_rate) / se
            p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
            # Determine winner
            if p_value < 0.05 and variant_a_rate > control_rate:
                winner = "variant_a"
                lift_pct = ((variant_a_rate - control_rate) / control_rate) * 100
            else:
                winner = "control"
                lift_pct = 0
            evaluation = {
                "winner": winner,
                "confidence_pct": (1 - p_value) * 100,
                "lift_pct": lift_pct,
                "recommendation": f"Winner: {winner}, Lift: {lift_pct:.2f}%"
            }
            self.status = "evaluated"
            logging.info(f"Evaluation completed: {evaluation}")
            return evaluation
        except Exception as e:
            logging.error(f"Error in evaluator agent: {str(e)}")
            raise
    def get_status(self):
        return self.status
