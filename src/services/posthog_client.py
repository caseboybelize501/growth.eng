import requests
import logging
class PostHogClient:
    def __init__(self, api_key, project_id):
        self.api_key = api_key
        self.project_id = project_id
        self.base_url = "https://app.posthog.com/api"
    def get_metrics(self):
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(f"{self.base_url}/projects/{self.project_id}/insights", headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"PostHog API error: {response.status_code}")
        except Exception as e:
            logging.error(f"Error fetching metrics from PostHog: {str(e)}")
            raise
