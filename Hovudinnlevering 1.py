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

