class nacitejTxt:

    def __init__(self, dataLog):

        # pokud chci nacitat z logu, odkomentovat tyto radky
        #adresaLog = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\2023\\Python\\DoLinuxuData\\stromDekod3_test.txt"
        #dataLog = self.nactiDataTxt(adresaLog)

        self.upravDataLog(dataLog)

        poleNadrazenychAdres = self.vratPoleNadrazenychAdresaru(dataLog)
        potomkyKNadrazenymAdresam = self.vyhhledejPotomkyKeVsemNadrazenymAdresam(dataLog, poleNadrazenychAdres)

        self.adresyDlePoctuUrovniNadrazene = self.vratPocetZanoreniKPotomkumNadrazeneAdresy(potomkyKNadrazenymAdresam)
        self.dataLog = dataLog



    def getAdresyDlePoctuUrovniNadrazene(self):
        return(self.adresyDlePoctuUrovniNadrazene)


    def getDataLog(self):
        return(self.dataLog)


    # je potreba opravit data logu, tak nemel problem se sustringy mezi uvozovkami
    def upravDataLog(self, dataLog):

        for i in range(0, len(dataLog)):
            radek = dataLog[i]
            radekObsahujeUvozovky = self.detekujRadekSUvozovkami(radek)

            if(radekObsahujeUvozovky == True):
                radekNew = self.vratRadekBezLomitek(radek)
                dataLog[i] = radekNew


    def vratRadekBezLomitek(self, radek):

        startEnd = self.vratDvojiciIndexuUvozovek(radek)
        radekNew = self.nahradVSubstringuLomitka(radek, startEnd)

        return(radekNew)


    #vlozi misto lomitek paragrafy
    def nahradVSubstringuLomitka(self, radek, startEnd):

        start = startEnd[0]
        end = startEnd[1]+1
        subString = radek[start:end:1]
        subStringNew = subString.replace('\\', '§')

        radekNew = radek.replace(subString, subStringNew)

        return(radekNew)


    def vratDvojiciIndexuUvozovek(self, radek):

        try:
            ind1 = radek.index('"')

            x = slice(ind1 + 1, len(radek) - 1)
            arrSlice = radek[x]

            ind2 = ind1 + arrSlice.index('"')
        except:
            ind1 = -1
            ind2 = -1

        startEnd = []
        startEnd.append(ind1)
        startEnd.append(ind2)

        return(startEnd)


    def detekujRadekSUvozovkami(self, radek):

        radekObsahujeUvozovky = False

        try:
            ind = radek.index("\"")
            if(ind > -1):
                radekObsahujeUvozovky = True
            else:
                radekObsahujeUvozovky = False

        except:
            radekObsahujeUvozovky = False

        return(radekObsahujeUvozovky)



    def vratPocetZanoreniKPotomkumNadrazeneAdresy(self, potomkyKNadrazenymAdresam):

        poleZakladnichAdres = self.ziskejPoleZakladnichAdres(potomkyKNadrazenymAdresam)
        pocetZanoreniPole = self.vytvorPoleUrovni(poleZakladnichAdres)

        adresyDlePoctuUrovniNadrazene = self.seradAdresyDlePoctuUrovni(potomkyKNadrazenymAdresam, pocetZanoreniPole)

        return(adresyDlePoctuUrovniNadrazene)


    def ziskejPoleZakladnichAdres(self, potomkyKNadrazenymAdresam):

        poleZakladnichAdres = []

        for i in range(0, len(potomkyKNadrazenymAdresam)):
            zakladniAdresa = potomkyKNadrazenymAdresam[i][0]
            poleZakladnichAdres.append(zakladniAdresa)

        return(poleZakladnichAdres)



    def seradAdresyDlePoctuUrovni(self, dataLog, pocetZanoreniPole):

        pocetZanoreniPoleUniq = self.unique(pocetZanoreniPole)
        adresyDlePoctuUrovni = []

        for i in range(0, len(pocetZanoreniPoleUniq)):
            pocetZanoreni = pocetZanoreniPoleUniq[i]
            adresyDaneUrovne = self.vratAdresyDaneUrovne(dataLog, pocetZanoreniPole, pocetZanoreni)

            adresyDlePoctuUrovni.append(adresyDaneUrovne)
            print()

        return(adresyDlePoctuUrovni)


    def vratAdresyDaneUrovne(self, dataLog, pocetZanoreniPole, zanoreniExp):

        adresyDaneUrovne = []

        for i in range(0, len(pocetZanoreniPole)):
            pocetZanoeeni = pocetZanoreniPole[i]
            if(pocetZanoeeni == zanoreniExp):
                adresa = dataLog[i]

                poleObsahujePolozku = self.detekujZeJePolePrazdne(adresa)
                if(poleObsahujePolozku == True):
                    adresyDaneUrovne.append(adresa)

        return(adresyDaneUrovne)


    def detekujZeJePolePrazdne(self, pole):

        poleObsahujePolozku = False

        for i in range(0, len(pole)):
            polozka = pole[i]
            polozka = polozka.strip()
            if(polozka != ""):
                poleObsahujePolozku = True
                break

        return(poleObsahujePolozku)


    # vrati pole, kdy kazdy radek udava pocet zanorteni
    def vytvorPoleUrovni(self, dataLog):

        pocetZanoreniPole = []

        for i in range(0, len(dataLog)):
            radek = dataLog[i]
            pocetZanoreni = self.vratPocetUrovniRadku(radek)

            pocetZanoreniPole.append(pocetZanoreni)

        return(pocetZanoreniPole)


    def vratPocetUrovniRadku(self, radek):

        radekSpl = radek.split('\\')
        pocetZanoreni = len(radekSpl)

        return(pocetZanoreni)


    def vyhhledejPotomkyKeVsemNadrazenymAdresam(self, dataLog, poleNadrazenychAdres):

        jedinecneAdresyNadrazene = self.unique(poleNadrazenychAdres)
        poleVsechPotomku = []

        for i in range(0, len(jedinecneAdresyNadrazene)):
            adresaNadrazena = jedinecneAdresyNadrazene[i]
            polePotomku = self.vyhledejVsechnyPotomkyKNadrazeneAdrese(dataLog, adresaNadrazena, poleNadrazenychAdres)

            poleVsechPotomku.append(polePotomku)

        return(poleVsechPotomku)


    def vyhledejVsechnyPotomkyKNadrazeneAdrese(self, dataLog, nadrazenaAdresaExp, poleNadrazenychAdres):

            # vrat pole potomku
            polePotomku = []
            polePotomku.append(nadrazenaAdresaExp)

            for i in range(0, len(dataLog)):
                nadrazenaAdresa = poleNadrazenychAdres[i]
                if(nadrazenaAdresa == nadrazenaAdresaExp):
                    polePotomku.append(dataLog[i])

            return(polePotomku)


    def vratPolePotomku(self, dataLog, nadrazenaAdresa):

        print()



    def vratPoleNadrazenychAdresaru(self, dataLog):

        poleNadrazenychAdres = []

        for i in range(0, len(dataLog)):
            radek = dataLog[i]
            adresaNadrazena = self.vratNadtrazenouAdresu(radek)

            poleNadrazenychAdres.append(adresaNadrazena)

        return(poleNadrazenychAdres)


    def vratNadtrazenouAdresu(self, adresa):

        adresaSpl = adresa.split('\\')
        adresaNew = ""

        for i in range(0, len(adresaSpl)-1):
            slozka = adresaSpl[i]
            if(i == 0):
                adresaNew = adresaNew + slozka
            else:
                adresaNew = adresaNew + '\\' + slozka

        return(adresaNew)




    def nactiDataTxt(self, adresaLog):
        pole = []

        r = -1
        with open(adresaLog, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n', '')
                pole.append(line)

        return (pole)



    def unique(self, dataLog):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in dataLog:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

        return(unique_list)