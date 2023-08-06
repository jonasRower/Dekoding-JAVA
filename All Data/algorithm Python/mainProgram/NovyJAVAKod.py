import mainProgram.Metody
import log.generujLog

class RoztahujData():

    def __init__(self, data):
        self.__data = data
        self.__dataPozadovaneTridy = []
        self.__poleRadkuKodu = []
        self.__volanaMetoda = []
        self.__volanaTrida = []
        self.__zacatekBloku = []
        self.__konecBloku = []

        self.poleRadkuN = []


    def getPoleRadkuN(self):
        return(self.poleRadkuN)


    # zacatek programu v teto tride
    def hlavni(self):

        # nazev tridy, kde je umistena metoda, ktera se bude dokumentovat
        pozadovanaTrida = "TextReader3.java"
        pozadovanaTrida = "SQL_GUI_Frame.java"

        # nazev metody, ktera se bude dokumetovat
        nazevMetody = "main"
        nazevMetody = "TlacDopravaActionPermed"

        # pocatecni kod, ktery se bude teprve roztahovat
        self.vratPocatecniKod(pozadovanaTrida, nazevMetody)

        self.roztahujKod()

        print("")

    # vrati pocatecni kod, ktery bude postupne roztahovat
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

        #return(PoleRadkuPozadovaneMetody)


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

            # poleRadkuN obsahuje pole radku noveho "modifikovaneho" kodu
            poleRadkuN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(poleRadkuN, True, vyjmiKodOdRadku,
                                                vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, poleRadkuDaneTridy, "")

            # tim jak se poleRadkuN "roztahuje", je potreba "roztahovat" i data
            # je potreba roztahovat i volane Metody a instance, tak aby radky vzajemne souhlasili
            volanaMetodaN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(volanaMetodaN, False,
                                vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, volanaMetodaDaneTridy, "")

            # vytvari pole aby vedel z jake tridy vklada data
            tridaZapis = self.ziskejNazevTridyProZapis(dataPozadovaneTridy, cisloRadkuZjistiBlok)
            zdrojovaTridaN = metodyProVytvareniJAVAKodu.vlozSubDataProJednotlivaPole(zdrojovaTridaN, False,
                     vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, volanaTridaDaneTridy, tridaZapis)

            cisloRadkuOdkudVkladatKod = cisloRadkuOdkudVkladatKod + 1

        print("")

        self.poleRadkuN = poleRadkuN
        self.vytvorDekod(poleRadkuN)


    def vytvorDekod(self, poleRadkuN):

        log.generujLog.loguData("elaboratedCode.txt", poleRadkuN)



    def vratCisloRadkuProVyberZacatkuAKonceBloku(self, volanaMetodaN, volanaMetodaO,
                                                 cisloRadkuvolanaMetodaN, volanaInstanceN):

        cisloRadkuZacKonBloku = -1
        nazevVolaneMetody = volanaMetodaN[cisloRadkuvolanaMetodaN]
        #nazevVolaneInstance = volanaInstanceN[cisloRadkuvolanaMetodaN]

        if (cisloRadkuvolanaMetodaN == 116):
            a = 4

        i = -1
        for dataNazevMetody in volanaMetodaO:
            i = i + 1
            if (dataNazevMetody == nazevVolaneMetody):

                # zatim kod funguje jen pro volani pouze v ramci jedne tridy
                # kdyz tam bude instance - je potreba rozsirit kod o nacitani dat z vice souboru
                try:
                    nazevVolaneInstance = volanaInstanceN[i]
                except:
                    cisloRadkuZacKonBloku = i
                    break

                #if (nazevVolaneInstance == ""):
                cisloRadkuZacKonBloku = i
                break

        return (cisloRadkuZacKonBloku)


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


    def vyhledejPoleRadkuDaneMetody2(self, cisloRadku, coVratit):
        nazevTridy = self.__dataPozadovaneTridy.volanaTrida[cisloRadku-1]
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
            dataDaneTridy = self.najdiDataPrislusneTridy(nazevSouboru)
            if (coVratit == "poleRadku"):
                poleDat = dataDaneTridy.poleRadku
            if (coVratit == "volanaMetoda"):
                poleDat = dataDaneTridy.volanaMetoda
            if (coVratit == "volanaTrida"):
                poleDat = dataDaneTridy.volanaTrida
            if (coVratit == "zacatekBloku"):
                poleDat = dataDaneTridy.zacatekBloku
            if (coVratit == "konecBloku"):
                poleDat = dataDaneTridy.konecBloku

        return(poleDat)


    def vratZdrojovaData(self, zdrojovaTrida, dataPozadovaneTridy):
        if (zdrojovaTrida == ""):
            dataZdrojoveTridy = dataPozadovaneTridy
        else:
            zdrojovaTrida = zdrojovaTrida.replace(".java", "")
            nazevSouboru = zdrojovaTrida + ".java"
            dataZdrojoveTridy = self.najdiDataPrislusneTridy2(nazevSouboru)
            if (dataZdrojoveTridy == ""):
                dataZdrojoveTridy = dataPozadovaneTridy

        return (dataZdrojoveTridy)


    # najde data pro prislusnou tridu
    def najdiDataPrislusneTridy(self, pozadovanyNazevSouboru, dataZdrojoveTridy):
        i = -1
        dataPozadovaneTridy = ""
        # zajisti aby pozadovanyNazevSouboru obsahoval vzdy priponu
        pozadovanyNazevSouboru = pozadovanyNazevSouboru.replace(".java", "")
        pozadovanyNazevSouboru = pozadovanyNazevSouboru + ".java"
        for x in dataZdrojoveTridy:
            i = i + 1
            nazevSouboru = dataZdrojoveTridy[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                dataPozadovaneTridy = dataZdrojoveTridy[i]
                break

        return (dataPozadovaneTridy)


    # najde data pro prislusnou tridu
    def najdiDataPrislusneTridy2(self, pozadovanyNazevSouboru):
        i = -1
        dataPozadovaneTridy = ""
        #zajisti aby pozadovanyNazevSouboru obsahoval vzdy priponu
        pozadovanyNazevSouboru = pozadovanyNazevSouboru.replace(".java","")
        pozadovanyNazevSouboru = pozadovanyNazevSouboru + ".java"
        for x in self.__data:
            i = i + 1
            nazevSouboru = self.__data[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                dataPozadovaneTridy = self.__data[i]
                break

            if(i == 11):
                a = 5

        return(dataPozadovaneTridy)


    def ziskejNazevTridyProZapis(self, dataPozadovaneTridy, cisloRadku):
        nazevSouboru = dataPozadovaneTridy.nazevSouboru
        aktualniTrida = nazevSouboru.replace(".java", "")

        try:
            zapisovanaTrida = dataPozadovaneTridy.volanaTrida[cisloRadku-1]
            if(aktualniTrida != zapisovanaTrida):
                tridaZapis = zapisovanaTrida
            else:
                tridaZapis = ""
        except:
            tridaZapis = ""

        return (tridaZapis)


    def pripravZdrojovouTridu(self, delkaPole):
        zdrojovaTrida = []
        for i in range(0, delkaPole):
            zdrojovaTrida.append("")

        return(zdrojovaTrida)