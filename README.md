# Dekoding-JAVA
Převádí zdrojový kód JAVA do stromové struktury.

toto je test

## Spuštění programu
Po stažení a spustíme program v IDE Pycharm

V souboru `StartProgramu.py` začíná běh programu.
Kód je následující:
```
import mainProgram.SeznamZdroju
import mainProgram.NovyJAVAKod


vykonavejHlavniProgram = mainProgram.SeznamZdroju.vykonavaniHlavnihoProgramu()
vykonavejHlavniProgram.hlavniProgram()
```

## Popis metod
### class `vykonavaniHlavnihoProgramu():`
třída je v souboru: `mainProgram.SeznamZdroju.py`.

#### metoda `def hlavniProgram(self):`
```
 def hlavniProgram(self):

        # Do adresyZdrojuData ulozi "Nazev JAVA souboru", "adresa pred nazev souboru" a "adresu s nazvem souboru"
        adresyZdrojuData = SeznamZdroju()
        adresyZdrojuData.vratSeznamAdresZdroju()

        # zde jsou data vsech souboru
        dataVsechSouboru = []

        # kod nize, bezi ve smycce
        # jsou jednotlive volany vsechny nazvy JAVA soubory, vcetne jejich adres
        pocetSouboru = len(adresyZdrojuData.seznamZdroju)
        for i in range(0, pocetSouboru):
            # ziska adresu se zdrojem (s nazvem souboru) a nazev zdroje (souboru)
            adresaZdroj = adresyZdrojuData.seznamAdresZdroju[i]
            zdroj = adresyZdrojuData.seznamZdroju[i]

            # hlavni program pro ziskani kompletnich dat pro jeden soubor
            startProgramu = mainProgram.NactiZdroj.NactiDataProJedenZdroj()

            # data pro jeden soubor ulozi sem
            dataJednohoSouboru = startProgramu.spustProgram(adresaZdroj, zdroj)

            # do kazdeho souboru dopise (dodatecne) jeste nazvy trid, na radcich s konstruktory
            dataJednohoSouboru = self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)

            # jednotlive se pridavaji data soubor po souboru
            dataVsechSouboru.append(dataJednohoSouboru)



        # projde data jeste jednou a doplni rozsahy slozenych zavorek
        # vyhledava totiz radky i z cizich trid,
        # proto je potreba tuto metodu spustit az po naplneni vsech ostatnich dat
        for i in range(1, pocetSouboru):
            dataJednohoSouboru = dataVsechSouboru[i]
            dataJednohoSouboru = self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)
            dataVsechSouboru = self.kVolaneMetodeNajdiNazevTridy(dataJednohoSouboru, dataVsechSouboru)

        #dataVsechSouboru[6].volanaTrida[40] = "VytvorDB"

        #self.podleNazvuSouboruPredejPoleSeSlozenymiZavorkami("NactiDotazy", dataVsechSouboru)

        novyJAVAKod = mainProgram.NovyJAVAKod.RoztahujData(dataVsechSouboru)
        novyJAVAKod = mainProgram.NovyJAVAKod2.RoztahujData(dataVsechSouboru)
        novyJAVAKod.hlavni()

        self.poleRadkuN = novyJAVAKod.getPoleRadkuN()
```

##### Popis proměnných
`adresyZdrojuData.vratSeznamAdresZdroju()` plní objekt `adresyZdrojuData` daty.  
`seznamAdres` obsahuje seznam všech adres k jednotlivým `.java` souborům - bez názvů `.java`  
`seznamAdresZdroju`obsahuje seznam všech adres k jednotlivým `.java souborům` - včetně názvů `.java`  
`seznamZdroju` obsahuje seznam názvů souborů `.java`  


###### Objekt `dataJednohoSouboru`  
V prvním cyklu zjišťuje data kódu v souboru:
`createOutput.java`

