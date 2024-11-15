# def __init__(self, poleId, poleRadku):

### list of variables
jsonDataArr   
self.jsonData   

### code of method
```
    def __init__(self, poleId, poleRadku):

        jsonDataArr = self.vratPoleDatJson(poleId, poleRadku)
        self.jsonData = self.generujJsonData(jsonDataArr)
```
