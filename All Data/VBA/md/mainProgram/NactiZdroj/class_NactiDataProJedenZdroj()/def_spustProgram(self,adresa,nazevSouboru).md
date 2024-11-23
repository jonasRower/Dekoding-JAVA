# def spustProgram(self, adresa, nazevSouboru):

### list of variables
<a href  
with open(adresa, mode  
linesOfFile   
line   
koncovyStrednik   
nazevMetody   
radekObsahujeKlicoveSlovo   
JeToKod   
data.volanaMetoda[18]   

### code of method
<pre>
 <code>
    def spustProgram(self, adresa, nazevSouboru):
        #adresa =  adresa JAVA souboru

        # ziska plnou adresu pro nacteni JAVA kodu
        # adresa = vstupniData.vratPlnouAdresu("sql_gui", "BarevnyJTextArea.java")
        # adresa = vstupniData.vratPlnouAdresu(balicek, nazevZdroje)


        # inicializuji tridu pro ukladani dat
        # nazevSouboru = "SQL_GUI_Frame.java"
        # adresa = 'C:\\Users\\jonas\\PycharmProjects\\DokumentaceJAVY\\Kod JAVY\\src\\SQL_GUI_Frame.java'
        #adresa = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\SQL_GUI_1\\src\\sql_gui\\SQL_GUI_Frame.java"
          

        # nastavi nazev souboru do dat
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_nazevSouboru(self,nazevSouboru).md">data.add_nazevSouboru(nazevSouboru)</a>

        # inicializuji tridu pro ostatni tridy
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_add_nazevSouboru(self,nazevSouboru).md">ostatniMetody=Metody.OstatniMetody()</a>

        # predavam objekt abych mohl volat "ostatniMetody" prave z "metodyJednohoRadku"
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def_add_nazevSouboru(self,nazevSouboru).md">metodyJednohoRadku=Metody.MetodyJednohoRadku(ostatniMetody)</a>

        # predavam objekt abych mohl volat "ostatniMetody" prave z "metodyPredavajiciDataSamostatne"
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def_add_nazevSouboru(self,nazevSouboru).md">metodyPredavajiciDataSamostatne=Metody.MetodyPredavajiciDataSamostatne(ostatniMetody,data)</a>



        with open(adresa, mode="r", encoding="utf-8") as f:

            linesOfFile = f.readlines()

            for r in range(0, len(linesOfFile)):

                line = linesOfFile[r]

                # prida radek do tridy Data
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_radek(self,radek).md">data.add_radek(line)</a>

                # Zjistuje, zda danyradek je kod, nebo zda se jedna o komentar + prida do tridy Data
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def_rozhodniZdaDanyRadekJeKod(self,radekKodu).md">JeToKod=metodyJednohoRadku.rozhodniZdaDanyRadekJeKod(line)</a>

                # Pokud se jedna o kod, pak zjistuje dalsi moznosti
                # pokud se o kod nejedna, pak ostatni moznosti nastavuje jako False
                koncovyStrednik = False
                nazevMetody = ""  # a nebo nazev metody prepise necim jinym
                radekObsahujeKlicoveSlovo = False

                if (JeToKod == True):

                    # zjistuje, zda radek obsahuje na konci strednik + prida do tridy Data
                      <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def_detekujPritomnostStrednikuNaKonciRadku(self,radekKodu).md">koncovyStrednik=metodyJednohoRadku.detekujPritomnostStrednikuNaKonciRadku(line)</a>

                    # Zjistuje zda radek obsahuje klicove slovo jako napr. if, for, while, catch, try
                      <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def_zjistiZdaRadekKoduObsahujeKlicoveSlovo(self,radekKodu).md">radekObsahujeKlicoveSlovo=metodyJednohoRadku.zjistiZdaRadekKoduObsahujeKlicoveSlovo(line)</a>

                    if (koncovyStrednik == False):
                        if (radekObsahujeKlicoveSlovo == False):
                              <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def_vratNazevMetody(self,radekKodu).md">nazevMetody=metodyJednohoRadku.vratNazevMetody(line)</a>

                # Zapise "{" nebo "}" podle toho, co se nachazi na aktualnim radku
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def_vratSlozenouZavorku(self,radekKodu).md">radekSeZavorkou=metodyJednohoRadku.vratSlozenouZavorku(line)</a>

                # Nastavuje hodnoty do pole
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_jeTotoKod(self,jeTotoKod).md">data.add_jeTotoKod(JeToKod)</a>
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_koncovyStrednik(self,koncovyStrednik).md">data.add_koncovyStrednik(koncovyStrednik)</a>
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_nazevMetody(self,nazevMetody).md">data.add_nazevMetody(nazevMetody)</a>
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_slozenaZavorka(self,slozenaZavorka).md">data.add_slozenaZavorka(radekSeZavorkou)</a>
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_klicoveSlovo(self,klicoveSlovo).md">data.add_klicoveSlovo(radekObsahujeKlicoveSlovo)</a>


                ###############################################################
                # nize se data zapisuji (do DataProgramu.py) primo v metodach


                # data do tridy Data se zapisuji uvnitr teto funkce (proto je vyzadovana indikace koncovyStrednik)
                # plati pro radek, napr:
                # Select selNejmensi = new Select(dotazNejmensi);
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def_vratNazevInstanceATridy(self,radekKodu,koncovyStrednik,radekObsahujeKlicoveSlovo).md">metodyPredavajiciDataSamostatne.vratNazevInstanceATridy(line,koncovyStrednik,radekObsahujeKlicoveSlovo)</a>

                # vrati nazev volane Instance a Metody napr:
                # DataSelectuNejmensi = selNejmensi.getDataSelectu();
                # data rovnou zapise do tridy Data
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def_vratNazevVolaneInstanceAMetody(self,radekKodu,koncovyStrednik,radekObsahujeKlicoveSlovo,r).md">metodyPredavajiciDataSamostatne.vratNazevVolaneInstanceAMetody(line,koncovyStrednik,radekObsahujeKlicoveSlovo,r)</a>

                # vrati nazev volane metody, napr:
                # pripravDataSelectu(NejvetsiSelect);
                # Navratova hodnota se zapisuje uvnitr metody, volanaMetoda zde je jen pro testovani
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def_vratNazevVolaneMetody(self,radekKodu,koncovyStrednik,klicoveSlovo,r).md">volanaMetoda=metodyPredavajiciDataSamostatne.vratNazevVolaneMetody(line,koncovyStrednik,radekObsahujeKlicoveSlovo,r)</a>

                # Implicitne vytvori pole "zacatek a konec Bloku" s hodnotami -1
                # A nasledne bude hodnoty prepisovat v metode dopisujIndexyOtevrenychAZavrenychZavorek  (az po ukonceni teto smycky)
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_zacatekBloku(self,zacatekBloku).md">data.add_zacatekBloku(-1)</a>
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_konecBloku(self,konecBloku).md">data.add_konecBloku(-1)</a>

                # Implicitne vytvori prazdne pole s volanymi tridami
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram/DataProgramu/class_Data/def_add_volanaTrida(self,volanaTrida).md">data.add_volanaTrida("")</a>


        print("")


        data.volanaMetoda[18] = "createOutput"



        # do poli data.zacatekBloku a data.konecBloku dopisuje indexy zavorek "{" a "}"
        # dopise je vzdy na ten radek kde je zapsana volana metoda
        # tzn. indexy "{" a "}" jsou indexy konkretni metody ulozene v data.nazevMetody
        # avsak zapsane na prislusny radek, na kterym se nachazi data.volanaMetoda
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def_dopisujIndexyOtevrenychAZavrenychZavorek(self).md">metodyPredavajiciDataSamostatne.dopisujIndexyOtevrenychAZavrenychZavorek()</a>


        # inicializuji tridu pro vytvareni noveho JAVoveho Kodu
        #novyJAVAKod = NovyJAVAKod.RoztahujData(data)
        #novyJAVAKod.hlavni()

        #testuje data
        #test.testujData(data)

        return(data)
 <code>
<pre>






















