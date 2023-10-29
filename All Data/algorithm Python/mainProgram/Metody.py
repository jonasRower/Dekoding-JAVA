
import numpy as np
import copy

class MetodyJednohoRadku():
    #tyto metody jsou postupne volany z NactiZdroj.py
    #Kazda metoda vraci nazpet navratovou hodnotu
    #a data z techto metod se zapisuji do DataProgramu uvnitr kodu NactiZdroj.py

    #konstruktor pro predani jineho objektu
    def __init__(self, obj):
        self.__obj = obj

    def __InjectedObj(self):
        return self.__obj


    # volano z HlavniVykonavajiciKod 1. v poradi
    # detekuje pritomnost komentare, pokud je na radce komentar, vynecha jej
    def rozhodniZdaDanyRadekJeKod(self, radekKodu):
        # print(radekKodu)
        radekKoduBezMezery = radekKodu.replace(" ", "")
        JeToKod = True

        try:
            indexKomentare = radekKoduBezMezery.index('//')
            #kod to neni, jen v pripade, ze komentar neni na nulté pozici radku
            if (indexKomentare == 0):
                JeToKod = False
            else:
                JeToKod = True
        except:
            pass

        return (JeToKod)


    # volano z HlavniVykonavajiciKod 2. v poradi
    # Vraci True nebo False, podle toho, zda na konci radku je strednik ci nikoliv
    def detekujPritomnostStrednikuNaKonciRadku(self, radekKodu):
        #Kdyz na konci radku neni strednik, pak se jedna o radek s metodou, nebo if, for, while ...
        #Kdyz na konci radku je strednik pak se jednosznacne jedna o vykonavajici kod
        #Tato funkce se vola za predpokladu
        #           JeToKod = True

        radekKoduBezMezery = radekKodu.replace(" ", "")
        posledniZnakRadku = radekKoduBezMezery[-2:-1]
        if (posledniZnakRadku == ";"):
            koncovyStrednik = True
        else:
            koncovyStrednik = False

        return (koncovyStrednik)


    # volano z HlavniVykonavajiciKod 3. v poradi
    # Zjistuje, zda radek obsahuje klicove slovo, jako napr. if, for, ...
    def zjistiZdaRadekKoduObsahujeKlicoveSlovo(self, radekKodu):

        # metoda je umistena v tride OstatniMetody,
        # to proto ze je soucasne i volana od jinud - z tohoto modulu (z jinych metod)
        klicoveSlovoNalezeno = self.__InjectedObj().detekujPritomnostKlicovehoSlova(radekKodu)

        return (klicoveSlovoNalezeno)


    # volano z HlavniVykonavajiciKod 4. v poradi
    # vraci nazev metody z typoveho kodu:
    # private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{
    def vratNazevMetody(self, radekKodu):

        nazevMetody = ""

        # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
        jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

        if (jednaSeOMetodu == True):
            # metodaPredZavorkou uvazuje jako cast nazvu pred "("
            indexZavorkyOtevrene = radekKodu.index('(')
            metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]

            # nasledne odstrani dalsi klicova slova, ktere do nazvu nepatri + mezery
            import vstupniData
            klicovaSlova = vstupniData.definiceKlicovychSlov()

            nazevMetody = metodaPredZavorkou
            for odstranitSlovo in klicovaSlova:
                nazevMetody = nazevMetody.replace(odstranitSlovo, "")

            # odstrani jeste nejaka dalsi slova
            nazevMetody = nazevMetody.replace("private", "")
            nazevMetody = nazevMetody.replace("public", "")
            nazevMetody = nazevMetody.replace("int", "")
            nazevMetody = nazevMetody.replace("double", "")
            nazevMetody = nazevMetody.replace("String", "")
            nazevMetody = nazevMetody.replace("void", "")

            #odstrani jeste hranate zavorky
            nazevMetody = nazevMetody.replace("[", "")
            nazevMetody = nazevMetody.replace("]", "")
            nazevMetody = nazevMetody.replace(" ", "")

        return (nazevMetody)


    # volano z HlavniVykonavajiciKod 5. v poradi
    # z radku kodu vrati { nebo } , ostatni znaky vymaze
    def vratSlozenouZavorku(self, radekKodu):

        indexZavorkyOtevrene = -1
        indexZavorkyZavrene = -1
        radekSeZavorkou = ""

        try:
            indexZavorkyOtevrene = radekKodu.index('{')
        except:
            pass

        try:
            indexZavorkyZavrene = radekKodu.index('}')
        except:
            pass

        if (indexZavorkyOtevrene > -1):
            radekSeZavorkou = "{"

        if (indexZavorkyZavrene > -1):
            radekSeZavorkou = "}"

        return (radekSeZavorkou)


