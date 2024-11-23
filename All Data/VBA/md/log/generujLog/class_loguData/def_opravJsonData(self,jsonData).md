# def opravJsonData(self, jsonData):

### list of variables
posledniRadek   
lastChar   
if(lastChar   
jsonData[len(jsonData) - 1]   
jsonDataNew   

### code of method
<pre>
 <code>
    def opravJsonData(self, jsonData):

        posledniRadek = jsonData[len(jsonData)-1]
        lastChar = posledniRadek[-1]

        if(lastChar == ','):
            posledniRadek = posledniRadek[:-1]

        jsonData[len(jsonData) - 1] = posledniRadek


        jsonDataNew = []
        jsonDataNew.append('[')
        jsonDataNew = jsonDataNew + jsonData
        jsonDataNew.append(']')
 <code>
<pre>
