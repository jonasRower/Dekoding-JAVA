
# vyhledava indexy paru zavorek

class paryZavorek:

    def __init__(self, poleRadku):

        poleIndexu = indexyJakoVstupy(poleRadku)

        self.poleIndexuZavorekOtevrenych = poleIndexu.getIndexyRadkuOtevrenych()
        self.poleIndexuZavorekZavrenych = poleIndexu.getIndexyRadkuZavrenych()

        for i in range(0, len(self.poleIndexuZavorekOtevrenych)):
            if(i == 12):
                a = 12

            poleIndexuZavorekOt = self.poleIndexuZavorekOtevrenych[i]
            poleIndexuZavorekZav = self.poleIndexuZavorekZavrenych[i]

            # vrati pole zavorek dane tridy
            dvojiceNejblizsichZavorek = self.vratNejblizsiIndexyZavorek(poleIndexuZavorekOt, poleIndexuZavorekZav)

            print()




    def vratNejblizsiIndexyZavorek(self, poleIndexuOt, poleIndexuZav):

        dvojiceNejblizsichZavorek = []

        poleIndZavorekOtevrenych = poleIndexuOt
        poleIndZavorekZavrenych = poleIndexuZav

        poleRozdiluKPrvnimIndexum = self.vratPoleRozdiluZavorek(poleIndexuOt, poleIndexuZav)
        poleNew = poleRozdiluKPrvnimIndexum

        for i in range(0, len(poleNew)):
            souradnicePoleMinItem = self.vratindexyNejmensihoPrvkuPole(poleNew)

            indexOtZav = souradnicePoleMinItem[1]
            indexZavZav = souradnicePoleMinItem[0]

            dvojiceOtZav = self.vratIndOtZav(indexOtZav, indexZavZav, poleIndZavorekOtevrenych, poleIndZavorekZavrenych)
            poleNew = self.zmensiPoleORadky(poleNew, indexOtZav, indexZavZav)

            # odebere dany indexy, aby je nevybiral znovu
            indOtZav = dvojiceOtZav[0]
            indZavZav = dvojiceOtZav[1]

            poleIndZavorekOtevrenych = self.odeberZPoleDanyIndex(poleIndZavorekOtevrenych, indOtZav)
            poleIndZavorekZavrenych = self.odeberZPoleDanyIndex(poleIndZavorekZavrenych, indZavZav)

            dvojiceNejblizsichZavorek.append(dvojiceOtZav)

        return(dvojiceNejblizsichZavorek)


    def odeberZPoleDanyIndex(self, pole, index):

        pole.remove(index)
        return(pole)


    def zmensiPoleORadky(self, pole, indexOtZav, indexZavZav):

        poleNew = []

        for r in range(0, len(pole)):
            if(r != indexZavZav):
                radek = pole[r]
                radekNew = []
                for s in range(0, len(pole)):
                    if (s != indexOtZav):
                        polozka = radek[s]
                        radekNew.append(polozka)

                poleNew.append(radekNew)

        return(poleNew)



    def vratIndOtZav(self, indexOtZav, indexZavZav, poleIndZavorekOtevrenych, poleIndZavorekZavrenych):

        indexOtevrenaZav = poleIndZavorekOtevrenych[indexOtZav]
        indexZavrenaZav = poleIndZavorekZavrenych[indexZavZav]

        dvojiceOtZav = []
        dvojiceOtZav.append(indexOtevrenaZav)
        dvojiceOtZav.append(indexZavrenaZav)

        return(dvojiceOtZav)


    #def odeberRadekASloupecZPole()



    # hleda indexy nejmensiho prvku ctvsrcoveho pole
    def vratindexyNejmensihoPrvkuPole(self, pole):

        itemMax = self.ziskejNaxińalniPrvek(pole) + 1
        itemMin = itemMax
        rsMin = []

        rMin = -1
        sMin = -1


        for r in range(0, len(pole)):
            radek = pole[r]
            for s in range(0, len(radek)):
                polozka = radek[s]

                if (polozka < itemMin):
                    itemMin = polozka
                    rMin = r
                    sMin = s

        rsMin.append(rMin)
        rsMin.append(sMin)

        return(rsMin)


    def ziskejNaxińalniPrvek(self, pole):

        itemMax = 0

        for r in range(0, len(pole)):
            radek = pole[r]
            for s in range(0, len(radek)):
                polozka = radek[s]

                if(polozka > itemMax):
                    itemMax = polozka

        return(itemMax)


    def vratPoleRozdiluZavorek(self, poleIndexuOt, poleIndexuZav):

        poleRozdiluKPrvnimIndexum = []

        for i in range(0, len(poleIndexuZav)):
            indZav = poleIndexuZav[i]
            poleRozdilu = self.vratRozdilyKzavZavorkam(indZav, poleIndexuOt)
            poleRozdiluKPrvnimIndexum.append(poleRozdilu)

        return(poleRozdiluKPrvnimIndexum)


    def vratRozdilyKzavZavorkam(self, indZav, poleIndexuOt):

        poleRozdilu = []

        for i in range(0, len(poleIndexuOt)):
            indOt = poleIndexuOt[i]
            rozdil = indOt - indZav
            poleRozdilu.append(rozdil)

        return (poleRozdilu)


    def vratPoleIndexuOtevrenychZavorek(self, poleRadku):

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekObsahujeZavorkuOtevrenou = self.detekujZdaRadekObsahujeSubStr(radek, '{')
            radekObsahujeZavorkuZavrenou = self.detekujZdaRadekObsahujeSubStr(radek, '}')

            self.poleIndexuZavorekOtevrenych = self.pridejDataDoPole(self.poleIndexuZavorekOtevrenych, radekObsahujeZavorkuOtevrenou, i)
            self.poleIndexuZavorekZavrenych = self.pridejDataDoPole(self.poleIndexuZavorekZavrenych, radekObsahujeZavorkuZavrenou, i)


    def pridejDataDoPole(self, poleIndexu, status, index):

        if(status == True):
            poleIndexu.append(index)

        return(poleIndexu)






    # zatimm jen vytvari testovaci data, na kterych bude kodTestovan
    def pripravTestovaciData(self):

        poleRadku = []
        poleRadku.append('')
        poleRadku.append('')
        poleRadku.append('{')
        poleRadku.append('')
        poleRadku.append('{')
        poleRadku.append('{')
        poleRadku.append('}')
        poleRadku.append('')
        poleRadku.append('')
        poleRadku.append('')
        poleRadku.append('}')
        poleRadku.append('')
        poleRadku.append('}')

        return(poleRadku)


