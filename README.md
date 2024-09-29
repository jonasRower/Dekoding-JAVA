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
třída je v souboru: `mainProgram.SeznamZdroju`.

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


|poleRadku|jeTotoKod|klicoveSlovo|koncovyStrednik|nazevMetody|slozenaZavorka|volanaMetoda|zacatekBloku|konecBloku|
|---------|---------|------------|---------------|-----------|--------------|------------|------------|----------|
|                                                                                          |True |False|False|                        |'' |''|-1|-1
|package createOutput;                                                                     |True |False|True |                        |'' |''|-1|-1
|                                                                                          |True |False|False|                        |'' |''|-1|-1
|import java.io.File;                                                                      |True |False|True |                        |'' |''|-1|-1
|import java.io.FileWriter;                                                                |True |False|True |                        |'' |''|-1|-1
|import java.io.IOException;                                                               |True |False|True |                        |'' |''|-1|-1
|import java.util.ArrayList;                                                               |True |False|True |                        |'' |''|-1|-1
|import java.util.HashMap;                                                                |True |False|True |                        |'' |''|-1|-1
|                                                                                          |True |False|False|                        |'' |''|-1|-1
|                                                                                          |True |False|False|                        |'' |''|-1|-1
|public class createOutput {                                                               |True |False|False|                        |'{'|''|-1|-1
|                                                                                          |True |False|False|                        |'' |''|-1|-1
|    //zatim nepouzivam                                                                    |False|False|False|                        |'' |''|-1|-1
|    //createLog(ArrayList<ArrayList<ArrayList<HashMap<String Integer>>>> data){"          |False|False|False|                        |'{'|''|-1|-1
|                                                                                          |True |False|False|                        |'' |''|-1|-1
|    //}                                                                                   |False|False|False|                        |'}'|''|-1|-1
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|    public createOutput(ArrayList<ArrayList<String>>logArrStr, String adresaProjektu, String nazevLogu){"                   |True|False|False|createOutput|'{'|'createOutput'|18|30
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|        String adresaProjektuFull;                                                        |True |False|True |                        |'' |'          '|-1|-1
|        adresaProjektuFull = ziskejAdresuKamGenerovat(adresaProjektu| nazevLogu);"        |True |False|True |                        |'' |'ziskejAdresuKamGenerovat'|34|42
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|        String text;                                                                      |True |False|True |                        |'' |'          '|-1|-1
|        text = vytvorPoleRadkuTxt(logArrStr);                                             |True |False|True |                        |'' |'vytvorPoleRadkuTxt'|44|66
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|        //vytiskne vystup do csv                                                          |False|False|False|                        |'' |'          '|-1|-1
|        vytiskniVystup(text| adresaProjektuFull);"                                        |True |False|True |                        |'' |'vytiskniVystup'|68|80
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|                                                                                          |True |False|False|                        |'' |'          '|-1|-1
|                                                                                          |True |False|False|                        |'' |''          |-1|-1
|    private String ziskejAdresuKamGenerovat(String adresaProjektu, String nazevLogu){"    |True |False|False|ziskejAdresuKamGenerovat|'{'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|       String adresaProjektuFull;                                                         |True |False|True |                        |' '|'          '|-1|-1
|        adresaProjektuFull = adresaProjektu + nazevLogu;                                  |True |False|True |                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|        return(adresaProjektuFull);                                                       |True |True |True |                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|''          |-1|-1
|    private String vytvorPoleRadkuTxt(ArrayList<ArrayList<String>>logArrStr){             |True |False|False|vytvorPoleRadkuTxt      |'{'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|        ArrayList<String> radekArr;                                                       |True |False|True |                        |' '|'          '|-1|-1
|        String hodnota;                                                                   |True |False|True |                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|        String text;                                                                      |True |False|True |                        |' '|'          '|-1|-1
|        text = """";"                                                                     |True |False|True |                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|        for (int r = 0; r < logArrStr.size(); r++) {                                      |True |True|False |                        |'{'|'          '|-1|-1
|            radekArr = logArrStr.get(r);                                                  |True |False|True |                        |' '|'get'|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|            for (int s = 0; s < radekArr.size(); s++) {                                   |True |True|False |                        |'{'|'          '|-1|-1
|                hodnota = radekArr.get(s);                                                |True |False|True |                        |''|'get'|-1|-1
|                text = text + hodnota + ""|"";"                                           |True |False|True |                        |' '|'          '|-1|-1
|            }                                                                             |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|            text = text + ""\n"";"                                                        |True |False|True |                        |' '|'          '|-1|-1
|        }                                                                                 |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|        return(text);                                                                     |True |True |True |                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|    private void vytiskniVystup(String text| String adresaProjektuFull){"                 |True |False|False|vytiskniVystup          |'{'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|        try {                                                                             |True |True |False|                        |'{'|'          '|-1|-1
|                FileWriter myWriter = new FileWriter(adresaProjektuFull);                 |True |False|True |                        |' '|'FileWriter'|-1|-1
|                myWriter.write(text);                                                     |True |False|True |                        |' '|'write'|-1|-1
|                myWriter.close();                                                         |True |False|True |                        |' '|'close'|-1|-1
|                System.out.println(""Successfully wrote to the file."");"                 |True |False|True |                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|            } catch (IOException e) {                                                     |True |True|False |                        |'}'|'          '|-1|-1
|                System.out.println(""An error occurred."");"                              |True |False|True |                        |' '|'          '|-1|-1
|                e.printStackTrace();                                                      |True |False|True |                        |' '|'printStackTrace'|-1|-1
|          }                                                                               |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|    }                                                                                     |True |False|False|                        |'}'|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|                                                                                          |True |False|False|                        |' '|'          '|-1|-1
|}                                                                                         |True |False|False|                        |'}'|'          '|-1|-1



