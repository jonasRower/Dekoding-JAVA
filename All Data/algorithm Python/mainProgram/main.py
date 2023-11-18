
import array


#dat breakpoint na radek 408 a otestovat !!!

class Data:

    def __init__(self):
        self.poleRadku = []
        self.jeTotoKod = []
        self.koncovyStrednik = []
        self.forCyklus = []
        self.ifPodminka = []
        self.nazevMetody = []
        self.nazevInstance = []

        self.nazevTridy = []
        self.volanaInstance = []
        self.volanaMetoda = []
        self.slozenaZavorka = []
        self.zacatekBloku = []
        self.konecBloku = []
        self.klicoveSlovo = []


    def add_radek(self, radek):
        self.poleRadku.append(radek)

    def add_jeTotoKod(self, jeTotoKod):
        self.jeTotoKod.append(jeTotoKod)

    def add_koncovyStrednik(self, koncovyStrednik):
        self.koncovyStrednik.append(koncovyStrednik)

    def add_forCyklus(self, forCyklus):
        self.forCyklus.append(forCyklus)

    def add_ifPodminka(self, ifPodminka):
        self.ifPodminka.append(ifPodminka)

    def add_klicoveSlovo(self, klicoveSlovo):
        self.klicoveSlovo.append(klicoveSlovo)

    def add_nazevMetody(self, nazevMetody):
        self.nazevMetody.append(nazevMetody)



    def add_nazevInstance(self, nazevInstance):
        self.nazevInstance.append(nazevInstance)

    def add_nazevTridy(self, nazevTridy):
        self.nazevTridy.append(nazevTridy)

    def add_volanaInstance(self, volanaInstance):
        self.volanaInstance.append(volanaInstance)

    def add_volanaMetoda(self, volanaMetoda):
        self.volanaMetoda.append(volanaMetoda)

        print()
    def add_slozenaZavorka(self, slozenaZavorka):
        self.slozenaZavorka.append(slozenaZavorka)

    def add_zacatekBloku(self, zacatekBloku):
        self.zacatekBloku.append(zacatekBloku)

    def add_konecBloku(self, konecBloku):
        self.konecBloku.append(konecBloku)





#########################################################################
#                METODY ROZPOZNAVAJICI TYP DAT                          #
#########################################################################

def rozhodniZdaDanyRadekJeKod(radekKodu):
   # print(radekKodu)
    radekKoduBezMezery = radekKodu.replace(" ","")
    JeToKod = True

    try:
        indexKomentare = radekKoduBezMezery.index('//')
        if(indexKomentare == 0):
            JeToKod = False
        else:
            JeToKod = True
    except:
       pass

    return(JeToKod)


def detekujPritomnostStrednikuNaKonciRadku(radekKodu):
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


def zjistiZdaRadekKoduObsahujeKlicoveSlovo(radekKodu):

    # Vraci True nebo False podle toho, zda radek obsahuje klicove slovo, ci nikoliv
    klicovaSlova = []
    klicovaSlova.append("for")
    klicovaSlova.append("if")
    klicovaSlova.append("while")
    klicovaSlova.append("try")
    klicovaSlova.append("catch")
    klicovaSlova.append("indexOf")
    klicovaSlova.append("substring")
    klicovaSlova.append("split")
    klicovaSlova.append("length")
    klicovaSlova.append("println")
    klicovaSlova.append("getLength")
    klicovaSlova.append("setForeground")
    klicovaSlova.append("return")

    # doplni do radku mezery, tak aby mohl pomoci mezer radek rozdelit
    # pokud by na radku mezera nebyla, nerozpoznal by klicove slovo
    radekKoduSMezerami = radekKodu.replace("(", " ")
    jednotlivaSlovaNaRadku = radekKoduSMezerami.split()

    klicoveSlovoNalezeno = False

    for klicoveSlovo in klicovaSlova:
        #pokud najde klicove slovo ve vnitrni smycce, ukonci i tu smycku vnejsi
        if (klicoveSlovoNalezeno == True):
            break
        for slovo in jednotlivaSlovaNaRadku:
            if (slovo == klicoveSlovo):
                klicoveSlovoNalezeno = True
                break

    return(klicoveSlovoNalezeno)


