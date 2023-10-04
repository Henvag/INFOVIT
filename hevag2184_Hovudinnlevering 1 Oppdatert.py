# Oppgåve 1

# Importerer "math" modulen

# Definerer ein funskjon med navn "pi" med argumentet "d", setter det til 2.
# Du vil difor kun få 2 desimalar om du ikkje skriv noko inn i funksjonskallet

# Lagar ei "if" setning som seier at om verdien til "d" er større enn 16 (antall desimal i math.pi) vil du få printa ut ei feilmelding
# Deretter returnerer eg verdien til "math.pi"

# Så returnerer eg verdien av "math.pi" avrunda til "d" desimalar
# Til slutt printar eg ut funksjonen i terminalen som du kan endre på ved å skrive inn ulike tall i funksjonskallet.

# Fjern docstrings for å kjøre programmet



import math

"""

def pi(d=2):
    if d > 16:
        print("Feil: For mange desimalar.")
        return math.pi
    return round(math.pi, d)

# Her er ulike eksempel på korleis funskjonen fungera

print(pi(4)) #

print(pi(10))

print(pi(50))

print(pi())

"""


# Oppgåve 2

# Definerar funksjonen "temperaturKonvertering" med dei to ulike argumentene "temperatur" og "skala"

# Lagar "if" setning, viss skala er det same som "C", lagar variabelen "fahrenheit" som inneheld formelen for konvertering frå celsius til fahrenheit,
# Returnerar verdien for "fahrenheit"

# Lagar "elif" setning, viss skala er det same som "F", lagar variabelen "celsius" som inneheld formelen for konvertering frå fahrenheit til celsius
# Returnerar verdien for "celsius"

# Lagar "else" setning, printar ut ei feilmelding om du skriv inn noko anna enn "C" eller "F"

# Fjern docstrings for å kjøre programmet

"""

def temperaturKonvertering(temperatur, skala="C"):
    if skala == "C":
        # Formel Celsius til Fahrenheit
        fahrenheit = (temperatur * 9/5) + 32
        return fahrenheit
    elif skala == "F":
        # Formel Fahrenheit til Celsius
        celsius = (temperatur - 32) * 5/9
        return celsius
    else:
        print("Vennligst bruk 'C' eller 'F'.")


# Her viser eg ulike eksempel på korleis funksjonen fungerar


# Printar funskjonen, 34 Celsius konverterast til Fahrenheit

print(temperaturKonvertering(34, 'C'))  

# Printar funksjonen, 93.32 Fahrenheit konverterast til Celsius

print(temperaturKonvertering(93.2, 'F'))

# Printar funksjonen, 34 Celsius konverterast til Fahrenheit som standard når du ikkje angir eit argument for skala

print(temperaturKonvertering(34))

"""


#Oppgåve 3

#3a) 

#Lagar to globale variablar for "saldo" og "rentesats"

#Lagar funksjon for "innskudd" med argumentet "beløp", deretter "global saldo" for å vise at variabelen er global, legger til verdien for beløp til saldo

#Lagar funksjon for "uttak" med argumentet "beløp", deretter "global saldo" for å vise at variabelen er global, lagar "if" setning som seier at vist saldoen etter uttakk er større eller lik null kjør funksjonen, lagar "else" setning som printer "Overtrekk" om  tidlegare setning ikkje er sann

#Lagar funksjon for "beregn_rente", gangar "saldo" med "rentesats" og returnerer verdien

#Lagar funksjon for "renteoppgjør", deretter "global saldo, rentesats" for å vise at variabelen er global, kaller "beregn_rente" funksjonen og lagrer resulatet i variabelen "rente", legger til renta til saldoen,
#lagar "if setning" som sjekkar om saldoen er større enn 1 million, printer "Gratulerer du har bonusrente" om det er tilfelle og setter "rentesats" til 0.02, lagar "else" setning som printer "Du har når ordinær rente" om saldo er under 1 million og setter "rentesats" til 0.01


#Nederst er eksemplar på bruken av dei ulike funksjonane

