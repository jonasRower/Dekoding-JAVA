# def vyhledavejNejmensiRozdily(self, rozdilyAll, maxPol):

### list of variables
minSourRSmin   
sourRSAll   
minRozdil   
<a href  
if(minSourRSmin   
sourR   
sourS   
sourRS   

### code of method
<pre>
 <code>
    def vyhledavejNejmensiRozdily(self, rozdilyAll, maxPol):

        minSourRSmin = []
        minSourRSmin.append(maxPol)

        sourRSAll = []

        for i in range(0, maxPol):
            minRozdil = minSourRSmin[0]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratSouradniceNejmensihoRozdilu(self,rozdilyAll,minRozdil).md">minSourRSmin=self.vratSouradniceNejmensihoRozdilu(rozdilyAll,maxPol*maxPol)</a>

            if(minSourRSmin == []):
                break

            sourR = minSourRSmin[1]
            sourS = minSourRSmin[2]

            sourRS = []
            sourRS.append(sourR)
            sourRS.append(sourS)

            sourRSAll.append(sourRS)

              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_zneplatniDanyRadekASloupec(self,rozdilyAll,sourR,sourS).md">rozdilyAll=self.zneplatniDanyRadekASloupec(rozdilyAll,sourR,sourS)</a>
            print()

        return(sourRSAll)
 <code>
<pre>

