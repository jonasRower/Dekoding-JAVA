import os
import mainProgram.NactiZdroj
import mainProgram.SeznamZdroju
import mainProgram.NovyJAVAKod
import mainProgram.Metody

from pathlib import Path

class SeznamZdroju():

    def __init__(self):
        self.seznamAdresZdroju = []
        self.seznamAdres = []
        self.seznamZdroju = []


    def add_AdresZdroju(self, adresaZdroje):                #full path
        self.seznamAdresZdroju.append(adresaZdroje)

    def add_Adresa(self, adresa):                           #path
        self.seznamAdres.append(adresa)

    def add_Zdroj(self, zdroj):
        self.seznamZdroju.append(zdroj)


    def vratSeznamAdresZdroju(self):

        #seznamZdroju = []
        adresaNadrazeneSlozky = self.vyhledejAdresuSrc()


        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(adresaNadrazeneSlozky):
            for file in f:
                #print("")
                if '.java' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            self.add_AdresZdroju(f)
            self.add_Zdroj(os.path.basename(f))
            self.add_Adresa(self.vratAdresu(f, os.path.basename(f)))

        return(self)



    def vratAdresu(self, adresaZdroj, zdroj):
        adresa = adresaZdroj.replace(zdroj,"")

        return(adresa)



    def vyhledejAdresuSrc(self):

        adresaZdroj = Path.cwd().parent.parent.parts
        adresaZdrojNew = ""

        for i in range(0, len(adresaZdroj)):
            nazevSlozky = adresaZdroj[i]
            adresaZdrojNew = adresaZdrojNew + nazevSlozky + '\\'

        adresaZdrojNew = adresaZdrojNew + "srcJAVA\\src"

        return (adresaZdrojNew)


