# def roztahujKod(self):

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
r   
zdrojovaTrida   
dataZdrojoveTridy   
cisloRadkuZjistiBlok   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
if(vyjmiKodOdRadku   
poleRadkuDaneTridy   
volanaMetodaDaneTridy   
volanaTridaDaneTridy   
self.poleRadkuN   
self.poleId   

### code of method
```
    def roztahujKod(self):

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


        # nasledne jde program smyckou a postupne roztahuje data
        r = -1
        for radek in dataPozadovaneTridy.poleRadku:
            r = r + 1

            # vrati radek kodu odkud bude vkladat kod = radek prvni metody za indexem "cisloRadkuOdkudVkladatKod" (z predchoziho cyklu)
            cisloRadkuOdkudVkladatKod = metodyProVytvareniJAVAKodu.vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, cisloRadkuOdkudVkladatKod)

            # vyhleda zdrojova data z jine tridy
            zdrojovaTrida = zdrojovaTridaN[cisloRadkuOdkudVkladatKod]
            dataZdrojoveTridy = self.vratZdrojovaData(zdrojovaTrida, dataPozadovaneTridy)

            # vrati index radku na kterem nalezne zacatek a konec bloku pro prvni volanou metodu za indexem "cisloRadku"
            cisloRadkuZjistiBlok = self.vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN, dataZdrojoveTridy.volanaMetoda, cisloRadkuOdkudVkladatKod, dataPozadovaneTridy.nazevInstance)
            cisloRadkuZjistiBlok = cisloRadkuZjistiBlok - 1

            # na zaklade cisloRadkuData vrati indexy zavorek bloku (tj. indexy "{" a "}")
            # jedna se tedy o blok kodu, ktery rozkopirovava a prenasi jinam
            vyjmiKodOdRadku = dataZdrojoveTridy.zacatekBloku[cisloRadkuZjistiBlok] - 1  # protoze otevrena zavorka muze byt az pod deklaraci
            vyjmiKodDoRadku = dataZdrojoveTridy.konecBloku[cisloRadkuZjistiBlok]

            # nekde je chyba - trida je posunuta o radek vys
            # opravuje data
            if(vyjmiKodOdRadku == -2):
                vyjmiKodOdRadku = dataZdrojoveTridy.zacatekBloku[cisloRadkuZjistiBlok-1]
                vyjmiKodDoRadku = dataZdrojoveTridy.konecBloku[cisloRadkuZjistiBlok-1]

            poleRadkuDaneTridy = self.vyhledejPoleRadkuDaneMetody(cisloRadkuZjistiBlok, zdrojovaTrida, "poleRadku", dataZdrojoveTridy)
            volanaMetodaDaneTridy = self.vyhledejPoleRadkuDaneMetody(cisloRadkuZjistiBlok, zdrojovaTrida, "volanaMetoda", dataZdrojoveTridy)
            volanaTridaDaneTridy = self.vyhledejPoleRadkuDaneMetody(cisloRadkuZjistiBlok, zdrojovaTrida, "volanaTrida", dataZdrojoveTridy)


            if (r == 0):
                cisloRadkuOdkudVkladatKod = 11
                poleRadkuDaneTridy = self.__data[1].poleRadku

            if (r == 1):
                cisloRadkuOdkudVkladatKod = 30
                poleRadkuDaneTridy = self.__data[1].poleRadku
                vyjmiKodOdRadku = 28
                vyjmiKodDoRadku = 31      # -1 !!

            #if (r == 2):
            #    cisloRadkuOdkudVkladatKod = -1  # ArrayList

            if (r == 3):
                cisloRadkuOdkudVkladatKod = -1  # ArrayList

            if (r == 4):
                cisloRadkuOdkudVkladatKod = -1  # ArrayList

            if (r == 5):
                cisloRadkuOdkudVkladatKod = -1  # ArrayList

            if (r == 2):
                cisloRadkuOdkudVkladatKod = 50
                poleRadkuDaneTridy = self.__data[11].poleRadku
                vyjmiKodOdRadku = 0
                vyjmiKodDoRadku = 20


            if(cisloRadkuOdkudVkladatKod > -1):

                # vrati poleId, rozsirene o novy subkod
                poleId = metodyProVytvareniJAVAKodu.vlozSubDataProPoleId(poleId, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy)

                # poleRadkuN obsahuje pole radku noveho "modifikovaneho" kodu
                poleRadkuN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(poleRadkuN, True, vyjmiKodOdRadku,
                                                    vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy, "")


                # tim jak se poleRadkuN "roztahuje", je potreba "roztahovat" i data
                # je potreba roztahovat i volane Metody a instance, tak aby radky vzajemne souhlasili
                volanaMetodaN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(volanaMetodaN, False,
                                    vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, volanaMetodaDaneTridy, "")


                # vytvari pole aby vedel z jake tridy vklada data
                #tridaZapis = self.ziskejNazevTridyProZapis(dataPozadovaneTridy, cisloRadkuZjistiBlok)
                #zdrojovaTridaN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(zdrojovaTridaN, False,
                #         vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, volanaTridaDaneTridy, tridaZapis)

                #cisloRadkuOdkudVkladatKod = cisloRadkuOdkudVkladatKod + 1

            if (r == 2):
                break

        print("")

        self.poleRadkuN = poleRadkuN
        self.poleId = poleId

        genHtmlProgram.generujHtml.genHtml(poleId, poleRadkuN)

        self.vytvorDekod(poleRadkuN)
```
### links


[poleId=metodyProVytvareniJAVAKodu.vlozSubDataProPoleId(poleId,vyjmiKodOdRadku,vyjmiKodDoRadku,cisloRadkuOdkudVkladatKod,poleRadkuDaneTridy)](../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProPoleId(self,_poleIdOrig,_vyjmiKodOdRadku,_vyjmiKodDoRadku,_vkladejOdRadku,_dataZdroj).md)  
