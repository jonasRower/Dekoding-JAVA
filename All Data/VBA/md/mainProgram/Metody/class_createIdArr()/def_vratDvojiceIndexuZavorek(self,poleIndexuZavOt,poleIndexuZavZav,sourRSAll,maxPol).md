# def vratDvojiceIndexuZavorek(self, poleIndexuZavOt, poleIndexuZavZav, sourRSAll, maxPol):

### list of variables
dvojiceOtZavAll   
sourR   
sourS   
indexOt   
indexZav   
<a href  
dvojiceOtZav   

### code of method
<pre>
 <code>
    def vratDvojiceIndexuZavorek(self, poleIndexuZavOt, poleIndexuZavZav, sourRSAll, maxPol):

        dvojiceOtZavAll = []

        for i in range(len(sourRSAll)-1, -1, -1):
            sourR = sourRSAll[i][0]
            sourS = sourRSAll[i][1]

            indexOt = int(poleIndexuZavOt[sourS])
            indexZav = int(poleIndexuZavZav[sourR])

            # omezi hodnoty, ktere pretekaji
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_createIdArr()\def omezHodnotu(self, hodnota, hodnotaMax)">indexOt=self.omezHodnotu(indexOt,maxPol)</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_createIdArr()\def omezHodnotu(self, hodnota, hodnotaMax)">indexZav=self.omezHodnotu(indexZav,maxPol)</a>

            dvojiceOtZav = []
            dvojiceOtZav.append(indexOt)
            dvojiceOtZav.append(indexZav)

            dvojiceOtZavAll.append(dvojiceOtZav)

        return(dvojiceOtZavAll)
 <code>
<pre>

