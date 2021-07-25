import tkinter as tk
from tkinter import ttk
from .summary import init_summary


class TaskPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.init_data()
        self.create_widget()

    def init_data(self):
        self.tasks = []
        try:
            data = self.back.get_data("projects")
            self.tasks.extend(data)
        except:
            # tk.messagebox.showwarning("API", "Error 200")
            ...

    def create_widget(self):
        label = ttk.Label(self, text=f"Vos sticks", font=self.controller.title_font).grid(row=0, column=2, sticky='w')
        init_summary(self, ttk)

        for cnt, org in enumerate(self.tasks):
            ttk.Button(self, text=f"{org}",
                       command=lambda: self.controller.show_frame("TaskPage")).grid(row=cnt+1, column=2, sticky='w')

        ttk.Button(self, text="nouveau sticks",
                       command=lambda: self.controller.show_frame("CreateTaskPage")).grid(row=4, column=2,
                                                                                         sticky='w')
