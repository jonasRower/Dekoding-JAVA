# def pridejMezeryPredRadek(subKod, pocetMezer):

### list of variables
i   
SubKodSMezerou   
mezeraPredSubKodem   
radekSubKoduSMezerou   

### code of method
```
def pridejMezeryPredRadek(subKod, pocetMezer):

    i = -1
    SubKodSMezerou = []

    mezeraPredSubKodem = ""
    for i in range(0, pocetMezer):
        mezeraPredSubKodem = mezeraPredSubKodem + " "

    mezeraPredSubKodem = mezeraPredSubKodem + "-->" + "  "

    for radekSubKodu in subKod:
        radekSubKoduSMezerou = mezeraPredSubKodem + radekSubKodu
        SubKodSMezerou.append(radekSubKoduSMezerou)

    return(SubKodSMezerou)
```
### links

