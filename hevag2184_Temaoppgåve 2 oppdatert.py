# Oppgåve 1

# Importerer "matte" modulen, definerer ein funskjon, Lagar variabel som spør brukaren om å skrive inn radius,
# Lagar variabel som gjør utregninga for radius i ein sirkel,
# Brukar "Print" for å få dette i terminalen og gjer at det er 3 desimalar med "f string", kjører funskjonen

# Fjern docstrings for å kjøre programmet :)


import random
import math

"""
def radius_sirkel():

    radius = float(input("Radius: "))
    areal = math.pi * radius ** 2

    print(f"Arealet til en sirkel med radius {radius:.3f} er {areal:.3f}")


radius_sirkel()

"""


# Oppgåve 2

# Definerer ein funksjon, lagar variabel som spør brukaren skrive inn ei setning,
# Lagar variabel som spør brukaren gjette lengda ved bruk av heiltal

# Lagar variabel som fjerner mellomrom fra "input" setninga før lengda blir returnert
# Lagar variabel som brukar "len" funskjonen som returnerer lengda i setninga

# Samanliknar den riktige lengda med det brukaren gjettar og skriv ut om dette er riktig eller feil, kjører funksjonen

# Fjern docstrings for å kjøre programmet :)

"""
def bokstav_gjetter():
    setning = input("Skriv ei tilfeldig setning: ")
    gjetting = int(input("Gjett lengda: "))

    setning_uten_mellomrom = setning.replace(" ", "")

    riktig_lengde = len(setning_uten_mellomrom)
    print(f"That's {riktig_lengde == gjetting}!!")


bokstav_gjetter()

"""

# Oppgåve 3

# Importerer "random" modulen , definerer ein funksjon, lagar variabel som spør brukaren skrive inn eit heiltal
# Lagar variabel som velger eit tilfeldig tal frå 0 til 9

# Lagar variabel som ganger tallet du skriver inn med 10 og plussar det tilfeldige tallet slik at det kjem på riktig posisjon
# Lagar variabel som delar det nye tallet på det gamle tallet

# Skriv dette ut i terminalen og brukar "f string" slik det blir i formatet eg ønskjer

# Fjern docstrings for å kjøre programmet :)

"""

def tilfeldig_tall():
    gammelt_tall = int(input("Gi meg eit tall: "))
    tilfeldig_tall = random.randint(0, 9)

    nytt_tall = gammelt_tall * 10 + tilfeldig_tall
    resultat = nytt_tall / gammelt_tall

    print(f"{nytt_tall:.0f}/{gammelt_tall} = {resultat:.1f}")


tilfeldig_tall()

"""
