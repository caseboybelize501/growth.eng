from src.agents.observe_agent import ObserveAgent
from src.agents.hypothesis_agent import HypothesisAgent
from src.agents.copywriter_agent import CopywriterAgent
from src.agents.deploy_agent import DeployAgent
from src.agents.monitor_agent import MonitorAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.memory_agent import MemoryAgent
from src.models import Experiment, Variant, Learning
from datetime import datetime
import logging
class GrowthOrchestrator:
    def __init__(self):
        self.observe_agent = ObserveAgent()
        self.hypothesis_agent = HypothesisAgent()
        self.copywriter_agent = CopywriterAgent()
        self.deploy_agent = DeployAgent()
        self.monitor_agent = MonitorAgent()
        self.evaluator_agent = EvaluatorAgent()
        self.memory_agent = MemoryAgent()
        self.last_run = None
    def run_pipeline(self):
        try:
            logging.info("Starting autonomous growth loop")
            metrics = self.observe_agent.observe()
            hypotheses = self.hypothesis_agent.reason(metrics)
            variants = self.copywriter_agent.reason(hypotheses)
            deployed = self.deploy_agent.act(variants)
            results = self.monitor_agent.act(deployed)
            evaluation = self.evaluator_agent.evaluate(results)
            self.memory_agent.store(evaluation)
            self.last_run = datetime.now().isoformat()
            logging.info("Autonomous growth loop completed")
        except Exception as e:
            logging.error(f"Error in autonomous loop: {str(e)}")
    def get_status(self):
        return {
            "last_run": self.last_run,
            "observe_agent": self.observe_agent.get_status(),
            "hypothesis_agent": self.hypothesis_agent.get_status(),
            "copywriter_agent": self.copywriter_agent.get_status(),
            "deploy_agent": self.deploy_agent.get_status(),
            "monitor_agent": self.monitor_agent.get_status(),
            "evaluator_agent": self.evaluator_agent.get_status(),
            "memory_agent": self.memory_agent.get_status()
        }
    def get_experiments(self):
        return []  # Placeholder
    def get_learnings(self):
        return []  # Placeholder
    def set_config(self, config):
        pass  # Placeholder
