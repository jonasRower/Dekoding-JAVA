# def prevedIndexySlovNaId(self, seznamIndexuSlovUniq, poleID):

### list of variables
slovaAId   
radek   
slovo   
seznamId   

### code of method
```
    def prevedIndexySlovNaId(self, seznamIndexuSlovUniq, poleID):

        slovaAId = []

        for i in range(0, len(seznamIndexuSlovUniq)):
            radek = seznamIndexuSlovUniq[i]
            slovo = radek[0]
            seznamId = self.vratIDDleIndexuRadku(radek, slovo, poleID)

            slovaAId.append(seznamId)

        return(slovaAId)
```
