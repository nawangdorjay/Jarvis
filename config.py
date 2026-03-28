"""Configuration for JARVIS"""
import os

LLM_CONFIG = {
    "local": {
        "provider": "ollama",
        "model": "llama3",
        "url": "http://localhost:11434"
    },
    "cloud": {
        "provider": "openai",
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY")
    },
    "fallback_to_cloud": True
}

VOICE_CONFIG = {
    "stt_provider": "whisper",
    "tts_provider": "tts",
    "language": "en"
}

N8N_CONFIG = {
    "webhook_url": os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook"),
    "api_key": os.getenv("N8N_API_KEY", "")
}