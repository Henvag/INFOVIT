#Oppgåve 1

# 1a)

#Koden er oppbygd på følgjande måte:

#Lagar funksjonen "multiplikasjonstabell" med argumentet "n"
#Variabelen "kolonnebreidde" blir laga som tek i bruk "len" funksjonen (https://www.w3schools.com/python/ref_func_len.asp). Den bereikna breidda på kolonnene ved å gjere "n*n" om til ei streng og deretter finne lengden av strengen med "len" 

#To "for" løkker blir laga. Den første går igjennom tala frå 1 til "n" i tabellen for radene i tabellen. Den andre går igjennom tala frå 1 til "n" i for kolonnene i tabellen
#Variabelen "produkt" gangar "i" med "j" (rad og kolonne)
#"Produkt" blir skreve ut med riktig formatering med "f-streng". "end" sørgjer for at vi ikkje går til neste linje på samme "produkt"

#Etter kvar rad går koden til neste linje ved "print" slik at det blir separate linjer

#Fjern docstrings for å kjøre programmet

"""

def multiplikasjonstabell(n):
    
    kolonnebreidde = len(str(n * n))

    
    for rad in range(1, n + 1):
        for kolonne in range(1, n + 1):
            
            produkt = rad * kolonne
           
            print(f'{produkt:>{kolonnebreidde}}', end=' ')
       
        print()




# Testing av koden
multiplikasjonstabell(3)
multiplikasjonstabell(5)



"""


# 1b)

#Gjør det samme som tidligera kode, men med penare utskrift

#Koden er endra på følgjande måte:

#Før loopen starta "printa" eg ut dei ulike symbola til overskrifta. Eg skriv deretter ut overskrifta i loopen

#Etter overskrifta lagar eg ei linje som skiljer den fra tabellen med ulike symbol

#Til slutt i tabellen er det lagt til eit strek symbol som går igjennom alle radene på same måte som i overskrifta

#Fjern docstrings for å kjøre programmet 

"""

def multiplikasjonstabell(n):
    kolonnebreidde = len(str(n * n))
    
    # Skriv ut overskrifta med tala 1 til n
    print(' * |', end=' ') #Ny
    for rad in range(1, n + 1):
        print(f'{rad:>{kolonnebreidde}}', end=' ')
    print()
    
    #Linje som skiljer overskrifta og tabellen
    print('---+' + '-' * (kolonnebreidde + 1) * n) #Ny
    
    #Tabellen
    for rad in range(1, n + 1):
        print(f'{rad:>{kolonnebreidde}} |', end=' ') #Ny
        for kolonne in range(1, n + 1):
            produkt = rad * kolonne
            print(f'{produkt:>{kolonnebreidde}}', end=' ')
        print()


# Testing av den nye koden
multiplikasjonstabell(4)

"""


#Oppgåve 2

# 2a) og 2b)


#For løkka oppbygd på følgjande måte:

#Lagar funksjonen "fakultet_while" med "n" som argument

#Lagar "if" setning som sjekkar om "n" er mindre enn 0 eller er ikkje eit heiltal ved hjelp av "isInstance" funksjonen (https://www.w3schools.com/python/ref_func_isinstance.asp)
#Om noko av dette er "True" blir det returnert ein feilmelding

#Lagar "elif" setning som seier at vist "n" er det same som 0 skal 1 blir returnert

#Reikninga av fakultet startar ved å bruke variabelen "resultat"

#Ei "for" løkke reknar resultatet med å multiplisere kvart tal fra 1 til "n"
#"Resultat" bir returnert til slutt


#While løkka oppbygd på følgjande måte:

#Lagar funksjonen "fakultet_while" med "n" som argument

#Lagar "if" setning som sjekkar om "n" er mindre enn 0 eller er ikkje eit heiltal ved hjelp av "isInstance" funksjonen (https://www.w3schools.com/python/ref_func_isinstance.asp)
#Om noko av dette er "True" blir det returnert ein feilmelding

#Lagar "elif" setning som seier at vist "n" er det same som 0 skal 1 blir returnert

#Reikninga av fakultet startar ved å bruke variabelen "resultat"

#Variabelen "i" brukes for å iterere mellom 1 til "n"

#Ei while løkke kjøre om "i" er mindre eller er lik "n". Variabelen "resultat" blir multiplisert med alle heiltallene frå 1 til "n"
#"Resultat" blir returnert til slutt


"""




#For løkke

def fakultet_for(n):
    if n < 0 or not isinstance(n, int):
        return f"Fakultetet av {n} er ikke definert."
    elif n == 0:
        return 1
    
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

print(fakultet_for(1))    
print(fakultet_for(-3.14159))

"""


#While løkke

"""

def fakultet_while(n):
    if n < 0 or not isinstance(n, int):
        return f"Fakultetet av {n} er ikke definert."
    elif n == 0:
        return 1
    
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        i += 1
    return resultat


"""
