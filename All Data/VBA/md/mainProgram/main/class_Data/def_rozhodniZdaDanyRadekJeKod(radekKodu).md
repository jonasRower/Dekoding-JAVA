# def rozhodniZdaDanyRadekJeKod(radekKodu):

### list of variables
radekKoduBezMezery   
JeToKod   
indexKomentare   
if(indexKomentare   

### code of method
```
def rozhodniZdaDanyRadekJeKod(radekKodu):
   # print(radekKodu)
    radekKoduBezMezery = radekKodu.replace(" ","")
    JeToKod = True

    try:
        indexKomentare = radekKoduBezMezery.index('//')
        if(indexKomentare == 0):
            JeToKod = False
        else:
            JeToKod = True
    except:
       pass

    return(JeToKod)
```
