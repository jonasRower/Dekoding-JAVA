# def roztahujKod(self, poleIntArr):

### list of variables
poleRadkuN   
volanaMetodaN   
dataPozadovaneTridy   
zdrojovaTridaN   
ostatniMetody   
metodyProVytvareniJAVAKodu   
cisloRadkuOdkudVkladatKod   
poleIdClass   
poleId   
radkyAtributy   
radekSlovaAtributyAll   
radek   
indexSouboru   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
dataDaneTridy   
poleRadkuDaneTridy   
radekSlovaAtributyAllNew   
self.poleRadkuN   
convertToJson   
poleRadkuJson   
slovaAId   

### code of method
```
    def roztahujKod(self, poleIntArr):

        poleRadkuN = self.__poleRadkuKodu
        volanaMetodaN = self.__volanaMetoda
        dataPozadovaneTridy = self.__dataPozadovaneTridy

        # jednotlive radky zdrojoveTridy budou odpovidat radkum, odkud jsou zdrojova data nacitana
        zdrojovaTridaN = self.pripravZdrojovouTridu(len(poleRadkuN))

        # inicializuji tridu pro ostatni metody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # inicializuje tridu s metodami
        metodyProVytvareniJAVAKodu = mainProgram.Metody.MetodyProVytvareniJAVAKodu(ostatniMetody, dataPozadovaneTridy)
        cisloRadkuOdkudVkladatKod = 0

        # inicializuje tridu pro originalni poleId
        poleIdClass = mainProgram.Metody.createIdArr(poleRadkuN, 0)

        # vytvori poles id
        poleId = poleIdClass.getPoleId()

        # vytvori defaultni data pro obarvovani
        radkyAtributy = mainProgram.obarvujText.barevnyText(dataPozadovaneTridy, ostatniMetody, poleRadkuN)
        radekSlovaAtributyAll = radkyAtributy.getRadekSlovaAtributyAll()


        for i in range(0, len(poleIntArr)):
            radek = poleIntArr[i]
            cisloRadkuOdkudVkladatKod = radek[0]
            indexSouboru = radek[1]
            vyjmiKodOdRadku = radek[2]
            vyjmiKodDoRadku = radek[3]

            dataDaneTridy = self.__data[indexSouboru]
            poleRadkuDaneTridy = dataDaneTridy.poleRadku


            # obarvuje text
            radkyAtributy = mainProgram.obarvujText.barevnyText(dataDaneTridy, ostatniMetody, poleRadkuDaneTridy)
            radekSlovaAtributyAllNew = radkyAtributy.getRadekSlovaAtributyAll()


            # vrati poleId, rozsirene o novy subkod
            poleId = metodyProVytvareniJAVAKodu.vlozSubDataProPoleId(poleId, vyjmiKodOdRadku, vyjmiKodDoRadku,
                                                                     cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy)

            # poleRadkuN obsahuje pole radku noveho "modifikovaneho" kodu
            poleRadkuN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(poleRadkuN, True, vyjmiKodOdRadku,
                                                vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy, "")

            radekSlovaAtributyAll = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(radekSlovaAtributyAll, True,
                                    vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, radekSlovaAtributyAllNew, "")


        self.poleRadkuN = poleRadkuN
        #self.poleId = poleId

        # generuje data do html nebo jsonu
        genHtmlProgram.generujHtml.genHtml(poleId, poleRadkuN)

        #json s obarvenymi radky tiskne rovnou
        convertToJson = mainProgram.obarvujText.poleNaJson(radekSlovaAtributyAll)
        poleRadkuJson = convertToJson.getPoleRadkuJson()
        slovaAId = convertToJson.getSlovaAId()

        log.generujLog.loguData("coloredText.json", poleRadkuJson, True)
        log.generujLog.loguData("wordsId.json", slovaAId, True)

        self.vytvorDekod(poleRadkuN)
```
### links



[zdrojovaTridaN=self.pripravZdrojovouTridu(len(poleRadkuN))](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_pripravZdrojovouTridu(self,_delkaPole).md)  
[poleId=poleIdClass.getPoleId()](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_getPoleId(self).md)  
[log.generujLog.loguData("wordsId.json",slovaAId,True)](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_createIdArr()/def_getPoleId(self).md)  
[self.vytvorDekod(poleRadkuN)](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_vytvorDekod(self,_poleRadkuN).md)  
