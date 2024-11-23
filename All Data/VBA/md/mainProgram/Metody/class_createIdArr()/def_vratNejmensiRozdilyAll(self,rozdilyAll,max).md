# def vratNejmensiRozdilyAll(self, rozdilyAll, max):

### list of variables
vybraneNejmensiIndexyArr   
radekRozdilu   
<a href  

### code of method
<pre>
 <code>
    def vratNejmensiRozdilyAll(self, rozdilyAll, max):

        vybraneNejmensiIndexyArr = []

        for i in range(0, len(rozdilyAll)):
            radekRozdilu = rozdilyAll[i]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratIndexNejmensihoRozdilZRadku(self, radekRozdilu, max).md">indexNejmensihoRozdilu=self.vratIndexNejmensihoRozdilZRadku(radekRozdilu,max)</a>

            vybraneNejmensiIndexyArr.append(indexNejmensihoRozdilu)

            # nastavi jiz vybrane polozky jako False, tak aby je jiz nevybiral znovu
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_oznacJizVybraneRozdily(self, rozdilyAll, vybranyIndex).md">rozdilyAll=self.oznacJizVybraneRozdily(rozdilyAll,indexNejmensihoRozdilu)</a>

        return(vybraneNejmensiIndexyArr)
 <code>
<pre>

