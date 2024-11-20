# def vratRadekJson(self, radek):

### list of variables
jsonSlovoStr   
jsonIdStr   
jsonRadek   

### code of method
```
    def vratRadekJson(self, radek):

        jsonSlovoStr = self.vratJsonSlovoStr(radek)
        jsonIdStr = self.vratJsonIdStr(radek)

        jsonRadek = jsonSlovoStr + jsonIdStr

        return(jsonRadek)
```
### links
[jsonIdStr=self.vratJsonIdStr(radek)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/jsonIdStr_=_'"id"_["'.md)  