class OstatniMetody():
    #tyto metody jsou volany odjinud nez z NactiZdroj.py
    #Vetsinou z modulu Metody.py
    #metody vraci navratove hodnoty a data sami nezapisuji

    # pouziva se konstruktor defaultni,
    # proto zde neni - teto tride (objektu) nepredavam zadny jiny objekt


    # __InjectedObj neni zatim vyuzit, je tu pripraven do budoucna
    def __InjectedObj(self):
        return self.__obj

    # metoda volana z teto tridy - z metody vratNazevMetody
    def indikujZdaSeJednaOMetodu(self, radekKodu):
        # to pozna na zaklade pritomnosti zavorek "(" a ")"
        # pokud tam zavorky nejsou, pak vraci false, jinak true

        jednaSeOMetodu = False
        jednaSeOArrayList = self.jednaSeOArrayList(radekKodu)

        if(jednaSeOArrayList == False):

            # zjisti index zavorky otevrene
            indexZavorkyOtevrene = 0
            try:
                indexZavorkyOtevrene = radekKodu.index('(')
            except:
                pass

            # zjisti index zavorky zavrene
            indexZavorkyZavrene = 0
            try:
                indexZavorkyZavrene = radekKodu.index(')')
            except:
                pass

            # pokud oba indexy (otevrene a zavrene zavorky) > 0, pak se jedna o metodu
            nazevMetody = ""
            if (indexZavorkyOtevrene > 0):
                if (indexZavorkyZavrene > 0):
                    jednaSeOMetodu = True

        return (jednaSeOMetodu)


    #detekuje, ze se jedna o ArrayList
    def jednaSeOArrayList(self, radekKodu):

        try:
            ind = radekKodu.index('>(')
            if(ind > 0):
                jednaSeOArrayList = True
            else:
                jednaSeOArrayList = False

        except:
            jednaSeOArrayList = False


        return(jednaSeOArrayList)


    # detekuje pritomnost klicoveho slova new na radku
    def obahujeRadekKoduKlicoveSlovoNew(self, radekKodu):

        indexSlovaNew = -1
        radekObsahujeNew = False
        try:
            indexSlovaNew = radekKodu.index('new ')
            if (indexSlovaNew > -1):
                radekObsahujeNew = True
        except:
            pass

        return (radekObsahujeNew)

    # detekuje pritomnost jineho klicoveho slova nez new
    def detekujPritomnostKlicovehoSlova(self, radekKodu):

        #Importuje vstupni data, kde je definice klicovych slov
        import vstupniData

        # Vraci True nebo False podle toho, zda radek obsahuje klicove slovo, ci nikoliv
        klicovaSlova = []
        klicovaSlova = vstupniData.definiceKlicovychSlov()

        # doplni do radku mezery, tak aby mohl pomoci mezer radek rozdelit
        # pokud by na radku mezera nebyla, nerozpoznal by klicove slovo
        radekKoduSMezerami = radekKodu.replace("(", " ")
        jednotlivaSlovaNaRadku = radekKoduSMezerami.split()

        klicoveSlovoNalezeno = False

        for klicoveSlovo in klicovaSlova:
            # pokud najde klicove slovo ve vnitrni smycce, ukonci i tu smycku vnejsi
            if (klicoveSlovoNalezeno == True):
                break
            for slovo in jednotlivaSlovaNaRadku:
                if (slovo == klicoveSlovo):
                    klicoveSlovoNalezeno = True
                    break

        return (klicoveSlovoNalezeno)


    #############################################################
    # Metody slouzi k vytvareni noveho JAVA Kodu

    # Metoda pridava mezery pred kazdy radek subKodu
    def pridejMezeryPredRadek(self, subKod, pocetMezer):


        SubKodSMezerou = []

        mezeraPredSubKodem = ""

        if(pocetMezer > -1):
            for i in range(0, pocetMezer):
                mezeraPredSubKodem = mezeraPredSubKodem + " "

            mezeraPredSubKodem = mezeraPredSubKodem + "-->" + "  "

        for radekSubKodu in subKod:
            radekSubKoduSMezerou = mezeraPredSubKodem + radekSubKodu
            SubKodSMezerou.append(radekSubKoduSMezerou)

        return (SubKodSMezerou)

    # Metoda nacita subKod mezi danymi radky
    def nactiSubKod(self, prvniRadek, posledniRadek, pocetMezer, dataPole):

        poleSubKod = []
        subKod = []


        # oprava, nevim, zda funguje spravne
        if(posledniRadek > len(dataPole)-1):
            posledniRadek = len(dataPole)-1

        for i in range(prvniRadek, posledniRadek):

            radekSubKodu = dataPole[i]
            poleSubKod.append(radekSubKodu)

        if (pocetMezer == 0):
            subKod = poleSubKod
        else:
            #subKod = OstatniMetody.pridejMezeryPredRadek(self, poleSubKod, pocetMezer)
            subKod = OstatniMetody.pridejMezeryPredRadek(self, poleSubKod, -1)

        # pro testovani
        #if(i == 85):
        #    a = 4
        #    if (radekSubKodu == ""):
        #        a = 4

        return (subKod)

    # Metoda spocita pocet mezer na zacatku radku, tak aby bylo mozno kod spravne odsadit
    def spocitejPocetMezerPredKodemNaRadku(self, radekKodu):
        pocetMezer = 0

        znakyRadku = list(radekKodu)
        for znak in znakyRadku:
            if (znak.isspace() == True):
                pocetMezer = pocetMezer + 1

        return (pocetMezer)

    # Metoda zanori konkretni subKod (kodNovy) do hlavniho Kodu
    def vlozSubKodDoKodu(self, kodOrig, kodNovy, vkladejOdRadku):

        kodNew = []

        delkaKoduOrig = len(kodOrig)
        delkaKoduNovy = len(kodNovy)
        celkovaDelka = delkaKoduOrig + delkaKoduNovy

        iOrig = -1
        iNovy = -1

        for i in range(0, celkovaDelka):
            if (i < vkladejOdRadku):
                iOrig = iOrig + 1
                radek = kodOrig[iOrig]
            if (i >= vkladejOdRadku):
                if (i < (vkladejOdRadku + delkaKoduNovy)):
                    iNovy = iNovy + 1
                    radek = kodNovy[iNovy]
                else:
                    iOrig = iOrig + 1
                    radek = kodOrig[iOrig]

            kodNew.append(radek)

        return (kodNew)


    # vrati cislo radku kde je "{"
    # zacne hledat od zadaneho radku smerem dolu
    def vratNejblizsiRadekSOtevrenouZavorkou(self, fromIndex, dataSlozenaZavorka):

        #jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

        i = fromIndex
        cisloRadkuSOtevrenouZavorkou = -1
        for x in dataSlozenaZavorka:

            radek = dataSlozenaZavorka[i]
            if (radek == "{"):
                cisloRadkuSOtevrenouZavorkou = i
                break

            i = i + 1
            if (i >= len(dataSlozenaZavorka)):
                break

        return (cisloRadkuSOtevrenouZavorkou)

    # vraci cislo radku, kde konci metoda
    # posledni radek pozna podle paroveho znaku }
    def vratCisloRadkuSKoncemBloku(self, fromIndex, dataSlozenaZavorka):

        i = fromIndex
        pocetOtevrenychZavorek = 0
        pocetZavrenychZavorek = 0
        posledniRadek = -1

        for x in dataSlozenaZavorka:
            radek = dataSlozenaZavorka[i]

            if (radek == "{"):
                pocetOtevrenychZavorek = pocetOtevrenychZavorek + 1

            if (radek == "}"):
                pocetZavrenychZavorek = pocetZavrenychZavorek + 1

            ZavorkyRozdil = pocetOtevrenychZavorek - pocetZavrenychZavorek

            if (ZavorkyRozdil == 0):
                posledniRadek = i + 1
                break

            i = i + 1

        return (posledniRadek)

    # Metoda volana z dopisujIndexyOtevrenychAZavrenychZavorek
    def najdiRadekVolaneMetody(self, nazevMetody, dataVolanaMetoda):

        radekVolaneMetody = -1
        r = -1

        for nazevMetodyData in dataVolanaMetoda:
            r = r + 1
            if (nazevMetodyData == nazevMetody):
                radekVolaneMetody = r

        return (radekVolaneMetody)

    # Metoda volana z NovyJAVAKod
    # Vraci cislo radku Metody (podle nazevMetody, nikoliv Metody Volane)
    def vratCisloRadkuNazvuMetody(self, data, nazevPozadovaneMetody):
        i = -1
        cisloRadkuMetody = -1
        for x in data.nazevMetody:
            i = i + 1
            nazevMetody = data.nazevMetody[i]
            if (nazevMetody == nazevPozadovaneMetody):
                cisloRadkuMetody = i
                break

        return(cisloRadkuMetody)


