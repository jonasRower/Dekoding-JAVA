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
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\NovyJAVAKod2\class_RoztahujData()\def najdiDataPrislusneTridy2(self, pozadovanyNazevSouboru)">dataPozadovaneTridy=self.najdiDataPrislusneTridy2(pozadovanaTrida)</a>

        # Najde cislo radku pozadovane metody (v dataPozadovaneTridy)
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def vratCisloRadkuNazvuMetody(self, data, nazevPozadovaneMetody)">cisloRadkuMetody=ostatniMetody.vratCisloRadkuNazvuMetody(dataPozadovaneTridy,nazevMetody)</a>

        # Najde cislo radku, kde je "{"
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def vratNejblizsiRadekSOtevrenouZavorkou(self, fromIndex, dataSlozenaZavorka)">vyjmiKodOdRadku=ostatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(cisloRadkuMetody,dataPozadovaneTridy.slozenaZavorka)</a>

        # Najde cislo radku, kde je "}"
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def vratCisloRadkuSKoncemBloku(self, fromIndex, dataSlozenaZavorka)">vyjmiKodDoRadku=ostatniMetody.vratCisloRadkuSKoncemBloku(vyjmiKodOdRadku,dataPozadovaneTridy.slozenaZavorka)</a>

        # Ziska pole radku kodu dane dokumentovane metody v dane tride
        # Jedna se o originalni data - neroztazena
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole)">KodPozadovaneMetody=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.poleRadku)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole)">VolaneMetodyUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.volanaMetoda)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole)">VolaneTridyUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.volanaTrida)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole)">ZacatekBlokuUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.zacatekBloku)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_OstatniMetody()\def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole)">KonecBlokuUvnitrMetodyPozadovane=ostatniMetody.nactiSubKod(vyjmiKodOdRadku,vyjmiKodDoRadku,0,dataPozadovaneTridy.konecBloku)</a>


        self.__dataPozadovaneTridy = dataPozadovaneTridy
        self.__poleRadkuKodu = KodPozadovaneMetody
        self.__volanaMetoda = VolaneMetodyUvnitrMetodyPozadovane
        self.__volanaTrida = VolaneTridyUvnitrMetodyPozadovane
        self.__zacatekBloku = ZacatekBlokuUvnitrMetodyPozadovane
        self.__konecBloku = KonecBlokuUvnitrMetodyPozadovane
 <code>
<pre>








