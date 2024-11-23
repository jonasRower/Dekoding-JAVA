# def generujJsonData(self, jsonDataArr):

### list of variables
jsonData   
id   
parent   
text   
<a href  

### code of method
<pre>
 <code>
    def generujJsonData(self, jsonDataArr):

        jsonData = []

        for i in range(0, len(jsonDataArr)):
            id = jsonDataArr[i][0]
            parent = jsonDataArr[i][1]
            text = jsonDataArr[i][2]

            text = text.replace("\n", "")
            text = text.replace('\"', '\'')

              <a href="../../../../../../All%20Data/VBA/md/genHtmlProgram/generujHtml/class_jsonData2/def_zapisJsonData(self, id, parent, text).md">redek=self.zapisJsonData(id,parent,text)</a>
            jsonData.append(redek)

        return (jsonData)
 <code>
<pre>
