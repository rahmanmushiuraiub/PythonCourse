import customtkinter as ctk
from tkinter import messagebox

class TaskListView(ctk.CTkFrame):
    """Task list dashboard view"""
    
    def __init__(self, parent, on_add, on_edit, on_delete, on_refresh):
        super().__init__(parent)
        self.on_add = on_add
        self.on_edit = on_edit
        self.on_delete = on_delete
        self.on_refresh = on_refresh
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the UI components"""
        # Title
        title = ctk.CTkLabel(self, text="Task Manager Dashboard", 
                            font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=20)
        
        # Search and filter frame
        filter_frame = ctk.CTkFrame(self)
        filter_frame.pack(fill="x", padx=20, pady=10)
        
        # Search box
        ctk.CTkLabel(filter_frame, text="Search:").grid(row=0, column=0, padx=5, pady=5)
        self.search_entry = ctk.CTkEntry(filter_frame, width=200)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        self.search_entry.bind('<KeyRelease>', lambda e: self.on_refresh())
        
        # Status filter
        ctk.CTkLabel(filter_frame, text="Status:").grid(row=0, column=2, padx=5, pady=5)
        self.status_filter = ctk.CTkComboBox(filter_frame, 
                                             values=["All", "Pending", "Completed"],
                                             command=lambda x: self.on_refresh())
        self.status_filter.set("All")
        self.status_filter.grid(row=0, column=3, padx=5, pady=5)
        
        # Priority filter
        ctk.CTkLabel(filter_frame, text="Priority:").grid(row=0, column=4, padx=5, pady=5)
        self.priority_filter = ctk.CTkComboBox(filter_frame,
                                               values=["All", "Low", "Medium", "High"],
                                               command=lambda x: self.on_refresh())
        self.priority_filter.set("All")
        self.priority_filter.grid(row=0, column=5, padx=5, pady=5)
        
        # Task list frame with scrollbar
        list_frame = ctk.CTkFrame(self)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Headers
        headers = ["ID", "Title", "Priority", "Deadline", "Status"]
        header_frame = ctk.CTkFrame(list_frame)
        header_frame.pack(fill="x", padx=5, pady=5)
        
        widths = [50, 300, 100, 120, 100]
        for i, (header, width) in enumerate(zip(headers, widths)):
            label = ctk.CTkLabel(header_frame, text=header, width=width,
                               font=ctk.CTkFont(weight="bold"))
            label.grid(row=0, column=i, padx=5, pady=5)
        
        # Scrollable frame for tasks
        self.scrollable_frame = ctk.CTkScrollableFrame(list_frame, height=300)
        self.scrollable_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Button frame
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(button_frame, text="Add Task", command=self.on_add,
                     fg_color="green", hover_color="darkgreen").pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Edit Task", command=self.handle_edit).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Delete Task", command=self.handle_delete,
                     fg_color="red", hover_color="darkred").pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Refresh", command=self.on_refresh).pack(side="left", padx=5)
        
        self.selected_task_id = None
        self.task_frames = {}
    
    def display_tasks(self, tasks):
        """Display tasks in the list"""
        # Clear existing tasks
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.task_frames.clear()
        widths = [50, 300, 100, 120, 100]
        
        for task in tasks:
            task_frame = ctk.CTkFrame(self.scrollable_frame)
            task_frame.pack(fill="x", pady=2)
            
            # Store reference to frame
            self.task_frames[task.task_id] = task_frame
            
            # Make frame clickable
            task_frame.bind("<Button-1>", lambda e, tid=task.task_id, frame=task_frame: self.select_task(tid, frame))
            task_frame.bind("<Double-Button-1>", lambda e, tid=task.task_id: self.on_edit(tid))
            
            values = [str(task.task_id), task.title, task.priority, task.deadline, task.status]
            
            for i, (value, width) in enumerate(zip(values, widths)):
                label = ctk.CTkLabel(task_frame, text=value, width=width, anchor="w")
                label.grid(row=0, column=i, padx=5, pady=5)
                label.bind("<Button-1>", lambda e, tid=task.task_id, frame=task_frame: self.select_task(tid, frame))
                label.bind("<Double-Button-1>", lambda e, tid=task.task_id: self.on_edit(tid))
    
    def select_task(self, task_id, clicked_frame):
        """Select a task and highlight it"""
        self.selected_task_id = task_id
        
        # Reset all frames to default color
        for frame in self.task_frames.values():
            frame.configure(fg_color=("gray90", "gray20"))
        
        # Highlight selected frame
        clicked_frame.configure(fg_color=("lightblue", "darkblue"))
    
    def handle_edit(self):
        """Handle edit button click"""
        if self.selected_task_id:
            self.on_edit(self.selected_task_id)
        else:
            messagebox.showwarning("No Selection", "Please select a task to edit")
    
    def handle_delete(self):
        """Handle delete button click"""
        if self.selected_task_id:
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
                self.on_delete(self.selected_task_id)
        else:
            messagebox.showwarning("No Selection", "Please select a task to delete")
    
    def get_search_query(self):
        """Get search query"""
        return self.search_entry.get()
    
    def get_status_filter(self):
        """Get status filter"""
        return self.status_filter.get()
    
    def get_priority_filter(self):
        """Get priority filter"""
        return self.priority_filter.get()
