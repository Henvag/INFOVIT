#Eg har tatt utgangspunkt i nokre videoar frå eksempel "Code Crush": (https://www.youtube.com/watch?v=TIa1HRpG9ac)
#Den forklara koreis ein kan bruke "count" metoden 

#Denne youtube shorten forklara koreis ein kan bruke "split" og "len" metodane ((https://www.youtube.com/shorts/HX4c1TW4Xlo))

#Denne forklara korleis ein kan bruke replace metoden (https://www.youtube.com/watch?v=m5DUFLa4IXs)

#Denne viser korleis ein kan finne mest brukte ord i ei streng ved hjelp av "append", "split","count" og "index" metodane(https://www.youtube.com/shorts/DdRtiCTX7WA)
















def telle_bokstaver(streng, bokstav): #(Oppgåve 1a) Funksjon som teller antall bokstavar i streng
    telling_bokstav = streng.count(bokstav)

    print(telling_bokstav)

    return telling_bokstav



telle_bokstaver("programmering", "m")



def telle_ord(streng): #(Oppgåve 1b) Funksjon som teller antall ord i streng. Streng blir omgjort til liste
    telling_ord = streng.split() 

    print(len(telling_ord)) 

    return len(telling_ord)

    

    
telle_ord("Python er gøy")


def erstatte_bokstav(streng, bokstav_finn, bokstav_erstatt): #(Oppgåve 2) Funksjon som erstatter bokstav i streng




    ny_streng = streng.replace(bokstav_finn, bokstav_erstatt)

    print(ny_streng)

    return ny_streng


erstatte_bokstav("banan", "a", "o")



def formater_navn(fornavn, etternavn, mellomnavn = None): #(Oppgåve 3a) Funksjon som formaterer fornavn og etternavn. #(Oppgåve 3b) Tar hensyn til mellomnavn

    if mellomnavn is None:

        nytt_navn = f"{fornavn} {etternavn}"  
        print(nytt_navn)

    else:
        nytt_navn = f"{fornavn} {etternavn} {mellomnavn}"

        print(nytt_navn)    
        
          

  
    

    return nytt_navn



formater_navn("Ola", "Nordmann") #(Oppgåve 3a) Kall på funksjonen

formater_navn("Ola", "Nordmann", "Johan") #(Oppgåve 3b) Kall på funksjonen





def finn_mest_brukte_ord(streng): #(Oppgåve 4) Funksjon som finner mest brukte ord i streng
    ord_liste = streng.split() 
    ord_telling = []
    for ord in ord_liste: #(Oppgåve 4) For løkke som går igjennom ord i lista
        telling = ord_liste.count(ord)
        ord_telling.append(telling) #(Oppgåve 4)Lagrar tellingen i ei liste

    index = ord_telling.index(max(ord_telling)) #(Oppgåve 4)Finn index til det mest brukte ordet
    mest_brukt_ord = ord_liste[index] #(Oppgåve 4) Finn ordet det mest brukte ordet

    print(mest_brukt_ord)

    return mest_brukt_ord




    


finn_mest_brukte_ord("Dette er en test som er enkel og grei") #(Oppgåve 4) Kall på funksjonen