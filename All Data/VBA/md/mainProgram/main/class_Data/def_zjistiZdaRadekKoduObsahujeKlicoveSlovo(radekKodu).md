# def zjistiZdaRadekKoduObsahujeKlicoveSlovo(radekKodu):

### list of variables
klicovaSlova   
radekKoduSMezerami   
jednotlivaSlovaNaRadku   
klicoveSlovoNalezeno   
slovo   

### code of method
```
def zjistiZdaRadekKoduObsahujeKlicoveSlovo(radekKodu):

    # Vraci True nebo False podle toho, zda radek obsahuje klicove slovo, ci nikoliv
    klicovaSlova = []
    klicovaSlova.append("for")
    klicovaSlova.append("if")
    klicovaSlova.append("while")
    klicovaSlova.append("try")
    klicovaSlova.append("catch")
    klicovaSlova.append("indexOf")
    klicovaSlova.append("substring")
    klicovaSlova.append("split")
    klicovaSlova.append("length")
    klicovaSlova.append("println")
    klicovaSlova.append("getLength")
    klicovaSlova.append("setForeground")
    klicovaSlova.append("return")

    # doplni do radku mezery, tak aby mohl pomoci mezer radek rozdelit
    # pokud by na radku mezera nebyla, nerozpoznal by klicove slovo
    radekKoduSMezerami = radekKodu.replace("(", " ")
    jednotlivaSlovaNaRadku = radekKoduSMezerami.split()

    klicoveSlovoNalezeno = False

    for klicoveSlovo in klicovaSlova:
        #pokud najde klicove slovo ve vnitrni smycce, ukonci i tu smycku vnejsi
        if (klicoveSlovoNalezeno == True):
            break
        for slovo in jednotlivaSlovaNaRadku:
            if (slovo == klicoveSlovo):
                klicoveSlovoNalezeno = True
                break

    return(klicoveSlovoNalezeno)
```
### links

