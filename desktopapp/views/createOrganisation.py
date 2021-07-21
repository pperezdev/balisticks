import tkinter as tk
from tkinter import ttk
from .summary import init_summary

class CreateOrganisationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = "Benjamin"
        self.init_data()
        self.create_widget()

    def init_data(self):
        self.tagstype = []
        self.datetype = []
        try:
            self.tagstype.extend(["A","B","C"])
            self.datetype.extend(["A", "B", "C"])
            #setup API
            # Get Tag Type
            # Get Date type
        except:
            ttk.showerror.showwarning("API", "Error 200")

    def create_widget(self):
        label = ttk.Label(self, text=f"Creer votre organisation", font=self.controller.title_font).grid(row=0,
                                                                                                      column=2,
                                                                                                      sticky='w')

        ttk.Button(self, text="create",
                   command=lambda: self.controller.show_frame("OrganisationPage")).grid(row=5, column=2, sticky='w')
        init_summary(self, ttk)

