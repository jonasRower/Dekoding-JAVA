# def prevedPoleStrNaPoleInt(self, poleStr):

### list of variables
poleIntArr   
radek   
radekIntArr   

### code of method
```
    def prevedPoleStrNaPoleInt(self, poleStr):

        poleIntArr = []

        for i in range(0, len(poleStr)):
            radek = poleStr[i]
            radekIntArr = self.prevedRadekNaRadekArr(radek)
            poleIntArr.append(radekIntArr)

        return(poleIntArr)
```
