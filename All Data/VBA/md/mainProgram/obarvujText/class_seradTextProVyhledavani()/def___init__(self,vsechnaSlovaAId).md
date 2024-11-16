# def __init__(self, vsechnaSlovaAId):

### list of variables
poleSlov   
poleID   
seznamIndexuSlovUniq   
slovaAId   
self.jsonRadekArr   

### code of method
```
    def __init__(self, vsechnaSlovaAId):

        poleSlov = self.vratPole1D(vsechnaSlovaAId, 0)
        poleID = self.vratPole1D(vsechnaSlovaAId, 1)
        seznamIndexuSlovUniq = self.vratPoleIndexuVsechVyskytu(poleSlov)

        slovaAId = self.prevedIndexySlovNaId(seznamIndexuSlovUniq, poleID)
        self.jsonRadekArr = self.prevedSlovaAIdNaJson(slovaAId)

        print()
```
