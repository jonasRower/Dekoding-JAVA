# def zjistiZdaSeJednaOIfPodminku(radekKodu):

### list of variables
jednotlivaSlovaNaRadku   
ifPodminka   
slovo   

### code of method
<pre>
 <code>
def zjistiZdaSeJednaOIfPodminku(radekKodu):

     jednotlivaSlovaNaRadku = radekKodu.split()
     ifPodminka = False
     for slovo in jednotlivaSlovaNaRadku:
         if (slovo == 'if'):
            ifPodminka = True
            break

     return (ifPodminka)
 <code>
<pre>
