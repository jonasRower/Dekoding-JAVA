# def vratPoleRozdiluKIndexuZav(self, poleIndexuZavOt, indexZav):

### list of variables
rozdilyArr   
indexOt   
rozdil   

### code of method
<pre>
 <code>
    def vratPoleRozdiluKIndexuZav(self, poleIndexuZavOt, indexZav):

        rozdilyArr = []

        for i in range(0, len(poleIndexuZavOt)):
            indexOt = poleIndexuZavOt[i]
            rozdil = indexZav - indexOt

            if(rozdil < 0):
                rozdil = False

            rozdilyArr.append(rozdil)

        return(rozdilyArr)
 <code>
<pre>
