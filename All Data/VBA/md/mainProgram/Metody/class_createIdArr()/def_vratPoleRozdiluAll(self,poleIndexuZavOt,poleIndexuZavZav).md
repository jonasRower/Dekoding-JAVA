# def vratPoleRozdiluAll(self, poleIndexuZavOt, poleIndexuZavZav):

### list of variables
rozdilyAll   
indexZav   
<a href  

### code of method
<pre>
 <code>
    def vratPoleRozdiluAll(self, poleIndexuZavOt, poleIndexuZavZav):

        rozdilyAll = []

        for i in range(0, len(poleIndexuZavZav)):
            indexZav = poleIndexuZavZav[i]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleRozdiluKIndexuZav(self, poleIndexuZavOt, indexZav).md">rozdilyArr=self.vratPoleRozdiluKIndexuZav(poleIndexuZavOt,indexZav)</a>

            rozdilyAll.append(rozdilyArr)

        return(rozdilyAll)
 <code>
<pre>
