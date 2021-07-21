import tkinter as tk
from tkinter import ttk
from .summary import init_summary

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = "Benjamin"
        self.create_widget()


    def create_widget(self):
        label = ttk.Label(self, text=f"Bienvenue {self.name}!", font=self.controller.title_font).grid(row=0,
                                                                                                      column=2,
                                                                                                      sticky='w')
        init_summary(self, ttk)

