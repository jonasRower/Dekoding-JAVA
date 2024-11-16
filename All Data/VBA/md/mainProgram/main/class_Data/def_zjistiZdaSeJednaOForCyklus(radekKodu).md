# def zjistiZdaSeJednaOForCyklus(radekKodu):

### list of variables
jednotlivaSlovaNaRadku   
forCyklus   
if (slovo   

### code of method
```
def zjistiZdaSeJednaOForCyklus(radekKodu):
    jednotlivaSlovaNaRadku = radekKodu.split()
    forCyklus = False
    for slovo in jednotlivaSlovaNaRadku:
        if (slovo == 'for'):
            forCyklus = True
            break

    return (forCyklus)
```
