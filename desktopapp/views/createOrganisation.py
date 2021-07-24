import tkinter as tk
from tkinter import ttk
from .summary import init_summary

class CreateOrganisationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = "Benjamin"
        self.entry_values = []
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
        organisation_name_label = ttk.Label(self, text="Nom")
        organisation_name_label.grid(row=3, column=2, sticky='w')

        organisation_name_entry = tk.Entry(self)
        organisation_name_entry.grid(row=4, column=2, sticky='w')

        ttk.Button(self, text="create",
                   command=lambda: push(self)).grid(row=5, column=2, sticky='w')

        init_summary(self, ttk)

        self.entry_values.extend([organisation_name_entry])

    def validation(self):
        """
        Regarde si les champs sont vides ou pas
        Si vide sort une erreur sinon insert dans la base de donnes
        :return:
        """

        tab = []
        for entrie in self.entry_values:
            if not entrie.get():  # si vide
                return False, "entry is empty"
            tab.append(entrie.get())

        print("Je suis le tab", tab)

        self.controller.back.insert_organisation(tab)

        return True, "Votre organisation est créer"

def push(self):
    m = self.controller.mother(self)
    if(m):
        self.controller.show_frame("OrganisationPage")