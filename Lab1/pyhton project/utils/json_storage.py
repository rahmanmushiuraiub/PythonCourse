import json
import os

class JsonStorage:
    """Handle JSON file storage operations"""
    
    def __init__(self, filename: str = "tasks.json", username: str = None):
        self.base_filename = filename
        self.username = username
        # Create user-specific filename
        if username:
            self.filename = f"tasks_{username}.json"
        else:
            self.filename = filename
    
    def set_username(self, username: str):
        """Set username for user-specific storage"""
        self.username = username
        self.filename = f"tasks_{username}.json"
    
    def load(self) -> dict:
        """Load data from JSON file"""
        if not os.path.exists(self.filename):
            return {'tasks': [], 'next_id': 1}
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {'tasks': [], 'next_id': 1}
    
    def save(self, data: dict):
        """Save data to JSON file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
