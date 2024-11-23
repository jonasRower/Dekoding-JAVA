# def spocitejPocetMezerPredKodemNaRadku(self, radekKodu):

### list of variables
pocetMezer   
znakyRadku   
znak.isspace()   

### code of method
<pre>
 <code>
    def spocitejPocetMezerPredKodemNaRadku(self, radekKodu):
        pocetMezer = 0

        znakyRadku = list(radekKodu)
        for znak in znakyRadku:
            if (znak.isspace() == True):
                pocetMezer = pocetMezer + 1

        return (pocetMezer)
 <code>
<pre>
