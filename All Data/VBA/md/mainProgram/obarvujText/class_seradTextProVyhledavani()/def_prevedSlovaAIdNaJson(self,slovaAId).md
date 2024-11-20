# def prevedSlovaAIdNaJson(self, slovaAId):

### list of variables
jsonRadekArr   
radek   
jsonRadek   

### code of method
```
    def prevedSlovaAIdNaJson(self, slovaAId):

        jsonRadekArr = []

        for i in range(0, len(slovaAId)):
            radek = slovaAId[i]
            jsonRadek = self.vratRadekJson(radek)

            jsonRadekArr.append(jsonRadek)

        return(jsonRadekArr)
```
### links
[jsonRadek=self.vratRadekJson(radek)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/jsonSlovoStr_=_self.vratJsonSlovoStr(radek).md)  