Kód je následující:
```
package createOutput;

import java.io.File;
import java.io.FileWriter;   
import java.io.IOException;  
import java.util.ArrayList;
import java.util.HashMap;


public class createOutput {
    
    //zatim nepouzivam
    //createLog(ArrayList<ArrayList<ArrayList<HashMap<String, Integer>>>> data){
        
    //}
    
    
    public createOutput(ArrayList<ArrayList<String>>logArrStr, String adresaProjektu, String nazevLogu){
        
        String adresaProjektuFull;
        adresaProjektuFull = ziskejAdresuKamGenerovat(adresaProjektu, nazevLogu);
        
        String text;
        text = vytvorPoleRadkuTxt(logArrStr);
        
        //vytiskne vystup do csv
        vytiskniVystup(text, adresaProjektuFull);
          
    }


    
    
    private String ziskejAdresuKamGenerovat(String adresaProjektu, String nazevLogu){
        
        String adresaProjektuFull;
        adresaProjektuFull = adresaProjektu + nazevLogu;
    
        return(adresaProjektuFull);
        
    }
    
    
    private String vytvorPoleRadkuTxt(ArrayList<ArrayList<String>>logArrStr){
        
        ArrayList<String> radekArr;
        String hodnota;
        
        String text;
        text = "";
        
        for (int r = 0; r < logArrStr.size(); r++) {
            radekArr = logArrStr.get(r);
            
            for (int s = 0; s < radekArr.size(); s++) {
                hodnota = radekArr.get(s);
                text = text + hodnota + ",";
            }
            
            text = text + "\n";
        }

        return(text);
       
    }
    
    
    private void vytiskniVystup(String text, String adresaProjektuFull){
        
        try {
                FileWriter myWriter = new FileWriter(adresaProjektuFull);
                myWriter.write(text);
                myWriter.close();
                System.out.println("Successfully wrote to the file.");
                
            } catch (IOException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();
          }
        
    }


    
}
```

Python plní objekt `dataJednohoSouboru`, který obsahuje jednotlivá pole:  
`jeTotoKod`  
`klicoveSlovo`  
`koncovyStrrednik`  
`konecBloku`  
`nazeInstance`  
`nazevMetody`  
`nazevTridy`  
`poleRadku`  
`slozenaZavorka`  
`volanaInstance`  
`volanaMetoda`  
`volanaTrida`  
`zacatekBloku`  

Některá pole jsou v tabulce níže (=jednotlivé sloupce).  
Ostatní pole si ukážeme na jiných datech.  

