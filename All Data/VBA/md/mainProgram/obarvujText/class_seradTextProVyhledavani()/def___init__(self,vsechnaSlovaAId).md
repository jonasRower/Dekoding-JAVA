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
### links
[poleSlov=self.vratPole1D(vsechnaSlovaAId,0)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/poleSlov_=_[].md)  
[seznamIndexuSlovUniq=self.vratPoleIndexuVsechVyskytu(poleSlov)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/poleSlovUniq_=_self.unique(poleSlov).md)  
[self.jsonRadekArr=self.prevedSlovaAIdNaJson(slovaAId)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/jsonRadekArr_=_[].md)  
