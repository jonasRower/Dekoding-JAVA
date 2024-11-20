# def detekujPritomnostStrednikuNaKonciRadku(radekKodu):

### list of variables
radekKoduBezMezery   
posledniZnakRadku   
koncovyStrednik   

### code of method
```
def detekujPritomnostStrednikuNaKonciRadku(radekKodu):
    #Kdyz na konci radku neni strednik, pak se jedna o radek s metodou, nebo if, for, while ...
    #Kdyz na konci radku je strednik pak se jednosznacne jedna o vykonavajici kod
    #Tato funkce se vola za predpokladu
    #           JeToKod = True

    radekKoduBezMezery = radekKodu.replace(" ", "")
    posledniZnakRadku = radekKoduBezMezery[-2:-1]
    if (posledniZnakRadku == ";"):
        koncovyStrednik = True
    else:
        koncovyStrednik = False

    return (koncovyStrednik)
```
### links

