# def vratPoleDatJson(self, poleIdParents, poleRadku):

### list of variables
jsonDataArr   
id   
i   
idParent   
radek   
radekJsonDataArr   

### code of method
<pre>
 <code>
    def vratPoleDatJson(self, poleIdParents, poleRadku):


        jsonDataArr = []

        for i in range(0, len(poleRadku)):

            id = str(i)

            if (i == 0):
                idParent = '#'
            else:
                idParent = str(poleIdParents[i])
                if (idParent == "-1"):
                    idParent = '0'


            radek = poleRadku[i]

            radekJsonDataArr = []
            radekJsonDataArr.append(id)
            radekJsonDataArr.append(idParent)
            radekJsonDataArr.append(radek)

            jsonDataArr.append(radekJsonDataArr)

        return (jsonDataArr)
 <code>
<pre>
