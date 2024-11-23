# def detekujZdaJeSlovoVPoli(self, pole, slovo):

### list of variables
radekObsahujeNew   
indexSlovaNew   

### code of method
<pre>
 <code>
    def detekujZdaJeSlovoVPoli(self, pole, slovo):

        radekObsahujeNew = False
        try:
            indexSlovaNew = pole.index(slovo)
            if (indexSlovaNew > -1):
                radekObsahujeNew = True
        except:
            pass

        return (radekObsahujeNew)
 <code>
<pre>
