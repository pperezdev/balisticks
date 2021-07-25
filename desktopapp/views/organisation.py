import tkinter as tk
from tkinter import ttk
from .summary import init_summary

class OrganisationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.init_data()
        self.create_widget()

    def init_data(self):
        self.organisations = []
        try:
            data = self.controller.back.get_data("organisations")
            self.organisations.extend(data)
        except:
            # tk.messagebox.showwarning("API", "Error 200")
            ...

    def create_widget(self):
        label = ttk.Label(self, text=f"Vos organisations", font=self.controller.title_font).grid(row=0,
                                                                                                      column=2,
                                                                                                      sticky='w')
        init_summary(self, ttk)

        cnt = 0

        for cnt, org in enumerate(self.organisations):
            ttk.Button(self, text=f"{org}",
                       command=lambda: self.controller.show_frame("ProjectPage")).grid(row=cnt+1, column=2, sticky='w')

        ttk.Button(self, text="nouvelle organisation",
                   command=lambda: self.controller.show_frame("CreateOrganisationPage")).grid(row=cnt + 2, column=2, sticky='w')