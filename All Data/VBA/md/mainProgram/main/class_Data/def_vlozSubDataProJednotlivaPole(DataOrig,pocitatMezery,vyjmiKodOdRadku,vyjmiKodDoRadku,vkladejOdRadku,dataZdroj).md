# def vlozSubDataProJednotlivaPole(DataOrig, pocitatMezery, vyjmiKodOdRadku, vyjmiKodDoRadku, vkladejOdRadku, dataZdroj):

### list of variables
dataNovy   
dataNew   
pocitatMezery   
pocetMezerPredKodem   
r   
data   
JeToKod   
koncovyStrednik   
ifPodminka   
forCyklus   
nazevMetody   
radekObsahujeKlicoveSlovo   
catch   
volanaMetoda   
radekSeZavorkou   
cisloRadkuOdkudVkladatKod   
poleRadkuN   
volanaMetodaN   
volanaInstanceN   
cisloRadkuZjistiBlok   
vyjmiKodOdRadku   
vyjmiKodDoRadku   
jeTotoKodN   
klicoveSlovoN   
koncovyStrednikN   
konecBlokuN   
nazevInstanceN   
nazevMetodyN   
nazevTridyN   
slozenaZavorkaN   
zacatekBlokuN   
i   
DataSlovnik   
PoradiRadku   
Radek   
TotoJeKod   
StrednikNaKonci   
CyklusFor   
PodminkaIf   
MetodaNazev   
TridaNazev   
InstanceVolana   
MetodaVolana   
DataPoRadcich   
dataNaRadku   
d   
d2   
car   
x   

### code of method
```
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
```
### links

