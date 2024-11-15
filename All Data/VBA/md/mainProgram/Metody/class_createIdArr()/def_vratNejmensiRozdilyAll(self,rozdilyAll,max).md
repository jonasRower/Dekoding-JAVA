# def vratNejmensiRozdilyAll(self, rozdilyAll, max):

### list of variables
vybraneNejmensiIndexyArr   
radekRozdilu   
indexNejmensihoRozdilu   
rozdilyAll   

### code of method
```
    def vratNejmensiRozdilyAll(self, rozdilyAll, max):

        vybraneNejmensiIndexyArr = []

        for i in range(0, len(rozdilyAll)):
            radekRozdilu = rozdilyAll[i]
            indexNejmensihoRozdilu = self.vratIndexNejmensihoRozdilZRadku(radekRozdilu, max)

            vybraneNejmensiIndexyArr.append(indexNejmensihoRozdilu)

            # nastavi jiz vybrane polozky jako False, tak aby je jiz nevybiral znovu
            rozdilyAll = self.oznacJizVybraneRozdily(rozdilyAll, indexNejmensihoRozdilu)

        return(vybraneNejmensiIndexyArr)
```
