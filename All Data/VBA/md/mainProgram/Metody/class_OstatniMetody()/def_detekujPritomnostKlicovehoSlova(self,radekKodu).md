# def detekujPritomnostKlicovehoSlova(self, radekKodu):

### list of variables
klicovaSlova   
radekKoduSMezerami   
jednotlivaSlovaNaRadku   
klicoveSlovoNalezeno   
slovo   

### code of method
<pre>
 <code>
    def detekujPritomnostKlicovehoSlova(self, radekKodu):

        #Importuje vstupni data, kde je definice klicovych slov
        import vstupniData

        # Vraci True nebo False podle toho, zda radek obsahuje klicove slovo, ci nikoliv
        klicovaSlova = []
        klicovaSlova = vstupniData.definiceKlicovychSlov()

        # doplni do radku mezery, tak aby mohl pomoci mezer radek rozdelit
        # pokud by na radku mezera nebyla, nerozpoznal by klicove slovo
        radekKoduSMezerami = radekKodu.replace("(", " ")
        jednotlivaSlovaNaRadku = radekKoduSMezerami.split()

        klicoveSlovoNalezeno = False

        for klicoveSlovo in klicovaSlova:
            # pokud najde klicove slovo ve vnitrni smycce, ukonci i tu smycku vnejsi
            if (klicoveSlovoNalezeno == True):
                break
            for slovo in jednotlivaSlovaNaRadku:
                if (slovo == klicoveSlovo):
                    klicoveSlovoNalezeno = True
                    break

        return (klicoveSlovoNalezeno)
 <code>
<pre>
