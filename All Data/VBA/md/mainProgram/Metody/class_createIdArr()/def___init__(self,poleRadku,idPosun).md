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
### links
[poleZavorek=self.vratPoleZavorek(poleRadku)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleZavorek(self,_poleRadku).md)  
[poleRadku2=self.vratPoleRadkuBezZavorekNaZacatkuRadku(poleRadku)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleRadkuBezZavorekNaZacatkuRadku(self,_poleRadku).md)  
[poleZavorek2=self.vratPoleZavorek(poleRadku2)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleZavorek(self,_poleRadku).md)  
[poleZavorek2=self.checkPoleZavorek2(poleZavorek,poleZavorek2)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_checkPoleZavorek2(self,_poleZavorek,_poleZavorek2).md)  
[poleZavorek=self.vratPouzePrazdnePoleZavorek(False,len(poleRadku))](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPouzePrazdnePoleZavorek(self,_uplnePrazdne,_delkaPole).md)  
[poleZavorek2=self.vratPouzePrazdnePoleZavorek(True,len(poleRadku))](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPouzePrazdnePoleZavorek(self,_uplnePrazdne,_delkaPole).md)  
[dvojiceOtZavAll=self.vratPoleDvojicZavOtZav(poleZavorek,poleZavorek2,len(poleRadku))](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleDvojicZavOtZav(self,_poleZavorek,_poleZavorek2,_max).md)  
[poleId=self.vytvorPoleId(dvojiceOtZavAll,len(poleRadku))](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vytvorPoleId(self,_dvojiceOtZavAll,_pocetRadku).md)  
[self.poleIdPosunute=self.posunPoleId(poleId,idPosun)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_posunPoleId(self,_poleId,_idPosun).md)  
