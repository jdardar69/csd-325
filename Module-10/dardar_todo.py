import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = [] if not tasks else tasks

        # Colors to match the assignment example (purple + yellow)
        PURPLE = "#7a1cff"
        YELLOW = "#f2d200"
        APP_BG = "#e6e6e6"

        # Window
        self.title("Dardar-ToDo")
        self.geometry("320x450")
        self.configure(bg=APP_BG)

        # Menu (File -> Exit)
        self.menu_bar = tk.Menu(
            self,
            bg=PURPLE,
            fg=YELLOW,
            activebackground=YELLOW,
            activeforeground="black"
        )
        self.file_menu = tk.Menu(
            self.menu_bar,
            tearoff=0,
            bg=PURPLE,
            fg=YELLOW,
            activebackground=YELLOW,
            activeforeground="black"
        )
        self.file_menu.add_command(label="Exit", command=self.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # Layout: canvas + scrollbar + task frame
        self.tasks_canvas = tk.Canvas(self, highlightthickness=0, bg=APP_BG)
        self.tasks_frame = tk.Frame(self.tasks_canvas, bg=APP_BG)
        self.text_frame = tk.Frame(self, bg=APP_BG)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        # Instruction label (required)
        self.instructions = tk.Label(
            self.tasks_frame,
            text="--- Add Items Here ---  |  Right-click a task to delete",
            bg=PURPLE,
            fg="white",
            pady=10
        )
        self.instructions.pack(side=tk.TOP, fill=tk.X)

        # Text entry at bottom
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Alternating task colors (purple/yellow like screenshot)
        self.colour_schemes = [
            {"bg": YELLOW, "fg": "black"},
            {"bg": PURPLE, "fg": "white"},
        ]

        # Event binds
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Mouse wheel scroll support
        self.bind_all("<MouseWheel>", self.mouse_scroll)   # Windows/macOS
        self.bind_all("<Button-4>", self.mouse_scroll)     # Linux up
        self.bind_all("<Button-5>", self.mouse_scroll)     # Linux down

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if task_text:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)

            # Right-click deletes a task (required)
            new_task.bind("<Button-3>", self.remove_task)

            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)
        return "break"

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            if task in self.tasks:
                self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, style = divmod(position, 2)
        scheme = self.colour_schemes[style]
        task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        self.tasks_canvas.itemconfig(self.canvas_frame, width=event.width)

    def mouse_scroll(self, event):
        if getattr(event, "delta", 0):
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            self.tasks_canvas.yview_scroll(1 if event.num == 5 else -1, "units")


if __name__ == "__main__":
    Todo().mainloop()
