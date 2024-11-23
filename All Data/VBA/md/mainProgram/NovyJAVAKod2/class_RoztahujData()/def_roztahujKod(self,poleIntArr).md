# def roztahujKod(self, poleIntArr):

### list of variables
<a href  
ostatniMetody   
metodyProVytvareniJAVAKodu   
cisloRadkuOdkudVkladatKod   
poleIdClass   
radkyAtributy   
radek   
indexSouboru   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
poleRadkuDaneTridy   
self.poleRadkuN   
convertToJson   

### code of method
<pre>
 <code>
    def roztahujKod(self, poleIntArr):

          
          
          

        # jednotlive radky zdrojoveTridy budou odpovidat radkum, odkud jsou zdrojova data nacitana
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_pripravZdrojovouTridu(self,delkaPole).md">zdrojovaTridaN=self.pripravZdrojovouTridu(len(poleRadkuN))</a>

        # inicializuji tridu pro ostatni metody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # inicializuje tridu s metodami
        metodyProVytvareniJAVAKodu = mainProgram.Metody.MetodyProVytvareniJAVAKodu(ostatniMetody, dataPozadovaneTridy)
        cisloRadkuOdkudVkladatKod = 0

        # inicializuje tridu pro originalni poleId
        poleIdClass = mainProgram.Metody.createIdArr(poleRadkuN, 0)

        # vytvori poles id
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_getPoleId(self).md">poleId=poleIdClass.getPoleId()</a>

        # vytvori defaultni data pro obarvovani
        radkyAtributy = mainProgram.obarvujText.barevnyText(dataPozadovaneTridy, ostatniMetody, poleRadkuN)
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/return(self.radekSlovaAtributyAll).md">radekSlovaAtributyAll=radkyAtributy.getRadekSlovaAtributyAll()</a>


        for i in range(0, len(poleIntArr)):
            radek = poleIntArr[i]
            cisloRadkuOdkudVkladatKod = radek[0]
            indexSouboru = radek[1]
            vyjmiKodOdRadku = radek[2]
            vyjmiKodDoRadku = radek[3]

              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/return(self.radekSlovaAtributyAll).md">dataDaneTridy=self.__data[indexSouboru]</a>
            poleRadkuDaneTridy = dataDaneTridy.poleRadku


            # obarvuje text
            radkyAtributy = mainProgram.obarvujText.barevnyText(dataDaneTridy, ostatniMetody, poleRadkuDaneTridy)
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/return(self.radekSlovaAtributyAll).md">radekSlovaAtributyAllNew=radkyAtributy.getRadekSlovaAtributyAll()</a>


            # vrati poleId, rozsirene o novy subkod
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProPoleId(self,poleIdOrig,vyjmiKodOdRadku,vyjmiKodDoRadku,vkladejOdRadku,dataZdroj).md">poleId=metodyProVytvareniJAVAKodu.vlozSubDataProPoleId(poleId,vyjmiKodOdRadku,vyjmiKodDoRadku,</a>
                                                                     cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy)

            # poleRadkuN obsahuje pole radku noveho "modifikovaneho" kodu
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProJednotlivaPole(self,DataOrig,pocitatMezery,vyjmiKodOdRadku,.md">poleRadkuN=metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(poleRadkuN,True,vyjmiKodOdRadku,</a>
                                                vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy, "")

              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProJednotlivaPole(self,DataOrig,pocitatMezery,vyjmiKodOdRadku,.md">radekSlovaAtributyAll=metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(radekSlovaAtributyAll,True,</a>
                                    vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, radekSlovaAtributyAllNew, "")


        self.poleRadkuN = poleRadkuN
        #self.poleId = poleId

        # generuje data do html nebo jsonu
        genHtmlProgram.generujHtml.genHtml(poleId, poleRadkuN)

        #json s obarvenymi radky tiskne rovnou
        convertToJson = mainProgram.obarvujText.poleNaJson(radekSlovaAtributyAll)
          
          

        log.generujLog.loguData("coloredText.json", poleRadkuJson, True)
        log.generujLog.loguData("wordsId.json", slovaAId, True)

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_vytvorDekod(self,poleRadkuN).md">self.vytvorDekod(poleRadkuN)</a>
 <code>
<pre>













