#Eg har tatt i bruk kodeskjelettet som startpunkt for oppgåva.
#Vidare har eg tatt utgangspunkt i dei ulike forelesningane, søkt på nettet og sett på ulike løysingar og videoar på "Youtube".
#Eg kjem til å legge ved linkar til dei ulike videoane og nettsidene eg har brukt i oppgåva.

"""
I "normaliser_tekst" funksjonen fjerner eg først spesialtegn med "replace" metoden (https://www.w3schools.com/python/ref_string_replace.asp).
Deretter brukar den "lower" metoden for å få små bokstavar (https://www.w3schools.com/python/ref_string_lower.asp#:~:text=The%20lower()%20method%20returns,Symbols%20and%20Numbers%20are%20ignored.).

"""






class Tekstanalyse:

    tekst = ''  # teksten som analyseres
    avsnittliste = []  # liste over normaliserte avsnitt i teksten
    ordlister = []  # liste av lister over ord som forekommer i hvert avsnitt
    ordtellinger = []  # liste av lister med ordtellinger for hvert avsnitt

    def __init__(self, tekst, avsnitt):
        self.tekst = tekst
        self.avsnitt = avsnitt

    def normaliser_tekst(self, spesialtegn='.,:;!?'):#Fjerner spesialtegn fra "self.tekst" og konverterer til små bokstaver.
        self.tekst = self.tekst.replace(spesialtegn, "")
        self.tekst = self.tekst.lower()

        print(self.tekst)

       
        

    def til_avsnitt(self, avsnittskille='\n\n'):#Deler "self.tekst" opp i en liste av avsnitt som lagres i "self.avsnitt" .
        
        
        self.avsnitt = avsnittskille


    def lag_ordliste(self, avsnittekst):#Lager en liste av ord som forekommer i avsnittet.
        
        pass

    def tell_ordforekomster(self, ordliste, avsnittekst):#Lager en liste over antall forekomster av ordene i ordliste i avsnittet.
        
        pass

    def analyser_tekst(self):#Lager en ordliste og teller ordforekomster for hvert avsnitt i teksten.
        
        ordlister = []
        ordtellinger = []
        for avsnittekst in self.avsnittliste:
            ordliste = self.lag_ordliste(avsnittekst)
            ordtelling = self.tell_ordforekomster(ordliste, avsnittekst)
            ordlister.append(ordliste)
            ordtellinger.append(ordtelling)
        self.ordlister = ordlister
        self.ordtellinger = ordtellinger

    def skriv_ut(self):#Skriver ut analyseresultatene for hvert avsnitt på skjermen.
        
        pass

    def lagre_til_fil(self, filnavn):#Lagrer analyseresultatene for hvert avsnitt i en fil.
        
        pass


# testkjøring
filnavn = 'eksempeltekst.txt'
eksempeltekst = open(filnavn).read() #Åpnar og returnerer innhaldet i filen som ein streng.
tekstanalyse = Tekstanalyse(eksempeltekst)
tekstanalyse.normaliser_tekst()
tekstanalyse.til_avsnitt()
tekstanalyse.analyser_tekst()
tekstanalyse.skriv_ut()