|  |poleRadku|jeTotoKod|klicoveSlovo|koncovyStrednik|nazevMetody|slozenaZavorka|volanaMetoda|zacatekBloku|konecBloku|
|--|---------|---------|------------|---------------|-----------|--------------|------------|------------|----------|
|00|                                                                                          |True |False|False|                        |'' |''|-1|-1
|01|package createOutput;                                                                     |True |False|True |                        |'' |''|-1|-1
|02|                                                                                          |True |False|False|                        |'' |''|-1|-1
|03|import java.io.File;                                                                      |True |False|True |                        |'' |''|-1|-1
|04|import java.io.FileWriter;                                                                |True |False|True |                        |'' |''|-1|-1
|05|import java.io.IOException;                                                               |True |False|True |                        |'' |''|-1|-1
|06|import java.util.ArrayList;                                                               |True |False|True |                        |'' |''|-1|-1
|07|import java.util.HashMap;                                                                |True |False|True |                        |'' |''|-1|-1
|08|                                                                                          |True |False|False|                        |'' |''|-1|-1
|09|                                                                                          |True |False|False|                        |'' |''|-1|-1
|10|public class createOutput {                                                               |True |False|False|                        |'{'|''|-1|-1
|11|                                                                                          |True |False|False|                        |'' |''|-1|-1
|12|    //zatim nepouzivam                                                                    |False|False|False|                        |'' |''|-1|-1
|13|    //createLog(ArrayList<ArrayList<ArrayList<HashMap<String Integer>>>> data){"          |False|False|False|                        |'{'|''|-1|-1
|14|                                                                                          |True |False|False|                        |'' |''|-1|-1
|15|    //}                                                                                   |False|False|False|                        |'}'|''|-1|-1
|16|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|17|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|18|    public createOutput(ArrayList<ArrayList<String>>logArrStr, String adresaProjektu, String nazevLogu){"                   |True|False|False|createOutput|'{'|'createOutput'|18|30
|19|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|20|        String adresaProjektuFull;                                                        |True |False|True |                        |'' |'          '|-1|-1
|21|        adresaProjektuFull = ziskejAdresuKamGenerovat(adresaProjektu, nazevLogu);"        |True |False|True |                        |'' |'ziskejAdresuKamGenerovat'|34|42
|22|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|23|        String text;                                                                      |True |False|True |                        |'' |'          '|-1|-1
|24|        text = vytvorPoleRadkuTxt(logArrStr);                                             |True |False|True |                        |'' |'vytvorPoleRadkuTxt'|44|66
|25|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|26|        //vytiskne vystup do csv                                                          |False|False|False|                        |'' |'          '|-1|-1
|27|        vytiskniVystup(text, adresaProjektuFull);"                                        |True |False|True |                        |'' |'vytiskniVystup'|68|80
|28|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|29|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|30|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|31|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|32|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|33|                                                                                          |True |False|False|                        |'' |''          |-1|-1
|34|    private String ziskejAdresuKamGenerovat(String adresaProjektu, String nazevLogu){"    |True |False|False|ziskejAdresuKamGenerovat|'{'|'          '|-1|-1
|35|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|36|       String adresaProjektuFull;                                                         |True |False|True |                        |' '|'          '|-1|-1
|37|        adresaProjektuFull = adresaProjektu + nazevLogu;                                  |True |False|True |                        |' '|'          '|-1|-1
|38|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|39|        return(adresaProjektuFull);                                                       |True |True |True |                        |' '|'          '|-1|-1
|40|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|41|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|42|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|43|                                                                                          |True |False|False|                        |' '|''          |-1|-1
|44|    private String vytvorPoleRadkuTxt(ArrayList<ArrayList<String>>logArrStr){             |True |False|False|vytvorPoleRadkuTxt      |'{'|'          '|-1|-1
|45|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|46|        ArrayList<String> radekArr;                                                       |True |False|True |                        |' '|'          '|-1|-1
|47|        String hodnota;                                                                   |True |False|True |                        |' '|'          '|-1|-1
|48|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|49|        String text;                                                                      |True |False|True |                        |' '|'          '|-1|-1
|50|        text = """";"                                                                     |True |False|True |                        |' '|'          '|-1|-1
|51|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|52|        for (int r = 0; r < logArrStr.size(); r++) {                                      |True |True|False |                        |'{'|'          '|-1|-1
|53|            radekArr = logArrStr.get(r);                                                  |True |False|True |                        |' '|'get'|-1|-1
|54|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|55|            for (int s = 0; s < radekArr.size(); s++) {                                   |True |True|False |                        |'{'|'          '|-1|-1
|56|                hodnota = radekArr.get(s);                                                |True |False|True |                        |''|'get'|-1|-1
|57|                text = text + hodnota + ""/"";"                                           |True |False|True |                        |' '|'          '|-1|-1
|58|            }                                                                             |True |False|False|                        |'}'|'          '|-1|-1
|59|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|60|            text = text + ""\n"";"                                                        |True |False|True |                        |' '|'          '|-1|-1
|61|        }                                                                                 |True |False|False|                        |'}'|'          '|-1|-1
|62|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|63|        return(text);                                                                     |True |True |True |                        |' '|'          '|-1|-1
|64|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|65|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|66|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|67|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|68|    private void vytiskniVystup(String text, String adresaProjektuFull){"                 |True |False|False|vytiskniVystup          |'{'|'          '|-1|-1
|69|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|70|        try {                                                                             |True |True |False|                        |'{'|'          '|-1|-1
|71|                FileWriter myWriter = new FileWriter(adresaProjektuFull);                 |True |False|True |                        |' '|'FileWriter'|-1|-1
|72|                myWriter.write(text);                                                     |True |False|True |                        |' '|'write'|-1|-1
|73|                myWriter.close();                                                         |True |False|True |                        |' '|'close'|-1|-1
|74|                System.out.println(""Successfully wrote to the file."");"                 |True |False|True |                        |' '|'          '|-1|-1
|75|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|76|            } catch (IOException e) {                                                     |True |True|False |                        |'}'|'          '|-1|-1
|77|                System.out.println(""An error occurred."");"                              |True |False|True |                        |' '|'          '|-1|-1
|78|                e.printStackTrace();                                                      |True |False|True |                        |' '|'printStackTrace'|-1|-1
|79|          }                                                                               |True |False|False|                        |'}'|'          '|-1|-1
|80|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|81|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|82|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|83|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|84|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|85|}                                                                                         |True |False|False|                        |'}'|'          '|-1|-1


Pole (sloupce) v tabulce znamenají: 
`poleRadku` - jednotlivé řádky kódu v poli  
`jeTotoKod` - je-li `False`, pak se jedná o komentář   
`klicoveSlovo` - pokud je `True`, pak obsahuje slovo např. `for`, `if`, ....  
`koncovyStrrednik` - pokud je `True`, pak je řádek kódu ukončen středníkem.  
`nazevMetody` - nazev metody v hlavičce  
`slozenaZavorka` - pokud je složená závorka, pak obsahuje danou závorku `{` nebo `}` , pokud tam není, je hodnota prázdná  
`volanaMetoda` - název metody, která je na daném řádku volána  
`zacatekBloku` - odkazuje na index řádku, kde je `{` dané metody na řádku, pokud konec bloku není, pak je `-1`  
`konecBloku` - odkazuje na index řádku, kde je `}` dané metody na řádku, pokud konec bloku není, pak je `-1`  
 

  
Příkazem  
`dataVsechSouboru.append(dataJednohoSouboru)`  
přidáváme jednotlivý objekt `dataJednohoSouboru` do objedktu `dataVsechSouboru`.  
`dataVsechSouboru` tedy obsahují data (tabulky výše) všech `.java` souborů


### class `NactiDataProJedenZdroj():`
Třída je v souboru: `mainProgram.nactiZdroj`.  
Touto metodou se získávají `dataJednohoSouboru`  

Metodu jsme volali z kódu, výše:
```
 def hlavniProgram(self):
    ....    
        for i in range(0, pocetSouboru):
            ....
            # hlavni program pro ziskani kompletnich dat pro jeden soubor
            startProgramu = mainProgram.NactiZdroj.NactiDataProJedenZdroj()

            # data pro jeden soubor ulozi sem
            dataJednohoSouboru = startProgramu.spustProgram(adresaZdroj, zdroj)
```

#### metoda `def spustProgram(self, adresa, nazevSouboru):`

```
    def spustProgram(self, adresa, nazevSouboru):
        #adresa =  adresa JAVA souboru

        # ziska plnou adresu pro nacteni JAVA kodu
        # adresa = vstupniData.vratPlnouAdresu("sql_gui", "BarevnyJTextArea.java")
        # adresa = vstupniData.vratPlnouAdresu(balicek, nazevZdroje)


        # inicializuji tridu pro ukladani dat
        data = DataProgramu.Data()

        # nastavi nazev souboru do dat
        data.add_nazevSouboru(nazevSouboru)

        # inicializuji tridu pro ostatni tridy
        ostatniMetody = Metody.OstatniMetody()

        # predavam objekt abych mohl volat "ostatniMetody" prave z "metodyJednohoRadku"
        metodyJednohoRadku = Metody.MetodyJednohoRadku(ostatniMetody)

        # predavam objekt abych mohl volat "ostatniMetody" prave z "metodyPredavajiciDataSamostatne"
        metodyPredavajiciDataSamostatne = Metody.MetodyPredavajiciDataSamostatne(ostatniMetody, data)



        with open(adresa, mode="r", encoding="utf-8") as f:

            linesOfFile = f.readlines()

            for r in range(0, len(linesOfFile)):

                line = linesOfFile[r]

                # prida radek do tridy Data
                data.add_radek(line)

                # Zjistuje, zda danyradek je kod, nebo zda se jedna o komentar + prida do tridy Data
                JeToKod = metodyJednohoRadku.rozhodniZdaDanyRadekJeKod(line)

                # Pokud se jedna o kod, pak zjistuje dalsi moznosti
                # pokud se o kod nejedna, pak ostatni moznosti nastavuje jako False
                koncovyStrednik = False
                nazevMetody = ""  # a nebo nazev metody prepise necim jinym
                radekObsahujeKlicoveSlovo = False

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

        # do poli data.zacatekBloku a data.konecBloku dopisuje indexy zavorek "{" a "}"
        # dopise je vzdy na ten radek kde je zapsana volana metoda
        # tzn. indexy "{" a "}" jsou indexy konkretni metody ulozene v data.nazevMetody
        # avsak zapsane na prislusny radek, na kterym se nachazi data.volanaMetoda
        metodyPredavajiciDataSamostatne.dopisujIndexyOtevrenychAZavrenychZavorek()


        # inicializuji tridu pro vytvareni noveho JAVoveho Kodu
        #novyJAVAKod = NovyJAVAKod.RoztahujData(data)
        #novyJAVAKod.hlavni()

        #testuje data
        #test.testujData(data)

        return(data)
```

K získání dat využíváme tříd:
`Metody.MetodyJednohoRadku(ostatniMetody)` - jsou metody, které detekují data na daném řádku kódu `JAVA`, aniž by musely znát řádky ostatní.  
`Metody.MetodyPredavajiciDataSamostatne(ostatniMetody, data)` - jsou metody, které získávají data na základě analýzy z více řádků kódu 'JAVA'. 
Obě třídy vyžadují objekt `ostatniMetody = Metody.OstatniMetody()`  
  
Smyčka běží na všech řádcích kódu daného souboru `.java`
```
...
        with open(adresa, mode="r", encoding="utf-8") as f:

            linesOfFile = f.readlines()

            for r in range(0, len(linesOfFile)):

                line = linesOfFile[r]
...
```

přičemž hodnoty se nastavují pomocí setrů v každé smyčce:
```
                # Nastavuje hodnoty do pole
                data.add_jeTotoKod(JeToKod)
                data.add_koncovyStrednik(koncovyStrednik)
                data.add_nazevMetody(nazevMetody)
                data.add_slozenaZavorka(radekSeZavorkou)
                data.add_klicoveSlovo(radekObsahujeKlicoveSlovo)      
```

ostatní data se zapisují prostřednictvíém třídy:
`metodyPredavajiciDataSamostatne`
