"""n8n Webhook Integration"""
import requests
from config import N8N_CONFIG

class N8NClient:
    def __init__(self):
        self.webhook_url = N8N_CONFIG["webhook_url"]
        self.api_key = N8N_CONFIG["api_key"]
    
    def trigger(self, payload: dict) -> dict:
        """Trigger an n8n webhook"""
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            return {"status": response.status_code, "response": response.json()}
        except Exception as e:
            return {"status": "error", "message": str(e)}