def zjistiZdaSeJednaOIfPodminku(radekKodu):

     jednotlivaSlovaNaRadku = radekKodu.split()
     ifPodminka = False
     for slovo in jednotlivaSlovaNaRadku:
         if (slovo == 'if'):
            ifPodminka = True
            break

     return (ifPodminka)


def zjistiZdaSeJednaOForCyklus(radekKodu):
    jednotlivaSlovaNaRadku = radekKodu.split()
    forCyklus = False
    for slovo in jednotlivaSlovaNaRadku:
        if (slovo == 'for'):
            forCyklus = True
            break

    return (forCyklus)


def zjistiZdaSeJednaOCatch(radekKodu):
    radekKodu = "      catch(Exception e) {System.out.println(e);}"
    jednotlivaSlovaNaRadku = radekKodu.split()
    catch = False
    for slovo in jednotlivaSlovaNaRadku:
        if (slovo == 'catch'):
            catch = True
            break

    return (catch)


def indikujZdaSeJednaOMetodu(radekKodu):
    # to pozna na zaklade pritomnosti zavorek "(" a ")"
    # pokud tam zavorky nejsou, pak vraci false, jinak true

    jednaSeOMetodu = False

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



def vratNazevMetody(radekKodu):
#K od vraci nazev metody z typoveho kodu:
# private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{

    nazevMetody = ""

    # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
    jednaSeOMetodu = indikujZdaSeJednaOMetodu(radekKodu)
    if (jednaSeOMetodu == True):

        # metodaPredZavorkou uvazuje jako cast nazvu pred "("
        indexZavorkyOtevrene = radekKodu.index('(')
        metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]

        #nasledne odstrani dalsi klicova slova, ktere do nazvu nepatri + mezery
        nazevMetody = metodaPredZavorkou.replace("private", "")
        nazevMetody = nazevMetody.replace("public", "")
        nazevMetody = nazevMetody.replace("boolean", "")
        nazevMetody = nazevMetody.replace("String", "")
        nazevMetody = nazevMetody.replace("int", "")
        nazevMetody = nazevMetody.replace("double", "")
        nazevMetody = nazevMetody.replace("void", "")
        nazevMetody = nazevMetody.replace("indexOf", "")
        nazevMetody = nazevMetody.replace("substring", "")
        nazevMetody = nazevMetody.replace("split", "")
        nazevMetody = nazevMetody.replace("length", "")
        nazevMetody = nazevMetody.replace("println", "")
        nazevMetody = nazevMetody.replace("getLength", "")
        nazevMetody = nazevMetody.replace("setForeground", "")
        nazevMetody = nazevMetody.replace("return", "")
        nazevMetody = nazevMetody.replace("[", "")
        nazevMetody = nazevMetody.replace("]", "")
        nazevMetody = nazevMetody.replace(" ", "")


    return(nazevMetody)


#detekuje pritomnost klicoveho slova new na radku
def obahujeRadekKoduKlicoveSlovoNew(radekKodu):

    indexSlovaNew = -1
    radekObsahujeNew = False
    try:
        indexSlovaNew = radekKodu.index('new')
        if(indexSlovaNew > -1):
            radekObsahujeNew = True
    except:
        pass

    return(radekObsahujeNew)


def vratNazevInstanceATridy(radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo):
    #vraci data z typoveho radku:
    #Select selNejmensi = new Select(dotazNejmensi);

    nazevInstance = ""
    nazevTridy = ""

    # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
    jednaSeOMetodu = indikujZdaSeJednaOMetodu(radekKodu)
    if (jednaSeOMetodu == True):

        #pokud radek neobsahuje strednik, pak se nejedna o radek typu:
        #Select selStredni = new Select(dotazStredni);
        #a tudis neni co resit a na konci funkce se zapisi data typu "" do pole
        if (koncovyStrednik == True):

            #Take radek nesmi obsahovat klicove slovo for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                # zjisti index klicoveho slova 'new'
                radekObsaheujeNew = obahujeRadekKoduKlicoveSlovoNew(radekKodu)
                if (radekObsaheujeNew == True):

                    #pokud klicove slovo "new" je obsazeno, pak proveruje, zda radekKodu obsahuje "="
                    if (radekObsaheujeNew == True):
                        indexRovnitka = 0
                        try:
                            indexRovnitka = radekKodu.index('=')
                        except:
                            pass

                        #pokud i obsahuje "=" pak pokracuje kod dal - oddeli nazev Instance a nazev Tridy
                        slovaNaRadku = radekKodu.split()
                        nazevTridy = slovaNaRadku[0]
                        nazevInstance = slovaNaRadku[1]


    #data do pole se predavaji zde
    data.add_nazevInstance(nazevInstance)
    data.add_nazevTridy(nazevTridy)


