# def vytvorPoleRadkuHtml(self, jsonData):

### list of variables
jsonData   
radkyPred   
radkyZa   
poleRadkuAll   

### code of method
```
    def vytvorPoleRadkuHtml(self, jsonData):

        # oprav jen texty, nikoliv cele radky!!
        jsonData = self.opravRadkyJsonData(jsonData)

        radkyPred = self.definujRadkyPred()
        radkyZa = self.definujRadkyZa()

        poleRadkuAll = radkyPred
        poleRadkuAll = poleRadkuAll + jsonData
        poleRadkuAll = poleRadkuAll + radkyZa

        return(poleRadkuAll)
```
