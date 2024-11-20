# def detekujZdaJeSlovoVPoli(self, pole, slovo):

### list of variables
radekObsahujeNew   
indexSlovaNew   

### code of method
```
    def detekujZdaJeSlovoVPoli(self, pole, slovo):

        radekObsahujeNew = False
        try:
            indexSlovaNew = pole.index(slovo)
            if (indexSlovaNew > -1):
                radekObsahujeNew = True
        except:
            pass

        return (radekObsahujeNew)
```
### links

