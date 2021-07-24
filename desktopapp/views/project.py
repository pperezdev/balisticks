import tkinter as tk
from tkinter import ttk
from .summary import init_summary

class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = "Benjamin"
        self.init_data()
        self.create_widget()

    def init_data(self):
        self.organisations = []
        try:
            self.organisations.extend(["AA","BPojet","Cfzfez"])
            #setup API
        except:
            ttk.showerror.showwarning("API", "Error 200")

    def create_widget(self):
        label = ttk.Label(self, text=f"Vos projets", font=self.controller.title_font).grid(row=0,
                                                                                                      column=2,
                                                                                                      sticky='w')
        init_summary(self, ttk)

        for cnt, org in enumerate(self.organisations):
            ttk.Button(self, text=f"{org}",
                       command=lambda: self.controller.show_frame("TaskPage")).grid(row=cnt+1, column=2, sticky='w')

        ttk.Button(self, text="nouveau projet",
                   command=lambda: self.controller.show_frame("CreateProjectPage")).grid(row=cnt + 2, column=2, sticky='w')