class vykonavaniHlavnihoProgramu():

    def hlavniProgram(self):

        # Do adresyZdrojuData ulozi "Nazev JAVA souboru", "adresa pred nazev souboru" a "adresu s nazvem souboru"
        adresyZdrojuData = SeznamZdroju()
        adresyZdrojuData.vratSeznamAdresZdroju()

        # zde jsou data vsech souboru
        dataVsechSouboru = []

        # kod nize, bezi ve smycce
        # jsou jednotlive volany vsechny nazvy JAVA soubory, vcetne jejich adres
        pocetSouboru = len(adresyZdrojuData.seznamZdroju)
        for i in range(0, pocetSouboru):
            # ziska adresu se zdrojem (s nazvem souboru) a nazev zdroje (souboru)
            adresaZdroj = adresyZdrojuData.seznamAdresZdroju[i]
            zdroj = adresyZdrojuData.seznamZdroju[i]

            # hlavni program pro ziskani kompletnich dat pro jeden soubor
            startProgramu = mainProgram.NactiZdroj.NactiDataProJedenZdroj()

            # data pro jeden soubor ulozi sem
            dataJednohoSouboru = startProgramu.spustProgram(adresaZdroj, zdroj)

            # do kazdeho souboru dopise (dodatecne) jeste nazvy trid, na radcich s konstruktory
            dataJednohoSouboru = self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)

            # jednotlive se pridavaji data soubor po souboru
            dataVsechSouboru.append(dataJednohoSouboru)



        # projde data jeste jednou a doplni rozsahy slozenych zavorek
        # vyhledava totiz radky i z cizich trid,
        # proto je potreba tuto metodu spustit az po naplneni vsech ostatnich dat
        for i in range(1, pocetSouboru):
            dataJednohoSouboru = dataVsechSouboru[i]
            dataJednohoSouboru = self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)
            dataVsechSouboru = self.kVolaneMetodeNajdiNazevTridy(dataJednohoSouboru, dataVsechSouboru)

        #dataVsechSouboru[6].volanaTrida[40] = "VytvorDB"

        #self.podleNazvuSouboruPredejPoleSeSlozenymiZavorkami("NactiDotazy", dataVsechSouboru)

        novyJAVAKod = mainProgram.NovyJAVAKod.RoztahujData(dataVsechSouboru)
        novyJAVAKod.hlavni()

        self.poleRadkuN = novyJAVAKod.getPoleRadkuN()



    ###################################################################


    # geter
    def getPoleRadkuN(self):
        return(self.poleRadkuN)


    ###################################################################

    # pro radek : NactiDotazy DotazyzTxt = new NactiDotazy();
    # doplni NactiDotazy do pole volanaMetoda
    # detekuje pouze, zda pole na danem radku obsahuje neco v nazevTridy a volanaMetoda
    # pokud ano, prepise nazev tridy do volane metody
    def doplnVolanouTriduKeKonstruktoru(self, dataJednohoSouboru):
        i = -1
        for x in dataJednohoSouboru.nazevTridy:
            i = i + 1
            nazevTridy = dataJednohoSouboru.nazevTridy[i]
            if (nazevTridy != ""):
                volanaMetoda = dataJednohoSouboru.volanaMetoda[i]
                if(volanaMetoda != ""):
                    dataJednohoSouboru.volanaTrida[i] = nazevTridy
                    dataJednohoSouboru.volanaInstance[i] = "_"      # "_" priznak indikuje, aby hledal nazev tridy na stejnem radku

        return(dataJednohoSouboru)


    def vratIndexDatDanehoSouboru(self, pozadovanaTrida, dataVsechSouboru):
        i = -1
        pozadovanaTrida = pozadovanaTrida.replace(".java", "")
        pozadovanyNazevSouboru = pozadovanaTrida + ".java"
        hledanyIndex = -1
        for x in dataVsechSouboru:
            i = i + 1
            nazevSouboru = dataVsechSouboru[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                hledanyIndex = i
                break

        return(hledanyIndex)


    def podleNazvuSouboruPredejPoleSeSlozenymiZavorkami(self, pozadovanaTrida, dataVsechSouboru):
        i = -1
        pozadovanyNazevSouboru = pozadovanaTrida + ".java"
        for x in dataVsechSouboru:
            i = i + 1
            nazevSouboru = dataVsechSouboru[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                slozeneZavorky = dataVsechSouboru[i].slozenaZavorka
                break

        return (slozeneZavorky)


    # k jednotlivym metodam ktere se volaji (v JAVE), z dat dataJednohoSouboru
    # je potreba dohledat instance -> tridy -> nazvy souboru, v kterych vyhledavat data
    def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru):

        #Inicializuje ostatniMetody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # index dataVsechSouboru ktere odpovidaji dataJednohoSouboru
        # zjistuje kvuli tomu, aby zapisoval do spravnych dat
        nazevTridy = dataJednohoSouboru.nazevSouboru
        IndexZapisDat = self.vratIndexDatDanehoSouboru(nazevTridy, dataVsechSouboru)

        i = -1
        for x in dataJednohoSouboru.nazevMetody:
            i = i + 1

            nazevMetodyHodnota = dataJednohoSouboru.volanaMetoda[i]
            zapisujData = True
            #nazevTridy = ""
            # pro testovani:
            if (i == 35):
                a = 4

            if (i == 41):
                a = 4


            if(nazevMetodyHodnota != ""):
                nazevInstance = dataJednohoSouboru.volanaInstance[i]

                if(nazevInstance == ""):
                    # nenalezne-li nazev Instance pak se jedna o metodu volanou ze stejne tridy
                    # a neni treba dohledavat nazev souboru a jejich data
                    slozeneZavorky = dataJednohoSouboru.slozenaZavorka
                    nazvyMetod = dataJednohoSouboru.nazevMetody
                    nazevTridy = dataJednohoSouboru.nazevSouboru
                    nazevTridy = nazevTridy.replace(".java", "")
                else:
                    if(nazevInstance == "_"):   #"_"
                        # pokud nazevInstance obsahuje priznak "_" pak nazev Tridy = volanaTrida (jedna se o radek konstruktoru)
                        nazevTridy = dataJednohoSouboru.volanaTrida[i]
                    else:
                        nazevTridy = self.dohledejNazevTridyKInstanci(dataJednohoSouboru, nazevInstance, i, nazevTridy)

                    hledanyIndex = self.vratIndexDatDanehoSouboru(nazevTridy, dataVsechSouboru)
                    if (hledanyIndex > -1):
                        slozeneZavorky = dataVsechSouboru[hledanyIndex].slozenaZavorka
                        nazvyMetod = dataVsechSouboru[hledanyIndex].nazevMetody
                    else:
                        zapisujData = False
                        # kdyz nenalezne tridu nema smysl nic zapisovat

                if (zapisujData == True):
                    # vyhleda cislo radku metody a to vzdy v datech tridy
                    # pokud je instance = "" pak se vyhledava v datech stejne tridy jako volana metoda
                    cisloRadkuMetody = self.dohledejCisloRadkuKDaneMetode(nazevMetodyHodnota, nazvyMetod)

                    if (cisloRadkuMetody > -1):
                        # Vyhleda index nejblizsi otevrene a zavrene zavorky
                        indexNejblizsiOtevreneZavorky = ostatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(cisloRadkuMetody, slozeneZavorky)
                        indexNejblizsiZavreneZavorky = ostatniMetody.vratCisloRadkuSKoncemBloku(indexNejblizsiOtevreneZavorky, slozeneZavorky)

                        # Zapise data do Zacatek/KonecBloku
                        dataVsechSouboru[IndexZapisDat].zacatekBloku[i-1] = indexNejblizsiOtevreneZavorky
                        dataVsechSouboru[IndexZapisDat].konecBloku[i-1] = indexNejblizsiZavreneZavorky

                        # Zapise nazev tridy v ktere bude vyhledavat
                        dataVsechSouboru[IndexZapisDat].volanaTrida[i-1] = nazevTridy

        return(dataVsechSouboru)

    # slozeneZavorky = self.podleNazvuSouboruPredejPoleSeSlozenymiZavorkami(nazevTridy, dataVsechSouboru)

    # pozadovane instanci dohledava nazev tridy
    def dohledejNazevTridyKInstanci(self, dataJednohoSouboru, pozadovanaInstance, hledejDoRadku, nazevTridyOrig):
        # hledejDoRadku - hleda od radku smerem nahoru

        # defaultne nastavuji
        # pokud se jedna o generovanou instanci, pak trida neni a vrati nazevTridyOriginalni
        nazevTridy = nazevTridyOrig

        # pro jistotu hledam od radku jeste jednoho nize
        hledejDoRadku = hledejDoRadku + 1

        # hledam od radku smerem nahoru, protoze predpokladam,
        # ze trida bude definovana nekde ned volanou instanci
        for i in range(hledejDoRadku, 0, -1):
            #prohledava data.nazevInstance , nikoliv volanaInstance
            nazevInstance = dataJednohoSouboru.nazevInstance[i]
            if (nazevInstance == pozadovanaInstance):
                nazevTridy = dataJednohoSouboru.nazevTridy[i]
                break

        return (nazevTridy)


    def dohledejCisloRadkuKDaneMetode(self, hledanaMetoda, nazvyMetod):
        i = - 1
        cisloRadkuDaneMetody = -1
        for nazevMetody in nazvyMetod:
            i = i + 1
            if(nazevMetody == hledanaMetoda):
                cisloRadkuDaneMetody = i
                break

        return(cisloRadkuDaneMetody)


    # Vrati True/False, podle toho, zda konkretni data obsahuji danou metodu
    def zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(self, dataJednohoSouboru, pozadovanyNazevMetody):
        dataZdrojeObsahujiMetodu = False
        for nazevMetody in dataJednohoSouboru.volanaMetoda:
            if(nazevMetody == pozadovanyNazevMetody):
                dataZdrojeObsahujiMetodu = True
                break

        return(dataZdrojeObsahujiMetodu)


    # vrati ty data, ktere obsahuji danou metodu
    def vyberDataKdeJeDanaMetoda(self, dataVsechSouboru, pozadovanyNazevMetody):
        i = -1
        dataObsahujiDanouMetodu = False
        celyZdrojSDanouMetodou = ""
        for x in dataVsechSouboru:
            i = i + 1
            dataJednohoSouboru = dataVsechSouboru[i]
            dataObsahujiDanouMetodu = self.zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(dataJednohoSouboru, pozadovanyNazevMetody)
            if(dataObsahujiDanouMetodu == True):
                celyZdrojSDanouMetodou = dataJednohoSouboru
                break

        return(celyZdrojSDanouMetodou)





