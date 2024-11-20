# def nactiSubKod(prvniRadek, posledniRadek, pocetMezer, dataPole):

### list of variables
poleSubKod   
subKod   
radekSubKodu   
if(pocetMezer   

### code of method
```
def nactiSubKod(prvniRadek, posledniRadek, pocetMezer, dataPole):

    poleSubKod = []
    subKod = []

    for i in range(prvniRadek, posledniRadek):
        radekSubKodu = dataPole[i]
        poleSubKod.append(radekSubKodu)

    if(pocetMezer == 0):
        subKod = poleSubKod
    else:
        subKod = pridejMezeryPredRadek(poleSubKod, pocetMezer)

    return(subKod)
```
### links

