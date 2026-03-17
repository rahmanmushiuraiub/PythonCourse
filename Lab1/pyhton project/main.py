
class TaskManagerApp():
    def_init_(self):
        self.title("Task Manager")
        width = 900
        height = 600
        self.geometry(f"{width}x{height}")
        self.task_list_view.pack(fill="both", expand=True)
        