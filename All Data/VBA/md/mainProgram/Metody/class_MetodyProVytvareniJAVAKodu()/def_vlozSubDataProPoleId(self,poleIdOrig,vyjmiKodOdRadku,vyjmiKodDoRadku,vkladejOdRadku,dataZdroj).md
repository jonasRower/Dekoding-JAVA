# def vlozSubDataProPoleId(self, poleIdOrig, vyjmiKodOdRadku, vyjmiKodDoRadku, vkladejOdRadku, dataZdroj):

### list of variables
dataNovy   
vlozOdRadku   
idPosun   
poleIdClass   
poleIdNew   
poleIdAll   

### code of method
```
    def vlozSubDataProPoleId(self, poleIdOrig, vyjmiKodOdRadku, vyjmiKodDoRadku, vkladejOdRadku, dataZdroj):

        if (vyjmiKodOdRadku > -1):

            dataNovy = OstatniMetody.nactiSubKod(self, vyjmiKodOdRadku, vyjmiKodDoRadku, -1, dataZdroj)

            vlozOdRadku = vkladejOdRadku + 2
            idPosun = vlozOdRadku - 1

            # vytvori poleId pro dataNovy
            poleIdClass = createIdArr(dataNovy, idPosun)
            poleIdNew = poleIdClass.getPoleId()

            poleIdAll = OstatniMetody.vlozSubKodDoKodu(self, poleIdOrig, poleIdNew, vlozOdRadku)

        else:
            poleIdAll = poleIdOrig

        return(poleIdAll)
```
### links

