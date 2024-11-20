# def vlozSubKodDoKodu(self, kodOrig, kodNovy, vkladejOdRadku):

### list of variables
kodNew   
delkaKoduOrig   
delkaKoduNovy   
celkovaDelka   
iOrig   
iNovy   
radek   
i >  

### code of method
```
    def vlozSubKodDoKodu(self, kodOrig, kodNovy, vkladejOdRadku):

        kodNew = []

        delkaKoduOrig = len(kodOrig)
        delkaKoduNovy = len(kodNovy)
        celkovaDelka = delkaKoduOrig + delkaKoduNovy

        iOrig = -1
        iNovy = -1

        for i in range(0, celkovaDelka):
            if (i < vkladejOdRadku):
                iOrig = iOrig + 1
                radek = kodOrig[iOrig]
            if (i >= vkladejOdRadku):
                if (i < (vkladejOdRadku + delkaKoduNovy)):
                    iNovy = iNovy + 1
                    radek = kodNovy[iNovy]
                else:
                    iOrig = iOrig + 1
                    radek = kodOrig[iOrig]

            kodNew.append(radek)

        return (kodNew)
```
### links

