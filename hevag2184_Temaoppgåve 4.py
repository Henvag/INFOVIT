#Eg har tatt utgangspunkt i forelesningsnotatene hovudsaklig nummer "F06" om objekt og klassar
#(https://mitt.uib.no/courses/41745/files/folder/Forelesningsnotater?preview=5364440)

#I tillegg har eg sett på denne videoen fra "CS Dojo" (https://www.youtube.com/watch?v=wfcWRAxRVBA)
#Den forklara ganske bra korleis klassar og objekt fungera

#Pluss denne som forklara litt om korleis du kan bruke loops på lister (https://www.youtube.com/watch?v=OnDr4J2UXSA)
















class Bil: #(Oppgåve 1.1) Lagar klassen



    def __init__(self, merke, modell, år, nåværende_år, eier): #(Oppgåve 1.2)Metode som initiaiserer objekta ved hjelp av ein "constructor"
        self.merke = str(merke)
        self.modell = str(modell)
        self.år = int(år)
        self.nåværende_år = int(nåværende_år) #(Oppgåve 1.3) Standardverdi for alder metoden
        self.eier = None #(Oppgåve 6.1) Nytt attributt i bil klassen
        
   
    def skriv_ut_info(self): #(Oppgåve 1.2)Metode som skriv ut informasjon om bilen
        print("Merke: " + self.merke, "Modell: " + self.modell, "År: " + str(self.år))
        if self.eier is not None: #(Oppgåve 6.3) Skriv ut info om eiger vist den har en
            print("Eier: Navn: " + self.eier.navn + ", Adresse: " + self.eier.adresse)

            


    def alder(self, nåværende_år =None):#(Oppgåve 3.1) Metode som skriv returnerer alder for bilen 
         if nåværende_år is None:#(Oppgåve 3.1) If setning sørger for at standardverdi blir printa utan argument
             nåværende_år = self.nåværende_år
    
         alder = nåværende_år - self.år
         return alder
    

class Eier: #(Oppgåve 5.1) Lagar klassen
    

    def __init__(self, navn, adresse):
        self.navn = str(navn)
        self.adresse = str(adresse)

    def skriv_ut_info(self): #(Oppgåve 5.2)Metode som skriv ut informasjon om eigaren
        print("Navn: " + self.navn, "Adresse: " + self.adresse)

        



første_bil = Bil("Toyota," , "Supra,", 1986, 2023, None) #(Oppgåve 2.1)Lagrar klassen i det første objektet

andre_bil = Bil("Nissan," , "Skyline R32,", 1989, 2023, None) #(Oppgåve 2.1)Lagrar klassen i det andre objektet




første_bil.skriv_ut_info() #(Oppgåve 2.2)Skriv ut første objektet ved bruk av metoden
andre_bil.skriv_ut_info() #(Oppgåve 2.2)Skriv ut andre objektet ved bruk av metoden

print(første_bil.alder()) #(Oppgåve 3.1)Skriv ut første objektet med standardverdi ved bruka av metode
print(andre_bil.alder(1990)) #(Oppgåve 3.1) Skriv ut andre objektet med eit argument ved bruka av metode



bilpark = [første_bil, andre_bil] #(Oppgåve 4.1)Liste med bilobjekta


def bilpark_info(bilpark): #(Oppgåve 4.2) Funksjon som går igjennom lista med ei løkke og skriv ut info med metoden
    for bilar in bilpark:
      bilar.skriv_ut_info() 

   

bilpark_info(bilpark)


eier = Eier("Elon Musk", "Muskgaten 23") #(Oppgåve 6.2) Lagar  objekt med klassen "Eier" 

første_bil.eier = eier # (Oppgåve 6.2) Knyttar Eier-objektet til første bil i bilparken

eier.skriv_ut_info() #(Oppgåve 5.2) Skriv ut info om eigar

første_bil.skriv_ut_info()

bilpark_info(bilpark) #(Oppgåve 6.4) Skriver ut info om bilparken, no inkludert med eigarinfo om det er tilgjengelig





