# def posunPoleId(self, poleId, idPosun):

### list of variables
poleIdNew   
id   
idNew   

### code of method
```
    def posunPoleId(self, poleId, idPosun):

        poleIdNew = []

        for i in range(0, len(poleId)):
            id = poleId[i]
            idNew = id + idPosun

            poleIdNew.append(idNew)

        return(poleIdNew)
```
### links

