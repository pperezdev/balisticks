import tkinter as tk

class InscirptionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("ConnexionPage"))
        button.pack()



    def forms(self):
        a = tk.Label(self.frame, text="First Name").grid(row=0, column=0)


