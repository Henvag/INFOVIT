"""
Vurdering klassen:

Klassen "Vurdering" blir laga. Det blir laga ein konstuktør som tar dei fire attiributtane tekst, skår, emne og student.
"Tekst" er vurderinga som studenten har gitt til emnet. "Skår er skåren fra 1-6 som studenten har gitt til emnet. "Emne" er emnet som studenten har gitt vurdering til. "Student" er studenten som har gitt vurdering til emnet.

"skrivUtVurdering" metoden returnerar ein string med brukernavnet til studenten, emnekode til emnet, vurderinga av teksten og skåren.
Alt dette er putta i ei "f" streng. Brukernavnet er henta fra student-objektet. Emnekode er henta fra emne-objektet. Tekst er henta fra attributtet "tekst" i konstruktøren og brukar en backslash escape character for å få med hermeteikn (https://www.w3schools.com/python/gloss_python_escape_characters.asp. Skår er henta fra attributtet skår i konstruktøren.





Student klassen: 

Klassen "Student" blir laga.Det blir laga ein konstuktør som tar dei tre attributtane brukernavn, e-post og vurderinger.
"Brukernavn" er brukernavnet til studenten. "E-post" er e-posten til studenten. "Vurderinger" er ei liste som inneheld alle vurderingane som studenten har gitt til emner.

"ny_vurdering" metoden blir brukt til å lage ei ny vurdering og legge den til i studentens liste med vurderinger. Den tar tre argumenter: emne, tekst og skala. "Emne" er emnet som studenten har gitt vurdering til. "Tekst" er vurderinga som studenten har gitt til emnet. "Skala" er skåren fra 1-6 som studenten har gitt til emnet.
"Vurdering" åpnar ein instans av klassen "Vurdering" og lagrar den i variabelen "vurdering". Deretter kallar "emne.legg_til_vurdering)" på "legg_til_vurdering" metoden på emne-objektet med den nye vurderinga som argument. 
Den nye vurderinga blir også lagt til i studentens liste med vurderinger med metoden "append" (https://www.w3schools.com/python/ref_list_append.asp).

"skriv_ut" metoden blir brukt til å skrive ut informasjon om studenten og alle vurderingane han/ho har gitt. Det blir printa ei "f" string som skriver ut studentens brukernavn og e-post
If setninga "if self.vurderinger" sjekkar om studenten har oppgitt nokre vurderingar. Om list er tom blir den ikkje printa. Om lista ikkje er tom blir det printa ut "Vurderinger:" og deretter blir det printa ut alle vurderingane i lista med ein for løkke. 
For kvar vurdering i lista blir det printa ut vurderinga med metoden "skrivUtVurdering" som returnerar ein string med brukernavnet til studenten, emnekode til emnet, vurderinga av teksten og skåren.
Til slutt vil "print()"  skrive ei tom linje for å skilje den aktuelle studentens informasjon med den neste studentens informasjon.



Emne klassen: 

Klassen "Emne" blir laga. Det blir laga ein konstruktør som tar dei tre attributtane emnekode, tittel og vurderingar.
"Emnekode" er emnekoden for emne. Tittel er tittelen på emnet. "Vurderingar" er ei liste som inneheld alle vurderingane som har blitt gitt for emnet.

"skriv_ut" metoden blir brukt til å skrive ut informasjon om emne.
Det blir laga ei "f" string som skriv ut "emnekode" og "tittel"
If setninga "if self.vurderingar" sjekkar om det er nokre vurderingar i emnet. Om lista er tom blir den ikkje printa. Om det er nokre vurderinga blir det printa ut "Vurderingar:".
Det blir laga ein "for" løkke "for vurdering in self.vurderinger" som itererer gjennom kva vurdering i "self.vurderinger". Inni for løkka blir det kalt på "skrivUtVurdering" metoden i "vurdering" klassen som blir printa ut.
i "gjennomsnittlig_vurdering = sum(v.skår for v in self.vurderinger / len(self.vurderinger)" blir det laga ein variabel "gjennomsnittlig_vurdering" som lagrar gjennomsnittet av alle skårene i vurderingane. "sum" metoden/funksjonen (https://www.w3schools.com/python/ref_func_sum.asp) summerer alle skårene i vurderingane. 
"len" metoden/funksjonen (https://www.w3schools.com/python/ref_func_len.asp) tel kor mange vurderingar det er i lista. Deretter blir det printa ut "Gjennomsnittlig vurdering:" og "gjennomsnittlig_vurdering" variabelen.
Til slutt vil "print()" skrive ut ei tom linje for å skille det aktuelle emnets informasjon med det neste emnets informasjon.

"legg_til_vurdering" metoden tar argumentet "vurdering". "Append" metoden blir brukt for å legge til vurdering i "self.vurderinger" lista.








"""

class Vurdering:
    def __init__(self, tekst, skår, emne, student): # Konstruktør
        self.tekst = tekst
        self.skår = skår
        self.emne = emne
        self.student = student

    def skrivUtVurdering(self): #Returnerer en string med vulderingen
        return f"{self.student.brukernavn}, {self.emne.emnekode}: \"{self.tekst}\", skår={self.skår}"
        


class Student:
    def __init__(self, brukernavn, e_post): # Konstruktør
        self.brukernavn = brukernavn
        self.e_post = e_post
        self.vurderinger = []

    def ny_vurdering(self, emne, tekst, skala): # Lager en ny vurdering og legger den til i studentens liste med vurderinger
        vurdering = Vurdering(tekst, skala, emne, self)
        emne.legg_til_vurdering(vurdering)
        self.vurderinger.append(vurdering)

    def skriv_ut(self): # Skriver ut informasjon om studenten og alle vurderingene han/hun har gitt
        print(f"Navn: {self.brukernavn}, epost: {self.e_post}")
        if self.vurderinger:
            print("Vurderinger:")
            for vurdering in self.vurderinger:
                print(vurdering.skrivUtVurdering())
        print()
        


class Emne:
    def __init__(self, emnekode, tittel): # Konstruktør
        self.emnekode = emnekode
        self.tittel = tittel
        self.vurderinger = []

    def skriv_ut(self): # Skriver ut informasjon om emnet og alle vurderingene som har blitt gitt for emnet
        print(f"Emne {self.emnekode}: {self.tittel}")
        if self.vurderinger:
            print("Vurderinger:")
            for vurdering in self.vurderinger:
                print(vurdering.skrivUtVurdering())
            gjennomsnittlig_vurdering = sum(v.skår for v in self.vurderinger) / len(self.vurderinger)
            print(f"Gjennomsnittlig vurdering: {gjennomsnittlig_vurdering}")
        
        print()

    def legg_til_vurdering(self, vurdering): # Legger til en vurdering i emnets liste med vurderinger
        self.vurderinger.append(vurdering)


alina = Student('Alina Farschian', 'afa754@student.uib.no')
alina.skriv_ut()

info132 = Emne('INFO132', 'Innføring i programmering')
info132.skriv_ut()

alina.ny_vurdering(info132, 'Kjempebra emne! Jeg tar det om igjen neste høst!', 5)
alina.skriv_ut()
info132.skriv_ut()

olea = Student('Olea Haldorsen', 'oha356@student.uib.no')
olea.skriv_ut()

olea.ny_vurdering(info132, 'Sånn passe. DATA110 om våren dekker omtrent det samme.', 3)
olea.skriv_ut()
info132.skriv_ut()
