# def roztahujKod(self):

### list of variables
<a href  
ostatniMetody   
metodyProVytvareniJAVAKodu   
cisloRadkuOdkudVkladatKod   
poleIdClass   
r   
zdrojovaTrida   
cisloRadkuZjistiBlok   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
if(vyjmiKodOdRadku   
self.poleRadkuN   
self.poleId   

### code of method
<pre>
 <code>
    def roztahujKod(self):

          
          
          

        # jednotlive radky zdrojoveTridy budou odpovidat radkum, odkud jsou zdrojova data nacitana
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_pripravZdrojovouTridu(self,delkaPole).md">zdrojovaTridaN=self.pripravZdrojovouTridu(len(poleRadkuN))</a>

        # inicializuji tridu pro ostatni metody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # inicializuje tridu s metodami
        metodyProVytvareniJAVAKodu = mainProgram.Metody.MetodyProVytvareniJAVAKodu(ostatniMetody, dataPozadovaneTridy)
        cisloRadkuOdkudVkladatKod = 0

        # inicializuje tridu pro originalni poleId
        poleIdClass = mainProgram.Metody.createIdArr(poleRadkuN, 0)

        # vytvori poles id
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_getPoleId(self).md">poleId=poleIdClass.getPoleId()</a>


        # nasledne jde program smyckou a postupne roztahuje data
        r = -1
        for radek in dataPozadovaneTridy.poleRadku:
            r = r + 1

            # vrati radek kodu odkud bude vkladat kod = radek prvni metody za indexem "cisloRadkuOdkudVkladatKod" (z predchoziho cyklu)
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vratCisloRadkuDalsiVolaneMetody(self,volanaMetodaN,hledejOdIndexu).md">cisloRadkuOdkudVkladatKod=metodyProVytvareniJAVAKodu.vratCisloRadkuDalsiVolaneMetody(volanaMetodaN,cisloRadkuOdkudVkladatKod)</a>

            # vyhleda zdrojova data z jine tridy
            zdrojovaTrida = zdrojovaTridaN[cisloRadkuOdkudVkladatKod]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vratZdrojovaData(self,zdrojovaTrida,dataPozadovaneTridy).md">dataZdrojoveTridy=self.vratZdrojovaData(zdrojovaTrida,dataPozadovaneTridy)</a>

            # vrati index radku na kterem nalezne zacatek a konec bloku pro prvni volanou metodu za indexem "cisloRadku"
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vratCisloRadkuProVyberZacatkuAKonceBloku(self,volanaMetodaN,volanaMetodaO,.md">cisloRadkuZjistiBlok=self.vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN,dataZdrojoveTridy.volanaMetoda,cisloRadkuOdkudVkladatKod,dataPozadovaneTridy.nazevInstance)</a>
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

              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vyhledejPoleRadkuDaneMetody(self,cisloRadku,nazevTridy,coVratit,dataZdrojoveTridy).md">poleRadkuDaneTridy=self.vyhledejPoleRadkuDaneMetody(cisloRadkuZjistiBlok,zdrojovaTrida,"poleRadku",dataZdrojoveTridy)</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vyhledejPoleRadkuDaneMetody(self,cisloRadku,nazevTridy,coVratit,dataZdrojoveTridy).md">volanaMetodaDaneTridy=self.vyhledejPoleRadkuDaneMetody(cisloRadkuZjistiBlok,zdrojovaTrida,"volanaMetoda",dataZdrojoveTridy)</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vyhledejPoleRadkuDaneMetody(self,cisloRadku,nazevTridy,coVratit,dataZdrojoveTridy).md">volanaTridaDaneTridy=self.vyhledejPoleRadkuDaneMetody(cisloRadkuZjistiBlok,zdrojovaTrida,"volanaTrida",dataZdrojoveTridy)</a>


            if (r == 0):
                cisloRadkuOdkudVkladatKod = 11
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vyhledejPoleRadkuDaneMetody(self,cisloRadku,nazevTridy,coVratit,dataZdrojoveTridy).md">poleRadkuDaneTridy=self.__data[1].poleRadku</a>

            if (r == 1):
                cisloRadkuOdkudVkladatKod = 30
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vyhledejPoleRadkuDaneMetody(self,cisloRadku,nazevTridy,coVratit,dataZdrojoveTridy).md">poleRadkuDaneTridy=self.__data[1].poleRadku</a>
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
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vyhledejPoleRadkuDaneMetody(self,cisloRadku,nazevTridy,coVratit,dataZdrojoveTridy).md">poleRadkuDaneTridy=self.__data[11].poleRadku</a>
                vyjmiKodOdRadku = 0
                vyjmiKodDoRadku = 20


            if(cisloRadkuOdkudVkladatKod > -1):

                # vrati poleId, rozsirene o novy subkod
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProPoleId(self,poleIdOrig,vyjmiKodOdRadku,vyjmiKodDoRadku,vkladejOdRadku,dataZdroj).md">poleId=metodyProVytvareniJAVAKodu.vlozSubDataProPoleId(poleId,vyjmiKodOdRadku,vyjmiKodDoRadku,cisloRadkuOdkudVkladatKod,poleRadkuDaneTridy)</a>

                # poleRadkuN obsahuje pole radku noveho "modifikovaneho" kodu
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProJednotlivaPole(self,DataOrig,pocitatMezery,vyjmiKodOdRadku,.md">poleRadkuN=metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(poleRadkuN,True,vyjmiKodOdRadku,</a>
                                                    vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy, "")


                # tim jak se poleRadkuN "roztahuje", je potreba "roztahovat" i data
                # je potreba roztahovat i volane Metody a instance, tak aby radky vzajemne souhlasili
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyProVytvareniJAVAKodu()/def_vlozSubDataProJednotlivaPole(self,DataOrig,pocitatMezery,vyjmiKodOdRadku,.md">volanaMetodaN=metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(volanaMetodaN,False,</a>
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

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_vytvorDekod(self,poleRadkuN).md">self.vytvorDekod(poleRadkuN)</a>
 <code>
<pre>

















