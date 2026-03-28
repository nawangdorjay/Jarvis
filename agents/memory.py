"""Memory Agent - Context retention"""
class MemoryAgent:
    def __init__(self):
        self.context = {}
        self.history = []
    
    def store(self, key: str, value: any) -> None:
        """Store information in memory"""
        self.context[key] = value
        self.history.append({"action": "store", "key": key})
    
    def retrieve(self, key: str) -> any:
        """Retrieve from memory"""
        return self.context.get(key)
    
    def get_context(self) -> dict:
        """Get all context"""
        return self.context