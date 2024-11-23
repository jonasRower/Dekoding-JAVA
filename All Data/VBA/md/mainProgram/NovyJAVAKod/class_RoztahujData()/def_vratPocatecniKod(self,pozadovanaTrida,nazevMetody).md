# def vratPocatecniKod(self, pozadovanaTrida, nazevMetody):

### list of variables
ostatniMetody   
<a href  
self.__dataPozadovaneTridy   
self.__poleRadkuKodu   
self.__volanaMetoda   
self.__volanaTrida   
self.__zacatekBloku   
self.__konecBloku   

### code of method
<pre>
 <code>
    def vratPocatecniKod(self, pozadovanaTrida, nazevMetody):

        # inicializuji tridu pro ostatni metody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # nalezne data pro tridu, ktera se bude dokumentovat
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,pozadovanyNazevSouboru).md">dataPozadovaneTridy=self.najdiDataPrislusneTridy2(pozadovanaTrida)</a>

        # Najde cislo radku pozadovane metody (v dataPozadovaneTridy)
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_vratCisloRadkuNazvuMetody(self,data,nazevPozadovaneMetody).md">cisloRadkuMetody=ostatniMetody.vratCisloRadkuNazvuMetody(dataPozadovaneTridy,nazevMetody)</a>

        # Najde cislo radku, kde je "{"
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_vratNejblizsiRadekSOtevrenouZavorkou(self,fromIndex,dataSlozenaZavorka).md">vyjmiKodOdRadku=ostatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(cisloRadkuMetody,dataPozadovaneTridy.slozenaZavorka)</a>

        # Najde cislo radku, kde je "}"
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_vratCisloRadkuSKoncemBloku(self,fromIndex,dataSlozenaZavorka).md">vyjmiKodDoRadku=ostatniMetody.vratCisloRadkuSKoncemBloku(vyjmiKodOdRadku,dataPozadovaneTridy.slozenaZavorka)</a>

        # Ziska pole radku kodu dane dokumentovane metody v dane tride
        # Jedna se o originalni data - neroztazena
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_nactiSubKod(self,prvniRadek,posledniRadek,pocetMezer,dataPole).md">KodPozadovaneMetody=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.poleRadku)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_nactiSubKod(self,prvniRadek,posledniRadek,pocetMezer,dataPole).md">VolaneMetodyUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.volanaMetoda)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_nactiSubKod(self,prvniRadek,posledniRadek,pocetMezer,dataPole).md">VolaneTridyUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.volanaTrida)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_nactiSubKod(self,prvniRadek,posledniRadek,pocetMezer,dataPole).md">ZacatekBlokuUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.zacatekBloku)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_nactiSubKod(self,prvniRadek,posledniRadek,pocetMezer,dataPole).md">KonecBlokuUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.konecBloku)</a>

        self.__dataPozadovaneTridy = dataPozadovaneTridy
        self.__poleRadkuKodu = KodPozadovaneMetody
        self.__volanaMetoda = VolaneMetodyUvnitrMetodyPozadovane
        self.__volanaTrida = VolaneTridyUvnitrMetodyPozadovane
        self.__zacatekBloku = ZacatekBlokuUvnitrMetodyPozadovane
        self.__konecBloku = KonecBlokuUvnitrMetodyPozadovane
 <code>
<pre>








