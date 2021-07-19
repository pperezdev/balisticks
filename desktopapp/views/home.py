import tkinter as tk
from tkinter import ttk



class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bienvenue sur la page", font=controller.title_font)
        label.grid(row=2, column=0)
        label.grid_rowconfigure(1, weight=1)
        label.grid_columnconfigure(1, weight=1)
        button = tk.Button(self, text="Dectionner",
                           command=lambda: controller.show_frame("ConnexionPage"))
        button.grid()

        self.create_widget()

    def create_widget(self):
        ttk.Separator(self, orient='vertical').place(relheight=1.0)
        balisticks = tk.Label(self, text="Balisiticks", font = (self.controller.title_font,20)).grid(row=0, column=0, sticky='w')

        your_profile = tk.Button(self,text="Your Profile").grid(row=2, column=0, sticky='w')
        #about = tk.Button(self, text = "About").grid(row=3, column=0, sticky='w')

