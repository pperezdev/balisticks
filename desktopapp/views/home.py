import tkinter as tk

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
