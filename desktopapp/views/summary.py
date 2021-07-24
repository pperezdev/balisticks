
def init_summary(self, ttk):
    sep = ttk.Separator(self, orient='vertical').grid(column=1, row=0, rowspan=10, sticky='ns')

    balisticks = ttk.Label(self, text="Balisticks", font=(self.controller.title_font, 20)).grid(row=0, column=0,
                                                                                                sticky='w')

    button_tasks = ttk.Button(self, text="Vos sticks",
                                      command=lambda: self.controller.show_frame("TaskPage"))

    button_tasks.grid(row=1, column=0, sticky='w')

    button_organisations = ttk.Button(self, text="Vos organisations",
                                      command=lambda: self.controller.show_frame("OrganisationPage"))
    button_organisations.grid(row=2, column=0, sticky='w')

    button_projects = ttk.Button(self, text="vos projets",
                                      command=lambda: self.controller.show_frame("ProjectPage"))
    button_projects.grid(row=3, column=0, sticky='w')

    your_profile = ttk.Button(self, text="votre profil",
                              command=lambda: self.controller.show_frame("HomePage"))
    your_profile.grid(row=4, column=0, sticky='w')

    button_disconnection = ttk.Button(self, text="Deconnection",
                                      command=lambda: self.controller.show_frame("ConnexionPage"))
    button_disconnection.grid(row=5, column=0, sticky='w')
