# def postupneVkladejSubKodyDoHlavnihoKodu(kodOrig, pocitatMezery, data):

### list of variables
urovenZanoreni   
i   
if (nazVolMetody !  
cisloRadku   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
if(pocitatMezery   
pocetMezerPredKodem   
kodNovy   
kodNew   

### code of method
```
def postupneVkladejSubKodyDoHlavnihoKodu(kodOrig, pocitatMezery, data):

    urovenZanoreni = 0
    i = - 1

    for nazVolMetody in data.volanaMetoda:
        i = i + 1
        if (nazVolMetody != ""):
            cisloRadku = vratCisloRadkuMetody(nazVolMetody)

            vyjmiKodOdRadku = data.zacatekBloku[cisloRadku]
            vyjmiKodDoRadku = data.konecBloku[cisloRadku]

            if(vyjmiKodOdRadku > -1):
                if (vyjmiKodDoRadku > -1):

                    #pokud se jedna o pole radku kodu, pak pocita mezery, u jinych typu dat to nema vyznam
                    if(pocitatMezery == True):
                        pocetMezerPredKodem = spocitejPocetMezerPredKodemNaRadku(kodOrig[i])
                    else:
                        pocetMezerPredKodem = 0

                    #Data do SubKodu se nacitaji z originalnich (modifikovanech) data.xxx (-proto kodOrig)
                    kodNovy = nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, pocetMezerPredKodem, kodOrig)
                    kodNew = vlozSubKodDoKodu(kodOrig, kodNovy, i+1)

                    break

    return (kodNew)
```
