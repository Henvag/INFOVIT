#Eg brukar "customtkinter" biblioteket for å bygge ein GUI som ser moderne ut.
#Den er basert og bygd oppå "tkinter" og har litt meir funksjonalitetar.
#For å installere "customtkinter" biblioteket må du skrive "pip install customtkinter" i terminalen.
#Eg har sett på dokumentasjonen  og tatt utgangspunkt i den.

#Link til all nødvendig informasjon om biblioteket: https://github.com/TomSchimansky/CustomTkinter


"""
Oppgåve 1: 

Først importerer eg "customtkinter" biblioteket/modulen .
Deretter brukar eg to funksjonar for å endre utseende på GUI'en der du kan spesifisere fargen som parameter.

"Root" lagar ein instans av "CTk" klassen som er hovudvindauget i GUI'en.
Eg brukar "geometry" metoden for å sette storleiken/oppløysninga på vindauget. Med andre ord "parent widget" (https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/)

Funskjonen "lukk_applikasjon" lukkar applikasjonen når den blir kalla på. Det blir gjort med den innebygde "destroy" metoden i "tkinter" (https://www.geeksforgeeks.org/destroy-method-in-tkinter-python/).

"Frame" lagar ein instans av "CTkFrame" klassen som er eit vindauge inni hovudvindauget. Parameterene bestemmer størrelsen.
Eg brukar "pack" metoden for å plassere "frame" i hovudvindauget. Med andre ord putter eg "child widget" inni "parent widget" (https://www.geeksforgeeks.org/python-pack-method-in-tkinter/).

"Overskrift" lagar ein instans av "CTkLabel" klassen som er ein tekst som blir vist i GUI'en. Parameterene bestemmer teksten og fonten. 
Dette blir og gjort med "pack" metoden. Overskrifta blir plassert i "frame" fordi "frame" er "parent widget" og "overskrift" er "child widget".

"farvel_knapp" lagar ein instans av "CTkButton" klassen som er ein knapp som blir vist i GUI'en. Parameterene bestemmer teksten og kva som skal skje når knappen blir trykt på.
I dette tilfellet blir "lukk_applikasjon" funksjonen kalla på når knappen blir trykt på. Dette blir og gjort med "pack" metoden. Knappen blir plassert i "frame" fordi "frame" er "parent widget" og "farvel_knapp" er "child widget".

"root.mainloop()" er ei løkke som held GUI'en oppe til den blir lukka. Den blir lukka når "lukk_applikasjon" funksjonen blir kalla på.




Oppgåve 2:


Eg lagar eit ny instans av hovudvindauget for å lage ein ny GUI ettersom den forrige er ferdig.
Variabelen "counter" skal halde på verdien til knappen.
 
Funksjonen "increment_counter" aukar verdien til "counter" variabelen med 1 og oppdaterer teksten til knappen. (https://coderslegacy.com/python/tkinter-config/).
Den hentar den globale variabelen "counter" og aukar verdien med 1. Deretter oppdaterer den teksten til knappen med den nye verdien til "counter" variabelen.

"Frame" lagar ein instans av "CTkFrame" klassen som er eit vindauge inni hovudvindauget. Parameterene bestemmer størrelsen.
Eg brukar "pack" metoden for å plassere "frame" i hovudvindauget. Med andre ord putter eg "child widget" inni "parent widget" (https://www.geeksforgeeks.org/python-pack-method-in-tkinter/).

"Overskrift" lagar ein instans av "CTkLabel" klassen som er ein tekst som blir vist i GUI'en. Parameterene bestemmer teksten og fonten. 
Dette blir og gjort med "pack" metoden. Overskrifta blir plassert i "frame" fordi "frame" er "parent widget" og "overskrift" er "child widget".


"verdiauking_knapp" lagar ein instans av "CTkButton" klassen som er ein knapp som blir vist i GUI'en. Parameterene bestemmer teksten og kva som skal skje når knappen blir trykt på.
I dette tilfellet blir "verdiauking_telling" funksjonen kalla på når knappen blir trykt på. Dette blir og gjort med "pack" metoden. Knappen blir plassert i "frame" fordi "frame" er "parent widget" og "farvel_knapp" er "child widget".

"root.mainloop()" er ei løkke som held GUI'en oppe til den blir lukka. 



"""


import customtkinter

customtkinter.set_appearance_mode("dark") #Eg set utseende til "dark" for å få ein mørk bakgrunn
customtkinter.set_default_color_theme("dark-blue") #Eg set farge tema til "dark-blue" for å få ein mørk blå farge på knappane


root = customtkinter.CTk() #Hovudvindauget i GUI'en
root.geometry("500x350")


def lukk_applikasjon(): #Lukkar applikasjonen
    root.destroy()



frame = customtkinter.CTkFrame(master=root) #Vindauge inni hovudvindauget 
frame.pack(pady=20, padx=60, fill="both", expand=True)

overskrift = customtkinter.CTkLabel(master=frame, text="Trykk på knappen", font=("Roboto", 24)) #Overskrift i GUI'en
overskrift.pack(pady=12, padx=10)

farvel_knapp = customtkinter.CTkButton(master=frame, text="Farvel", command=lukk_applikasjon) #Knapp som lukkar applikasjonen
farvel_knapp.pack(pady=12, padx=10)


root.mainloop()












root = customtkinter.CTk() #Hovudvindauget i GUI'en
root.geometry("500x350")

counter = 0 #Knapp verdi

def verdiauking_telling(): #Funksjon som aukar verdien til "counter" variabelen med 1 og oppdaterer teksten til knappen
    global counter
    counter += 1
    verdiauking_knapp.configure(text=str(counter))

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

overskrift = customtkinter.CTkLabel(master=frame, text="Trykk på knappen", font=("Roboto", 24)) #Overskrift i GUI'en
overskrift.pack(pady=12, padx=10)

verdiauking_knapp = customtkinter.CTkButton(master=frame, text="0", command=verdiauking_telling) #Knapp som aukar verdien til "counter" variabelen med 1 og oppdaterer teksten til knappen
verdiauking_knapp.pack(pady=12, padx=10)

root.mainloop() #Løkke som held GUI'en oppe til den blir lukka

