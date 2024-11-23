# def vratIDDleIndexuRadku(self, radek, slovo, poleID):

### list of variables
slovoAId   
indexRadku   
id   

### code of method
<pre>
 <code>
    def vratIDDleIndexuRadku(self, radek, slovo, poleID):

        slovoAId = []
        slovoAId.append(slovo)

        for i in range(1, len(radek)):
            indexRadku = radek[i]
            id = poleID[indexRadku]
            slovoAId.append(id)

        return(slovoAId)
 <code>
<pre>
