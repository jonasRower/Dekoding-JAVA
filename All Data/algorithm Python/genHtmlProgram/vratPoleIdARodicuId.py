class poleIdARodicuId:

    def __init__(self, adresyDlePoctuUrovniNadrazene):

        self.poleId = self.ziskejPoleId0(adresyDlePoctuUrovniNadrazene)
        self.poleRodicuId = self.zapisRodiceVsechUrovni(adresyDlePoctuUrovniNadrazene, self.poleId)


    def getPoleId(self):
        return(self.poleId)


    def getPoleRodicuId(self):
        return (self.poleRodicuId)



    def zapisRodiceVsechUrovni(self, adresyDlePoctuUrovniNadrazene, poleId):

        poleIdUrovneAll = []
        poleIdUrovne1 = []

        # prida vychozi uroven
        poleIdUrovneNewVychozi = self.vratRodiceVychoziUrovne(poleId)
        poleIdUrovne1.append(poleIdUrovneNewVychozi)
        poleIdUrovneAll.append(poleIdUrovne1)


        for i in range(1, len(adresyDlePoctuUrovniNadrazene)):
            uroven = i
            poleUroven = adresyDlePoctuUrovniNadrazene[uroven]

            if(i == 8):
                a = 10

            poleIdUrovneNew = self.vratRodiceProDanouUroven(poleId, uroven, adresyDlePoctuUrovniNadrazene, poleUroven)
            poleIdUrovneAll.append(poleIdUrovneNew)
            print()

        return(poleIdUrovneAll)


    def vratRodiceVychoziUrovne(self, poleId):

        poleIdVychozi = poleId[0][0]
        poleIdUrovneNew = []

        prvniPolozka = '#'
        poleIdUrovneNew.append(prvniPolozka)

        for i in range(1, len(poleIdVychozi)):
            id = poleIdVychozi[i]
            idNew = self.vytvorIdNew(id)

            poleIdUrovneNew.append(idNew)

        return (poleIdUrovneNew)



    def vratRodiceProDanouUroven(self, poleId, uroven, adresyDlePoctuUrovniNadrazene, poleUroven):

        poleIdUrovneNew = []

        idUroven = poleId[uroven]

        for i in range(0, len(idUroven)):
            polePodUroven1 = poleUroven[i]
            polozkaExp = polePodUroven1[0]

            #if(polozkaExp == 'C:\\Users\\jonas\\OneDrive\\Dokumenty\\2023\\Python\\testDll\\.idea'):
            #    a = "err"

            idRodic = self.vyhledejRodicePredchoziUrovne(uroven, polozkaExp, adresyDlePoctuUrovniNadrazene, poleId)

            # pokud rodice nenajde, je to asi proto, protoze neodmazal posledni lomitko
            if(idRodic == False):
                idRodic = self.vyhledejRodicePredchoziUrovne(uroven, polozkaExp, adresyDlePoctuUrovniNadrazene, poleId)

                polozkaExp = polozkaExp[0:len(polozkaExp)-2:1]
                print()

            idPodUroven = idUroven[i]
            idPodUrovenNew = self.vratIdPodUrovne(idPodUroven, idRodic)

            poleIdUrovneNew.append(idPodUrovenNew)
            print()

        return(poleIdUrovneNew)


    def vratIdPodUrovne(self, idPodUroven, idRodic):

        idPodUrovenNew = []
        idPodUrovenNew.append(idRodic)

        for i in range(1, len(idPodUroven)):
            id = idPodUroven[i]
            idNew = self.vytvorIdNew(id)
            idPodUrovenNew.append(idNew)

        return(idPodUrovenNew)


    def vytvorIdNew(self, id):

        idSpl = id.split('-')
        idNew = idSpl[0]

        for i in range(1, len(idSpl)-1):
            idNew = idNew + '-' + idSpl[i]

        return(idNew)



    def vyhledejRodicePredchoziUrovne(self, uroven, polozkaExp, adresyDlePoctuUrovniNadrazene, poleId):

        indexPredchoziUrovne = uroven - 1
        polozkyPredchoziUrovne = adresyDlePoctuUrovniNadrazene[indexPredchoziUrovne]
        poleIdPredchoziUrovne = poleId[indexPredchoziUrovne]

        for i in range(0, len(polozkyPredchoziUrovne)):
            adresyDlePoctuUrovniNadrazene1 = polozkyPredchoziUrovne[i]
            poleId1 = poleIdPredchoziUrovne[i]

            id = self.vyhledejIDRodicePredchoziUrovne1(polozkaExp, adresyDlePoctuUrovniNadrazene1, poleId1)

            if(id != False):
                break

        return(id)


    def vyhledejIDRodicePredchoziUrovne1(self, polozkaExp, adresyDlePoctuUrovniNadrazene1, poleId1):

        id = False

        for i in range(1, len(adresyDlePoctuUrovniNadrazene1)):
            polozka = adresyDlePoctuUrovniNadrazene1[i]
            if (polozka == polozkaExp):
                id = poleId1[i]
                break

        if(id == False):
            a = "err"

        return(id)


    def ziskejPoleId0(self, adresyDlePoctuUrovniNadrazene):

        poleId0 = []

        for i0 in range(0, len(adresyDlePoctuUrovniNadrazene)):
            polozky0 = adresyDlePoctuUrovniNadrazene[i0]
            id0 = str(i0)

            poleId1 = self.ziskejPoleId1(polozky0, id0)
            poleId0.append(poleId1)

        return(poleId0)


    def ziskejPoleId1(self, polozky0, id0):

        poleId1 = []

        for i1 in range(0, len(polozky0)):
            polozky1 = polozky0[i1]
            id1 = id0 + '-' + str(i1)

            poleIdPolozky1 = self.vratIdKPolozky1(polozky1, id1)
            poleId1.append(poleIdPolozky1)

        return(poleId1)


    def vratIdKPolozky1(self, polozky1, id1):

        poleIdPolozky1 = []
        poleIdPolozky1.append(id1)

        for i in range(1, len(polozky1)):
            id = id1 + "-" + str(i)
            poleIdPolozky1.append(id)

        return(poleIdPolozky1)


