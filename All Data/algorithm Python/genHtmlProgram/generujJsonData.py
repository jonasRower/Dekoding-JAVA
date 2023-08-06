import copy

class jsonData:

    def __init__(self, adresy, poleId, poleRodicu, dataLog):

        self.poleRadku = []
        self.poleDatJson = []
        self.generujPoleRadku(adresy, poleId, poleRodicu)

        self.errorOption = '#'
        #self.errorOption = 'last'
        #self.errorOption = 'end'

        #self.countRows = 16


        #odmaze duplicitni radky
        oprava = opravDuplicitniPolozkyVPoleDat(self.poleDatJson)
        poleDatJsonNew = oprava.getPoleDatJsonModif()

        # test
        #poleDatJsonNew = self.poleDatJson

        #vygeneruje pole radku do html
        self.generujPoleRadkuHtml(poleDatJsonNew)

        # opravi polsedmni radek, odmaze ","
        self.opravPosledniRadek()




    def getPoleRadku(self):
        return(self.poleRadku)



    def generujPoleRadkuHtml(self, poleDatJson):

        for i in range(0, len(poleDatJson)):

            #if(i == self.countRows):
            #    break

            id = poleDatJson[i][0]

            if(i == 45):
                a = 10

            if(id != False):
                parent = poleDatJson[i][1]
                text = poleDatJson[i][2]



                # prda radek do pole radku
                radek = self.zapisJsonData(id, parent, text)

                if(radek == False):
                    break
                else:
                    self.poleRadku.append(radek)

                self.latestParent = parent



    # na poslednim radku je treba vymazat ','
    def opravPosledniRadek(self):

        radek = self.poleRadku[len(self.poleRadku)-1]
        radekNew = radek.replace('},', '}')
        self.poleRadku[len(self.poleRadku) - 1] = radekNew


    def generujpoleDatJsonNew(self, adresyFalse, poleDatJson):

        poleDatJsonNew = []

        for i in range(0, len(adresyFalse)):
            adresa = adresyFalse[i]
            if(adresa != False):
                radek = []
                radek.append(poleDatJson[i][0])
                radek.append(poleDatJson[i][1])
                radek.append(poleDatJson[i][2])

                poleDatJsonNew.append(radek)

        return(poleDatJsonNew)



    def generujPoleRadku(self, adresy, poleId, poleRodicu):

        for i in range(0, len(adresy)):
            adresy1 = adresy[i]
            poleId1 = poleId[i]
            poleRodicu1 = poleRodicu[i]

            self.generujPoleRadku1(adresy1, poleId1, poleRodicu1)


    def generujPoleRadku1(self, adresy1, poleId1, poleRodicu1):

        for i in range(0, len(adresy1)):
            adresy2 = adresy1[i]
            poleId2 = poleId1[i]
            poleRodicu2 = poleRodicu1[i]

            self.generujPoleRadku2(adresy2, poleId2, poleRodicu2)


    def generujPoleRadku2(self, adresy2, poleId2, poleRodicu2):

        for i in range(0, len(adresy2)):
            adresa = adresy2[i]
            id = poleId2[i]
            rodic = poleRodicu2[i]

            if(rodic == False):
               a = 10


            nazevSlozky = self.vratNazevSlozky(adresa)
            self.zapisPoleDat(id, rodic, nazevSlozky)
            #self.zapisJsonData(id, rodic, nazevSlozky)


    def vratNazevSlozky(self, adreesa):

        adresaSpl = adreesa.split('\\')
        nazevSlozky = adresaSpl[len(adresaSpl)-1]

        return(nazevSlozky)


    def zapisPoleDat(self, id, parent, text):

        dataJedenRadek = []
        dataJedenRadek.append(id)
        dataJedenRadek.append(parent)
        dataJedenRadek.append(text)

        self.poleDatJson.append(dataJedenRadek)


    def zapisJsonData(self, id, parent, text):

        text = text.replace('"', '\\"')
        try:
            radek = '                { "id": "' + id + '", "parent": "' + parent + '", "text": "' + text + '" },'
        except:
            # pokud nastane chyba, resi se to dle moznosti:
            # pokud je nastaveno:

            #self.errorOption = '#'     - nastavi parent jako '#' - cimz by mel vytvorit novou vetev
            #self.errorOption = 'last'  - nastavi parent jako predchozi posledni parent, cimz napoji na posledni vetev
            #self.errorOption = 'end'   - ukonci zapis

            if(self.errorOption  == '#'):
                parent = '#'
                radek = '                { "id": "' + id + '", "parent": "' + parent + '", "text": "' + text + '" },'

            if (self.errorOption == 'last'):
                parent = self.latestParent
                radek = '                { "id": "' + id + '", "parent": "' + parent + '", "text": "' + text + '" },'

            if (self.errorOption == 'end'):
                radek = False

        return(radek)





