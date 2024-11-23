# def prevedSlovaAIdNaJson(self, slovaAId):

### list of variables
jsonRadekArr   
radek   
<a href  

### code of method
<pre>
 <code>
    def prevedSlovaAIdNaJson(self, slovaAId):

        jsonRadekArr = []

        for i in range(0, len(slovaAId)):
            radek = slovaAId[i]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/jsonSlovoStr = self.vratJsonSlovoStr(radek).md">jsonRadek=self.vratRadekJson(radek)</a>

            jsonRadekArr.append(jsonRadek)

        return(jsonRadekArr)
 <code>
<pre>
