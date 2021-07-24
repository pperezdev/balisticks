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
        varGender = tk.StringVar()

        # --------------------------------------------------
        #               Creation of a list based on a file
        # --------------------------------------------------
        countries = []  # creation of the list of countries
        variableCountry = tk.StringVar()
        fileCountries = open('data/countries.txt', 'r')
        for country in fileCountries:
            country = country.rstrip("\n")
            countries.append(country[3:])
        variableCountry.set(countries[0])

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
            variable=varGender,
            value='Male',
            font=('Times', 10),

        )

        female_rb = tk.Radiobutton(
            gender_frame,
            text='Female',
            bg='#CCCCCC',
            variable=varGender,
            value='Female',
            font=('Times', 10),

        )

        register_country = tk.OptionMenu(
            self,
            variableCountry,
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
            command= lambda: self.controller.mother(self)
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

        # var.set('Male')
        print(varGender.get())

        gender_frame.grid(row=5, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=tk.LEFT)
        female_rb.pack(expand=True, side=tk.LEFT)

        self.entry_values.extend([register_first_name, register_last_name, register_email, register_mobile, varGender,
                                  variableCountry, register_pwd, pwd_again])

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

        if tab[6] != tab[7]:
            return False, "The password is not the same"

        val, message = self.controller.check_email(tab[2])
        if not val : return val, message

        val, message = self.controller.check_number(tab[3])
        if not val: return val, message

        print("Je suis le tab", tab)

        self.controller.back.insert_users(tab)

        return True, "Votre compte est créer"