#Fjern docstrings for å kjøre programmet


"""

saldo = 500 

rentesats = 0.01


def innskudd(beløp):
    global saldo
    saldo += beløp

def uttak(beløp):
    global saldo
    if saldo - beløp >= 0:
        saldo -= beløp
    else:
        print("Overtrekk.")

def beregn_rente():
    return saldo * rentesats 

def renteoppgjør():
    global saldo, rentesats
    rente = beregn_rente()
    saldo += rente
    if saldo > 1000000:
        print("Gratulerer, du får bonusrente!")
        rentesats = 0.02
    else:
        print("Du har nå ordinær rente.")
        rentesats = 0.01





# Eksempel på bruk
print(saldo)
print(rentesats)

innskudd(300)
print(saldo)

uttak(100)
print(saldo)

rente = beregn_rente()
print(rente)

print(saldo)

renteoppgjør()
print(saldo)


innskudd(1000000)
print("Gratulerer, du får bonusrente!")
print(saldo)
print(rentesats)

uttak(500000)
print("Du har nå ordinær rente.")
print(saldo)
print(rentesats)

uttak(1000000)
print("Overtrekk.")
print(saldo)
   
    
"""


    
#3b)

#Samme koden som i oppgåve "3a)" men med implementert brukargrensesnitt. Lagt til "input" av heiltal i "innskudd" og "uttak" funksjonane. Også lagt til at det printast "Ikkje dekning" om du skriv inn for stort beløp i "uttak"

#Laga ny funksjon med navnet "vis_saldo" som viser saldoen i terminalen

#Laga ny funksjon med navnet "velg" som fungera som brukargrensesnittet. Dei ulike funksjonane får ulike tal som du kan skrive inn i terminalen.

#Fjern docstrings for å kjøre programmet

"""


saldo = 500
rentesats = 0.01

def vis_saldo():
    print("Saldo:", saldo)

def innskudd():
    global saldo
    beløp = float(input("Beløp: "))
    saldo += beløp

def uttak():
    global saldo
    beløp = float(input("Beløp: "))
    if saldo - beløp >= 0:
        saldo -= beløp
    else:
        print("Ikkje dekning.")
    vis_saldo()

def renteoppgjør():
    global saldo, rentesats
    rente = saldo * rentesats
    saldo += rente
    if saldo > 1000000:
        print("Gratulerer, du får bonusrente!")
        rentesats = 0.02
    else:
        print("Du har nå ordinær rente.")
        rentesats = 0.01
    vis_saldo()

def velg():
    while True:
        print("\n------------------------")
        print("1 - vis saldo")
        print("2 - innskudd")
        print("3 - uttak")
        print("4 - renteoppgjør")
        print("------------------------")
        valg = input("Velg handling: ")
        
        if valg == '1':
            vis_saldo()
        elif valg == '2':
            innskudd()
        elif valg == '3':
            uttak()
        elif valg == '4':
            renteoppgjør()
        else:
            print("Ugyldig valg. Prøv igjen.")


# Test av grensesnittet i ein "while" loop
while True:
    velg()


"""



#3c)

#Samme koden som i oppgåve 3b) men implementert eit valg i grensesnittet som viser dei tre siste endringane i saldoen. Dette blir gjort ved hjelp av ei liste og "append" metoden som lagrar endringane som ei tekststreng. 

#Funksjonen "siste_endringer" skriv ut dei tre siste saldo endringane i "endringar" lista

#Fjern docstrings for å kjøre programmet


