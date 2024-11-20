# def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole):

### list of variables
poleSubKod   
subKod   
posledniRadek   
radekSubKodu   
pocetMezer   

### code of method
```
    def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole):

        poleSubKod = []
        subKod = []


        # oprava, nevim, zda funguje spravne
        if(posledniRadek > len(dataPole)-1):
            posledniRadek = len(dataPole)-1

        for i in range(prvniRadek, posledniRadek):

            radekSubKodu = dataPole[i]
            poleSubKod.append(radekSubKodu)

        if (pocetMezer == 0):
            subKod = poleSubKod
        else:
            #subKod = OstatniMetody.pridejMezeryPredRadek(self, poleSubKod, pocetMezer)
            subKod = OstatniMetody.pridejMezeryPredRadek(self, poleSubKod, -1)

        # pro testovani
        #if(i == 85):
        #    a = 4
        #    if (radekSubKodu == ""):
        #        a = 4

        return (subKod)
```
### links

