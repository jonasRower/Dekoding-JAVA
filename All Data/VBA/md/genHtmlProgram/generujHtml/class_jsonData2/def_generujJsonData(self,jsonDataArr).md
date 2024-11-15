# def generujJsonData(self, jsonDataArr):

### list of variables
jsonData   
id   
parent   
text   
redek   

### code of method
```
    def generujJsonData(self, jsonDataArr):

        jsonData = []

        for i in range(0, len(jsonDataArr)):
            id = jsonDataArr[i][0]
            parent = jsonDataArr[i][1]
            text = jsonDataArr[i][2]

            text = text.replace("\n", "")
            text = text.replace('\"', '\'')

            redek = self.zapisJsonData(id, parent, text)
            jsonData.append(redek)

        return (jsonData)
```