def vratNazevVolaneMetody(radekKodu, koncovyStrednik, klicoveSlovo, r):

    metodaPredZavorkou = ""

    if (koncovyStrednik == True):
        if (klicoveSlovo == False):

            # potvrdi zda radek neobsahuje klicove slovo "new"
            radekObsaheujeNew = obahujeRadekKoduKlicoveSlovoNew(radekKodu)

            if(radekObsaheujeNew == False):

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

                    metodaPredZavorkou = metodaPredZavorkou.replace(" ","")

                    # pole je jiz vytvorene (v metode vratNazevVolaneInstanceAMetody)
                    # a proto pro zapisovani se nepouziva append a zapisuji se data zde
                    # zapise se tedy volanaMetoda, pokud neobsahuje ""
                    if (metodaPredZavorkou != ""):

                        # zapisuje pouze ty data, ktere nebyly zapsany
                        if (data.volanaMetoda[r] == ""):
                            # jelikoz v metode vratNazevVolaneInstanceAMetody
                            # zapisuje "" pokud metoda se jmenuje napr. indexOf,
                            # pak se prepisuje kod zde - je tedy treba odfiltrovat i napr: "originalniSelect.indexOf"
                            # to se pozna prave diky tecce
                            try:
                                indexTecky = metodaPredZavorkou.index('.')
                                #kdyz najde tecku, pak neprovede nic (tecka v metodaPredZavorkou, nikoliv v radekKodu)
                            except:
                                #kdyz tecku nenajde, pak zapise data e2e
                                data.volanaMetoda[r] = metodaPredZavorkou

                except:
                    pass


    #Data se vraceji pro formalnost, pouze pro testovani
    return(metodaPredZavorkou)




def vratNazevVolaneInstanceAMetody(radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo,r):
    # vraci data z typoveho radku:
    # DataSelectuNejmensi = selNejmensi.getDataSelectu();

    volanaInstance = ""
    volanaMetoda = ""

    #Test: radekKodu = "indexOfFROM = originalniSelect.indexOf(FROM);"

    # kod ma vyznam vykonavat pouze tehdy, pokud radek obsahuje strednik
    if (koncovyStrednik == True):

        # a pokud radek neobsahuje klicove slovo jako napr. for, if, catch ...
        if(radekObsahujeKlicoveSlovo == False):

            # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
            jednaSeOMetodu = indikujZdaSeJednaOMetodu(radekKodu)
            if (jednaSeOMetodu == True):
                indexZavorkyOtevrene = radekKodu.index('(')
                kodRadkuPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
                slovaNaRadku = kodRadkuPredZavorkou.split()
                InstanceAMetoda = slovaNaRadku[-1]
                InstanceAMetodaArr = InstanceAMetoda.split(".")

                if (len(InstanceAMetodaArr) == 2):
                    volanaInstance = InstanceAMetodaArr[0]
                    volanaMetoda = InstanceAMetodaArr[1]

                    jeInstanceKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(volanaInstance)
                    jeMetodaKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(volanaMetoda)

                    #proveri, zda se nahodnou nejedna o klicove slovo, pokud ano, pak jej prepise na""
                    if (jeInstanceKlicoveSlovo == True):
                        volanaInstance = ""
                        volanaMetoda = ""

                    if(jeMetodaKlicoveSlovo == True):
                        volanaInstance = ""
                        volanaMetoda = ""

                    #if(volanaMetoda == "indexOf"):
                    #    jeMetodaKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(volanaMetoda)
                     #   print("")
                     #   volanaInstance = ""
                     #   volanaMetoda = ""

    data.add_volanaInstance(volanaInstance)
    data.add_volanaMetoda(volanaMetoda)
    print("")

def vratSlozenouZavorku(radekKodu):
    # z radku kodu vrati { nebo } , ostatni znaky vymaze
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


#########################################################################
#      METODY DOPISUJICI HODNOTY DO JIZ PREDPRIPRAVENYCH DAT            #
#########################################################################

