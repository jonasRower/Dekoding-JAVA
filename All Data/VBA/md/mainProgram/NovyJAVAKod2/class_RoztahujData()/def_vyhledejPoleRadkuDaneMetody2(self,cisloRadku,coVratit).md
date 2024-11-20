# def vyhledejPoleRadkuDaneMetody2(self, cisloRadku, coVratit):

### list of variables
nazevTridy   
if(nazevTridy   
coVratit   
poleDat   
nazevSouboru   
dataDaneTridy   

### code of method
```
    def vyhledejPoleRadkuDaneMetody2(self, cisloRadku, coVratit):
        nazevTridy = self.__dataPozadovaneTridy.volanaTrida[cisloRadku-1]
        if(nazevTridy == ""):
            if (coVratit == "poleRadku"):
                poleDat = self.__dataPozadovaneTridy.poleRadku
            if (coVratit == "volanaMetoda"):
                poleDat = self.__dataPozadovaneTridy.volanaMetoda
            if (coVratit == "volanaTrida"):
                poleDat = self.__dataPozadovaneTridy.volanaTrida
            if (coVratit == "zacatekBloku"):
                poleDat = self.__dataPozadovaneTridy.zacatekBloku
            if (coVratit == "konecBloku"):
                poleDat = self.__dataPozadovaneTridy.konecBloku
        else:
            nazevSouboru = nazevTridy + ".java"
            dataDaneTridy = self.najdiDataPrislusneTridy(nazevSouboru)
            if (coVratit == "poleRadku"):
                poleDat = dataDaneTridy.poleRadku
            if (coVratit == "volanaMetoda"):
                poleDat = dataDaneTridy.volanaMetoda
            if (coVratit == "volanaTrida"):
                poleDat = dataDaneTridy.volanaTrida
            if (coVratit == "zacatekBloku"):
                poleDat = dataDaneTridy.zacatekBloku
            if (coVratit == "konecBloku"):
                poleDat = dataDaneTridy.konecBloku

        return(poleDat)
```
### links






[dataDaneTridy=self.najdiDataPrislusneTridy(nazevSouboru)](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy(self,_pozadovanyNazevSouboru,_dataZdrojoveTridy).md)  
