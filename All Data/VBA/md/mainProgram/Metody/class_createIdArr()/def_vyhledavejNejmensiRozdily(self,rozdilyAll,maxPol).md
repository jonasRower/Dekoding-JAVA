# def vyhledavejNejmensiRozdily(self, rozdilyAll, maxPol):

### list of variables
minSourRSmin   
sourRSAll   
minRozdil   
if(minSourRSmin   
sourR   
sourS   
sourRS   
rozdilyAll   

### code of method
```
    def vyhledavejNejmensiRozdily(self, rozdilyAll, maxPol):

        minSourRSmin = []
        minSourRSmin.append(maxPol)

        sourRSAll = []

        for i in range(0, maxPol):
            minRozdil = minSourRSmin[0]
            minSourRSmin = self.vratSouradniceNejmensihoRozdilu(rozdilyAll, maxPol*maxPol)

            if(minSourRSmin == []):
                break

            sourR = minSourRSmin[1]
            sourS = minSourRSmin[2]

            sourRS = []
            sourRS.append(sourR)
            sourRS.append(sourS)

            sourRSAll.append(sourRS)

            rozdilyAll = self.zneplatniDanyRadekASloupec(rozdilyAll, sourR, sourS)
            print()

        return(sourRSAll)
```
### links
[minSourRSmin=self.vratSouradniceNejmensihoRozdilu(rozdilyAll,maxPol*maxPol)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratSouradniceNejmensihoRozdilu(self,_rozdilyAll,_minRozdil).md)  
[rozdilyAll=self.zneplatniDanyRadekASloupec(rozdilyAll,sourR,sourS)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_zneplatniDanyRadekASloupec(self,_rozdilyAll,_sourR,_sourS).md)  