def vratNejblizsiRadekSOtevrenouZavorkou(fromIndex):
    # vrati cislo radku kde je "{"
    # zacne hledat od zadaneho radku smerem dolu

    i = fromIndex
    cisloRadkuSOtevrenouZavorkou = -1
    for x in data.slozenaZavorka:

        radek = data.slozenaZavorka[i]
        if (radek == "{"):
            cisloRadkuSOtevrenouZavorkou = i
            break

        i = i + 1
        if (i >= len(data.slozenaZavorka)):
            break

    return (cisloRadkuSOtevrenouZavorkou)


def vratCisloRadkuSKoncemBloku(fromIndex):
    # vraci cislo radku, kde konci metoda
    # posledni radek pozna podle paroveho znaku }

    i = fromIndex
    pocetOtevrenychZavorek = 0
    pocetZavrenychZavorek = 0
    posledniRadek = -1

    for x in data.slozenaZavorka:
        radek = data.slozenaZavorka[i]

        if (radek == "{"):
            pocetOtevrenychZavorek = pocetOtevrenychZavorek + 1

        if (radek == "}"):
            pocetZavrenychZavorek = pocetZavrenychZavorek + 1

        ZavorkyRozdil = pocetOtevrenychZavorek - pocetZavrenychZavorek

        if (ZavorkyRozdil == 0):
            posledniRadek = i + 1
            break

        i = i + 1

    return(posledniRadek)

# Metoda volana z dopisujIndexyOtevrenychAZavrenychZavorek
def najdiRadekVolaneMetody(nazevMetody):

    radekVolaneMetody = -1
    r = -1

    for nazevMetodyData in data.volanaMetoda:
        r = r + 1
        if (nazevMetodyData == nazevMetody):
            radekVolaneMetody = r

    return(radekVolaneMetody)


def dopisujIndexyOtevrenychAZavrenychZavorek():
    # dopisuje indexy otevrenych a zavrenych zavorek ( "{", "}" ) na radek v Data, kde je volana metoda
    # proto je potreba vyhledavat volanou metodu

    i = -1

    for nazevMetodyHodnota in data.nazevMetody:
        i = i + 1
        radekObsahujeKlicoveSlovo = data.klicoveSlovo[i]

        indexNejblizsiOtevreneZavorky = -1
        indexNejblizsiZavreneZavorky = -1

        #zapisuje zacatek a konec bloku, v pripadech, kdy se nejedna o klicove slovo, tedy for, if, catch ...
        if (radekObsahujeKlicoveSlovo == False):

            if (nazevMetodyHodnota != ""):
                vyhledejOdRadku = i - 1
                indexNejblizsiOtevreneZavorky = vratNejblizsiRadekSOtevrenouZavorkou(vyhledejOdRadku)
                indexNejblizsiZavreneZavorky = vratCisloRadkuSKoncemBloku(indexNejblizsiOtevreneZavorky)

                radekVolaneMetody = najdiRadekVolaneMetody(nazevMetodyHodnota)
                if (radekVolaneMetody > -1):
                    data.zacatekBloku[radekVolaneMetody] = indexNejblizsiOtevreneZavorky
                    data.konecBloku[radekVolaneMetody] = indexNejblizsiZavreneZavorky


#########################################################################
#                   METODY VYTVAREJICI NOVY KOD                         #
#########################################################################

# Metoda spocita pocet mezer na zacatku radku, tak aby bylo mozno kod spravne odsadit
def spocitejPocetMezerPredKodemNaRadku(radekKodu):
    pocetMezer = 0

    znakyRadku = list(radekKodu)
    for znak in znakyRadku:
        if(znak.isspace() == True):
            pocetMezer = pocetMezer + 1

    return(pocetMezer)


# Metoda pridava mezery pred kazdy radek subKodu
def pridejMezeryPredRadek(subKod, pocetMezer):

    i = -1
    SubKodSMezerou = []

    mezeraPredSubKodem = ""
    for i in range(0, pocetMezer):
        mezeraPredSubKodem = mezeraPredSubKodem + " "

    mezeraPredSubKodem = mezeraPredSubKodem + "-->" + "  "

    for radekSubKodu in subKod:
        radekSubKoduSMezerou = mezeraPredSubKodem + radekSubKodu
        SubKodSMezerou.append(radekSubKoduSMezerou)

    return(SubKodSMezerou)


