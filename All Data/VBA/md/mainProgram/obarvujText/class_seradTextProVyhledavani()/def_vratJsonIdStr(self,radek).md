# def vratJsonIdStr(self, radek):

### list of variables
jsonIdStr   
id   

### code of method
```
    def vratJsonIdStr(self, radek):

        jsonIdStr = '"id": ["'

        for i in range(1, len(radek)):
            id = radek[i]
            jsonIdStr = jsonIdStr + str(id) + '"'

            if(i < len(radek)-1):
                jsonIdStr = jsonIdStr + ', "'

            else:
                jsonIdStr = jsonIdStr + '] },'

        return(jsonIdStr)
```
