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

Fornavn = "Henrik\n"

Etternavn = "Vågseth"

"""

def navn():
    print(Fornavn + Etternavn)


navn()

"""

#Oppgåve 2

#2a)

"""
def valuta_kalkulator(sum_kroner):
    dollar_kurs = 11.62
    euro_kurs = 10.2
    
    sum_euro = sum_kroner / euro_kurs
    sum_dollar = sum_kroner / dollar_kurs

    return euro_kurs, dollar_kurs

    


sum_kroner = float(input("Skriv beløpet i norske kroner"))
sum_euro, sum_dollar = valuta_kalkulator(sum_kroner)

print(f"{sum_kroner:.2f} NOK er same som {sum_euro:.2f} Euro eller {sum_dollar:2f} dollar")

"""

def valuta_kalkulator():
    norske_kroner = float(input("Skriv inn beløp i norske kroner: ")) #Ber
    dollarkurs = 11.62
    eurokurs = 10.2

    euro_belop = norske_kroner / eurokurs
    dollar_belop = norske_kroner / dollarkurs

    print(f"{norske_kroner:.2f} norske kroner tilsvarer {euro_belop:.2f} Euro og {dollar_belop:.2f} Dollar")

if __name__ == "__main__":
    main()