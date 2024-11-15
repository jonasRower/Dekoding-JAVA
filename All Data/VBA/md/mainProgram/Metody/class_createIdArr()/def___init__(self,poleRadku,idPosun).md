# def __init__(self, poleRadku, idPosun):

### list of variables
poleZavorek   
poleRadku2   
poleZavorek2   
dvojiceOtZavAll   
poleId   
self.poleIdPosunute   

### code of method
```
    def __init__(self, poleRadku, idPosun):

        """
        poleZavorek = self.vratPoleZavorek(poleRadku)

        # muze se stat, ze je uzavrena zavorka na zacatku radku, pak vraci radky bez 1. znaku
        poleRadku2 = self.vratPoleRadkuBezZavorekNaZacatkuRadku(poleRadku)
        poleZavorek2 = self.vratPoleZavorek(poleRadku2)

        poleZavorek2 = self.checkPoleZavorek2(poleZavorek, poleZavorek2)
        """

        poleZavorek = self.vratPouzePrazdnePoleZavorek(False, len(poleRadku))
        poleZavorek2 = self.vratPouzePrazdnePoleZavorek(True, len(poleRadku))

        dvojiceOtZavAll = self.vratPoleDvojicZavOtZav(poleZavorek, poleZavorek2, len(poleRadku))
        poleId = self.vytvorPoleId(dvojiceOtZavAll, len(poleRadku))
        self.poleIdPosunute = self.posunPoleId(poleId, idPosun)
```
