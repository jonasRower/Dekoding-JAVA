# def vratSouradniceNejmensihoRozdilu(self, rozdilyAll, minRozdil):

### list of variables
minSourRSmin   
rozdilyRadek   
polozka   
if(polozka !  
minRozdil   
minSourR   
minSourS   

### code of method
```
    def vratSouradniceNejmensihoRozdilu(self, rozdilyAll, minRozdil):

        minSourRSmin = []

        for r in range(0, len(rozdilyAll)):
            rozdilyRadek = rozdilyAll[r]
            for s in range(0, len(rozdilyRadek)):
                polozka = rozdilyRadek[s]
                if(polozka != False):
                    if(polozka < minRozdil):

                        minRozdil = polozka
                        minSourR = r
                        minSourS = s

                        minSourRSmin = []

                        minSourRSmin.append(minRozdil)
                        minSourRSmin.append(minSourR)
                        minSourRSmin.append(minSourS)


        return(minSourRSmin)
```
