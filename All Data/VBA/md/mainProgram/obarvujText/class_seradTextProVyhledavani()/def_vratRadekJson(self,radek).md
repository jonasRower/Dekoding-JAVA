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
