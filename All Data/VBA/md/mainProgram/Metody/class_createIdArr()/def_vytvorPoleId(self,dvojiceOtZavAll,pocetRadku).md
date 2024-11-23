# def vytvorPoleId(self, dvojiceOtZavAll, pocetRadku):

### list of variables
poleId   
odInd   
doInd   
<a href  

### code of method
<pre>
 <code>
    def vytvorPoleId(self, dvojiceOtZavAll, pocetRadku):

        poleId = []

        # vytvori prazdne pole
        for i in range(0, pocetRadku):
            poleId.append(0)

        # postupne prepisuje id
        for i in range(0, len(dvojiceOtZavAll)):
            odInd = dvojiceOtZavAll[i][0]
            doInd = dvojiceOtZavAll[i][1]

              <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_createIdArr()\def vratPoleIdDleOdDo(self, poleId, odInd, doInd)">poleId=self.vratPoleIdDleOdDo(poleId,odInd,doInd)</a>

        return(poleId)
 <code>
<pre>
