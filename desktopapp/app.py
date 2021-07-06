import tkinter as tk
from tkinter import font as tkfont
from desktopapp.views import connexion, home, inscription
from desktopapp.config import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.grid(row=0, column=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (connexion.ConnexionPage, home.HomePage, inscription.InscirptionPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ConnexionPage")
        self.defineGeometry(600, 600, 600, 600  )


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



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
