import mainProgram.Metody
import log.generujLog
import genHtmlProgram.generujHtml
import mainProgram.obarvujText
from pathlib import Path
import re

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

        input = self.nactiInput()
        dataIndexyRadku = self.nactiDataIndexyRadku()
        poleIntArr = self.prevedPoleStrNaPoleInt(dataIndexyRadku)


        # nazev tridy, kde je umistena metoda, ktera se bude dokumentovat
        pozadovanaTrida = input[0]

        # nazev metody, ktera se bude dokumetovat
        nazevMetody = input[1]

        # pocatecni kod, ktery se bude teprve roztahovat
        self.vratPocatecniKod(pozadovanaTrida, nazevMetody)

        self.roztahujKod(poleIntArr)

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
        self.poleId = poleId

        # generuje data do html nebo jsonu
        genHtmlProgram.generujHtml.genHtml(poleId, poleRadkuN)

        #json s obarvenymi radky tiskne rovnou
        convertToJson = mainProgram.obarvujText.poleNaJson(radekSlovaAtributyAll)
        poleRadkuJson = convertToJson.getPoleRadkuJson()
        slovaAId = convertToJson.getSlovaAId()

        log.generujLog.loguData("coloredText.json", poleRadkuJson, True)
        log.generujLog.loguData("wordsId.json", slovaAId, True)

        self.vytvorDekod(poleRadkuN)



        #vytvarej json pomoci balicku v Log, tim ze tam pridam dalsi modul


    def vytvorDekod(self, poleRadkuN):

        log.generujLog.loguData("elaboratedCode.txt", poleRadkuN, False)


    def nactiInput(self):

        adresaProjektuNew = self.ziskejAdresuInputu("input\\Start-class-method.txt")
        input = self.nactiDataTxt(adresaProjektuNew)

        return(input)


    def nactiDataIndexyRadku(self):

        adresaProjektuNew = self.ziskejAdresuInputu("input\\data.csv")
        input = self.nactiDataTxt(adresaProjektuNew)

        return (input)


    def nactiDataTxt(self, adresaLog):

        pole = []

        r = -1
        with open(adresaLog, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n' ,'')
                pole.append(line)

        return (pole)


    def ziskejAdresuInputu(self, soubor):

        adresaProjektu = Path.cwd().parent.parent.parts
        adresaProjektuNew = ""

        for i in range(0, len(adresaProjektu)):
            nazevSlozky = adresaProjektu[i]
            adresaProjektuNew = adresaProjektuNew + nazevSlozky + '\\'

        adresaProjektuNew = adresaProjektuNew + soubor

        return(adresaProjektuNew)


    def prevedPoleStrNaPoleInt(self, poleStr):

        poleIntArr = []

        for i in range(0, len(poleStr)):
            radek = poleStr[i]
            radekIntArr = self.prevedRadekNaRadekArr(radek)
            poleIntArr.append(radekIntArr)

        return(poleIntArr)


    #ef vyberJenCislo(self):

    def prevedRadekNaRadekArr(self, radek):

        radekSpl = radek.split(',')
        radekIntArr = []

        for i in range(0, len(radekSpl)):
            radekPolozka = radekSpl[i]
            polozkaIntArr = re.findall(r'\d+', radekPolozka)
            polozkaInt = int(polozkaIntArr[0])

            radekIntArr.append(polozkaInt)

        return(radekIntArr)




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