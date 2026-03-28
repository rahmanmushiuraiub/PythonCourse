from datetime import datetime
from typing import Optional

class Task:
    """Task data model"""
    
    def __init__(self, task_id: int, title: str, priority: str, 
                 deadline: str, status: str = "Pending"):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.status = status
    
    def to_dict(self) -> dict:
        """Convert task to dictionary"""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'priority': self.priority,
            'deadline': self.deadline,
            'status': self.status
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Task':
        """Create task from dictionary"""
        return Task(
            task_id=data['task_id'],
            title=data['title'],
            priority=data['priority'],
            deadline=data['deadline'],
            status=data['status']
        )