# Tyto metody predavaji data do Modulu DataProgramu samostatne
# Zapis dat neprobiha v modulu HlavniVykonavajiciKod, ale zde - na konci kazde metody
class MetodyPredavajiciDataSamostatne():

    # konstruktor pro predani jineho objektu
    # predavam i data - DataProgramu.py -> pro ukladani dat
    def __init__(self, obj, data):
        self.__obj = obj
        self.__data = data

    # slouzi k volani metody z jineho objektu
    def __InjectedObj(self):
        return self.__obj


    # vraci data z typoveho radku:
    # Select selNejmensi = new Select(dotazNejmensi);
    def vratNazevInstanceATridy(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo):

        nazevInstance = ""
        nazevTridy = ""

        # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
        jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

        if (jednaSeOMetodu == True):

            # pokud radek neobsahuje strednik, pak se nejedna o radek typu:
            # Select selStredni = new Select(dotazStredni);
            # a tudis neni co resit a na konci funkce se zapisi data typu "" do pole
            if (koncovyStrednik == True):

                # Take radek nesmi obsahovat klicove slovo for, if, catch ...
                if (radekObsahujeKlicoveSlovo == False):

                    # zjisti index klicoveho slova 'new'
                    radekObsahujeNew = self.__InjectedObj().obahujeRadekKoduKlicoveSlovoNew(radekKodu)
                    if (radekObsahujeNew == True):

                        # pokud klicove slovo "new" je obsazeno, pak proveruje, zda radekKodu obsahuje "="
                        if (radekObsahujeNew == True):
                            indexRovnitka = 0
                            try:
                                indexRovnitka = radekKodu.index('=')
                            except:
                                pass

                            # pokud i obsahuje "=" pak pokracuje kod dal - oddeli nazev Instance a nazev Tridy
                            slovaNaRadku = radekKodu.split()
                            nazevTridy = slovaNaRadku[0]
                            nazevInstance = slovaNaRadku[1]

        # data do pole se predavaji zde
        self.__data.add_nazevInstance(nazevInstance)
        self.__data.add_nazevTridy(nazevTridy)
    #print("")



    # vraci data z typoveho radku:
    # DataSelectuNejmensi = selNejmensi.getDataSelectu();
    def vratNazevVolaneInstanceAMetody(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo, r):

        volanaInstance = ""
        volanaMetoda = ""

        # Test: radekKodu = "indexOfFROM = originalniSelect.indexOf(FROM);"

        # kod ma vyznam vykonavat pouze tehdy, pokud radek obsahuje strednik
        if (koncovyStrednik == True):

            # a pokud radek neobsahuje klicove slovo jako napr. for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
                jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

                if (jednaSeOMetodu == True):
                    indexZavorkyOtevrene = radekKodu.index('(')
                    kodRadkuPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
                    slovaNaRadku = kodRadkuPredZavorkou.split()
                    InstanceAMetoda = slovaNaRadku[-1]
                    InstanceAMetodaArr = InstanceAMetoda.split(".")

                    if (len(InstanceAMetodaArr) == 2):
                        volanaInstance = InstanceAMetodaArr[0]
                        volanaMetoda = InstanceAMetodaArr[1]

                        jeInstanceKlicoveSlovo = self.__InjectedObj().detekujPritomnostKlicovehoSlova(volanaInstance)
                        jeMetodaKlicoveSlovo = self.__InjectedObj().detekujPritomnostKlicovehoSlova(volanaMetoda)

                        # proveri, zda se nahodnou nejedna o klicove slovo, pokud ano, pak jej prepise na""
                        if (jeInstanceKlicoveSlovo == True):
                            volanaInstance = ""
                            volanaMetoda = ""

                        if (jeMetodaKlicoveSlovo == True):
                            volanaInstance = ""
                            volanaMetoda = ""

        self.__data.add_volanaInstance(volanaInstance)
        self.__data.add_volanaMetoda(volanaMetoda)


    def zapisMetoduJakoKonstruktor(self, radekKodu, r):
        try:
            indexZavorkyOtevrene = radekKodu.index('(')
            metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
            try:
                indexNew = metodaPredZavorkou.index('new')
                nazevKonstruktoru = metodaPredZavorkou[(indexNew + 3):(len(metodaPredZavorkou))]
                nazevKonstruktoru = nazevKonstruktoru.replace(" ", "")

                self.__data.volanaMetoda[r] = nazevKonstruktoru
            except:
                pass
        except:
            pass



    def vratNazevVolaneMetody(self, radekKodu, koncovyStrednik, klicoveSlovo, r):
        metodaPredZavorkou = ""

        if (koncovyStrednik == True):
            if (klicoveSlovo == False):

                # potvrdi zda radek neobsahuje klicove slovo "new"
                radekObsaheujeNew = self.__InjectedObj().obahujeRadekKoduKlicoveSlovoNew(radekKodu)

                if (radekObsaheujeNew == True):
                    # pak zapise konstruktor
                    self.zapisMetoduJakoKonstruktor(radekKodu, r)
                else:
                    # if (radekObsaheujeNew == False):
                    # aby to byla metoda musi tam byt zavorky, proto telo metody je v celem tele try:
                    try:
                        indexZavorkyOtevrene = radekKodu.index('(')
                        metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]

                        # ale nemusi tam byt = (tj. muze byt volani jak zleve tak i prave strany)
                        # protoze nemusi, pak zbytek tela je za pass
                        try:
                            # Tento kod se uplatni, pokud je volana metoda na prave strane vyrazu
                            indexRovnitka = metodaPredZavorkou.index('=')
                            metodaPredZavorkou = metodaPredZavorkou[(indexRovnitka + 1):(len(metodaPredZavorkou))]

                            # pokud kod dojde sem, pak pokracuje za pass
                        except:
                            pass

                        metodaPredZavorkou = metodaPredZavorkou.replace(" ", "")

                        # pole je jiz vytvorene (v metode vratNazevVolaneInstanceAMetody)
                        # a proto pro zapisovani se nepouziva append a zapisuji se data zde
                        # zapise se tedy volanaMetoda, pokud neobsahuje ""
                        if (metodaPredZavorkou != ""):

                            # zapisuje pouze ty data, ktere nebyly zapsany
                            if (self.__data.volanaMetoda[r] == ""):
                                # jelikoz v metode vratNazevVolaneInstanceAMetody
                                # zapisuje "" pokud metoda se jmenuje napr. indexOf,
                                # pak se prepisuje kod zde - je tedy treba odfiltrovat i napr: "originalniSelect.indexOf"
                                # to se pozna prave diky tecce
                                try:
                                    indexTecky = metodaPredZavorkou.index('.')
                                    # kdyz najde tecku, pak neprovede nic (tecka v metodaPredZavorkou, nikoliv v radekKodu)
                                except:
                                    # kdyz tecku nenajde, pak zapise data
                                    self.__data.volanaMetoda[r] = metodaPredZavorkou

                    except:
                        pass

        # Data se vraceji pro formalnost, pouze pro testovani
        return (metodaPredZavorkou)


    def dopisujIndexyOtevrenychAZavrenychZavorek(self):
        # dopisuje indexy otevrenych a zavrenych zavorek ( "{", "}" ) na radek v Data, kde je volana metoda
        # proto je potreba vyhledavat volanou metodu

        i = -1

        for nazevMetodyHodnota in self.__data.nazevMetody:
            i = i + 1
            radekObsahujeKlicoveSlovo = self.__data.klicoveSlovo[i]

            indexNejblizsiOtevreneZavorky = -1
            indexNejblizsiZavreneZavorky = -1

            # zapisuje zacatek a konec bloku, v pripadech, kdy se nejedna o klicove slovo, tedy for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                if (nazevMetodyHodnota != ""):
                    vyhledejOdRadku = i - 1
                    indexNejblizsiOtevreneZavorky = OstatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(self, vyhledejOdRadku, self.__data.slozenaZavorka)
                    indexNejblizsiZavreneZavorky = OstatniMetody.vratCisloRadkuSKoncemBloku(self, indexNejblizsiOtevreneZavorky, self.__data.slozenaZavorka)

                    dataVolanaMetoda = self.__data.volanaMetoda
                    radekVolaneMetody = OstatniMetody.najdiRadekVolaneMetody(self, nazevMetodyHodnota, self.__data.volanaMetoda)
                    if (radekVolaneMetody > -1):
                        self.__data.zacatekBloku[radekVolaneMetody] = indexNejblizsiOtevreneZavorky
                        self.__data.konecBloku[radekVolaneMetody] = indexNejblizsiZavreneZavorky

       # return(self)

