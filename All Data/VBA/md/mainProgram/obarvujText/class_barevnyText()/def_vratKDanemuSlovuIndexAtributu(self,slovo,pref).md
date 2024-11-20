# def vratKDanemuSlovuIndexAtributu(self, slovo, pref):

### list of variables
pref   
atributNalezen   
if(atributNalezen   

### code of method
```
    def vratKDanemuSlovuIndexAtributu(self, slovo, pref):

        if (pref == 1 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.nazevInstanceAr, slovo)
            if(atributNalezen == True):
                return(1)

        if (pref == 2 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.nazevMetodyArr, slovo)
            if(atributNalezen == True):
                return(2)

        if (pref == 3 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.nazevTridyArr, slovo)
            if(atributNalezen == True):
                return(3)

        if (pref == 4 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.volanaInstanceArr, slovo)
            if(atributNalezen == True):
                return(4)

        if (pref == 5 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.volanaMetodaArr, slovo)
            if(atributNalezen == True):
                return(5)

        if (pref == 6 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.volanaTridaArr, slovo)
            if(atributNalezen == True):
                return(6)

        return(0)
```
### links
[atributNalezen=self.detekujZdaJeSlovoVPoli(self.nazevInstanceAr,slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/radekObsahujeNew_=_False.md)  
[atributNalezen=self.detekujZdaJeSlovoVPoli(self.nazevMetodyArr,slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/radekObsahujeNew_=_False.md)  
[atributNalezen=self.detekujZdaJeSlovoVPoli(self.nazevTridyArr,slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/radekObsahujeNew_=_False.md)  
[atributNalezen=self.detekujZdaJeSlovoVPoli(self.volanaInstanceArr,slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/radekObsahujeNew_=_False.md)  
[atributNalezen=self.detekujZdaJeSlovoVPoli(self.volanaMetodaArr,slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/radekObsahujeNew_=_False.md)  
[atributNalezen=self.detekujZdaJeSlovoVPoli(self.volanaTridaArr,slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/radekObsahujeNew_=_False.md)  
