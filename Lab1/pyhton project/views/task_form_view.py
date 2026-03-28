import customtkinter as ctk
from tkinter import messagebox, Frame
from tkcalendar import DateEntry
from datetime import datetime

class TaskFormView(ctk.CTkToplevel):
    """Add/Edit task form view"""
    
    def __init__(self, parent, on_save, task=None):
        super().__init__(parent)
        self.on_save = on_save
        self.task = task
        
        self.title("Edit Task" if task else "Add Task")
        self.geometry("400x380")
        
        # Keep window on top
        self.transient(parent)
        self.grab_set()
        self.lift()
        self.focus_force()
        
        self.setup_ui()
        
        if task:
            self.populate_fields()
    
    def setup_ui(self):
        """Setup the UI components"""
        # Title
        title_text = "Edit Task" if self.task else "Add New Task"
        title = ctk.CTkLabel(self, text=title_text, 
                            font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=20)
        
        # Form frame
        form_frame = ctk.CTkFrame(self)
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Task Title
        ctk.CTkLabel(form_frame, text="Task Title:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.title_entry = ctk.CTkEntry(form_frame, width=250)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Priority
        ctk.CTkLabel(form_frame, text="Priority:").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.priority_combo = ctk.CTkComboBox(form_frame, values=["Low", "Medium", "High"], width=250)
        self.priority_combo.set("Medium")
        self.priority_combo.grid(row=1, column=1, padx=10, pady=10)
        
        # Deadline
        ctk.CTkLabel(form_frame, text="Deadline:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        
        # Create a frame to hold the DateEntry widget
        date_frame = Frame(form_frame, bg="#2b2b2b")
        date_frame.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # DateEntry calendar widget
        self.deadline_picker = DateEntry(
            date_frame,
            width=30,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='yyyy-mm-dd',
            font=('Arial', 10)
        )
        self.deadline_picker.pack()
        
        # Status
        ctk.CTkLabel(form_frame, text="Status:").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.status_combo = ctk.CTkComboBox(form_frame, values=["Pending", "Completed"], width=250)
        self.status_combo.set("Pending")
        self.status_combo.grid(row=3, column=1, padx=10, pady=10)
        
        # Buttons
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkButton(button_frame, text="Save", command=self.handle_save,
                     fg_color="green", hover_color="darkgreen").pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Cancel", command=self.destroy).pack(side="right", padx=5)
    
    def populate_fields(self):
        """Populate fields with task data"""
        if self.task:
            self.title_entry.insert(0, self.task.title)
            self.priority_combo.set(self.task.priority)
            
            # Set date in DateEntry
            try:
                date_obj = datetime.strptime(self.task.deadline, "%Y-%m-%d")
                self.deadline_picker.set_date(date_obj)
            except ValueError:
                pass
            
            self.status_combo.set(self.task.status)
    
    def handle_save(self):
        """Handle save button click"""
        title = self.title_entry.get().strip()
        priority = self.priority_combo.get()
        deadline = self.deadline_picker.get_date().strftime("%Y-%m-%d")
        status = self.status_combo.get()
        
        if not title:
            messagebox.showerror("Error", "Task title is required")
            return
        
        task_id = self.task.task_id if self.task else None
        self.on_save(task_id, title, priority, deadline, status)
        self.destroy()
