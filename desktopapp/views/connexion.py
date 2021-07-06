import tkinter as tk


class ConnexionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Connexion",
                            command=self.connexion)
        button2 = tk.Button(self, text="Inscription",
                            command=self.inscription)
        button1.pack()
        button2.pack()

    def connexion(self):
        self.controller.show_frame("HomePage")

    def inscription(self):
        self.controller.show_frame("InscirptionPage")
