import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("500x350")


def lukk_applikasjon():
    root.destroy()



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

overskrift = customtkinter.CTkLabel(master=frame, text="Trykk på knappen", font=("Roboto", 24))
overskrift.pack(pady=12, padx=10)

farvel_knapp = customtkinter.CTkButton(master=frame, text="Farvel", command=lukk_applikasjon)
farvel_knapp.pack(pady=12, padx=10)


root.mainloop()