# Metoda nacita subKod mezi danymi radky
def nactiSubKod(prvniRadek, posledniRadek, pocetMezer, dataPole):

    poleSubKod = []
    subKod = []

    for i in range(prvniRadek, posledniRadek):
        radekSubKodu = dataPole[i]
        poleSubKod.append(radekSubKodu)

    if(pocetMezer == 0):
        subKod = poleSubKod
    else:
        subKod = pridejMezeryPredRadek(poleSubKod, pocetMezer)

    return(subKod)


# Metoda zanori konkretni subKod (kodNovy) do hlavniho Kodu
def vlozSubKodDoKodu(kodOrig, kodNovy, vkladejOdRadku):

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

    return(kodNew)


#prohledava data.nazevMetody a hleda souhlasny nazev Metody, shodny s volanou metodou
def vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN, volanaMetodaO, cisloRadkuvolanaMetodaN, volanaInstanceN):

    cisloRadkuZacKonBloku = -1
    nazevVolaneMetody = volanaMetodaN[cisloRadkuvolanaMetodaN]
    nazevVolaneInstance = volanaInstanceN[cisloRadkuvolanaMetodaN]

    i = -1
    for dataNazevMetody in volanaMetodaO:
        i = i + 1
        if(dataNazevMetody == nazevVolaneMetody):

            # zatim kod funguje jen pro volani pouze v ramci jedne tridy
            # kdyz tam bude instance - je potreba rozsirit kod o nacitani dat z vice souboru
            nazevVolaneInstance = volanaInstanceN[i]

            if (nazevVolaneInstance == ""):
                cisloRadkuZacKonBloku = i
                break

    return(cisloRadkuZacKonBloku)

#vratCisloRadkuDalsiVolaneMetody(poleRadkuN, cisloRadkuData)


# vrat index radku prvni volane metody za danym indexem
def vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, hledejOdIndexu):
    delkaDatVolanaMetodaN = len(volanaMetodaN)

    #Nalezne prvni volanou metodu v poliRadku (resp. poli volanaMetodaN) za danym indexem
    for i in range(hledejOdIndexu, delkaDatVolanaMetodaN):
        nazVolMetody = volanaMetodaN[i]

        if (nazVolMetody != ""):
            cisloRadkuNasledujiciMetody = i
            break

        #vrati cislo radku odkazujici na radek, kde se nalezne zacatek a konec Bloku
        #if (nazVolMetody != ""):
        #    cisloRadkuData = vratCisloRadkuMetody(nazVolMetody)
        #    break

    return (cisloRadkuNasledujiciMetody)


#def vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, hledejOdIndexu)
  #  delkaDatVolanaMetodaN = len(volanaMetodaN)


#Metoda postupne zanoruje subKody do hlavnihio kodu
def postupneVkladejSubKodyDoHlavnihoKodu(kodOrig, pocitatMezery, data):

    urovenZanoreni = 0
    i = - 1

    for nazVolMetody in data.volanaMetoda:
        i = i + 1
        if (nazVolMetody != ""):
            cisloRadku = vratCisloRadkuMetody(nazVolMetody)

            vyjmiKodOdRadku = data.zacatekBloku[cisloRadku]
            vyjmiKodDoRadku = data.konecBloku[cisloRadku]

            if(vyjmiKodOdRadku > -1):
                if (vyjmiKodDoRadku > -1):

                    #pokud se jedna o pole radku kodu, pak pocita mezery, u jinych typu dat to nema vyznam
                    if(pocitatMezery == True):
                        pocetMezerPredKodem = spocitejPocetMezerPredKodemNaRadku(kodOrig[i])
                    else:
                        pocetMezerPredKodem = 0

                    #Data do SubKodu se nacitaji z originalnich (modifikovanech) data.xxx (-proto kodOrig)
                    kodNovy = nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, pocetMezerPredKodem, kodOrig)
                    kodNew = vlozSubKodDoKodu(kodOrig, kodNovy, i+1)

                    break

    return (kodNew)

