import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from .summary import init_summary


class CreateProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.entry_values = []
        self.init_data()
        self.create_widget()


    def init_data(self):
        self.tagstype = []
        self.datetype = []
        try:
            data = self.controller.back.get_data("organisations")
            self.organisation.extend(data)
        except:
            #tk.messagebox.showwarning("API", "Error 200")
            ...

    def create_widget(self):
        label = ttk.Label(self, text=f"Creer votre projet", font=self.controller.title_font).grid(row=0,
                                                                                                  column=2,
                                                                                                  sticky='w')
        organisation_name_label = ttk.Label(self, text="Nom")
        organisation_name_label.grid(row=2, column=2, sticky='w')

        organisation_name_entry = tk.Entry(self)
        organisation_name_entry.grid(row=3, column=2, sticky='w')

        variableOrganisation = tk.StringVar()
        organisation = ["Organisation 1", "Organisation 2", "Organisation 3", "Organisation 4"]
        variableOrganisation.set(organisation[0])

        # --------------------------------------------------
        #               Create Label
        # --------------------------------------------------

        ttk.Label(self, text="Description").grid(row=4, column=2, sticky='w')
        ttk.Label(self, text="Organisations").grid(row=6, column=2, sticky='w')

        # --------------------------------------------------
        #               Create Entry
        # --------------------------------------------------

        description = tk.Entry(self)
        description.grid(row=5, column=2, sticky='w')

        self.entryOrganisation = tk.OptionMenu(self, variableOrganisation, *organisation)
        self.entryOrganisation.grid(row=7, column=2, sticky='w')

        # --------------------------------------------------
        #               Placement of objects
        # --------------------------------------------------

        ttk.Button(self, text="create",
                   command=lambda: push(self)).grid(row=12, column=2, sticky='w')

        init_summary(self, ttk)

        self.entry_values.extend([variableOrganisation, organisation_name_entry, description])

    def validation(self):
        """
        Regarde si les champs sont vides ou pas
        Si vide sort une erreur sinon insert dans la base de donnes
        :return:
        """

        tab = []
        tab.append(self.controller.user['id'])

        for entrie in self.entry_values:
            if not entrie.get():  # si vide
                return False, "entry is empty"
            tab.append(entrie.get())

        print("Je suis le tab", tab)

        self.controller.back.insert_project(tab)

        return True, "Votre projet est créer"


def push(self):
    m = self.controller.mother(self)

    if (m):
        self.controller.show_frame("ProjectPage")
