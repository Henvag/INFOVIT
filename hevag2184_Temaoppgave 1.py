#Oppgåve 1 

#Program 1 (Ta vekk docstrings for å kjøre programmet)

#Skriv ut navnet mitt på ulike linjer ved hjelp av "print"

"""


Fornavn = "Henrik\n"

Etternavn = "Vågseth"


print(Fornavn + Etternavn)

"""
#Program 2 (Ta vekk docstrings for å kjøre programmet)

#Lagar ein funksjon som skriv ut navnet mitt ved hjelp av "print"

"""
Fornavn = "Henrik\n"

Etternavn = "Vågseth"



def navn():
    print(Fornavn + Etternavn)


navn()

"""

#Oppgåve 2

#2a) (Ta vekk docstrings for å kjøre programmet)

#Definerer ein funksjon, brukar "float" funksjonen for å få med desimaltal, brukar "input" funskjonen for å skrive inn beløp
#Gjør de ulike regnestykkene med bruk av variabler, printer ut svaret med to desimaler og kjører den definerte funksjonen


"""

def valuta_kalkulator(): 
    norske_kroner = float(input("Skriv inn beløp i norske kroner: ")) 
    dollarkurs = 11.62
    eurokurs = 10.2

    euro = norske_kroner / eurokurs
    dollar = norske_kroner / dollarkurs

    print(f"{norske_kroner:.2f} norske kroner tilsvarer {euro:.2f} Euro og {dollar:.2f} Dollar")






valuta_kalkulator()

"""
    

#Oppgåve 2

#2b) (Ta vekk docstrings for å kjøre programmet)

#Samme kode som tidlegare men la til spesialtegna "$" og "€" for finare utskrift. 


"""

def valuta_kalkulator(): 
    norske_kroner = float(input("Skriv inn beløp i norske kroner: ")) 
    dollarkurs = 11.62
    eurokurs = 10.2 

    euro = norske_kroner / eurokurs
    dollar = norske_kroner / dollarkurs

    print(f"{norske_kroner:.2f} norske kroner tilsvarer {euro:.2f}\N{euro sign} og {dollar:.2f}\N{dollar sign}")






valuta_kalkulator()


"""
