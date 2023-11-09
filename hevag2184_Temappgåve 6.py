"""


Oppgave 1:

I "lag_fortegnelse" funksjonen tar den "personer" som parameter.
Det er ei liste med tupler som inneholder navn og alder.

Ein tom fortegnelse/dictionary blir laga i variabelen "fortegnelse"

Ei for løkke itererer igjennom alle personane i "personer" parameteret.
I løkka blir tuplene splitta i navn og alder.
Deretter blir oppføringa lagt til i fortegnelsen og returnert.

Eg brukte denne videoen for å få litt meir forståelse rundt fortegnelser:
https://www.youtube.com/watch?v=daefaLgNkw0



Oppgave 2: 

I "sorter_personer_etter_navn" funksjonen tar den "personer" som parameter.
Det er ei dictionary som inneholder navn og alder.

Fortegnelsen blir konvertert til ei liste av tupler i variabelen "person_liste" ved hjelp av "items" metoden (https://www.w3schools.com/python/ref_dictionary_items.asp)

Deretter blir lista sortert ved hjelp av "sort" metoden (https://www.w3schools.com/python/ref_list_sort.asp)
Til slutt blir lista returnert.



Oppgåve 3:
I "finn_gjensidige_venner" funksjonen tar den "venneliste" og "navn" som parameter.
Den hentar lista over vennar ved å bruke "navn" som nøkkelen i "venneliste

Det blir laga ei tom liste for å lagre navna på dei gjensidige vennane.

Vidare itererar "for" loopen igjennom alle personane i "venneliste".
Det blir sjekka om den gitte personen er i deira "venneliste" og om seg sjølv er i den gitte personen si "venneliste"
Om begge betingelsane er oppfylt vil personen bli lagt til i lista over gjensidige venner med "append" metoden (https://www.w3schools.com/python/ref_list_append.asp)

Til slutt blir lista returnert



"""


def lag_fortegnelse(personer):
    fortegnelse = {}  # Opprettar ein tom dictionary for å lagre data

    for person in personer:
        navn, alder = person  # Splittar tuppel inn i navn og alder
        fortegnelse[navn] = alder  # Legger til oppføringa i fortegnelsen

    return fortegnelse

# Funksjonstest
personer = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
resultat1 = lag_fortegnelse(personer)
print(resultat1)





  

def sorter_personer_etter_navn(personer):
    # Konverterar dictionary til liste av tupler
    person_liste = list(personer.items())
    
    # Sorterar lista alfabetisk
    person_liste.sort()
    
    return person_liste



#Funksjonstest
personer = {"Alice": 25, "Charlie": 35, "Bob": 30}
resultat2 = sorter_personer_etter_navn(personer)
print(resultat2)









def finn_gjensidige_venner(venneliste, navn):
    # Henter lista over venner for personen
    venner = venneliste[navn]
    
    # Lagar ei tom liste for å lagre gjensidige venner
    gjensidige_venner = []
    
    # Itererer over alle andre personar i vennelista
    for person, personens_venner in venneliste.items():
        # Sjekker om den gitte personen er i deira venneliste
        if person != navn and person in venner and navn in personens_venner:
            # Legger til personen i lista over gjensidige venner
            gjensidige_venner.append(person)
    
    return gjensidige_venner




# Funksjonstest

vennefortegnelse = {"Alice": ["Bob", "Charlie", "Devin"], "Bob": ["Charlie"], "Charlie": ["Alice"], "Devin": ["Alice", "Bob"]}
print(finn_gjensidige_venner(vennefortegnelse, 'Alice'))