def vlozSubDataProJednotlivaPole(DataOrig, pocitatMezery, vyjmiKodOdRadku, vyjmiKodDoRadku, vkladejOdRadku, dataZdroj):

    dataNovy = []
    dataNew = []

    # pokud se jedna o pole radku kodu, pak pocita mezery, u jinych typu dat to nema vyznam
    if (pocitatMezery == True):
        pocetMezerPredKodem = spocitejPocetMezerPredKodemNaRadku(DataOrig[vkladejOdRadku])
    else:
        pocetMezerPredKodem = 0

    dataNovy = nactiSubKod(vyjmiKodOdRadku, vyjmiKodDoRadku, pocetMezerPredKodem, dataZdroj)
    dataNew = vlozSubKodDoKodu(DataOrig, dataNovy, vkladejOdRadku + 1)


    return (dataNew)




#########################################################################
#                HLAVNI VYKONAVAJICI KOD                                #
#########################################################################

#spocitejPocetMezerPredKodemNaRadku("")

#vratNazevVolaneMetody("", True)
#vlozSubKodDoKodu()

#vratNejblizsiRadekSOtevrenouZavorkou()
#vratCisloRadkuSKoncemBloku()
zjistiZdaRadekKoduObsahujeKlicoveSlovo("")
#zjistiZdaSeJednaOCatch("")



r = -1
data = Data()
with open('C:\\Users\\jonas\\PycharmProjects\\DokumentaceJAVY\\Kod JAVY\\src\\sql_gui\\BarevnyJTextArea.java', 'r') as f:
    for line in f:
        r = r + 1
        # prida radek do tridy Data
        data.add_radek(line)

        # Zjistuje, zda danyradek je kod, nebo zda se jedna o komentar + prida do tridy Data
        JeToKod = rozhodniZdaDanyRadekJeKod(line)
        data.add_jeTotoKod(JeToKod)

        # Pokud se jedna o kod, pak zjistuje dalsi moznosti
        # pokud se o kod nejedna, pak ostatni moznosti nastavuje jako False
        koncovyStrednik = False
        ifPodminka = False
        forCyklus = False
        nazevMetody = ""  # a nebo nazev metody prepise necim jinym


        if (JeToKod == True):

            # zjistuje, zda radek obsahuje na konci strednik + prida do tridy Data
            koncovyStrednik = detekujPritomnostStrednikuNaKonciRadku(line)

            # Zjistuje zda radek obsahuje klicove slovo jako napr. if, for, while, catch, try
            radekObsahujeKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(line)


            if (koncovyStrednik == False):


                # pokud na konci radku neni strednik, pak se muze jednat o if, for
                # overuje zda se jedna o if-podminku
                ifPodminka = zjistiZdaSeJednaOIfPodminku(line)

                # overuje zda se jedna o for-cyklus
                forCyklus = zjistiZdaSeJednaOForCyklus(line)

                # overuje zda se jedna o catch klauzuli
                catch = zjistiZdaSeJednaOCatch(line)

                if (radekObsahujeKlicoveSlovo == False):
                    if (ifPodminka == False):
                        if (forCyklus == False):
                            if (catch == False):
                                nazevMetody = vratNazevMetody(line)



        # data do tridy Data se zapisuji uvnitr teto funkce (proto je vyzadovana indikace koncovyStrednik)
        # plati pro radek, napr:
        # Select selNejmensi = new Select(dotazNejmensi);
        vratNazevInstanceATridy(line, koncovyStrednik, radekObsahujeKlicoveSlovo)

        # vrati nazev volane Instance a Metody napr:
        # DataSelectuNejmensi = selNejmensi.getDataSelectu();
        # data rovnou zapise do tridy Data
        vratNazevVolaneInstanceAMetody(line, koncovyStrednik, radekObsahujeKlicoveSlovo,r)

        # vrati nazev volane metody, napr:
        # pripravDataSelectu(NejvetsiSelect);
        # Navratova hodnota se zapisuje uvnitr metody, volanaMetoda zde je jen pro testovani
        volanaMetoda = vratNazevVolaneMetody(line, koncovyStrednik, radekObsahujeKlicoveSlovo, r)

        # Zapise "{" nebo "}" podle toho, co se nachazi na aktualnim radku
        radekSeZavorkou = vratSlozenouZavorku(line)


        # Nastavuje hodnoty do pole
        # Dane promenne se nastavi jako false na zacatku a bud se prenastavi, nebo ne
        # V obou pripadech se zapisuji a proto je potreba zapisovat data az na zaver cyklu
        data.add_koncovyStrednik(koncovyStrednik)
        # data.add_ifPodminka(ifPodminka)
        # data.add_forCyklus(forCyklus)
        data.add_nazevMetody(nazevMetody)
        data.add_slozenaZavorka(radekSeZavorkou)
        data.add_klicoveSlovo(radekObsahujeKlicoveSlovo)

        # Implicitne vytvori pole "zacatek a konec Bloku" s hodnotami -1
        # A nasledne bude hodnoty prepisovat v metode dopisujIndexyOtevrenychAZavrenychZavorek  (az po ukonceni teto smycky)
        data.add_zacatekBloku(-1)
        data.add_konecBloku(-1)

