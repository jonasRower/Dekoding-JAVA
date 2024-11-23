# def prevedSlovaJednohoRadku(self, radek, id):

### list of variables
jsonStejneId   
dvojiceradek   
dvojice   
jsonWordAtr   

### code of method
<pre>
 <code>
    def prevedSlovaJednohoRadku(self, radek, id):

        jsonStejneId = []

        for i in range(0, len(radek)):
            dvojiceradek = radek[i]
            dvojice = dvojiceradek.split("\',\'")

            jsonWordAtr = self.prevedDvojiciNaKlicHodnota(dvojice, id)
            jsonStejneId.append(jsonWordAtr + ',')

        return(jsonStejneId)
 <code>
<pre>
