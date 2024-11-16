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
