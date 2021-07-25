import re
import tkinter as tk
from tkinter import font as tkfont
from views import connexion, home, inscription, organisation, task, project, createOrganisation, createProject, createTask
from config import *
from services.back import back
import datetime

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.user = {
            "id": 0,
            "pseudo": "",
            "name": "",
            "surname": "",
            "mail": "",
            "phone": "",
            "password": "",
            "birthday": "2021-07-25 18:49:28.055818",
            "picture": "nothing",
            "banner": "nothing",
            "inscriptiondate": datetime.datetime.now()
        }
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.grid(row=0, column=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.back = back()

        self.frames = {}
        for F in (connexion.ConnexionPage, home.HomePage, inscription.InscirptionPage,
                  organisation.OrganisationPage, project.ProjectPage, task.TaskPage,
                  createOrganisation.CreateOrganisationPage, createProject.CreateProjectPage,
                  createTask.CreateTaskPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ConnexionPage")
        self.defineGeometry(600, 600, 600, 600)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        self.setTitle(page_name)

    def defineGeometry(self, width, height, width_max, height_max):
        self.width = width
        self.height = height
        self.width_max = width_max
        self.height_max = height_max

        self.geometry(f"{self.width}x{self.height}")
        self.minsize(self.width, self.height)
        self.maxsize(self.width_max, self.height_max)

    def setTitle(self, title):
        self.title(f"{APP_NAME} - {title[:-4]}")

    def browseButton(self):
        return tk.filedialog.askdirectory()

    def mother(self, view):
        valid, message = view.validation()
        if valid:
            tk.messagebox.showinfo("", message)
            return True
        else:
            tk.messagebox.showerror('error', message)
            return False

    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(regex, email):
            return False, "Adress e-mail is not correct "
        return True, ""

    def check_number(self, phone_number):
        pattern = re.compile(r'^[0-9]{10}$')
        if not re.match(pattern, phone_number):
            return False, "Phone number is not correct "
        return True, ""

    def insertion_database(self):
        return

    # fonction qui permet de vérifier l'insertion, une autre permettant d'ajouter dans la database
    # et la dernière une fonction mère qui lance le tout


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
