"""Voice Agent - Speech I/O"""
import sys

class VoiceAgent:
    def __init__(self):
        self.name = "Voice"
        self.listening = False
    
    def speak(self, text: str) -> None:
        """Text to speech"""
        print(f"🤖 JARVIS: {text}")
    
    def listen(self) -> str:
        """Speech to text (placeholder)"""
        return "Voice input not available in CLI mode"
    
    def activate(self) -> None:
        """Activate voice mode"""
        self.listening = True
        self.speak("Voice mode activated")
    
    def deactivate(self) -> None:
        """Deactivate voice mode"""
        self.listening = False