import re
import tkinter as tk
from tkinter import messagebox


class InscirptionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font).grid(row=0, column=0)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("ConnexionPage"))
        button.grid(row=11, column=0, sticky='w')
        self.entry_values = []
        self.forms()

    def forms(self):

        # --------------------------------------------------
        #               Set value by default
        # --------------------------------------------------
        var = tk.StringVar()

        # --------------------------------------------------
        #               Creation of a list based on a file
        # --------------------------------------------------
        countries = []  # creation of the list of countries
        variable = tk.StringVar()
        fileCountries = open('data/countries.txt', 'r')
        for country in fileCountries:
            country = country.rstrip("\n")
            countries.append(country[3:])
        variable.set(countries[0])

        # --------------------------------------------------
        #               Create Label
        # --------------------------------------------------

        tk.Label(
            self,
            text="First Name",
            bg='#CCCCCC'
        ).grid(row=1, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Last Name",
            bg='#CCCCCC'
        ).grid(row=2, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Enter Email",
            bg='#CCCCCC'
        ).grid(row=3, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Contact Number",
            bg='#CCCCCC'
        ).grid(row=4, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Select Gender",
            bg='#CCCCCC'
        ).grid(row=5, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Select Country",
            bg='#CCCCCC'
        ).grid(row=6, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Enter Password",
            bg='#CCCCCC'
        ).grid(row=7, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self,
            text="Re-Enter Password",
            bg='#CCCCCC'
        ).grid(row=8, column=0, sticky=tk.W, pady=10)

        gender_frame = tk.LabelFrame(
            self,
            bg='#CCCCCC',
            padx=10,
            pady=10,
        )

        # --------------------------------------------------
        #               Create Entry
        # --------------------------------------------------
        register_first_name = tk.Entry(
            self
        )

        register_last_name = tk.Entry(self)

        register_email = tk.Entry(
            self
        )

        register_mobile = tk.Entry(
            self
        )

        male_rb = tk.Radiobutton(
            gender_frame,
            text='Male',
            bg='#CCCCCC',
            variable=var,
            value='Male',
            font=('Times', 10),

        )

        female_rb = tk.Radiobutton(
            gender_frame,
            text='Female',
            bg='#CCCCCC',
            variable=var,
            value='Female',
            font=('Times', 10),

        )

        register_country = tk.OptionMenu(
            self,
            variable,
            *countries
        )

        register_country.config(
            width=15,
        )
        register_pwd = tk.Entry(
            self,
            show='*'
        )
        pwd_again = tk.Entry(
            self,
            show='*'
        )

        register_btn = tk.Button(
            self,
            width=15,
            text='Register',
            relief=tk.SOLID,
            cursor='hand2',
            command=self.mother
        )

        # --------------------------------------------------
        #               Placement of objects
        # --------------------------------------------------

        register_first_name.grid(row=1, column=1, pady=10, padx=20)
        register_last_name.grid(row=2, column=1, pady=10, padx=20)
        register_email.grid(row=3, column=1, pady=10, padx=20)
        register_mobile.grid(row=4, column=1, pady=10, padx=20)
        register_country.grid(row=6, column=1, pady=10, padx=20)
        register_pwd.grid(row=7, column=1, pady=10, padx=20)
        pwd_again.grid(row=8, column=1, pady=10, padx=20)
        register_btn.grid(row=9, column=1, pady=10, padx=20)
        self.grid()

        #var.set('Male')
        print(var.get())

        gender_frame.grid(row=5, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=tk.LEFT)
        female_rb.pack(expand=True, side=tk.LEFT)

        self.entry_values.extend([register_first_name, register_last_name, register_email, register_mobile,var,
                                  register_pwd, pwd_again])

    def mother(self):
        if self.validation():
            messagebox.showinfo("", "All it's ok")
        else:
            messagebox.showerror('', 'Problem')

    def validation(self):
        """
        Regarde si les champs sont vides ou pas
        Si vide sort une erreur sinon insert dans la base de donnes
        :return:
        """

        tab = []
        for entrie in self.entry_values:
            if not entrie.get():  # si vide
                messagebox.showerror("Error", "is empty")
                return False
            tab.append(entrie.get())
        print("Je suis le tab",tab)
        if tab[5] != tab[6]:
            messagebox.showerror("Error password", "The password is not the same")
            return False

        self.check_email(tab[2])
        self.check_number(tab[3])

        return True

    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(regex, email):
            messagebox.showerror("Error", "Adress e-mail is not correct ")
            return False

    def check_number(self, phone_number):
        pattern = re.compile(r'^[0-9]{1,10}$')
        if not re.match(pattern, phone_number):
            messagebox.showerror("Error", "Phone number is not correct ")
            return False

    def insertion_database(self):
        return

    # fonction qui permet de vérifier l'insertion, une autre permettant d'ajouter dans la database
    # et la dernière une fonction mère qui lance le tout