# Metody vytvarejici novy JAVA kod
class MetodyProVytvareniJAVAKodu():

    # konstruktor pro predani jineho objektu
    # predavam i data - DataProgramu.py -> pro ukladani dat
    def __init__(self, obj,  data):
        self.__obj = obj
        self.__data = data

    def __InjectedObj(self):
        return self.__obj

    # vraci cislo radku, kde se nachazi dalsi volana metoda (za zadanym indexem - hledejOdIndexu)
    def vratCisloRadkuDalsiVolaneMetody(self, volanaMetodaN, hledejOdIndexu):
        delkaDatVolanaMetodaN = len(volanaMetodaN)
        cisloRadkuNasledujiciMetody = -1

        # Nalezne prvni volanou metodu v poliRadku (resp. poli volanaMetodaN) za danym indexem
        for i in range(hledejOdIndexu, delkaDatVolanaMetodaN):
            nazVolMetody = volanaMetodaN[i]

            if (nazVolMetody != ""):
                cisloRadkuNasledujiciMetody = i
                break


            # vrati cislo radku odkazujici na radek, kde se nalezne zacatek a konec Bloku
            # if (nazVolMetody != ""):
            #    cisloRadkuData = vratCisloRadkuMetody(nazVolMetody)
            #    break

        return (cisloRadkuNasledujiciMetody)


    # vraci cislo radku v DataProgramu.Data, z ktereho se daji vycist radky, kde se nachazi "{" a "}"
    def vratCisloRadkuProVyberZacatkuAKonceBloku(self, volanaMetodaN, volanaMetodaO,
                                                 cisloRadkuvolanaMetodaN, volanaInstanceN):

        cisloRadkuZacKonBloku = -1
        nazevVolaneMetody = volanaMetodaN[cisloRadkuvolanaMetodaN]
        nazevVolaneInstance = volanaInstanceN[cisloRadkuvolanaMetodaN]

        i = -1
        for dataNazevMetody in volanaMetodaO:
            i = i + 1
            if (dataNazevMetody == nazevVolaneMetody):

                # zatim kod funguje jen pro volani pouze v ramci jedne tridy
                # kdyz tam bude instance - je potreba rozsirit kod o nacitani dat z vice souboru
                nazevVolaneInstance = volanaInstanceN[i]

                #if (nazevVolaneInstance == ""):
                cisloRadkuZacKonBloku = i
                break

        return (cisloRadkuZacKonBloku)


    # prohledava data.nazevMetody a hleda souhlasny nazev Metody, shodny s volanou metodou
    def vratCisloRadkuProVyberZacatkuAKonceBloku(self, volanaMetodaN, volanaMetodaO, cisloRadkuvolanaMetodaN,
                                                 volanaInstanceN):

        cisloRadkuZacKonBloku = -1
        nazevVolaneMetody = volanaMetodaN[cisloRadkuvolanaMetodaN]
        #nazevVolaneInstance = volanaInstanceN[cisloRadkuvolanaMetodaN]

        i = -1
        for dataNazevMetody in volanaMetodaO:
            i = i + 1
            if (dataNazevMetody == nazevVolaneMetody):

                # zatim kod funguje jen pro volani pouze v ramci jedne tridy
                # kdyz tam bude instance - je potreba rozsirit kod o nacitani dat z vice souboru
                nazevVolaneInstance = volanaInstanceN[i]

                if (nazevVolaneInstance == ""):
                    cisloRadkuZacKonBloku = i
                    break

        return (cisloRadkuZacKonBloku)



    def vlozSubDataProPoleId(self, poleIdOrig, vyjmiKodOdRadku, vyjmiKodDoRadku, vkladejOdRadku, dataZdroj):

        if (vyjmiKodOdRadku > -1):

            dataNovy = OstatniMetody.nactiSubKod(self, vyjmiKodOdRadku, vyjmiKodDoRadku, -1, dataZdroj)

            vlozOdRadku = vkladejOdRadku + 2
            idPosun = vlozOdRadku - 1

            # vytvori poleId pro dataNovy
            poleIdClass = createIdArr(dataNovy, idPosun)
            poleIdNew = poleIdClass.getPoleId()

            poleIdAll = OstatniMetody.vlozSubKodDoKodu(self, poleIdOrig, poleIdNew, vlozOdRadku)

        else:
            poleIdAll = poleIdOrig

        return(poleIdAll)


    # vklada nova data do puvodniho kodu (do noveho kodu, ale nove vytvoreneho v predchozim cyklu)
    def vlozSubDataProJednotlivaPole(self, DataOrig, pocitatMezery, vyjmiKodOdRadku,
                                     vyjmiKodDoRadku, vkladejOdRadku, dataZdroj, pozadovanaHodnota):

        dataNovy = []
        dataNew = []

        #jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu("")

        # pokud se jedna o pole radku kodu, pak pocita mezery, u jinych typu dat to nema vyznam
        if (pocitatMezery == True):
            pocetMezerPredKodem = OstatniMetody.spocitejPocetMezerPredKodemNaRadku(self, DataOrig[vkladejOdRadku])
        else:
           pocetMezerPredKodem = 0

        if (vyjmiKodOdRadku > -1):
            dataNovy = OstatniMetody.nactiSubKod(self, vyjmiKodOdRadku, vyjmiKodDoRadku, pocetMezerPredKodem, dataZdroj)

            # prepise prazdne hodnoty hodnotami pozadovanymi
            dataNovy = self.prepisPolozkySubKodu(dataNovy, pozadovanaHodnota)

            #vkladam data o 2 radky nize, kvuli tomu, ze obcas jsou posunute zavorky
            dataNew = OstatniMetody.vlozSubKodDoKodu(self, DataOrig, dataNovy, vkladejOdRadku + 2)
        else:
            dataNew = DataOrig

        return (dataNew)


    def prepisPolozkySubKodu(self, dataPole, hodnota):
        # prepisuje hodnotou, pouze pokud hodnota != ""
        if(hodnota != ""):
            i = -1
            for x in dataPole:
                i = i + 1
                dataPole[i] = hodnota

        return(dataPole)


