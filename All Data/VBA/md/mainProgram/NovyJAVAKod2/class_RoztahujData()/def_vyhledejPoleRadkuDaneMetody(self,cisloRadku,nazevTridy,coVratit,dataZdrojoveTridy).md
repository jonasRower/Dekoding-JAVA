# def vyhledejPoleRadkuDaneMetody(self, cisloRadku, nazevTridy, coVratit, dataZdrojoveTridy):

### list of variables
nazevTridy   
if(nazevTridy   
coVratit   
poleDat   
nazevSouboru   
a   
dataDaneTridy   
if(dataDaneTridy   

### code of method
```
    def vyhledejPoleRadkuDaneMetody(self, cisloRadku, nazevTridy, coVratit, dataZdrojoveTridy):
        nazevTridy = dataZdrojoveTridy.volanaTrida[cisloRadku-1]
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
            if (coVratit == "poleRadku"):
               a = 4

            dataDaneTridy = self.najdiDataPrislusneTridy2(nazevSouboru)
            if (coVratit == "poleRadku"):
                if(dataDaneTridy == ""):
                    poleDat = self.__dataPozadovaneTridy.poleRadku
                else:
                    poleDat = dataDaneTridy.poleRadku

            if (coVratit == "volanaMetoda"):
                if (dataDaneTridy == ""):
                    poleDat = self.__dataPozadovaneTridy.volanaMetoda
                else:
                    poleDat = dataDaneTridy.volanaMetoda

            if (coVratit == "volanaTrida"):
                if (dataDaneTridy == ""):
                    poleDat = self.__dataPozadovaneTridy.volanaTrida
                else:
                    poleDat = dataDaneTridy.volanaTrida

            if (coVratit == "zacatekBloku"):
                if (dataDaneTridy == ""):
                   poleDat = self.__dataPozadovaneTridy.zacatekBloku
                else:
                    poleDat = dataDaneTridy.zacatekBloku

            if (coVratit == "konecBloku"):
                if (dataDaneTridy == ""):
                    poleDat = self.__dataPozadovaneTridy.konecBloku
                else:
                    poleDat = dataDaneTridy.konecBloku


        return(poleDat)
```
### links





[dataDaneTridy=self.najdiDataPrislusneTridy2(nazevSouboru)](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
[poleDat=self.__dataPozadovaneTridy.poleRadku](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
[poleDat=self.__dataPozadovaneTridy.volanaMetoda](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
[poleDat=self.__dataPozadovaneTridy.volanaTrida](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
[poleDat=self.__dataPozadovaneTridy.zacatekBloku](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
[poleDat=self.__dataPozadovaneTridy.konecBloku](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
