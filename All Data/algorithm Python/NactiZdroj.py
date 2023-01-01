import DataProgramu
import Metody


#########################################################################
#                HLAVNI VYKONAVAJICI KOD                                #
#########################################################################

class NactiDataProJedenZdroj():

    #def spustProgram(self, balicek, nazevZdroje):
    def spustProgram(self, adresa, nazevSouboru):
        #adresa =  adresa JAVA souboru

        # ziska plnou adresu pro nacteni JAVA kodu
        # adresa = vstupniData.vratPlnouAdresu("sql_gui", "BarevnyJTextArea.java")
        # adresa = vstupniData.vratPlnouAdresu(balicek, nazevZdroje)


        # inicializuji tridu pro ukladani dat
        # nazevSouboru = "SQL_GUI_Frame.java"
        # adresa = 'C:\\Users\\jonas\\PycharmProjects\\DokumentaceJAVY\\Kod JAVY\\src\\SQL_GUI_Frame.java'
        #adresa = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\SQL_GUI_1\\src\\sql_gui\\SQL_GUI_Frame.java"
        data = DataProgramu.Data()

        # nastavi nazev souboru do dat
        data.add_nazevSouboru(nazevSouboru)

        # inicializuji tridu pro ostatni tridy
        ostatniMetody = Metody.OstatniMetody()

        # predavam objekt abych mohl volat "ostatniMetody" prave z "metodyJednohoRadku"
        metodyJednohoRadku = Metody.MetodyJednohoRadku(ostatniMetody)

        # predavam objekt abych mohl volat "ostatniMetody" prave z "metodyPredavajiciDataSamostatne"
        metodyPredavajiciDataSamostatne = Metody.MetodyPredavajiciDataSamostatne(ostatniMetody, data)


        r = -1
        with open(adresa, 'r') as f:
            for line in f:
                r = r + 1

                # prida radek do tridy Data
                data.add_radek(line)

                # Zjistuje, zda danyradek je kod, nebo zda se jedna o komentar + prida do tridy Data
                JeToKod = metodyJednohoRadku.rozhodniZdaDanyRadekJeKod(line)

                # Pokud se jedna o kod, pak zjistuje dalsi moznosti
                # pokud se o kod nejedna, pak ostatni moznosti nastavuje jako False
                koncovyStrednik = False
                nazevMetody = ""  # a nebo nazev metody prepise necim jinym

                if (JeToKod == True):

                    # zjistuje, zda radek obsahuje na konci strednik + prida do tridy Data
                    koncovyStrednik = metodyJednohoRadku.detekujPritomnostStrednikuNaKonciRadku(line)

                    # Zjistuje zda radek obsahuje klicove slovo jako napr. if, for, while, catch, try
                    radekObsahujeKlicoveSlovo = metodyJednohoRadku.zjistiZdaRadekKoduObsahujeKlicoveSlovo(line)

                    if (koncovyStrednik == False):
                        if (radekObsahujeKlicoveSlovo == False):
                            nazevMetody = metodyJednohoRadku.vratNazevMetody(line)

                # Zapise "{" nebo "}" podle toho, co se nachazi na aktualnim radku
                radekSeZavorkou = metodyJednohoRadku.vratSlozenouZavorku(line)

                # Nastavuje hodnoty do pole
                data.add_jeTotoKod(JeToKod)
                data.add_koncovyStrednik(koncovyStrednik)
                data.add_nazevMetody(nazevMetody)
                data.add_slozenaZavorka(radekSeZavorkou)
                data.add_klicoveSlovo(radekObsahujeKlicoveSlovo)


                ###############################################################
                # nize se data zapisuji (do DataProgramu.py) primo v metodach


                # data do tridy Data se zapisuji uvnitr teto funkce (proto je vyzadovana indikace koncovyStrednik)
                # plati pro radek, napr:
                # Select selNejmensi = new Select(dotazNejmensi);
                metodyPredavajiciDataSamostatne.vratNazevInstanceATridy(line, koncovyStrednik, radekObsahujeKlicoveSlovo)

                # vrati nazev volane Instance a Metody napr:
                # DataSelectuNejmensi = selNejmensi.getDataSelectu();
                # data rovnou zapise do tridy Data
                metodyPredavajiciDataSamostatne.vratNazevVolaneInstanceAMetody(line, koncovyStrednik, radekObsahujeKlicoveSlovo, r)

                # vrati nazev volane metody, napr:
                # pripravDataSelectu(NejvetsiSelect);
                # Navratova hodnota se zapisuje uvnitr metody, volanaMetoda zde je jen pro testovani
                volanaMetoda = metodyPredavajiciDataSamostatne.vratNazevVolaneMetody(line, koncovyStrednik, radekObsahujeKlicoveSlovo, r)

                # Implicitne vytvori pole "zacatek a konec Bloku" s hodnotami -1
                # A nasledne bude hodnoty prepisovat v metode dopisujIndexyOtevrenychAZavrenychZavorek  (az po ukonceni teto smycky)
                data.add_zacatekBloku(-1)
                data.add_konecBloku(-1)

                # Implicitne vytvori prazdne pole s volanymi tridami
                data.add_volanaTrida("")

        print("")

        # do poli data.zacatekBloku a data.konecBloku dopisuje indexy zavorek "{" a "}"
        # dopise je vzdy na ten radek kde je zapsana volana metoda
        # tzn. indexy "{" a "}" jsou indexy konkretni metody ulozene v data.nazevMetody
        # avsak zapsane na prislusny radek, na kterym se nachazi data.volanaMetoda
        metodyPredavajiciDataSamostatne.dopisujIndexyOtevrenychAZavrenychZavorek()


        # inicializuji tridu pro vytvareni noveho JAVoveho Kodu
        #novyJAVAKod = NovyJAVAKod.RoztahujData(data)
        #novyJAVAKod.hlavni()

        return(data)


    def xx(self):
        print("")