#########################################################################



# do poli data.zacatekBloku a data.konecBloku dopisuje indexy zavorek "{" a "}"
# dopise je vzdy na ten radek kde je zapsana volana metoda
# tzn. indexy "{" a "}" jsou indexy konkretni metody ulozene v data.nazevMetody
# avsak zapsane na prislusny radek, na kterym se nachazi data.volanaMetoda
dopisujIndexyOtevrenychAZavrenychZavorek()

cisloRadkuOdkudVkladatKod = 0

poleRadkuN = []
volanaMetodaN = []
volanaInstanceN = []

# prekopiruje pole radku do noveho pole
# poleRadkuN - je nove pole - pole, ktere je roztahovano

# data.volanaMetoda - je originalni pole,
# a zustava zachovano aby z nej bylo mozne nacitat nezmenena data
# (jinak by bylo potreba vsechny indexy radku prepocitavat)
poleRadkuN = data.poleRadku
volanaMetodaN = data.volanaMetoda
volanaInstanceN = data.volanaInstance

r = -1
for radek in data.poleRadku:
    r = r + 1

    #vrati radek kodu odkud bude vkladat kod = radek prvni metody za indexem "cisloRadkuOdkudVkladatKod" (z predchoziho cyklu)
    cisloRadkuOdkudVkladatKod = vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, cisloRadkuOdkudVkladatKod)

    #vrati index radku na kterem nalezne zacatek a konec bloku pro prvni volanou metodu za indexem "cisloRadku"
    cisloRadkuZjistiBlok = vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN, data.volanaMetoda, cisloRadkuOdkudVkladatKod, data.nazevInstance)

    # na zaklade cisloRadkuData vrati indexy zavorek bloku (tj. indexy "{" a "}")
    # jedna se tedy o blok kodu, ktery rozkopirovava a prenasi jinam
    vyjmiKodOdRadku = data.zacatekBloku[cisloRadkuZjistiBlok] - 1  #protoze otevrena zavorka muze byt az pod deklaraci
    vyjmiKodDoRadku = data.konecBloku[cisloRadkuZjistiBlok]

    # poleRadkuN obsahuje pole radku noveho "modifikovaneho" kodu
    poleRadkuN = vlozSubDataProJednotlivaPole(poleRadkuN, True, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, data.poleRadku)

    # tim jak se poleRadkuN "roztahuje", je potreba "roztahovat" i data
    # je potreba roztahovat i volane Metody a instance, tak aby radky vzajemne souhlasili
    volanaMetodaN = vlozSubDataProJednotlivaPole(volanaMetodaN, False, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, data.volanaMetoda)
    volanaInstanceN = vlozSubDataProJednotlivaPole(volanaInstanceN, False, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, data.volanaInstance)

    cisloRadkuOdkudVkladatKod = cisloRadkuOdkudVkladatKod + 1

    # ########################
    # dodelat mazani dat
    # ##################

    print("")


#-----------

cisloRadkuOdkudVkladatKod = cisloRadkuOdkudVkladatKod + 1
cisloRadkuOdkudVkladatKod = vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, cisloRadkuOdkudVkladatKod)

cisloRadkuZjistiBlok = vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN, data.volanaMetoda, cisloRadkuOdkudVkladatKod)

vyjmiKodOdRadku = data.zacatekBloku[cisloRadkuZjistiBlok] - 1
vyjmiKodDoRadku = data.konecBloku[cisloRadkuZjistiBlok]

poleRadkuN = vlozSubDataProJednotlivaPole(poleRadkuN, True, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, data.poleRadku)
volanaMetodaN = vlozSubDataProJednotlivaPole(volanaMetodaN, False, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, data.volanaMetoda)
volanaInstanceN = vlozSubDataProJednotlivaPole(volanaInstanceN, False, vyjmiKodOdRadku, vyjmiKodDoRadku, cisloRadkuOdkudVkladatKod, data.volanaInstance)