# nedat do samostatneho modulu - vytvorPoleId.py ??
# Metody vytvarejici poleId do jsTree
class createIdArr():

    def __init__(self, poleRadku, idPosun):

        poleZavorek = self.vratPoleZavorek(poleRadku)

        # muze se stat, ze je uzavrena zavorka na zacatku radku, pak vraci radky bez 1. znaku
        poleRadku2 = self.vratPoleRadkuBezZavorekNaZacatkuRadku(poleRadku)
        poleZavorek2 = self.vratPoleZavorek(poleRadku2)

        poleZavorek2 = self.checkPoleZavorek2(poleZavorek, poleZavorek2)

        dvojiceOtZavAll = self.vratPoleDvojicZavOtZav(poleZavorek, poleZavorek2, len(poleRadku))
        poleId = self.vytvorPoleId(dvojiceOtZavAll, len(poleRadku))
        self.poleIdPosunute = self.posunPoleId(poleId, idPosun)



    def getPoleId(self):
        return(self.poleIdPosunute)


    def checkPoleZavorek2(self, poleZavorek, poleZavorek2):

        for i in range(0, len(poleZavorek)):
            zavorka1 = poleZavorek[i]
            zavorka2 = poleZavorek2[i]

            if(zavorka1 != ""):
                if(zavorka1 == zavorka2):
                    poleZavorek2[i] = ""

        return(poleZavorek2)


    def posunPoleId(self, poleId, idPosun):

        poleIdNew = []

        for i in range(0, len(poleId)):
            id = poleId[i]
            idNew = id + idPosun

            poleIdNew.append(idNew)

        return(poleIdNew)


    def vytvorPoleId(self, dvojiceOtZavAll, pocetRadku):

        poleId = []

        # vytvori prazdne pole
        for i in range(0, pocetRadku):
            poleId.append(0)

        # postupne prepisuje id
        for i in range(0, len(dvojiceOtZavAll)):
            odInd = dvojiceOtZavAll[i][0]
            doInd = dvojiceOtZavAll[i][1]

            poleId = self.vratPoleIdDleOdDo(poleId, odInd, doInd)

        return(poleId)


    def vratPoleIdDleOdDo(self, poleId, odInd, doInd):

        for i in range(odInd, doInd):
            poleId[i] = odInd - 1

        return(poleId)


    def vratPoleRadkuBezZavorekNaZacatkuRadku(self, poleRadku):

        poleRadku2 = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radek = radek.strip()

            radekBezPrvnihoZnaku = radek[1:len(radek):1]
            poleRadku2.append(radekBezPrvnihoZnaku)

        return(poleRadku2)



    def vratPoleDvojicZavOtZav(self, poleZavorek, poleZavorek2, max):

        poleIndexuZavOt1 = self.vratPoleIndexu(poleZavorek, '{')
        poleIndexuZavZav1 = self.vratPoleIndexu(poleZavorek, '}')

        poleIndexuZavOt2 = self.vratPoleIndexu(poleZavorek2, '{')
        poleIndexuZavZav2 = self.vratPoleIndexu(poleZavorek2, '}')

        poleIndexuZavOt = self.slucPole(poleIndexuZavOt1, poleIndexuZavOt2)
        poleIndexuZavZav = self.slucPole(poleIndexuZavZav1, poleIndexuZavZav2)

        #muze se stat, ze nenajde vsechny zavorky, pak doplnuje indexy krajnimi hodnotami
        poleIndexuZavOt = self.doplnChybejiciZavorkyOtZav(poleIndexuZavOt, poleIndexuZavZav, True, max)
        poleIndexuZavZav = self.doplnChybejiciZavorkyOtZav(poleIndexuZavOt, poleIndexuZavZav, False, max)


        rozdilyAll = self.vratPoleRozdiluAll(poleIndexuZavOt, poleIndexuZavZav)
        sourRSAll = self.vyhledavejNejmensiRozdily(copy.deepcopy(rozdilyAll), len(poleZavorek))
        dvojiceOtZavAll = self.vratDvojiceIndexuZavorek(poleIndexuZavOt, poleIndexuZavZav, sourRSAll, max)


        return(dvojiceOtZavAll)


    def vratDvojiceIndexuZavorek(self, poleIndexuZavOt, poleIndexuZavZav, sourRSAll, maxPol):

        dvojiceOtZavAll = []

        for i in range(len(sourRSAll)-1, -1, -1):
            sourR = sourRSAll[i][0]
            sourS = sourRSAll[i][1]

            indexOt = int(poleIndexuZavOt[sourS])
            indexZav = int(poleIndexuZavZav[sourR])

            # omezi hodnoty, ktere pretekaji
            indexOt = self.omezHodnotu(indexOt, maxPol)
            indexZav = self.omezHodnotu(indexZav, maxPol)

            dvojiceOtZav = []
            dvojiceOtZav.append(indexOt)
            dvojiceOtZav.append(indexZav)

            dvojiceOtZavAll.append(dvojiceOtZav)

        return(dvojiceOtZavAll)


    def omezHodnotu(self, hodnota, hodnotaMax):

        if(hodnota > hodnotaMax):
            hodnotaNew = hodnotaMax
        else:
            hodnotaNew = hodnota

        return(hodnotaNew)


    # nekdy je chyba, ze se nenajdou vsechny dvojice zavorek
    def doplnChybejiciZavorkyOtZav(self, poleIndexuZavOt, poleIndexuZavZav, ot, maxVal):

        pocetOt = len(poleIndexuZavOt)
        pocetZav = len(poleIndexuZavZav)

        arrNew = []

        if(pocetOt != pocetZav):

            pocetMax = max(pocetOt, pocetZav)


            for i in range(0, pocetMax):

                if (ot == True):

                    pocetChyb = pocetMax - pocetOt
                    if(i < pocetChyb):
                        hodnota = -i
                    else:
                        hodnota = poleIndexuZavOt[i - pocetChyb]

                else:

                    pocetChyb = pocetMax - pocetZav
                    if (i > pocetChyb):
                        hodnota = maxVal + i - pocetChyb - 1
                    else:
                        if(i > len(poleIndexuZavZav)-1):
                            try:
                                hodnota = poleIndexuZavZav[len(poleIndexuZavZav)-1] + 1
                            except:
                                hodnota = 0
                        else:
                            hodnota = poleIndexuZavZav[i]

                arrNew.append(hodnota)

        return(arrNew)




    def slucPole(self, poleA, poleB):

        list1 = poleA + poleB
        x = np.array(list1)
        poleUniq = np.unique(x)

        return(poleUniq)


    def vyhledavejNejmensiRozdily(self, rozdilyAll, maxPol):

        minSourRSmin = []
        minSourRSmin.append(maxPol)

        sourRSAll = []

        for i in range(0, maxPol):
            minRozdil = minSourRSmin[0]
            minSourRSmin = self.vratSouradniceNejmensihoRozdilu(rozdilyAll, maxPol*maxPol)

            if(minSourRSmin == []):
                break

            sourR = minSourRSmin[1]
            sourS = minSourRSmin[2]

            sourRS = []
            sourRS.append(sourR)
            sourRS.append(sourS)

            sourRSAll.append(sourRS)

            rozdilyAll = self.zneplatniDanyRadekASloupec(rozdilyAll, sourR, sourS)
            print()

        return(sourRSAll)


    # na dany radek a sloupec zapise False, cimz anuluje polozky a nemuze je znovu hledat jako minimalni
    def zneplatniDanyRadekASloupec(self, rozdilyAll, sourR, sourS):

        for r in range(0, len(rozdilyAll)):
            rozdilyRadek = rozdilyAll[r]
            for s in range(0, len(rozdilyAll)):
                hodnota = rozdilyAll[r][s]
                if(r == sourR):
                    hodnota = False
                if(s == sourS):
                    hodnota = False

                rozdilyAll[r][s] = hodnota

        return(rozdilyAll)


    def vratSouradniceNejmensihoRozdilu(self, rozdilyAll, minRozdil):

        minSourRSmin = []

        for r in range(0, len(rozdilyAll)):
            rozdilyRadek = rozdilyAll[r]
            for s in range(0, len(rozdilyRadek)):
                polozka = rozdilyRadek[s]
                if(polozka != False):
                    if(polozka < minRozdil):

                        minRozdil = polozka
                        minSourR = r
                        minSourS = s

                        minSourRSmin = []

                        minSourRSmin.append(minRozdil)
                        minSourRSmin.append(minSourR)
                        minSourRSmin.append(minSourS)


        return(minSourRSmin)



    def vratNejmensiRozdilyAll(self, rozdilyAll, max):

        vybraneNejmensiIndexyArr = []

        for i in range(0, len(rozdilyAll)):
            radekRozdilu = rozdilyAll[i]
            indexNejmensihoRozdilu = self.vratIndexNejmensihoRozdilZRadku(radekRozdilu, max)

            vybraneNejmensiIndexyArr.append(indexNejmensihoRozdilu)

            # nastavi jiz vybrane polozky jako False, tak aby je jiz nevybiral znovu
            rozdilyAll = self.oznacJizVybraneRozdily(rozdilyAll, indexNejmensihoRozdilu)

        return(vybraneNejmensiIndexyArr)


    # na vsech ostatnich radcich nastavi jiz vybrane hodnoty jako False
    def oznacJizVybraneRozdily(self, rozdilyAll, vybranyIndex):

        for i in range(0, len(rozdilyAll)):
            rozdilyAll[i][vybranyIndex] = False

        return(rozdilyAll)


    def vratIndexNejmensihoRozdilZRadku(self, radekRozdilu, max):

        nejmensiRozdil = max
        index = 0

        for i in range(0, len(radekRozdilu)):
            rozdil = radekRozdilu[i]
            if(rozdil != False):
                if(rozdil < nejmensiRozdil):
                    nejmensiRozdil = rozdil
                    index = i

        return(index)



    def vratPoleRozdiluAll(self, poleIndexuZavOt, poleIndexuZavZav):

        rozdilyAll = []

        for i in range(0, len(poleIndexuZavZav)):
            indexZav = poleIndexuZavZav[i]
            rozdilyArr = self.vratPoleRozdiluKIndexuZav(poleIndexuZavOt, indexZav)

            rozdilyAll.append(rozdilyArr)

        return(rozdilyAll)


    def vratPoleRozdiluKIndexuZav(self, poleIndexuZavOt, indexZav):

        rozdilyArr = []

        for i in range(0, len(poleIndexuZavOt)):
            indexOt = poleIndexuZavOt[i]
            rozdil = indexZav - indexOt

            if(rozdil < 0):
                rozdil = False

            rozdilyArr.append(rozdil)

        return(rozdilyArr)


    def vratPoleZavorek(self, poleRadku):

        poleZavorek = []

        for i in range(0, len(poleRadku)):

            radek = poleRadku[i]
            met1 = MetodyJednohoRadku(False)
            slozenaZavorka = met1.vratSlozenouZavorku(radek)

            poleZavorek.append(slozenaZavorka)

        return(poleZavorek)



    def vratPoleIndexu(self, poleRadku, strExp):

        poleIndexuRadku = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            if(radek == strExp):
                poleIndexuRadku.append(i)


        return(poleIndexuRadku)