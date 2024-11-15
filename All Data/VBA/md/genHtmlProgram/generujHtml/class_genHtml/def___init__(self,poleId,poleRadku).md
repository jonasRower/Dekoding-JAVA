# def __init__(self, poleId, poleRadku):

### list of variables
jsonDataClass   
jsonData   
html   

### code of method
```
    def __init__(self, poleId, poleRadku):

        jsonDataClass = jsonData2(poleId, poleRadku)
        jsonData = jsonDataClass.getJsonData()

        html = novyHtml(jsonData)
        log.generujLog.loguData("jsTree.json", jsonData, True)
```
