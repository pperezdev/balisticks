import tkinter as tk
from tkinter import ttk
from .summary import init_summary
from tkcalendar import *


class CreateTaskPage(tk.Frame):

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
            self.tagstype.extend(["A", "B", "C"])
            self.datetype.extend(["A", "B", "C"])
            # setup API
            # Get Tag Type
            # Get Date type
        except:
            ttk.showerror.showwarning("API", "Error 200")

    def create_widget(self):
        label = ttk.Label(self, text=f"Creer votre STICKS", font=self.controller.title_font).grid(row=0,
                                                                                                  column=2,
                                                                                                  sticky='w')
        organisation_name_label = ttk.Label(self, text="Nom")
        organisation_name_label.grid(row=2, column=2, sticky='w')

        organisation_name_entry = tk.Entry(self)
        organisation_name_entry.grid(row=3, column=2, sticky='w')

        variableTask = tk.StringVar()
        task_priority = ["Option 1", "Option 2", "Option 3", "Option 4"]
        variableTask.set(task_priority[0])

        # --------------------------------------------------
        #               Create Label
        # --------------------------------------------------

        ttk.Label(self, text="Libelle").grid(row=4, column=2, sticky='w')
        ttk.Label(self, text="Date Debut").grid(row=6, column=2, sticky='w')
        ttk.Label(self, text="Date fin").grid(row=8, column=2, sticky='w')
        #ttk.Label(self, text="Collaborate").grid(row=10, column=2, sticky='w')
        ttk.Label(self, text="Priorité de la task").grid(row=13, column=2, sticky='w')

        # --------------------------------------------------
        #               Create Entry
        # --------------------------------------------------

        libelle = tk.Entry(self)
        dateDebut = Calendar(self, selectmode = 'day',
               year = 2021, month = 7,
               day = 22, width=15)
        dateFin = Calendar(self, selectmode = 'day',
               year = 2021, month = 7,
               day = 22, width=15)
        #collaborate = tk.Entry(self)
        entryTaskPriotite = tk.OptionMenu(self, variableTask, *task_priority)

        # --------------------------------------------------
        #               Placement of objects
        # --------------------------------------------------

        libelle.grid(row=5, column=2)
        dateDebut.grid(row=7, column=2, pady=10)
        dateFin.grid(row=9, column=2, pady=10)
        #collaborate.grid(row=11, column=2)
        entryTaskPriotite.grid(row=13, column=2)

        ttk.Button(self, text="create",
                   command=lambda: push(self)).grid(row=20, column=2, sticky='w')

        init_summary(self, ttk)

        self.entry_values.extend([organisation_name_entry, libelle, dateFin,
                                  dateFin, variableTask])

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
            #tab.append(entrie)

        print("Je suis le tab", tab)

        self.controller.back.insert_organisation(tab)

        return True, "Votre sticks est créer"


def push(self):
    m = self.controller.mother(self)
    if (m):
        self.controller.show_frame("TaskPage")
