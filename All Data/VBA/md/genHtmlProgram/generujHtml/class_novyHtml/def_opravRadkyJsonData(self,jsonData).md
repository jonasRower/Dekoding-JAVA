# def opravRadkyJsonData(self, jsonData):

### list of variables
radek   
jsonData[i]   

### code of method
```
    def opravRadkyJsonData(self, jsonData):

        for i in range(0, len(jsonData)):
            radek = jsonData[i]
            radek = radek.replace('§', '/')
            radek = radek.replace('\\\"', '\\')

            jsonData[i] = radek

        return (jsonData)
```