class opravDuplicitniPolozkyVPoleDat:

    def __init__(self, poleDatJson):

        poleId = self.vratPole1D(poleDatJson, 0)
        poleRodicu = self.vratPole1D(poleDatJson, 1)
        poleText = self.vratPole1D(poleDatJson, 2)

        poleVsechVyskytuAll = self.vratPoleIndexuRadkuStejnychTextu(poleText)
        poleDvojicAll = self.vratDvojiceProVsechnyVyskyty(poleVsechVyskytuAll, poleId, poleRodicu)

        poleRadkuModif = self.vytvorPoleDatKteraSeBudouModifikovat(poleDvojicAll, poleDatJson)
        self.poleDatJsonModif = self.modifikujPoleDatJson(poleRadkuModif, poleDatJson)



    def getPoleDatJsonModif(self):
        return(self.poleDatJsonModif)


    def vratDvojiceProVsechnyVyskyty(self, poleVsechVyskytuAll, poleId, poleRodicu):

        poleDvojicAll = []

        for i in range(0, len(poleVsechVyskytuAll)):
            subPole = poleVsechVyskytuAll[i]
            delkaSubPole = len(subPole)
            if(delkaSubPole > 2):
                poleDvojic = self.parujDelsiSeznamIndexu(subPole, poleId, poleRodicu)
                poleDvojicAll.append(poleDvojic)

                #odmaze polozku subpole z poleVsechVyskytuAll, jelikoz jiz data rozdelil do poleDvojicAll
                poleVsechVyskytuAll[i] = False

        poleDvojicAll2D = self.prevedPoleNa2D(poleDvojicAll)
        poleDvojicAllNew = poleVsechVyskytuAll + poleDvojicAll2D

        return(poleDvojicAllNew)


    # preved pole zpet na 2D, jelikoz ted neni
    def prevedPoleNa2D(self, poleDvojicAll):

        poleDvojicAll2D = []

        for i1 in range(0, len(poleDvojicAll)):
            radek = poleDvojicAll[i1]

            for i2 in range(0, len(radek)):
                dvojice = radek[i2]
                if(dvojice[1] > -1):
                    poleDvojicAll2D.append(dvojice)

        return(poleDvojicAll2D)


    def parujDelsiSeznamIndexu(self, poleIndexu, poleId, poleRodicu):

        poleIdIndexy = self.vratpolePolozekProDaneIndexy(poleIndexu, poleId)
        poleRodicuIndexy = self.vratpolePolozekProDaneIndexy(poleIndexu, poleRodicu)

        poleDvojic = []

        for i in range(0, len(poleIdIndexy)):
            idFrArr = poleIndexu[i]
            polozkaJeJizZapsana = self.detekujZdaPolozkuJizZapsal(poleDvojic, idFrArr)

            # pokud jiz polozka nebyla vybrana predchozim cyklem, pak ji zapisuje
            if(polozkaJeJizZapsana == False):
                id = poleIdIndexy[i]
                try:
                    indexRodiceIndexy = poleRodicuIndexy.index(id)
                    parentFrArr = poleIndexu[indexRodiceIndexy]
                except:
                    parentFrArr = -1

                dvojice = []
                dvojice.append(idFrArr)
                dvojice.append(parentFrArr)

                poleDvojic.append(dvojice)

        return(poleDvojic)


    def detekujZdaPolozkuJizZapsal(self, poleDvojic, polozkaExp):

        polozkaJizZapsana = False

        for i in range(0, len(poleDvojic)):
            dvojice = poleDvojic[i]
            polozka = dvojice[1]

            if(polozka == polozkaExp):
                polozkaJizZapsana = True
                break

        return(polozkaJizZapsana)


    def vratpolePolozekProDaneIndexy(self, poleIndexu, polePolozek):

        polePolozekSel = []

        for i in range(0, len(poleIndexu)):
            index = poleIndexu[i]
            polozka = polePolozek[index]
            polePolozekSel.append(polozka)

        return(polePolozekSel)


    def vratPoleIndexuRadkuStejnychTextu(self, poleText):

        poleVsechVyskytuAll = []

        poleTextUniq = self.unique(poleText)
        for i in range(0, len(poleTextUniq)):
            text = poleTextUniq[i]
            poleVsechVyskytu = self.vratPoleVsechVyskytu(poleText, text)

            if(len(poleVsechVyskytu)> 1):
                poleVsechVyskytuAll.append(poleVsechVyskytu)

        return(poleVsechVyskytuAll)


    def vratPoleVsechVyskytu(self, poleText, text):

        indFind = -1
        poleVsechVyskytu = []

        for i in range(0, len(poleText)):
            indFind = self.vratIndexFrom(poleText, indFind+1, text)

            if(indFind == -1):
                break
            else:
                poleVsechVyskytu.append(indFind)


        return(poleVsechVyskytu)



    def vratIndexFrom(self, arr, indexFrom, find):

        x = slice(indexFrom, len(arr)-1)
        arrSlice = arr[x]

        try:
            indFind = indexFrom + arrSlice.index(find)
        except:
            indFind = -1

        return(indFind)


    def modifikujPoleDatJson(self, poleRadkuModif, poleDatJson):

        poleDatJsonModifNew = copy.deepcopy(poleDatJson)

        for i in range(0, len(poleRadkuModif)):
            indexRadku = poleRadkuModif[i][0]

            id = poleRadkuModif[i][1]
            parent = poleRadkuModif[i][2]
            text = poleRadkuModif[i][3]

            poleDatJsonModifNew[indexRadku][0] = id
            poleDatJsonModifNew[indexRadku][1] = parent
            poleDatJsonModifNew[indexRadku][2] = text


        return(poleDatJsonModifNew)


    def vytvorPoleDatKteraSeBudouModifikovat(self, poleDvojicIndexuRadku, poleDatJson):

        poleRadkuModif = []

        for i in range(0, len(poleDvojicIndexuRadku)):

            if(poleDvojicIndexuRadku[i] != False):

                indexRadku = poleDvojicIndexuRadku[i][0]
                indexRadkuId = poleDvojicIndexuRadku[i][1]

                poleRadkuModif = self.opravRadek(indexRadku, indexRadkuId, poleDatJson, poleRadkuModif)
                poleRadkuModif = self.vymazRadek(indexRadkuId, poleRadkuModif)


        return(poleRadkuModif)



    def vymazRadek(self, indexRadku, poleRadkuModif):

        poleRadkuModif = self.pridejRadekDoPole(poleRadkuModif, indexRadku, False, False, False)
        return(poleRadkuModif)



    def opravRadek(self, indexRadku, indexRadkuId, poleDatJson, poleRadkuModif):

        # opravi radek
        id = poleDatJson[indexRadkuId][0]
        parent = poleDatJson[indexRadku][1]
        text = poleDatJson[indexRadku][2]

        poleRadkuModif = self.pridejRadekDoPole(poleRadkuModif, indexRadku, id, parent, text)

        return(poleRadkuModif)


    def pridejRadekDoPole(self, pole, pol1, pol2, pol3, pol4):

        radek = []
        radek.append(pol1)
        radek.append(pol2)
        radek.append(pol3)
        radek.append(pol4)

        pole.append(radek)

        return(pole)


    def vratPole1D(self, pole2D, index):

        pole1D = []

        for i in range(0, len(pole2D)):
            polozka = pole2D[i][index]
            pole1D.append(polozka)

        return(pole1D)


    def unique(self, dataLog):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in dataLog:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

        return(unique_list)
