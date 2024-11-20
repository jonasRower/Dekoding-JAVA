# def vratDvojiceIndexuZavorek(self, poleIndexuZavOt, poleIndexuZavZav, sourRSAll, maxPol):

### list of variables
dvojiceOtZavAll   
sourR   
sourS   
indexOt   
indexZav   
dvojiceOtZav   

### code of method
```
    def vratDvojiceIndexuZavorek(self, poleIndexuZavOt, poleIndexuZavZav, sourRSAll, maxPol):

        dvojiceOtZavAll = []

        for i in range(len(sourRSAll)-1, -1, -1):
            sourR = sourRSAll[i][0]
            sourS = sourRSAll[i][1]

            indexOt = int(poleIndexuZavOt[sourS])
            indexZav = int(poleIndexuZavZav[sourR])

            # omezi hodnoty, ktere pretekaji
            indexOt = self.omezHodnotu(indexOt, maxPol)
            indexZav = self.omezHodnotu(indexZav, maxPol)

            dvojiceOtZav = []
            dvojiceOtZav.append(indexOt)
            dvojiceOtZav.append(indexZav)

            dvojiceOtZavAll.append(dvojiceOtZav)

        return(dvojiceOtZavAll)
```
### links
[indexOt=self.omezHodnotu(indexOt,maxPol)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_omezHodnotu(self,_hodnota,_hodnotaMax).md)  
[indexZav=self.omezHodnotu(indexZav,maxPol)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_omezHodnotu(self,_hodnota,_hodnotaMax).md)  
