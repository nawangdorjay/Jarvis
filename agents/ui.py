"""UI Agent - XR Interface"""
class UIAgent:
    def __init__(self):
        self.panels = []
    
    def create_panel(self, name: str, content: dict) -> None:
        """Create a floating UI panel"""
        self.panels.append({"name": name, "content": content})
    
    def show_panel(self, name: str) -> dict:
        """Show a panel"""
        for panel in self.panels:
            if panel["name"] == name:
                return panel
        return None
    
    def list_panels(self) -> list:
        """List all panels"""
        return [p["name"] for p in self.panels]