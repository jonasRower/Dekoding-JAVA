# def vlozSubDataProJednotlivaPole(self, DataOrig, pocitatMezery, vyjmiKodOdRadku,

### list of variables
dataNovy   
dataNew   
if (pocitatMezery   
pocetMezerPredKodem   

### code of method
```
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
            dataNovy = self.prepisPolozkySubKodu(dataNovy, pozadovanaHodnota)

            #vkladam data o 2 radky nize, kvuli tomu, ze obcas jsou posunute zavorky
            dataNew = OstatniMetody.vlozSubKodDoKodu(self, DataOrig, dataNovy, vkladejOdRadku + 2)
        else:
            dataNew = DataOrig

        return (dataNew)
```
