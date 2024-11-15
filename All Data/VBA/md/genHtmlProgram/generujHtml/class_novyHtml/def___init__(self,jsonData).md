# def __init__(self, jsonData):

### list of variables
poleRadkuAll   

### code of method
```
    def __init__(self, jsonData):

        poleRadkuAll = self.vytvorPoleRadkuHtml(jsonData)
        log.generujLog.loguData("index.html", poleRadkuAll, False)
```
