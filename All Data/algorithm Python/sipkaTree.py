# tento modul transformuje data z textoveho souboru se sipkami do html pro tree.js

from numpy import *
import collections.abc
import copy

import vytvorJson

class konvertujData():

    def __init__(self, poleRadkuN):

        #self.detekujZavorkuForIf('                                  -->          for (int i = 0; i < SeznamRadkuArr.length; i++) {')

        poleOdsazeniSipek = self.vratPoleOdsazeniVsechSipek(poleRadkuN)
        poleRozmezi = self.detekujRozmeziDvouOdsazeni(poleOdsazeniSipek)

        poleRadkuVsechUrovni = self.ziskejPoleRadkuProVsechnaOdsazeni(poleRadkuN, poleRozmezi)
        indexyRadkuSZavorkami = self.ziskejVsechnyRadkySOtevrenouSlozenouZavorkou(poleRadkuN)

        vnorenaDataAll = self.vratPrvniPosledniIndexyOdsazeniSipek(poleOdsazeniSipek, poleRozmezi, poleRadkuN)
        indexyRadkuSZavorkamiNew = self.opravujIndexyRadkuSZavorkami(vnorenaDataAll, indexyRadkuSZavorkami, poleRadkuN)

        indexySRodici = self.opravujIndexyVnorenaDataAll(vnorenaDataAll, indexyRadkuSZavorkamiNew, 2)


        # vytvori js-soubor, kam tiskne strom
        dataTree = vytvorJson.createJSON(vnorenaDataAll, indexySRodici, poleRadkuN)


    # jednotlive polozky v 'indexyRadkuSZavorkami' prepise na -1, pro ty radky kde je
    #def odeberNeValidniIndexyRadku(self):


    def opravujIndexyRadkuSZavorkami(self, vnorenaDataAll, indexyRadkuSZavorkami, poleRadkuN):

        hledatRodice = self.vratHledatRodice(vnorenaDataAll, indexyRadkuSZavorkami)
        nazvyRodiceArr = self.vratNazvyRodiceArr(hledatRodice, poleRadkuN)
        indexyRadkuRodiceArr = self.vyhledejIndexyRadkuSRodici(hledatRodice, nazvyRodiceArr, poleRadkuN)
        indexyRadkuSZavorkamiNew = self.opravIndexyRadkuSZavorkami(indexyRadkuSZavorkami, hledatRodice, indexyRadkuRodiceArr)

        return(indexyRadkuSZavorkamiNew)


    def opravIndexyRadkuSZavorkami(self, indexyRadkuSZavorkami, indexyChybne, indexyOpravene):

        indexyRadkuSZavorkamiNew = copy.deepcopy(indexyRadkuSZavorkami)

        for i in range(0, len(indexyChybne)):
            indKOprave = indexyChybne[i]
            indIndChyb = indexyRadkuSZavorkami.index(indKOprave)
            indOpravene = indexyOpravene[i]

            indexyRadkuSZavorkamiNew[indIndChyb] = indOpravene

        return(indexyRadkuSZavorkamiNew)


    def vyhledejIndexyRadkuSRodici(self, hledatRodiceIndexy, nazvyRodiceArr, poleRadkuN):

        indexyRadkuRodiceArr = []

        for i in range(0, len(nazvyRodiceArr)):
            nazevRodice = nazvyRodiceArr[i]
            hledatRodiceOdIndexu = hledatRodiceIndexy[i]
            indexRadkuRodice = self.vyhledavejRodiceOdRadku(nazevRodice, hledatRodiceOdIndexu, poleRadkuN)

            indexyRadkuRodiceArr.append(indexRadkuRodice)

        return(indexyRadkuRodiceArr)


    # vyhledava indexy radku shodne s nazvem rodice, vzdy nahoru
    def vyhledavejRodiceOdRadku(self, nazevRodice, hledejOdRadku, poleRadkuN):

        indexRadkuRodice = -1

        for i in range(hledejOdRadku-1, 0, -1):
            radek = poleRadkuN[i]
            ind = self.vratIndexZnaku(radek, nazevRodice)
            if(ind > -1):
                indexRadkuRodice = i
                break

        return(indexRadkuRodice)


    def vratNazvyRodiceArr(self, hledatRodice, poleRadkuN):

        nazvyRodiceArr = []

        for i in range(0, len(hledatRodice)):
            indexRodice = hledatRodice[i]
            radek = poleRadkuN[indexRodice]

            nazevRodice = self.ziskejNazevRodice(radek, 'void')
            nazevRodice2 = self.ziskejNazevRodice(nazevRodice, '[]')

            nazevRodice2 = nazevRodice2.replace('[]', '')
            nazevRodice2 = nazevRodice2.replace(' ', '')
            nazevRodice2 = nazevRodice2 + '('

            nazvyRodiceArr.append(nazevRodice2)

        return(nazvyRodiceArr)


    def ziskejNazevRodice(self, radek, znak):

        ind = self.vratIndexZnaku(radek, znak)
        ind = ind + len(znak)
        strZaInd = radek[ind:len(radek):1]

        indZa = self.vratIndexZnaku(strZaInd, '(')
        if(indZa == -1):
            strPredInd = strZaInd
        else:
            strPredInd = strZaInd[0:indZa:1]

        return(strPredInd)


    def vratHledatRodice(self, vnorenaDataAll, indexyRadkuSZavorkami):

        # vyuzivam jiz stavajicich metod
        zanorenaDvojiceTrueFalse = self.opravujIndexyVnorenaDataAll(vnorenaDataAll, indexyRadkuSZavorkami, 0)
        vsechnyIndexy = self.nactiVsechnyIndexy(zanorenaDvojiceTrueFalse, False)
        hledatRodice = self.vratIndexyHledatRodice(vsechnyIndexy, indexyRadkuSZavorkami)

        return(hledatRodice)


    def vratIndexyHledatRodice(self, vsechnyIndexy, indexyRadkuSZavorkami):

        hledatRodice = []

        for i in range(0, len(vsechnyIndexy)):
            index = vsechnyIndexy[i]
            hledatRodiceIndex = indexyRadkuSZavorkami[index]
            hledatRodice.append(hledatRodiceIndex)

        return(hledatRodice)



    # vrati pole vsech indexu, ktere nejsou -1
    def nactiVsechnyIndexy(self, zanorenaDvojiceTrueFalse, indexyRadkuSZavorkami):

        vsechnyIndexy = []

        for i1 in range(0, len(zanorenaDvojiceTrueFalse)):
            indexySekce = zanorenaDvojiceTrueFalse[i1]

            for i2 in range(0, len(indexySekce)):
                indexySekce2 = indexySekce[i2]

                for i3 in range(0, len(indexySekce2)):
                    indexSekce3 = indexySekce2[i3]
                    if(indexyRadkuSZavorkami == False):
                        if(indexSekce3 != -1):
                            vsechnyIndexy.append(indexSekce3)
                    else:
                        # zatim nedela nic
                        print()

        return(vsechnyIndexy)



    def vyhledejNejblizsiNizsiIndex(self, indexExp, indexyRadkuSZavorkami):

        hledanyNizsiIndex = -1

        for i in range(1, len(indexyRadkuSZavorkami)):
            ind0 = indexyRadkuSZavorkami[i-1]
            ind1 = indexyRadkuSZavorkami[i]

            if(ind1 > indexExp):
                hledanyNizsiIndex = ind0
                break

        return(hledanyNizsiIndex)



    # jelikoz jsou v zdroji (se sipkami) chyby, opravuji se data zde:
    def opravujIndexyVnorenaDataAll(self, vnorenaDataAll, poleRadkuN, opravujData):

        vnorenaDataAllNew = []

        for i in range(0, len(vnorenaDataAll)):
            dvojiceJedneUrovne = vnorenaDataAll[i]
            dvojiceJedneUrovneNew = self.opravujZanorenaData(dvojiceJedneUrovne, poleRadkuN, opravujData)
            vnorenaDataAllNew.append(dvojiceJedneUrovneNew)

        return(vnorenaDataAllNew)


    def opravujZanorenaData(self, dvojiceJedneUrovne, poleRadkuN, opravujData):

        dvojiceJedneUrovneNew = []

        for i in range(0, len(dvojiceJedneUrovne)):
            zanorenaDvojice = dvojiceJedneUrovne[i]
            if(opravujData == 1):
                zanorenaDvojiceNew = self.opravujDataJedneSekce(zanorenaDvojice, poleRadkuN)

            if(opravujData == 0):
                zanorenaDvojiceNew = self.detekujZdaVyhledavatRodiceTrueFalse(zanorenaDvojice, poleRadkuN)

            if (opravujData == 2):
                zanorenaDvojiceNew = self.vratPoleIndexuRodicuSekce(zanorenaDvojice, poleRadkuN)

            dvojiceJedneUrovneNew.append(zanorenaDvojiceNew)

        return(dvojiceJedneUrovneNew)


    def vratPoleIndexuRodicuSekce(self, zanorenaDvojice, indexyRadkuSZavorkami):

        indexyRodicuSekce = []

        for i in range(0, len(zanorenaDvojice)):
            dvojice = zanorenaDvojice[i]
            indexExp = dvojice[0]
            hledanyNizsiIndex = self.vyhledejNejblizsiNizsiIndex(indexExp, indexyRadkuSZavorkami)

            indexyRodicuSekce.append(hledanyNizsiIndex)

        return(indexyRodicuSekce)


    def detekujZdaVyhledavatRodiceTrueFalse(self, zanorenaDvojice, indexyRadkuSZavorkami):

        zanorenaDvojiceTrueFalse = []
        zanorenaDvojiceTrueFalse.append(-1)

        for i in range(1, len(zanorenaDvojice)):
            dvojiceJedneUrovne = zanorenaDvojice[i]

            indexStart = dvojiceJedneUrovne[0]
            indexIndexStart = self.vratIndexZnaku(indexyRadkuSZavorkami, indexStart)

            zanorenaDvojiceTrueFalse.append(indexIndexStart)

        return(zanorenaDvojiceTrueFalse)


    def opravujDataJedneSekce(self, zanorenaDvojice, poleRadkuN):

        zanorenaDvojiceNew = []
        zanorenaDvojiceNew.append(zanorenaDvojice[0])

        for i in range(1, len(zanorenaDvojice)):
            dvojiceJedneUrovne = zanorenaDvojice[i]

            dvojiceStart = dvojiceJedneUrovne[0]
            radek = poleRadkuN[dvojiceStart]
            naRadkuJeJenSipka = self.detekujZdaNaRadkuJeJenSipka(radek)

            if (naRadkuJeJenSipka == True):
                indexRadkuJenBezSipky = self.najdiRadekJizBezJenSipky(dvojiceStart, poleRadkuN)
            else:
                indexRadkuJenBezSipky = dvojiceStart

            # vytvori nova data
            dvojiceEnd = dvojiceJedneUrovne[1]

            dvojiceJedneUrovneNew = []
            dvojiceJedneUrovneNew.append(indexRadkuJenBezSipky)
            dvojiceJedneUrovneNew.append(dvojiceEnd)

            zanorenaDvojiceNew.append(dvojiceJedneUrovneNew)

        return(zanorenaDvojiceNew)


    # pokud je na radku jen sipka, pak vyhledava radek nasledujici, kde sipka jiz neni
    def najdiRadekJizBezJenSipky(self, hledejOdRadku, poleRadkuN):

        radekJenBezSipky = -1

        for i in range(hledejOdRadku, len(poleRadkuN)):
            radek = poleRadkuN[i]
            naRadkuJeJenSipka = self.detekujZdaNaRadkuJeJenSipka(radek)

            if(naRadkuJeJenSipka == False):
                radekJenBezSipky = i
                break

        return(radekJenBezSipky)


    # detekuje, zda na radku je jen sipka a nic vic
    def detekujZdaNaRadkuJeJenSipka(self, radek):

        radekNew = radek.replace(' ', '')
        radekNew = radekNew.replace('\n', '')

        if(radekNew == '-->'):
            naRadkuJeJenSipka = True
        else:
            naRadkuJeJenSipka = False


        return(naRadkuJeJenSipka)


    def vratPrvniPosledniIndexyOdsazeniSipek(self, poleOdsazeniSipek, poleRozmezi, poleRadkuN):

        poleOdsazeniSipekUniq = self.unique(poleOdsazeniSipek)
        poleRozmeziDvojice = self.vratPoleRozmeziDvojice(poleRozmezi)
        odsazeniProDvojice = self.ziskejOdsazeniProDvojice(poleOdsazeniSipek, poleRozmeziDvojice)
        poleDvojicRozmeziProOdsazeni = self.seskupRozmeziDvojice(odsazeniProDvojice, poleRozmeziDvojice, poleOdsazeniSipekUniq)

        vnorenaDataAll = self.slucDvojice(poleDvojicRozmeziProOdsazeni)

        #opravi data
        vnorenaDataAllNew = self.opravujIndexyVnorenaDataAll(vnorenaDataAll, poleRadkuN, 1)

        return(vnorenaDataAllNew)


    # slouci dvojice, aby vedel ktera je do ktere zanorena
    def slucDvojice(self, poleDvojicRozmeziProOdsazeni):

        vnorenaDataAll = []

        for i in range(len(poleDvojicRozmeziProOdsazeni)-1, 1, -1):
            dvojiceRozmeziProOdsazeni1 = poleDvojicRozmeziProOdsazeni[i]
            dvojiceRozmeziProOdsazeni0 = poleDvojicRozmeziProOdsazeni[i-1]

            vnorenaData = self.slucujPosledniDveDvojice(dvojiceRozmeziProOdsazeni0, dvojiceRozmeziProOdsazeni1)
            vnorenaDataAll.append(vnorenaData)  # otestovat, asi se ne vse generuje spravne

        return(vnorenaDataAll)


    def slucujPosledniDveDvojice(self, dvojiceRozmeziProOdsazeni0, dvojiceRozmeziProOdsazeni1):

        poleOcekavanychIndexu = self.ziskejSeznamOcekavanychIndexu(dvojiceRozmeziProOdsazeni0)
        zaJakyIndexVlozitPole = self.ziskejZaJakyIndexVlozit(poleOcekavanychIndexu, dvojiceRozmeziProOdsazeni1)
        sloucenaData = self.vlozDvojiceRozmezi(dvojiceRozmeziProOdsazeni0, dvojiceRozmeziProOdsazeni1, zaJakyIndexVlozitPole)
        vnorenaData = self.vnorDataDoSebe(sloucenaData, dvojiceRozmeziProOdsazeni1)

        return(vnorenaData)


    def vnorDataDoSebe(self, sloucenaData, dvojiceRozmeziProOdsazeni1):

        indexyIntervalu = self.ziskejIndexyIntervalu(sloucenaData, dvojiceRozmeziProOdsazeni1)
        indexySloucenychDat = self.ziskejIndexySloucenychDat(indexyIntervalu)
        rodiceADeti = []        # na indexu 0 je rodic, pak jsou deti

        try:
            for i in range(0, len(sloucenaData)):
                rodic = sloucenaData[i]
                indexySloucData = indexySloucenychDat[i]
                vnorenaDataProRodice = self.ziskejVnorDataroRodice(rodic, dvojiceRozmeziProOdsazeni1, indexySloucData)
                rodiceADeti.append(vnorenaDataProRodice)
        except:
            udelejNic = True

        return(rodiceADeti)


    def ziskejVnorDataroRodice(self, rodicDvojice, dvojiceRozmeziProOdsazeni1,indexySloucData):

        rodicChild = []
        rodicChild.append(rodicDvojice)

        for i in range(0, len(indexySloucData)):
            index = indexySloucData[i]
            dvojicerozmezi = dvojiceRozmeziProOdsazeni1[index]
            rodicChild.append(dvojicerozmezi)

        return(rodicChild)


    def ziskejIndexySloucenychDat(self, indexyIntervalu):

        indexyIntervaluUniq = self.unique(indexyIntervalu)
        indexySloucenychDat = []

        for i in range(0, len(indexyIntervaluUniq)):
            index = indexyIntervaluUniq[i]
            seznamIndexu = self.vratSeznamIndexu(index, indexyIntervalu)

            indexySloucenychDat.append(seznamIndexu)

        return(indexySloucenychDat)

    # def vratVnorenaDataProJednohoRodice(self, dvojiceRodic, ):


    def vratSeznamIndexu(self, indexExp, pole):

        seznamIndexu = []

        for i in range(0, len(pole)):
            index = pole[i]
            if(index == indexExp):
                seznamIndexu.append(i)

        return(seznamIndexu)


    def ziskejIndexyIntervalu(self, sloucenaData, dvojiceRozmeziProOdsazeni1):

        indexyIntervalu = []

        if (sloucenaData != False):

            for i in range(0, len(dvojiceRozmeziProOdsazeni1)):
                dvojice = dvojiceRozmeziProOdsazeni1[i]
                zac = dvojice[0]
                kon = dvojice[1]

                indexIntervalu = -1

                indexIntervaluZac = self.vratVJakemJeCisloIntervalu(zac, sloucenaData)
                indexIntervaluKon = self.vratVJakemJeCisloIntervalu(kon, sloucenaData)

                if (indexIntervaluZac == indexIntervaluKon):
                    indexIntervalu = indexIntervaluZac

                indexyIntervalu.append(indexIntervalu)

        return(indexyIntervalu)


    def vratVJakemJeCisloIntervalu(self, cislo, intervaly):

        cisloIntervalu = -1

        for i in range(0, len(intervaly)):
            interval = intervaly[i]
            cisloJeVIntervalu = self.detekujZdaJeCisloVIntervalu(cislo, interval)
            if(cisloJeVIntervalu == True):
                cisloIntervalu = i
                break

        return(cisloIntervalu)


    def detekujZdaJeCisloVIntervalu(self, cislo, interval):

        cisloJeVIntervalu = False
        zacInterv = interval[0]
        konInterv = interval[1]

        if(cislo >= zacInterv):
            if(cislo <= konInterv):
                cisloJeVIntervalu = True

        return(cisloJeVIntervalu)


    # tady pokračovat
    # vymyslet strukturu, jak to prevest na jsoun s rodici a detmi

    # podivat se, jak vypada json a napasovat na nej data, ktera jsou tady
    def vlozDvojiceRozmezi(self, dvojiceRozmeziProOdsazeni0, dvojiceRozmeziProOdsazeni1, zaJakyIndexVlozitPole):

        dvojiceRozmeziProOdsazeniNew = dvojiceRozmeziProOdsazeni0.copy()

        for i in range(len(zaJakyIndexVlozitPole) - 1, -1, -1):
            vlozZaIndex = zaJakyIndexVlozitPole[i]
            if(vlozZaIndex > -1):
                vlozDvojici = dvojiceRozmeziProOdsazeni1[i]
                dvojiceRozmeziProOdsazeniNew.insert(vlozZaIndex+1, vlozDvojici)
                print()


        sloucenaData = self.slucDataKteraJdouZaSebou(dvojiceRozmeziProOdsazeniNew)

        return(sloucenaData)



    def slucDataKteraJdouZaSebou(self, dvojiceRozmeziProOdsazeni):

        indSlucArr = self.ziskejPoleIndexuNavazujicichDvojic(dvojiceRozmeziProOdsazeni)
        vratData = indSlucArr

        if(indSlucArr != False):
            indSlucArr2 = self.ziskejPoleIndexuNavazujicichDvojic(indSlucArr)

            if(indSlucArr2 != False):
                vratData = indSlucArr2


        return(vratData)



    def ziskejPoleIndexuNavazujicichDvojic(self, dvojiceRozmeziProOdsazeni):

        indSlucArr = []

        for i in range(1, len(dvojiceRozmeziProOdsazeni)):
            dvojiceRozmezi0 = dvojiceRozmeziProOdsazeni[i-1]
            dvojiceRozmezi1 = dvojiceRozmeziProOdsazeni[i]

            jeToPole = isinstance(dvojiceRozmezi0, collections.abc.Sequence)

            if(jeToPole == True):
                indPrvni = dvojiceRozmezi1[0]
                indPosl = dvojiceRozmezi0[1]
            else:   # pokud není pole
                indPrvni = dvojiceRozmezi1
                indPosl = dvojiceRozmezi0
                print()

            if(indPrvni == indPosl+1):
                indSlucArr.append(i)


        if(len(indSlucArr) > 0):
            prvniAPosledniIndexy = self.ziskejSeznamPrvnichAPoslednichIndexu(indSlucArr)
            dvojiceRozmeziProOdsazeniNew = self.ziskejPrvniPosledniRozmeziOdsazeni(dvojiceRozmeziProOdsazeni, prvniAPosledniIndexy)
        else:
            dvojiceRozmeziProOdsazeniNew = False

        return(dvojiceRozmeziProOdsazeniNew)



    # slouci nejaka data, avsak v dalsim cyklu opet neslucuje
    # sloucene odsazeni je chybne
    def ziskejPrvniPosledniRozmeziOdsazeni(self, dvojiceRozmeziProOdsazeni, prvniAPosledniIndexy):

        dvojiceRozmeziProOdsazeniNew = []
        prvniAPosledniIndexyJizZapsane = -1

        for i in range(0, len(dvojiceRozmeziProOdsazeni)):
            dvojice = dvojiceRozmeziProOdsazeni[i]
            indexJeVPoli = self.vratZdaJeIndexVPoli(prvniAPosledniIndexy, i)

            if(indexJeVPoli == False):
                dvojiceRozmeziProOdsazeniNew.append(dvojice)
            else:
                #prvniAPosledniIndexy = indexJeVPoli # nevraci True, ale indexy
                # aby zapsal jen 1x
                # ted to nejak nefunguje, prijit na to proc??
                if(prvniAPosledniIndexyJizZapsane != indexJeVPoli):
                    slouceneOdsazeni = self.ziskejSlouceneOdsazeni(dvojiceRozmeziProOdsazeni, indexJeVPoli)
                    dvojiceRozmeziProOdsazeniNew.append(slouceneOdsazeni)

                    prvniAPosledniIndexyJizZapsane = indexJeVPoli

        return(dvojiceRozmeziProOdsazeniNew)



    def ziskejSlouceneOdsazeni(self, dvojiceRozmeziProOdsazeni, prvniAPosledniIndexy):

        prvni = prvniAPosledniIndexy[0]
        posl = prvniAPosledniIndexy[1]

        prvRozm = self.ziskejDvojiciProDanyIndex(dvojiceRozmeziProOdsazeni, prvni)
        poslRozm = self.ziskejDvojiciProDanyIndex(dvojiceRozmeziProOdsazeni, posl)

        prvIndRozm = prvRozm[0]
        poslIndRozm = poslRozm[1]

        dvojNew = []
        dvojNew.append(prvIndRozm)
        dvojNew.append(poslIndRozm)

        return(dvojNew)



    def ziskejDvojiciProDanyIndex(self, dvojiceRozmeziProOdsazeni, index):

        dvojiceProDanyIndex = dvojiceRozmeziProOdsazeni[index]

        return (dvojiceProDanyIndex)


    # bud vrati False, nebo dvojici krajnich indexu
    def vratZdaJeIndexVPoli(self, prvniAPosledniIndexy, index):

        indexJeVPoli = False
        ukonciPoPrvnimCyklu = False

        for i in range(0, len(prvniAPosledniIndexy)):
            prvniPoslInd = prvniAPosledniIndexy[i]

            if(type(prvniPoslInd) == int):
                prvniPoslInd = prvniAPosledniIndexy
                ukonciPoPrvnimCyklu = True

            prvniIndex = prvniPoslInd[0]
            poslIndex = prvniPoslInd[1]

            indexJeVPoli = self.vratZdaJeIndexVPoli2(prvniIndex, poslIndex, index)


            if(indexJeVPoli == True):
                indexJeVPoli = prvniPoslInd
                break

            if(ukonciPoPrvnimCyklu == True):
                break

        """
        else:   # pokud je dimenze = 1

            prvniIndex = prvniAPosledniIndexy[0]
            poslIndex = prvniAPosledniIndexy[1]

            indexJeVPoli = self.vratZdaJeIndexVPoli2(prvniIndex, poslIndex, index)
        """

        return(indexJeVPoli)



    def vratZdaJeIndexVPoli2(self, prvniIndex, poslIndex, index):

        indexJeVPoli = False

        if(index >= prvniIndex):
            if(index <= poslIndex):
                indexJeVPoli = True

        return(indexJeVPoli)



    def ziskejSeznamPrvnichAPoslednichIndexu(self, indSlucArr):

        prvniAPosledniIndexy = []
        prvniIndexAPosledniIndex = self.ziskejPrvniAPosledniZRadyJdoucichIndexu(indSlucArr, 0)
        prvniAPosledniIndexy.append(prvniIndexAPosledniIndex)

        for i in range(0, len(indSlucArr)):
            posledniIndex = prvniIndexAPosledniIndex[1]
            zacniOdIndexu = indSlucArr.index(posledniIndex)

            if(zacniOdIndexu == len(indSlucArr)-1):
                break

            prvniIndexAPosledniIndex = self.ziskejPrvniAPosledniZRadyJdoucichIndexu(indSlucArr, zacniOdIndexu+1)
            prvniAPosledniIndexy.append(prvniIndexAPosledniIndex)

        return(prvniAPosledniIndexy)


    def ziskejPrvniAPosledniZRadyJdoucichIndexu(self, indSlucArr, zacniOdIndexu):

        prvniIndex = indSlucArr[zacniOdIndexu]
        posledniIndex = -1

        for i in range(zacniOdIndexu+1, len(indSlucArr)):
            indCur = indSlucArr[i]
            indPrev = indSlucArr[i-1]

            if(indCur != indPrev+1):
                if (indCur > indPrev):
                    posledniIndex = indPrev
                    break


        if(i == len(indSlucArr)-1):
            posledniIndex = indSlucArr[i]

        if(posledniIndex == -1):
            posledniIndex = prvniIndex

        prvniIndexAPosledniIndex = []
        prvniIndexAPosledniIndex.append(prvniIndex-1)
        prvniIndexAPosledniIndex.append(posledniIndex)

        return(prvniIndexAPosledniIndex)



    def ziskejZaJakyIndexVlozit(self, poleOcekavanychIndexu, dvojiceRozmeziProOdsazeni1):

        zaJakyIndexVlozitPole = []

        for i in range(0, len(dvojiceRozmeziProOdsazeni1)):
            dvojice = dvojiceRozmeziProOdsazeni1[i]
            indexPrvni = dvojice[0]

            try:
                indOcek = poleOcekavanychIndexu.index(indexPrvni)
            except:
                indOcek = -1


            zaJakyIndexVlozitPole.append(indOcek)


        return(zaJakyIndexVlozitPole)



    def ziskejSeznamOcekavanychIndexu(self, dvojiceRozmeziProOdsazeni0):

        poleOcekavanychIndexu = []

        for i in range(0, len(dvojiceRozmeziProOdsazeni0)):
            dvojice = dvojiceRozmeziProOdsazeni0[i]
            poslIndex = dvojice[1]
            ocekIndex = poslIndex + 1

            poleOcekavanychIndexu.append(ocekIndex)

        return(poleOcekavanychIndexu)


    def seskupRozmeziDvojice(self, odsazeniProDvojice, poleRozmeziDvojice, poleOdsazeniSipekUniq):

        poleDvojicRozmeziProOdsazeni = []

        for i in range(0, len(poleOdsazeniSipekUniq)):
            odsazeni = poleOdsazeniSipekUniq[i]
            indexyRozmeziDvojice = self.vratVsechnyIndexyRozmeziDvojice(odsazeniProDvojice, odsazeni)
            poleRozmeziProOdsazeni = self.vratPoleRozmeziProOdsazeni(indexyRozmeziDvojice, poleRozmeziDvojice)

            poleDvojicRozmeziProOdsazeni.append(poleRozmeziProOdsazeni)

        return(poleDvojicRozmeziProOdsazeni)


    def vratPoleRozmeziProOdsazeni(self, indexyRozmeziDvojice, poleRozmeziDvojice):

        poleRozmeziProOdsazeni = []

        for i in range(0, len(indexyRozmeziDvojice)):
            index = indexyRozmeziDvojice[i]
            rozmeziProOdsazeni = poleRozmeziDvojice[index]
            poleRozmeziProOdsazeni.append(rozmeziProOdsazeni)

        return(poleRozmeziProOdsazeni)


    def vratVsechnyIndexyRozmeziDvojice(self, odsazeniProDvojice, odsazeniSipekExp):

        indexyRozmeziDvojice = []

        for i in range(0, len(odsazeniProDvojice)):
            odsazeniSipek = odsazeniProDvojice[i]
            if(odsazeniSipek == odsazeniSipekExp):
                indexyRozmeziDvojice.append(i)

        return(indexyRozmeziDvojice)



    def ziskejOdsazeniProDvojice(self, poleOdsazeniSipek, poleRozmeziDvojice):

        odsazeniProDvojice = []

        for i in range(0, len(poleRozmeziDvojice)):
            rozmeziDvojice = poleRozmeziDvojice[i]
            posledniIndex = rozmeziDvojice[1]
            odsazeniPoslešdniIndex= poleOdsazeniSipek[posledniIndex]
            odsazeniProDvojice.append(odsazeniPoslešdniIndex)

        return(odsazeniProDvojice)


    def vratPoleRozmeziDvojice(self, poleRozmezi):

        poleRozmeziDvojice = []

        for i in range(0, len(poleRozmezi)):
            rozmezi0 = poleRozmezi[i-1]
            rozmezi1 = poleRozmezi[i]-1

            # opravi data
            if(rozmezi0 > rozmezi1):
                rozmezi0 = 0

            dvojice = []
            dvojice.append(rozmezi0)
            dvojice.append(rozmezi1)

            poleRozmeziDvojice.append(dvojice)


        return(poleRozmeziDvojice)


    def ziskejVsechnyRadkySOtevrenouSlozenouZavorkou(self, poleRadkuN):
        #jednaSeOForIf
        indexyRadkuSZavorkami = []

        for i in range(0, len(poleRadkuN)):
            radek = poleRadkuN[i]
            indexZavOtSloz = self.vratIndexZnaku(radek, '{')
            if(indexZavOtSloz > -1):
                samotnaZavorkaNaRadku = self.detekujZdaNaRadkuJeJenZavrenaZav(radek)

                if(samotnaZavorkaNaRadku == True):
                    indexRadkuObezav = self.vyhledejRadekSObemaZavorkami(poleRadkuN, i)
                    indexyRadkuSZavorkamiAppend = indexRadkuObezav
                    #indexyRadkuSZavorkami.append(indexRadkuObezav)

                else:
                    indexyRadkuSZavorkamiAppend = i
                    #indexyRadkuSZavorkami.append(i)


                radekForIf = poleRadkuN[indexyRadkuSZavorkamiAppend]
                jednaSeOForIf = self.detekujZavorkuForIf(radekForIf)
                if(jednaSeOForIf == False):
                    indexyRadkuSZavorkami.append(indexyRadkuSZavorkamiAppend)

        return(indexyRadkuSZavorkami)


    # postupuje v protismeru, nahoru a hleda nejblizsi radek, ktery ma zavorky ()
    def vyhledejRadekSObemaZavorkami(self, poleRadkuN, indRadku):

        indexRadkuObezav = -1

        for i in range(indRadku, 0, -1):
            radek = poleRadkuN[i]
            radekMaObeZavorky = self.detekujZdaRadekMaObeZavorky(radek)
            if(radekMaObeZavorky == True):
                indexRadkuObezav = i
                break

        return(indexRadkuObezav)


    # detekuje zda je na radku dvojice zavorek '()'
    def detekujZdaRadekMaObeZavorky(self, radek):

        radekMaObeZavorky = False

        indOt = self.vratIndexZnaku(radek, '(')
        indZav = self.vratIndexZnaku(radek, ')')

        if(indOt > -1):
            if(indZav > indOt):
                radekMaObeZavorky = True

        return(radekMaObeZavorky)



    def detekujZavorkuForIf(self, radek):

        radek = radek.replace('-->', '')
        radek = radek.replace('()', '')

        indOt = self.vratIndexZnaku(radek, '(')
        indZav = self.vratIndexZnaku(radek, ')') + 1

        predOt = radek[0:indOt:1]
        zaZav = radek[indZav:len(radek):1]
        meziZav = radek[indOt:indZav:1]

        predOt = predOt.replace(' ', '')
        zaZav = zaZav.replace(' ', '')

        jednaSeOForIf = False

        if(predOt == 'for'):
            jednaSeOForIf = self.detekujZavorkuFor(meziZav)

        if (predOt == 'if'):
            jednaSeOForIf = self.detekujZavorkuIf(meziZav)


        return(jednaSeOForIf)



    def detekujZavorkuFor(self, meziZav):

        meziZavSpl = meziZav.split(';')
        if(len(meziZavSpl)==3):
            jednaSeOFor = True
        else:
            jednaSeOFor = False

        return(jednaSeOFor)



    def detekujZavorkuIf(self, meziZav):

        # aby to bylo jednodusi, nahradi znak nerovnosti nebo '==' s ';;'
        # pak to porovna uplne stejne jako ve 'detekujZavorkuFor'

        meziZav = meziZav.replace('<', ';;')
        meziZav = meziZav.replace('>', ';;')
        meziZav = meziZav.replace('==', ';;')

        meziZavSpl = meziZav.split(';;')
        if(len(meziZavSpl)==2):
            jednaSeOIf = True
        else:
            jednaSeOIf = False

        return(jednaSeOIf)


    # detekuje, ze je na radku pouze zavrena zavorka a nic vic
    def detekujZdaNaRadkuJeJenZavrenaZav(self, radek):

        radekNew = radek.replace('-->', '')
        radekNew = radekNew.replace('\n', '')
        radekNew = radekNew.replace(' ', '')

        if(radekNew == '{'):
            samotnaZavorkaNaRadku = True
        else:
            samotnaZavorkaNaRadku = False


        return(samotnaZavorkaNaRadku)


    def ziskejPoleRadkuProVsechnaOdsazeni(self, poleRadkuN, poleRozmezi):

        poleRadkuVsechUrovni = []

        for i in range(0, len(poleRozmezi)):
            poleRadkuUrovne = self.ziskejPoleRadkuProJednoOdsazeni(poleRadkuN, poleRozmezi, i)
            poleRadkuVsechUrovni.append(poleRadkuUrovne)

        return(poleRadkuVsechUrovni)



    def ziskejPoleRadkuProJednoOdsazeni(self, poleRadkuN, poleRozmezi, indexRozmezi):

        poleRadkuUrovne = []

        if(indexRozmezi == 0):
            prvniRadek = 0
        else:
            prvniRadek = poleRozmezi[indexRozmezi-1]

        posledniRadek = poleRozmezi[indexRozmezi]

        for i in range(prvniRadek, posledniRadek):
            radek = poleRadkuN[i]
            poleRadkuUrovne.append(radek)


        return(poleRadkuUrovne)


    def detekujRozmeziDvouOdsazeni(self, poleOdsazeniSipek):

        poleRozmezi = []

        for i in range(1, len(poleOdsazeniSipek)):
            odsazeni0 = poleOdsazeniSipek[i-1]
            odsazeni1 = poleOdsazeniSipek[i]

            if(odsazeni0 != odsazeni1):
                rozmezi = i
                poleRozmezi.append(rozmezi)

        return(poleRozmezi)



    def vratPoleOdsazeniVsechSipek(self, poleRadkuN):

        poleOdsazeniSipek = []

        for i in range(0, len(poleRadkuN)):
            radek = poleRadkuN[i]
            odsazeniSipky = self.vratIndexZnaku(radek, '-->')
            poleOdsazeniSipek.append(odsazeniSipky)

        return(poleOdsazeniSipek)


    def vratIndexZnaku(self, radek, znak):

        try:
            indexZnaku = radek.index(znak)
        except:
            indexZnaku = -1


        return(indexZnaku)


    # function to get unique values
    def unique(self, list1):

        # intilize a null list
        unique_list = []

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

        return(unique_list)
