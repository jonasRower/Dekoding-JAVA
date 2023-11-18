


import operator as op

# prirazuje k textu atributy, tak aby mohl vykreslovat text barevne

class barevnyText():

    def __init__(self, dataDaneTridy, ostatniMetody, poleRadkuNOdDo):

        self.ostatniMetody = ostatniMetody

        #poleRadkuNOdDo = dataDaneTridy.poleRadku
        #poleRadkuNOdDo = self.vratJenPotrebnyKodPoleRadku(poleRadkuDaneTridy, vyjmiKodOdRadku, vyjmiKodDoRadku)

        self.nazevInstanceAr = self.vratJenPotrebnaData(dataDaneTridy.nazevInstance)
        self.nazevMetodyArr = self.vratJenPotrebnaData(dataDaneTridy.nazevMetody)
        self.nazevTridyArr = self.vratJenPotrebnaData(dataDaneTridy.nazevTridy)
        self.volanaInstanceArr = self.vratJenPotrebnaData(dataDaneTridy.volanaInstance)
        self.volanaMetodaArr = self.vratJenPotrebnaData(dataDaneTridy.volanaMetoda)
        self.volanaTridaArr = self.vratJenPotrebnaData(dataDaneTridy.volanaTrida)

        self.radekSlovaAtributyAll = self.rozdelRadkyNaSlova(poleRadkuNOdDo)
        #poleNaJson(radekSlovaAtributyArr)


    def getRadekSlovaAtributyAll(self):

        return(self.radekSlovaAtributyAll)



    def vratJenPotrebnaData(self, dataDaneTridyArr):

        potrebnaData = []

        for i in range(0, len(dataDaneTridyArr)):
            polozka = dataDaneTridyArr[i]

            if(polozka != ""):
                if (polozka != "_"):
                    potrebnaData.append(polozka)

        return(potrebnaData)


    # vrati index radku s danym slovem
    def rozdelRadkyNaSlova(self, poleRadku):

        radekSlovaAtributyAll = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekSpl = radek.split(' ')
            radekSlova = self.vratRadekJenSlova(radekSpl)

            radekSlovaAtributy = self.priradAtributyKeVsemSlovumRadku(radekSlova)
            radekSlovaAtributyAll.append(str(radekSlovaAtributy))

        return(radekSlovaAtributyAll)


    def priradAtributyKeVsemSlovumRadku(self, radekSlova):

        radekSlovaAtributy = []
        pref = 0

        for i in range(0, len(radekSlova)):
            slovo = radekSlova[i]
            slovo = slovo.replace('\n', '')
            indexAtributu = 0

            #detekuje, zda se nejedna o zakladni typ atributu, napr. "String"
            nazevAtributu = self.vratAtributZakladni(slovo)
            slovoPredZavorkou = slovo

            #pokud nenajde, pak pokracuje dale
            if(nazevAtributu == ""):

                slovoPredZavorkou = self.odeberZeSlovaObsahZavorky(slovo)
                indexAtributu = self.vratKDanemuSlovuIndexAtributu(slovoPredZavorkou, pref)
                pref = indexAtributu

                # pokud vrati 0, pak bezi znovu na stejnem slovu
                if(indexAtributu == 0):
                    indexAtributu = self.vratKDanemuSlovuIndexAtributu(slovoPredZavorkou, pref)


            slovoAAtribut = self.vratDvojiciSlovoANazevAtributu(slovoPredZavorkou, indexAtributu, nazevAtributu)
            radekSlovaAtributy.append(slovoAAtribut)

        return(radekSlovaAtributy)


    def vratAtributZakladni(self, slovo):

        nazevAtributu =  ""

        if(slovo == "String"):
            nazevAtributu = "dataType"

        if(slovo == "String[]"):
            nazevAtributu = "dataType"

        if(slovo == "String[][]"):
            nazevAtributu = "dataType"

        if (slovo == "int"):
            nazevAtributu = "dataType"

        if (slovo == "int[]"):
            nazevAtributu = "dataType"

        if (slovo == "int[][]"):
            nazevAtributu = "dataType"

        if (slovo == "double"):
            nazevAtributu = "dataType"

        if (slovo == "double[]"):
            nazevAtributu = "dataType"

        if (slovo == "double[][]"):
            nazevAtributu = "dataType"

        if (slovo == "true"):
            nazevAtributu = "trueFalse"

        if (slovo == "false"):
            nazevAtributu = "trueFalse"

        if (slovo == "="):
            nazevAtributu = "rovnitko"

        if (slovo == "public"):
            nazevAtributu = "publicPrivate"

        if (slovo == "private"):
            nazevAtributu = "publicPrivate"

        if (slovo == "new"):
            nazevAtributu = "operator"

        if (slovo == "for"):
            nazevAtributu = "operator"

        if (slovo == "if"):
            nazevAtributu = "operator"

        if (slovo == "else"):
            nazevAtributu = "operator"

        if (slovo == "while"):
            nazevAtributu = "operator"

        if (slovo == "package"):
            nazevAtributu = "packageImport"

        if (slovo == "import"):
            nazevAtributu = "packageImport"


        return(nazevAtributu)


    def vratDvojiciSlovoANazevAtributu(self, slovo, indexAtributu, nazevAtributu):

        slovoAAtribut = []

        if(nazevAtributu == ""):
            if (indexAtributu > 0):
                nazevAtributu = self.priradNazevAtributu(indexAtributu)
            else:
                nazevAtributu = ""

        slovoAAtribut.append(slovo)
        slovoAAtribut.append(nazevAtributu)

        return(slovoAAtribut)


    def priradNazevAtributu(self, indexAtributu):

        if(indexAtributu == 1):
            return ("nazevInstance")

        if (indexAtributu == 2):
            return ("nazevMetody")

        if (indexAtributu == 3):
            return ("nazevTridy")

        if (indexAtributu == 4):
            return ("volanaInstance")

        if (indexAtributu == 5):
            return ("volanaMetoda")

        if (indexAtributu == 6):
            return ("volanaTrida")



    def odeberZeSlovaObsahZavorky(self, radek):

        try:
            indexZavory = radek.index('(')
            radekPredZavorkou = radek[0:indexZavory:1]
        except:
            radekPredZavorkou = radek

        return(radekPredZavorkou)


    # aby algoritmus bezel efektivneji preferuje se preferovana volba "pref", pokud je 0, bezi normalne
    def vratKDanemuSlovuIndexAtributu(self, slovo, pref):

        if (pref == 1 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.nazevInstanceAr, slovo)
            if(atributNalezen == True):
                return(1)

        if (pref == 2 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.nazevMetodyArr, slovo)
            if(atributNalezen == True):
                return(2)

        if (pref == 3 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.nazevTridyArr, slovo)
            if(atributNalezen == True):
                return(3)

        if (pref == 4 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.volanaInstanceArr, slovo)
            if(atributNalezen == True):
                return(4)

        if (pref == 5 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.volanaMetodaArr, slovo)
            if(atributNalezen == True):
                return(5)

        if (pref == 6 or pref == 0):
            atributNalezen = self.detekujZdaJeSlovoVPoli(self.volanaTridaArr, slovo)
            if(atributNalezen == True):
                return(6)

        return(0)


    def detekujZdaJeSlovoVPoli(self, pole, slovo):

        radekObsahujeNew = False
        try:
            indexSlovaNew = pole.index(slovo)
            if (indexSlovaNew > -1):
                radekObsahujeNew = True
        except:
            pass

        return (radekObsahujeNew)


    def vratRadekJenSlova(self, radekSpl):

        radekSlova = []

        for i in range(0, len(radekSpl)):
            slovo = radekSpl[i]

            if(slovo != ""):
                radekSlova.append(slovo)

        return(radekSlova)


    # vrati jen potrebne rady "vyjmiKodOdRadku-vyjmiKodDoRadku"
    def vratJenPotrebnyKodPoleRadku(self, poleRadkuDaneTridy, vyjmiKodOdRadku, vyjmiKodDoRadku):

        poleRadkuNOdDo = self.ostatniMetody.nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, 0,
                                                                     poleRadkuDaneTridy)

        return (poleRadkuNOdDo)



