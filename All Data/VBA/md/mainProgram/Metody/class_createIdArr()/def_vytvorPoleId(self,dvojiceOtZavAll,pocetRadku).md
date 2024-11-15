# def vytvorPoleId(self, dvojiceOtZavAll, pocetRadku):

### list of variables
poleId   
odInd   
doInd   

### code of method
```
    def vytvorPoleId(self, dvojiceOtZavAll, pocetRadku):

        poleId = []

        # vytvori prazdne pole
        for i in range(0, pocetRadku):
            poleId.append(0)

        # postupne prepisuje id
        for i in range(0, len(dvojiceOtZavAll)):
            odInd = dvojiceOtZavAll[i][0]
            doInd = dvojiceOtZavAll[i][1]

            poleId = self.vratPoleIdDleOdDo(poleId, odInd, doInd)

        return(poleId)
```
