from src.services.cms_client import CMSClient
import logging
class DeployAgent:
    def __init__(self):
        self.cms_client = CMSClient()
        self.status = "idle"
    def act(self, variants):
        try:
            deployed = []
            for variant in variants:
                result = self.cms_client.deploy_variant(variant)
                deployed.append(result)
            self.status = "deployed"
            logging.info(f"Deployed variants: {len(deployed)}")
            return deployed
        except Exception as e:
            logging.error(f"Error in deploy agent: {str(e)}")
            raise
    def get_status(self):
        return self.status