# aby bylo pole citelnejsi, prevadi na json
class poleNaJson():

    def __init__(self, pole):

        self.vsechnaSlovaAId = []
        self.poleRadkuJson = self.prevedVsechnyRadky(pole)

        vyhledavaniSlov = seradTextProVyhledavani(self.vsechnaSlovaAId)
        self.slovaAId = vyhledavaniSlov.getJsonRadekArr()



    def getPoleRadkuJson(self):
        return(self.poleRadkuJson)


    def getSlovaAId(self):
        return(self.slovaAId)


    def prevedVsechnyRadky(self, pole):

        poleRadkuJson = []

        for i in range(0, len(pole)):
            radek = pole[i]

            radekMod = radek.replace('[[', '')
            radekMod = radekMod.replace(']]', '')

            radekSpl = radekMod.split('], [')

            jsonStejneId = self.prevedSlovaJednohoRadku(radekSpl, i)
            poleRadkuJson = poleRadkuJson + jsonStejneId

        return(poleRadkuJson)


    def prevedSlovaJednohoRadku(self, radek, id):

        jsonStejneId = []

        for i in range(0, len(radek)):
            dvojiceradek = radek[i]
            dvojice = dvojiceradek.split("\',\'")

            jsonWordAtr = self.prevedDvojiciNaKlicHodnota(dvojice, id)
            jsonStejneId.append(jsonWordAtr + ',')

        return(jsonStejneId)


    def prevedDvojiciNaKlicHodnota(self, dvojiceRadek, id):

        dvojice = str(dvojiceRadek).split(',')

        slovo = self.odeberUvozovky(dvojice[0])
        atribut = self.odeberUvozovky(dvojice[1])

        jsonWordAtr = '{ "id": "' + str(id) + '" , "word": "' + slovo + '" , "atribute": "' + atribut + '" }'

        #prida vsechna slova a id do pole
        self.zapisVsechnaSlovaAId(slovo, id)

        return(jsonWordAtr)



    def zapisVsechnaSlovaAId(self, slovo, id):

        if(slovo != ""):

            slovoAId = []

            slovoAId.append(slovo)
            slovoAId.append(id)

            self.vsechnaSlovaAId.append(slovoAId)


    def odeberUvozovky(self, slovo):

        slovoNew = slovo.replace("\'", '')
        slovoNew = slovoNew.replace("\"", '')
        slovoNew = slovoNew.replace("[", '')
        slovoNew = slovoNew.replace("]", '')

        return(slovoNew)