#zjisti na kterych radcich jsou indexy zavorek
class indexyJakoVstupy:

    def __init__(self, poleRadku):

        self.indexyRadkuOtevrenych = self.ziskejIndexyRadkuProTypZavorky(poleRadku, '{')
        self.indexyRadkuZavrenych = self.ziskejIndexyRadkuProTypZavorky(poleRadku, '}')

        print()


    def getIndexyRadkuOtevrenych(self):
        return(self.indexyRadkuOtevrenych)


    def getIndexyRadkuZavrenych(self):
        return(self.indexyRadkuZavrenych)



    def ziskejIndexyRadkuProTypZavorky(self, poleRadku, typZavorky):

        poleIndBool = self.vratPoleBoolZavProVsechnyUrovne(poleRadku, typZavorky)
        poleBoolFull = self.rozsirPoleOPolozkyFalse(poleIndBool)
        indexyRadkuPoSloupcich = self.ziskejIndexyBoolDleSloupcu(poleBoolFull)

        return(indexyRadkuPoSloupcich)


    def ziskejIndexyBoolDleSloupcu(self, pole):

        pocetSloupcu = len(pole[0])
        indexyRadkuPoSloupcich = []

        for s in range(0, pocetSloupcu):
            sloupec = self.vratSloupecPole(pole, s)
            indexyTrue = self.vratPoleIndexuTrueProSloupec(sloupec)

            indexyRadkuPoSloupcich.append(indexyTrue)

        return (indexyRadkuPoSloupcich)


    def vratPoleIndexuTrueProSloupec(self, sloupec):

        poleIndexu = []

        for i in range(0, len(sloupec)):
            polozka = sloupec[i]
            if (polozka == True):
                poleIndexu.append(i)

        return (poleIndexu)


    def vratSloupecPole(self, pole, indexSloupce):

        sloupec = []

        for r in range(0, len(pole)):
            polozka = pole[r][indexSloupce]
            sloupec.append(polozka)

        return (sloupec)


    def rozsirPoleOPolozkyFalse(self, pole):

        pocetSloupcu = self.vratMaximalniPocetSloupcuPole(pole)
        poleFalse = self.vytvorPoleNew(len(pole), pocetSloupcu)

        for r in range(0, len(pole)):
            for s in range(0, pocetSloupcu):
                try:
                    if (pole[r][s] == True):
                        poleFalse[r][s] = True
                except:
                    pass

        return (poleFalse)

    def vytvorPoleNew(self, pocetRadku, pocetSloupcu):

        poleFalse = []

        for r in range(0, pocetRadku):
            radekNew = []
            for s in range(0, pocetSloupcu):
                radekNew.append(False)

            poleFalse.append(radekNew)

        return (poleFalse)

    def vratMaximalniPocetSloupcuPole(self, pole):

        delkaRadkuMax = 0

        for i in range(0, len(pole)):
            radek = pole[i]
            delkaRadku = len(radek)
            if (delkaRadku > delkaRadkuMax):
                delkaRadkuMax = delkaRadku

        return (delkaRadkuMax)

    def vratPoleBoolZavProVsechnyUrovne(self, poleRadku, subStr):

        poleIndBool = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekSpl = radek.split('\\')
            radekBool = self.vratPoleBoolProDanyRadek(radekSpl, subStr)

            poleIndBool.append(radekBool)

        return (poleIndBool)

    def vratPoleBoolProDanyRadek(self, radek, substr):

        radekBool = []

        for i in range(0, len(radek)):
            polozka = radek[i]
            polozkaObsahujeSubStr = self.detekujZdaRadekObsahujeSubStr(polozka, substr)
            radekBool.append(polozkaObsahujeSubStr)

        return (radekBool)

        print()


    def detekujZdaRadekObsahujeSubStr(self, radek, substr):

        try:
            ind = radek.index(substr)
            if (ind > -1):
                substrNalezen = True
            else:
                substrNalezen = False
        except:
            substrNalezen = False

        return (substrNalezen)


