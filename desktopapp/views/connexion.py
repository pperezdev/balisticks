import tkinter as tk


class ConnexionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text='Balisticks', font=controller.title_font).grid(row=0, column=1)

        button1 = tk.Button(self, text="Connexion",
                            command=self.connexion,width=15,height=2)
        button2 = tk.Button(self, text="Inscription",
                            command=self.inscription,width=15,height=2)

        button1.grid(row=10, column=1)
        button2.grid(row=11, column=1)

        self.create_widget()

    def connexion(self):
        self.controller.show_frame("HomePage")

    def inscription(self):
        self.controller.show_frame("InscirptionPage")


    def create_widget(self):
        login = tk.Entry(self).grid(row=6, column=1)
        password = tk.Entry(self).grid(row=7, column=1, pady=10, padx=20)







