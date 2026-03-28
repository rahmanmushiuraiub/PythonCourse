from typing import List, Optional
from models.task import Task
from utils.json_storage import JsonStorage

class TaskManager:
    """Controller for managing tasks"""
    
    def __init__(self, storage: JsonStorage):
        self.storage = storage
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from storage"""
        data = self.storage.load()
        self.tasks = [Task.from_dict(task_data) for task_data in data.get('tasks', [])]
        self.next_id = data.get('next_id', 1)
    
    def save_tasks(self):
        """Save tasks to storage"""
        data = {
            'tasks': [task.to_dict() for task in self.tasks],
            'next_id': self.next_id
        }
        self.storage.save(data)
    
    def add_task(self, title: str, priority: str, deadline: str, status: str = "Pending") -> Task:
        """Add new task"""
        task = Task(self.next_id, title, priority, deadline, status)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task
    
    def edit_task(self, task_id: int, title: str, priority: str, deadline: str, status: str):
        """Edit existing task"""
        task = self.get_task_by_id(task_id)
        if task:
            task.title = title
            task.priority = priority
            task.deadline = deadline
            task.status = status
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete task by ID"""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get task by ID"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.tasks
    
    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title"""
        query = query.lower()
        return [task for task in self.tasks if query in task.title.lower()]
    
    def filter_by_status(self, status: str) -> List[Task]:
        """Filter tasks by status"""
        if status == "All":
            return self.tasks
        return [task for task in self.tasks if task.status == status]
    
    def filter_by_priority(self, priority: str) -> List[Task]:
        """Filter tasks by priority"""
        if priority == "All":
            return self.tasks
        return [task for task in self.tasks if task.priority == priority]
    
    def get_report_data(self) -> dict:
        """Generate report data"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.status == "Completed"])
        pending = len([t for t in self.tasks if t.status == "Pending"])
        high_priority = len([t for t in self.tasks if t.priority == "High"])
        
        return {
            'total_tasks': total,
            'completed_tasks': completed,
            'pending_tasks': pending,
            'high_priority_tasks': high_priority
        }
