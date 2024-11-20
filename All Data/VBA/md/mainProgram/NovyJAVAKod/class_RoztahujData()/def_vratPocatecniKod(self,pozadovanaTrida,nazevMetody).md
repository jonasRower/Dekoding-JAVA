# def vratPocatecniKod(self, pozadovanaTrida, nazevMetody):

### list of variables
ostatniMetody   
dataPozadovaneTridy   
cisloRadkuMetody   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
KodPozadovaneMetody   
VolaneMetodyUvnitrMetodyPozadovane   
VolaneTridyUvnitrMetodyPozadovane   
ZacatekBlokuUvnitrMetodyPozadovane   
KonecBlokuUvnitrMetodyPozadovane   
self.__dataPozadovaneTridy   
self.__poleRadkuKodu   
self.__volanaMetoda   
self.__volanaTrida   
self.__zacatekBloku   
self.__konecBloku   

### code of method
```
    def vratPocatecniKod(self, pozadovanaTrida, nazevMetody):

        # inicializuji tridu pro ostatni metody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # nalezne data pro tridu, ktera se bude dokumentovat
        dataPozadovaneTridy = self.najdiDataPrislusneTridy2(pozadovanaTrida)

        # Najde cislo radku pozadovane metody (v dataPozadovaneTridy)
        cisloRadkuMetody = ostatniMetody.vratCisloRadkuNazvuMetody(dataPozadovaneTridy, nazevMetody)

        # Najde cislo radku, kde je "{"
        vyjmiKodOdRadku = ostatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(cisloRadkuMetody, dataPozadovaneTridy.slozenaZavorka)

        # Najde cislo radku, kde je "}"
        vyjmiKodDoRadku = ostatniMetody.vratCisloRadkuSKoncemBloku(vyjmiKodOdRadku, dataPozadovaneTridy.slozenaZavorka)

        # Ziska pole radku kodu dane dokumentovane metody v dane tride
        # Jedna se o originalni data - neroztazena
        KodPozadovaneMetody = ostatniMetody.nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, 0, dataPozadovaneTridy.poleRadku)
        VolaneMetodyUvnitrMetodyPozadovane = ostatniMetody.nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, 0, dataPozadovaneTridy.volanaMetoda)
        VolaneTridyUvnitrMetodyPozadovane = ostatniMetody.nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, 0, dataPozadovaneTridy.volanaTrida)
        ZacatekBlokuUvnitrMetodyPozadovane = ostatniMetody.nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, 0, dataPozadovaneTridy.zacatekBloku)
        KonecBlokuUvnitrMetodyPozadovane = ostatniMetody.nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, 0, dataPozadovaneTridy.konecBloku)

        self.__dataPozadovaneTridy = dataPozadovaneTridy
        self.__poleRadkuKodu = KodPozadovaneMetody
        self.__volanaMetoda = VolaneMetodyUvnitrMetodyPozadovane
        self.__volanaTrida = VolaneTridyUvnitrMetodyPozadovane
        self.__zacatekBloku = ZacatekBlokuUvnitrMetodyPozadovane
        self.__konecBloku = KonecBlokuUvnitrMetodyPozadovane
```
### links
[dataPozadovaneTridy=self.najdiDataPrislusneTridy2(pozadovanaTrida)](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
[cisloRadkuMetody=ostatniMetody.vratCisloRadkuNazvuMetody(dataPozadovaneTridy,nazevMetody)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_vratCisloRadkuNazvuMetody(self,_data,_nazevPozadovaneMetody).md)  
[#Jednaseooriginalnidata-neroztazena](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_OstatniMetody()/def_vratCisloRadkuNazvuMetody(self,_data,_nazevPozadovaneMetody).md)  
[KodPozadovaneMetody=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.poleRadku)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_nactiSubKod(self,_prvniRadek,_posledniRadek,_pocetMezer,_dataPole).md)  