#vloziSubKody do poleRadkuN
poleRadkuN = postupneVkladejSubKodyDoHlavnihoKodu(poleRadkuN, True, data)

# je potreba vlozit data i do pole s volanymi metodami,
# aby volane metody vyhledaval na spravnych radcich
volanaMetodaN = postupneVkladejSubKodyDoHlavnihoKodu(volanaMetodaN, False, data)

# to same plati i pro pole s volanymi instancemi
volanaInstanceN = postupneVkladejSubKodyDoHlavnihoKodu(volanaInstanceN, False, data)


"""
#Nove pole dat
poleRadkuN = []
jeTotoKodN = []
klicoveSlovoN = []
koncovyStrednikN = []
konecBlokuN = []
nazevInstanceN = []
nazevMetodyN = []
nazevTridyN = []
poleRadkuN = []
slozenaZavorkaN = []
volanaInstanceN = []
volanaMetodaN = []
zacatekBlokuN = []

jeTotoKodN = postupneVkladejSubKodyDoHlavnihoKodu(data.jeTotoKod, False)
klicoveSlovoN = postupneVkladejSubKodyDoHlavnihoKodu(data.klicoveSlovo, False)
koncovyStrednikN = postupneVkladejSubKodyDoHlavnihoKodu(data.koncovyStrednik, False)
konecBlokuN = postupneVkladejSubKodyDoHlavnihoKodu(data.konecBloku, False)
nazevInstanceN = postupneVkladejSubKodyDoHlavnihoKodu(data.nazevInstance, False)
nazevMetodyN = postupneVkladejSubKodyDoHlavnihoKodu(data.nazevMetody, False)
nazevTridyN = postupneVkladejSubKodyDoHlavnihoKodu(data.nazevTridy, False)
poleRadkuN = postupneVkladejSubKodyDoHlavnihoKodu(data.poleRadku, True)
slozenaZavorkaN = postupneVkladejSubKodyDoHlavnihoKodu(data.slozenaZavorka, False)
volanaInstanceN = postupneVkladejSubKodyDoHlavnihoKodu(data.volanaInstance, False)
volanaMetodaN = postupneVkladejSubKodyDoHlavnihoKodu(data.volanaMetoda, False)
zacatekBlokuN = postupneVkladejSubKodyDoHlavnihoKodu(data.zacatekBloku, False)
"""

#vratNejblizsiRadekSOtevrenouZavorkou()
#########################################################################
#               Nize prepisuji Data do pole slovniku

i = -1
DataSlovnik = []
for radek in data.poleRadku:
    i = i + 1

    PoradiRadku = i
    Radek = data.poleRadku[i]
    TotoJeKod = data.jeTotoKod[i]
    StrednikNaKonci = data.koncovyStrednik[i]
    CyklusFor = data.forCyklus[i]
    PodminkaIf = data.ifPodminka[i]
    MetodaNazev = data.nazevMetody[i]
    TridaNazev = data.nazevTridy[i]
    InstanceVolana = data.volanaInstance[i]
    MetodaVolana = data.volanaMetoda[i]

    DataPoRadcich = {
        "Nazev Aktualni Tridy": "Moje Trida",
        "Cislo Radku": PoradiRadku,
        "Je kod na radku": TotoJeKod,
        "Kod Na Radku": Radek,
        "Koncovy strednik": StrednikNaKonci,
        "Cyklus For": CyklusFor,
        "Podminka If": PodminkaIf,
        "Nazev Metody": MetodaNazev,
        "Nazev Tridy": TridaNazev,
        "Nazev volane Instance": InstanceVolana,
        "Nazev Volene Metody": MetodaVolana
    }

    dataNaRadku = DataPoRadcich.items()

    DataSlovnik.append(dataNaRadku)
print("OK")


"""
d = DataPoRadcich.items()
d2 = []

d2.append(d)
d2.append(d)

print(d2)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)
"""


#print(poleRadku)






#result = sentence.index('Java')
#print("Substring 'Java':", result)



def detekujRadekKodu(poleRadku):
    #pro kazdy radek,kde je kod - tj. neni tam prazdny radek, nebo komentar, zapise true
    #for x in poleRadku:
    #    print(x)
    radek = "//"