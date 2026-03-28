import customtkinter as ctk
from controllers.task_manager import TaskManager
from utils.json_storage import JsonStorage
from views.task_list_view import TaskListView
from views.task_form_view import TaskFormView

class TaskManagerApp(ctk.CTk):
    """Main application controller"""
    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Task Manager")
        self.geometry("900x600")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize storage and manager
        self.storage = JsonStorage("tasks.json")
        self.task_manager = TaskManager(self.storage)
        
        # Create task list view
        self.task_list_view = TaskListView(
            self,
            on_add=self.show_add_task,
            on_edit=self.show_edit_task,
            on_delete=self.delete_task,
            on_refresh=self.refresh_tasks
        )
        self.task_list_view.pack(fill="both", expand=True)
        
        # Initial load
        self.refresh_tasks()
    
    def refresh_tasks(self):
        """Refresh task list with filters"""
        # Get filters
        search_query = self.task_list_view.get_search_query()
        status_filter = self.task_list_view.get_status_filter()
        priority_filter = self.task_list_view.get_priority_filter()
        
        # Apply filters
        tasks = self.task_manager.get_all_tasks()
        
        if search_query:
            tasks = [t for t in tasks if search_query.lower() in t.title.lower()]
        
        if status_filter != "All":
            tasks = [t for t in tasks if t.status == status_filter]
        
        if priority_filter != "All":
            tasks = [t for t in tasks if t.priority == priority_filter]
        
        self.task_list_view.display_tasks(tasks)
    
    def show_add_task(self):
        """Show add task form"""
        TaskFormView(self, on_save=self.add_task)
    
    def show_edit_task(self, task_id):
        """Show edit task form"""
        task = self.task_manager.get_task_by_id(task_id)
        if task:
            TaskFormView(self, on_save=self.edit_task, task=task)
    
    def add_task(self, task_id, title, priority, deadline, status):
        """Add new task"""
        self.task_manager.add_task(title, priority, deadline, status)
        self.refresh_tasks()
    
    def edit_task(self, task_id, title, priority, deadline, status):
        """Edit existing task"""
        self.task_manager.edit_task(task_id, title, priority, deadline, status)
        self.refresh_tasks()
    
    def delete_task(self, task_id):
        """Delete task"""
        self.task_manager.delete_task(task_id)
        self.refresh_tasks()

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()
