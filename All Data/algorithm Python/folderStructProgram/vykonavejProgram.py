class hlavniProgram:

    def __init__(self, poleRadkuLog):

        odsTotPole = self.vratPoleOdsazeni(poleRadkuLog)
        poleRadkuBezSipek = self.vratPoleRadkuBezSipek(poleRadkuLog)
        poleAdres = self.vytvorPoleAdres(poleRadkuBezSipek, odsTotPole)

        self.poleAdres = poleAdres

        print()


    def getPoleDat(self):
        return(self.poleAdres)


    def vytvorPoleAdres(self, poleRadkuLog, odsTotPole):

        odsPrev = 0
        radekPrev = ""
        poleAdres = []

        adresaPredchozi = ""

        for i in range(0, len(poleRadkuLog)):
            radek = poleRadkuLog[i].strip()
            odsAct = odsTotPole[i]

            if(i == 23):
                a = 0

            if(radek == ''):
                radek = '\\'

            odsazeniDoprava = self.detekujOdsazeniDoprava(odsAct, odsPrev)
            odsazeniDoleva = self.detekujOdsazeniDoleva(odsAct, odsPrev)

            if(odsazeniDoprava == True):
                radek = self.pridejDalsiUroven(adresaPredchozi, radek)
                radekPrev = radek
            else:
                radekKonciLomitkem = self.detekujZdaRadekKonciLomitkem(radekPrev)
                if(radekKonciLomitkem == False):
                    radekPrev = self.odeberVseZaLomikem(radekPrev)

                radek = radekPrev + radek
                radek = radek.replace('\\\\', '\\')

            if(odsazeniDoleva == True):
                radek = self.uberPosledniUroven(radekPrev, radek)
                print()

            poleAdres.append(radek)

            odsPrev = odsAct
            adresaPredchozi = radek


        return(poleAdres)


    def detekujZdaRadekKonciLomitkem(self, radek):

        posledni2Znaky = radek[len(radek) - 2:]
        if(posledni2Znaky == '\\'):
            radekKonciLomitkem = True
        else:
            radekKonciLomitkem = False

        return(radekKonciLomitkem)


    def odeberVseZaLomikem(self, radek):

        radekReverse = radek[::-1]
        try:
            indexLomitkaRev = radekReverse.index('\\')
        except:
            indexLomitkaRev = 0

        indexLomitka = len(radek) - indexLomitkaRev
        stringPredLomitkem = radek[0:indexLomitka:1]

        return(stringPredLomitkem)



    def pridejDalsiUroven(self, radekPrev, radek):

        radekNew = ""

        if (radekPrev != ""):
            radekPrev = radekPrev + '\\'
            radekNew = radekPrev + radek
            radekNew = radekNew.replace('\\\\', '\\')

        return(radekNew)


    def uberPosledniUroven(self, radekPrev, radek):

        cestaNew = self.vratCestuBezPosledmiUrovne(radekPrev)

        return(cestaNew)


    def vratCestuBezPosledmiUrovne(self, cesta):

        cestaSpl = cesta.split('\\')
        cestaNew = cestaSpl[0]

        for i in range(1, len(cestaSpl)-2):
            slozka = cestaSpl[i]
            cestaNew = cestaNew + '\\' + slozka
            print()

        return(cestaNew)


    def detekujOdsazeniDoprava(self, odsAct, odsPrev):

        if(odsAct > odsPrev):
            odsazeniDoprava = True
        else:
            odsazeniDoprava = False

        return(odsazeniDoprava)


    def detekujOdsazeniDoleva(self, odsAct, odsPrev):

        if (odsAct < odsPrev):
            odsazeniDoleva = True
        else:
            odsazeniDoleva = False

        return (odsazeniDoleva)


    def vratPoleRadkuBezSipek(self, poleRadkuLog):

        poleRadkuBezSipek = []

        for i in range(0, len(poleRadkuLog)):
            radek = poleRadkuLog[i]
            radekNew = radek.replace('-->', '')
            radekNew = radekNew.strip()

            poleRadkuBezSipek.append(radekNew)

        return(poleRadkuBezSipek)


    def vratPoleOdsazeni(self, poleRadkuLog):

        poleObsazenychRadku = self.vratSeznamObsazenychRadku(poleRadkuLog)
        poleOdsazeniSipek = self.vratPoleIndexuRadkuObsahujiciSipky(poleRadkuLog, poleObsazenychRadku)
        poleOdsazeniZaokr = self.zaokrouhliOdsazeni(poleOdsazeniSipek)
        poleOdsazeniDleZavorky = self.vratOdsazeniDleZavorekKododu(poleRadkuLog)

        odsTotPole = self.sectiOdsazeni(poleOdsazeniZaokr, poleOdsazeniDleZavorky)

        return(odsTotPole)


    def sectiOdsazeni(self, poleOdsazeniZaokr, poleOdsazeniDleZavorky):

        odsTotPole = []

        for i in range(0, len(poleOdsazeniZaokr)):
            ods1 = poleOdsazeniZaokr[i]
            ods2 = poleOdsazeniDleZavorky[i]

            odsTot = ods1 + ods2
            odsTotPole.append(odsTot)

        return(odsTotPole)


    def vratOdsazeniDleZavorekKododu(self, poleRadkuLog):

        odsazeniDleZavorky = 0
        poleOdsazeniDleZavorky = []

        for i in range(0, len(poleRadkuLog)):

            poleOdsazeniDleZavorky.append(odsazeniDleZavorky)

            # odsazeni probiha az na vzdy dalsim radku, tudiz je potreba proves kod  az po vlozeni do pole
            # vykona se kod pro dalsi radek

            radek = poleRadkuLog[i]
            radekObsahujeZavorkuOtevrenou = self.detekujSubString(radek, '{')
            radekObsahujeZavorkuZavrenou = self.detekujSubString(radek, '}')

            if(radekObsahujeZavorkuOtevrenou == True):
                odsazeniDleZavorky = odsazeniDleZavorky + 10

            if(radekObsahujeZavorkuZavrenou == True):
                odsazeniDleZavorky = odsazeniDleZavorky - 10

        return(poleOdsazeniDleZavorky)


    # nektere radky muzou byt odskoceny, dle originalu, napr. o mezernik, proto odsazeni se zaokrouhluje
    def zaokrouhliOdsazeni(self, poleOdsazeniSipek):

        poleOdsazeniZaokr = []

        for i in range(0, len(poleOdsazeniSipek)):
            odsazeni = poleOdsazeniSipek[i]
            odsazeni10 = odsazeni/10
            odsazeniZaokr = round(odsazeni10, 0)
            odsazeniZaokr = int(odsazeniZaokr*10)
            poleOdsazeniZaokr.append(odsazeniZaokr)

        return(poleOdsazeniZaokr)



    # ziska pole boolean, pokud je True, pka na radku neco je, jinak tam neni nic
    def vratSeznamObsazenychRadku(self, poleRadkuLog):

        poleObsazenychRadku = []

        for i in range(0, len(poleRadkuLog)):
            radek = poleRadkuLog[i]
            radek = radek.strip()

            if(radek == ''):
                radekJeObsazeny = False
            else:
                radekJeObsazeny = True

            poleObsazenychRadku.append(radekJeObsazeny)

        return(poleObsazenychRadku)


    def vratPoleIndexuRadkuObsahujiciSipky(self, poleRadkuLog, poleObsazenychRadku):

        poleOdsazeniSipek = []
        odsazeniSipkyPrev = 0

        for i in range(0, len(poleRadkuLog)):
            radek = poleRadkuLog[i]
            radekJeObsazeny = poleObsazenychRadku[i]

            if(radekJeObsazeny == True):
                odsazeniSipky = self.ziskejOdsazeniSipky(radek)
            else:
                odsazeniSipky = odsazeniSipkyPrev


            poleOdsazeniSipek.append(odsazeniSipky)
            odsazeniSipkyPrev = odsazeniSipky

        return(poleOdsazeniSipek)


    def ziskejOdsazeniSipky(self, radek):

        odsazeniSipky = 0

        try:
            odsazeniSipky = radek.index('--> ')
        except:
            pass

        return(odsazeniSipky)


    def detekujSubString(self, radek, subStr):

        try:
            ind = radek.index(subStr)
            if(ind > -1):
                radekObsahujeSubString = True
            else:
                radekObsahujeSubString = False
        except:
            radekObsahujeSubString = False

        return(radekObsahujeSubString)