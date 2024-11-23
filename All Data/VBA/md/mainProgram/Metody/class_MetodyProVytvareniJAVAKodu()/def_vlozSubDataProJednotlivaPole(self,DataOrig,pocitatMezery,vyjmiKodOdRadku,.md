# def vlozSubDataProJednotlivaPole(self, DataOrig, pocitatMezery, vyjmiKodOdRadku,

### list of variables
dataNovy   
dataNew   
pocitatMezery   
pocetMezerPredKodem   
<a href  

### code of method
<pre>
 <code>
    def vlozSubDataProJednotlivaPole(self, DataOrig, pocitatMezery, vyjmiKodOdRadku,
                                     vyjmiKodDoRadku, vkladejOdRadku, dataZdroj, pozadovanaHodnota):


        dataNovy = []
        dataNew = []

        #jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu("")

        # pokud se jedna o pole radku kodu, pak pocita mezery, u jinych typu dat to nema vyznam
        if (pocitatMezery == True):
            pocetMezerPredKodem = OstatniMetody.spocitejPocetMezerPredKodemNaRadku(self, DataOrig[vkladejOdRadku])
        else:
           pocetMezerPredKodem = 0

        if (vyjmiKodOdRadku > -1):
            dataNovy = OstatniMetody.nactiSubKod(self, vyjmiKodOdRadku, vyjmiKodDoRadku, pocetMezerPredKodem, dataZdroj)

            # prepise prazdne hodnoty hodnotami pozadovanymi
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_prepisPolozkySubKodu(self, dataPole, hodnota).md">dataNovy=self.prepisPolozkySubKodu(dataNovy,pozadovanaHodnota)</a>

            #vkladam data o 2 radky nize, kvuli tomu, ze obcas jsou posunute zavorky
            dataNew = OstatniMetody.vlozSubKodDoKodu(self, DataOrig, dataNovy, vkladejOdRadku + 2)
        else:
            dataNew = DataOrig

        return (dataNew)
 <code>
<pre>