class seradTextProVyhledavani():

    def __init__(self, vsechnaSlovaAId):

        poleSlov = self.vratPole1D(vsechnaSlovaAId, 0)
        poleID = self.vratPole1D(vsechnaSlovaAId, 1)
        seznamIndexuSlovUniq = self.vratPoleIndexuVsechVyskytu(poleSlov)

        slovaAId = self.prevedIndexySlovNaId(seznamIndexuSlovUniq, poleID)
        self.jsonRadekArr = self.prevedSlovaAIdNaJson(slovaAId)

        print()


    def getJsonRadekArr(self):
        return(self.jsonRadekArr)


    def prevedSlovaAIdNaJson(self, slovaAId):

        jsonRadekArr = []

        for i in range(0, len(slovaAId)):
            radek = slovaAId[i]
            jsonRadek = self.vratRadekJson(radek)

            jsonRadekArr.append(jsonRadek)

        return(jsonRadekArr)

    def vratRadekJson(self, radek):

        jsonSlovoStr = self.vratJsonSlovoStr(radek)
        jsonIdStr = self.vratJsonIdStr(radek)

        jsonRadek = jsonSlovoStr + jsonIdStr

        return(jsonRadek)


    def vratJsonSlovoStr(self, radek):

        slovo = radek[0]
        jsonSlovoStr = '{ "word": "' + slovo + '" ,'

        return(jsonSlovoStr)


    def vratJsonIdStr(self, radek):

        jsonIdStr = '"id": ["'

        for i in range(1, len(radek)):
            id = radek[i]
            jsonIdStr = jsonIdStr + str(id) + '"'

            if(i < len(radek)-1):
                jsonIdStr = jsonIdStr + ', "'

            else:
                jsonIdStr = jsonIdStr + '] },'

        return(jsonIdStr)


    def prevedIndexySlovNaId(self, seznamIndexuSlovUniq, poleID):

        slovaAId = []

        for i in range(0, len(seznamIndexuSlovUniq)):
            radek = seznamIndexuSlovUniq[i]
            slovo = radek[0]
            seznamId = self.vratIDDleIndexuRadku(radek, slovo, poleID)

            slovaAId.append(seznamId)

        return(slovaAId)


    def vratIDDleIndexuRadku(self, radek, slovo, poleID):

        slovoAId = []
        slovoAId.append(slovo)

        for i in range(1, len(radek)):
            indexRadku = radek[i]
            id = poleID[indexRadku]
            slovoAId.append(id)

        return(slovoAId)


    def vratPoleIndexuVsechVyskytu(self, poleSlov):

        poleSlovUniq = self.unique(poleSlov)
        seznamIndexuSlovUniq = []

        for i in range(0, len(poleSlovUniq)):
            slovo = poleSlovUniq[i]
            seznamIndexu = self.vratSeznamIndexuRadkuProDaneSlovo(poleSlov, slovo)
            seznamIndexuSlovUniq.append(seznamIndexu)

        return(seznamIndexuSlovUniq)


    def vratSeznamIndexuRadkuProDaneSlovo(self, pole, slovoExp):

        seznamIndexu = []
        seznamIndexu.append(slovoExp)

        for i in range(0, len(pole)):
            slovo = pole[i]
            if(slovo == slovoExp):
                seznamIndexu.append(i)

        return(seznamIndexu)


    def vratPole1D(self, pole2D, index):

        poleSlov = []

        for i in range(0, len(pole2D)):
            slovo = pole2D[i][index]
            poleSlov.append(slovo)

        return(poleSlov)


    def unique(self, list1):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if op.countOf(unique_list, x) == 0:
                unique_list.append(x)

        return(unique_list)

