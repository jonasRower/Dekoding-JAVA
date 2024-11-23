# def zjistiZdaSeJednaOForCyklus(radekKodu):

### list of variables
jednotlivaSlovaNaRadku   
forCyklus   
slovo   

### code of method
<pre>
 <code>
def zjistiZdaSeJednaOForCyklus(radekKodu):
    jednotlivaSlovaNaRadku = radekKodu.split()
    forCyklus = False
    for slovo in jednotlivaSlovaNaRadku:
        if (slovo == 'for'):
            forCyklus = True
            break

    return (forCyklus)
 <code>
<pre>