"""


saldo = 500
rentesats = 0.01
endringar = []  # Ei liste for å holde oversikt over endringane i saldoen

def vis_saldo():
    print("Saldo:", saldo)

def innskudd():
    global saldo
    beløp = float(input("Beløp: "))
    saldo += beløp
    endringar.append(f"+{beløp}")  # Legg til innskudd som en endring

def uttak():
    global saldo
    beløp = float(input("Beløp: "))
    if saldo - beløp >= 0:
        saldo -= beløp
        endringar.append(f"-{beløp}")  # Legg til uttak som en endring
    else:
        print("Ikkje dekning.")
    vis_saldo()

def renteoppgjør():
    global saldo, rentesats
    rente = saldo * rentesats
    saldo += rente
    if saldo > 1000000:
        print("Gratulerer, du får bonusrente!")
        rentesats = 0.02
    else:
        print("Du har nå ordinær rente.")
        rentesats = 0.01
    endringar.append(f"+{rente}")  # Legg til renteoppgjør som en endring

def siste_endringer():
    print("\nSiste endringar:")
    for endring in endringar[-3:]:
        print(endring)

def velg():
    while True:
        print("\n------------------------")
        print("1 - vis saldo")
        print("2 - innskudd")
        print("3 - uttak")
        print("4 - renteoppgjør")
        print("5 - siste endringar")
        print("------------------------")
        valg = input("Velg handling: ")
        
        if valg == '1':
            vis_saldo()
        elif valg == '2':
            innskudd()
        elif valg == '3':
            uttak()
        elif valg == '4':
            renteoppgjør()
        elif valg == '5':
            siste_endringer()
        else:
            print("Ugyldig valg. Prøv igjen.")

# Test av grensesnittet i ein "while" loop
while True:
    velg()


"""


#Oppgåve 4

#Dei ulike omgrepa innafor denne koden har eg funne på "https://www.w3schools.com/python/default.asp" sin python dokumentasjon (Eg har oppdatert denne koden til å inkludere funksjonane "min og "max" slik oppgåva spør om)

#Koden kan tolkast på følgjande framgangsmåte:

#Importerer "random" modulen slik eg kan lage tilfeldige siffer

#Funksjonen "tre_tilfeldege" blir laga. 
#Ei liste som inneheld tre ulike tal blir tildelt variabelen "tal". 
#Tre tilfeldige tal mellom 1 og 9 blir generert ved hjelp av "random.randint" (https://www.w3schools.com/python/ref_random_randint.asp) metoden frå "random modulen"
#Ei "for" løkke blir laga som genererar ein sekvens med tre tal ved hjelp av "range" funksjonen (https://www.w3schools.com/python/ref_func_range.asp).

#Variabelen "største_tal" blir laga som brukar "max" funksjonen (https://www.w3schools.com/python/ref_func_max.asp#:~:text=Definition%20and%20Usage,an%20alphabetically%20comparison%20is%20done.) til å finne det største talet
#Variabelen "minste_tal" blir laga som brukar "min" funksjonen (https://www.w3schools.com/python/ref_func_min.asp) til å finne det minste talet

#Brukar "remove" metoden (https://www.w3schools.com/python/ref_list_remove.asp) for å fjerne det største og minste talet i lista

#Brukar "insert metoden" (https://www.w3schools.com/python/ref_list_insert.asp) for å leggje til det minste talet tilbake i lista på index "0" og det største talet på index "2"
#Tala er no i stigande rekkjefølgje

#Variabelen "tal_stigande_rekkjefølgje" brukar "map" (https://www.w3schools.com/python/ref_func_map.asp) til å konvertere alle tala i lista "tal" til ei streng
#Difor kan eg no bruke "join" metoden (https://www.w3schools.com/python/ref_string_join.asp) for å slå saman strengene i lista utan mellomrom
#Til slutt blir det konvertert til eit heiltal via "int" og verdien blir returnert





#Fjern docstrings for å kjøre programmet




import random

def tre_tilfeldege():
    
    tal = [random.randint(1, 9) for _ in range(3)]

    største_tal = max(tal)

    minste_tal = min(tal)

    tal.remove(største_tal)

    tal.remove(minste_tal)

    
    tal.insert(0, minste_tal)

    tal.insert(2, største_tal)

    
    tal_stigande_rekkjefølgje = int(''.join(map(str, tal)))

    return tal_stigande_rekkjefølgje







# Testing av funksjonen
print(tre_tilfeldege())
print(tre_tilfeldege())
print(tre_tilfeldege())
print(tre_tilfeldege())
print(tre_tilfeldege())


