# def checkPoleZavorek2(self, poleZavorek, poleZavorek2):

### list of variables
zavorka1   
zavorka2   
if(zavorka1 !  
if(zavorka1   
poleZavorek2[i]   

### code of method
```
    def checkPoleZavorek2(self, poleZavorek, poleZavorek2):

        for i in range(0, len(poleZavorek)):
            zavorka1 = poleZavorek[i]
            zavorka2 = poleZavorek2[i]

            if(zavorka1 != ""):
                if(zavorka1 == zavorka2):
                    poleZavorek2[i] = ""

        return(poleZavorek2)
```
