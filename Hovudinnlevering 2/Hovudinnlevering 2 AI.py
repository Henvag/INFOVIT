class Tekstanalyse:

    tekst = ''  # teksten som analyseres
    avsnittliste = []  # liste over normaliserte avsnitt i teksten
    ordlister = []  # liste av lister over ord som forekommer i hvert avsnitt
    ordtellinger = []  # liste av lister med ordtellinger for hvert avsnitt

    def __init__(self, tekst):
        self.tekst = tekst

    def normaliser_tekst(self, spesialtegn='.,:;!?'): #"Fjerner spesialtegn fra self.tekst og konverterer til små bokstaver."
        
        self.tekst = self.tekst.lower()
        for tegn in spesialtegn:
            self.tekst = self.tekst.replace(tegn, '')

    def til_avsnitt(self, avsnittskille='\n\n'): #Deler self.tekst opp i en liste av avsnitt som lagres i self.avsnittliste.
        
        self.avsnittliste = self.tekst.split(avsnittskille)

    def lag_ordliste(self, avsnittekst): #Lager en liste av ord som forekommer i avsnittet.
        
        return avsnittekst.split()

    def tell_ordforekomster(self, ordliste, avsnittekst): #Lager en liste over antall forekomster av ordene i ordliste i avsnittet.
        
        tellinger = []
        for ord in ordliste:
            tellinger.append(avsnittekst.count(ord))
        return tellinger

    def skriv_ut(self): #Skriver ut analyseresultatene for hvert avsnitt på skjermen.
        
        for i in range(len(self.avsnittliste)):
            print(f"Avsnitt {i+1}:")
            print(f"Avsnitttekst: {self.avsnittliste[i]}")
            print(f"Ordliste: {self.ordlister[i]}")
            print(f"Ordtelling: {self.ordtellinger[i]}")

    def skriv_ut(self): #Skriver ut analyseresultatene for hvert avsnitt på skjermen.
        
        for i in range(len(self.avsnittliste)):
            print(f"Avsnitt {i+1}:")
            for j in range(len(self.ordlister[i])):
                print(f"{self.ordlister[i][j]}: {self.ordtellinger[i][j]}")

    def lagre_til_fil(self, filnavn): #Lagrer analyseresultatene for hvert avsnitt i en fil.
        
        with open(filnavn, 'w') as f:
            for i in range(len(self.avsnittliste)):
                f.write(f"Avsnitt {i+1}:\n")
                for j in range(len(self.ordlister[i])):
                    
                    f.write(f"{self.ordlister[i][j]}: {self.ordtellinger[i][j]}\n")



    def analyser_tekst(self): #Lager en ordliste og teller ordforekomster for hvert avsnitt i teksten.

        ordlister = []
        ordtellinger = []
        for avsnittekst in self.avsnittliste:
            ordliste = self.lag_ordliste(avsnittekst)
            ordtelling = self.tell_ordforekomster(ordliste, avsnittekst)
            ordlister.append(ordliste)
            ordtellinger.append(ordtelling)
        self.ordlister = ordlister
        self.ordtellinger = ordtellinger
 
      

# testkjøring
filnavn = 'eksempeltekst.txt'
eksempeltekst = open(filnavn).read()
tekstanalyse = Tekstanalyse(eksempeltekst)
tekstanalyse.normaliser_tekst()
tekstanalyse.til_avsnitt()
tekstanalyse.analyser_tekst()
tekstanalyse.skriv_ut()
