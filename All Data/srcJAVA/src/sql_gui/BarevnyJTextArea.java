
package sql_gui;

import java.awt.Color;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;
//


public class BarevnyJTextArea {
    
    private JTextPane jTextPane3;
    private boolean[][] PoleShody;
    
    private int rPol;
    private int sPol;
    
    private String[] DotazySQL;
    int vyberDotazVlevo;
    
    String[][] DataSelectuNejmensi;
    String[][] DataSelectuStredni;
    
    String[] NazvySloupcu;
    int[] pocetZnakuVeSloupcich;
    
    
    
    //Konstruktor
    BarevnyJTextArea(JTextPane jTextPane1, String[] DotazySQL, int vyberDotazVlevo, boolean[] poleVyberu) throws SQLException, ClassNotFoundException {
        
        this.jTextPane3 = jTextPane1;
        this.DotazySQL = DotazySQL;
        this.vyberDotazVlevo = vyberDotazVlevo;
        
        boolean NejmensiSelect;
        boolean StredniSelect;
        boolean NejvetsiSelect;
        
        boolean zvyraznujPolozky;
        zvyraznujPolozky = false;
        
        NejmensiSelect = poleVyberu[0];
        StredniSelect = poleVyberu[1];
        NejvetsiSelect = poleVyberu[2];
        
        pripravDataSelectu(NejvetsiSelect);
        
        //vykresli barevny text v zavislosti na druhu vyberu
        if (NejmensiSelect == true){
            vratBarevnyText(DataSelectuNejmensi, false);
        }
        if (StredniSelect == true){
            PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);
            vratBarevnyText(DataSelectuStredni, true);
        }
        if (NejvetsiSelect == true){
            //pole se jmenuji stejne jako u stredniho selectu (DataSelectuStredniho obsahuji data nejvetsi)
            PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);
            vratBarevnyText(DataSelectuStredni, true);
        }
        
    }
    
    
    private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{       
        
        String dotazNejmensi;
        String dotazStredni;
        //String dotazNejvetsi;   - zatim nevyuzito
        
        //plati pro dotaz z comboboxu - DotazVpravo
//        if (vyberDotazVlevo > DotazySQL.length){
//            SQL_GUI_Frame.
//        }
        
        dotazNejmensi = DotazySQL[vyberDotazVlevo];
        dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);
        
        //Vytvori Select a pripravi data
        Select selNejmensi = new Select(dotazNejmensi);
        Select selStredni = new Select(dotazStredni);

        //Vrati data ze Selectu
        DataSelectuNejmensi = selNejmensi.getDataSelectu();
        DataSelectuStredni = selStredni.getDataSelectu();
        
        NazvySloupcu = selStredni.getNazvySloupcu();
        pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();
        
        String HlavickaStr;
        HlavickaStr = vratStringHlavicky();
        
    }
    
    
    //pretizeny kontstruktor - zatim docasne
    private boolean[][] vratPoleShody(String[][] DataSelectu1, String[][] DataSelectu2){
        
        String[][] vetsiDataSelectu;
        String[][] mensiDataSelectu;
        boolean[][] poleShody;
        boolean JeDelsiDataSelectu2;
        
        String HodnotaVetsiSelect;
        //String HodnotaMensiSelect;
        
        boolean nalezenaShoda;
        
        //Kontroluje ktere pole je vetsi
        JeDelsiDataSelectu2 = DelsiDataSelectu2(DataSelectu1, DataSelectu2);
        
        if (JeDelsiDataSelectu2 == true){
            vetsiDataSelectu = DataSelectu2;
            mensiDataSelectu = DataSelectu1;
        } else {
            vetsiDataSelectu = DataSelectu1;
            mensiDataSelectu = DataSelectu2;
        }
        
        poleShody = new boolean[vetsiDataSelectu.length][vetsiDataSelectu[0].length];
        
        //prenastavuje polozky na nulu (pro 1. vyhledavani) - pouzito v vratRadekASloupecNalezenePolozkyVPoli
        rPol = 0;
        sPol = 0;
        
        for (int s = 0; s < vetsiDataSelectu[0].length; s++) {       
            for (int r = 0; r < vetsiDataSelectu.length; r++) {
                HodnotaVetsiSelect = vetsiDataSelectu[r][s];
                nalezenaShoda = vratRadekASloupecNalezenePolozkyVPoli(mensiDataSelectu, HodnotaVetsiSelect);
                
                //zapisuje nalezene shody do pole
                poleShody[r][s] = nalezenaShoda;
     
                System.out.println(rPol + "  " + sPol);
            }
        }
        
        //prekontroluje pole shody, protoze nektere polozky mohou byt spatne oznacene
        poleShody = prekontrolujPoleShody(poleShody, mensiDataSelectu, vetsiDataSelectu);
        
        //this.vetsiDataSelectu = vetsiDataSelectu;
        return(poleShody);
        
    }
    
    
    private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){
        
        String[] mensiDataSelectuRadek;
        String[] vetsiDataSelectuRadek;
        String mensiDataSelectuHodnota;
        String vetsiDataSelectuHodnota;
        
        boolean[] poleShodyRadek;
        
        int delkaVetsiDataSelectuRadek;
        int delkaMensiDataSelectuRadek;
        
        //nastavi pole poleShodyNew jako false pro vsechny polozky
        boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];
        for (int r = 0; r < poleShodyNew.length; r++) {
            for (int s = 0; s < poleShodyNew[0].length; s++) {
                poleShodyNew[r][s] = false;
            }
        }      
        
        boolean shodaMVData;
        
        for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {
            //vrati dany radek vetsich Dat Selectu    
            vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);
            delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;
            
            shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se
            
            //vetsi radek porovnava se vsemi radky z mensich dat
            for (int rM = 0; rM < mensiDataSelectu.length; rM++) {
                mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);
                
                //nejdrive porovna jejich delku, zda jsou stejne dlouhe
                delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;
                if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) {
                    
                    //porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji
                    shodaMVData = true;     //defaultni hodnota, ktera se prepise
                    for (int s = 0; s < mensiDataSelectuRadek.length; s++) {

                        vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];
                        mensiDataSelectuHodnota = mensiDataSelectuRadek[s];
                     
                        if (mensiDataSelectuHodnota != null){
                            //pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false
                            //pokud jsou hodnoty stejne, pak shodaMVData zustane true
                            if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false){
                                shodaMVData = false;
                                break;
                            }
                            
                        } else {
                            shodaMVData = false;
                            break;
                        }
                    }
                    
                    //pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans
                    //musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false
                    //preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek
                    if (shodaMVData == true){

                        poleShodyRadek = vratPoleShodyRadek(poleShody, rV);    

                        for (int s = 0; s < poleShody[0].length; s++) {
                            poleShodyNew[rV][s] = poleShodyRadek[s];
                        }
                    } 
                    
                } else {
                    //pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit
                    shodaMVData = false;
                }
            }
        }
        
        return (poleShodyNew);
        
    }
    
    //metoda volana z prekontrolujPoleShody
    private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){
        
        boolean shoda;
        String vetsiDataSelectuHodnota;
        ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();
        String[] radekVetsiDataSelectu;
        
        for (int s = 0; s < vetsiDataSelectu[0].length; s++) {
            shoda = poleShody[radek][s];
            if (shoda == true){
                vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];
                radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);
            }
        }
 
        radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);
        return (radekVetsiDataSelectu);
        
    }
    
    //metoda volana z prekontrolujPoleShody
    private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){
        
        int pocetSloupcu;
    
        pocetSloupcu = mensiDataSelectu[0].length;
        String[] radekMensiDataSelectu = new String[pocetSloupcu];
        
        for (int s = 0; s < pocetSloupcu; s++) {
            radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];
        }
        
        return (radekMensiDataSelectu);
        
    }
          
    //metoda volana z prekontrolujPoleShody
    private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){
        
        int pocetSloupcu;
        
        pocetSloupcu = poleShody[0].length;
        boolean[] radekPoleShody = new boolean[pocetSloupcu];
        
         for (int s = 0; s < pocetSloupcu; s++) {
            radekPoleShody[s] = poleShody[radek][s];
        }
         
        return (radekPoleShody);
        
    }
    
    
    
    
    
    
    
    private void prekontrolujPoleShody2(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){
        
        String[] mensiDataSelectuRadek;
        String[] vetsiDataSelectuRadek;

        mensiDataSelectuRadek = new String[5];
        vetsiDataSelectuRadek = new String[5];
        
        String mensiDataSelectuHodnota;
        String mensiDataSelectuHodnota0;    //hodnota z 0-teho sloupce
        String vetsiDataSelectHodnota;
        String vetsiDataSelectHodnota0;     //hodnota z 0-teho sloupce
        
       
        boolean shoda;
        boolean shoda0;                     //shoda z 0-teho sloupce
        boolean shodnyRadek;
        boolean shodnyRadekNalezen;
        int posledniRV = 0;
        
        //index rM udava cislo radku mensiDataSelectu
        for (int rM = 0; rM < mensiDataSelectu.length; rM++) {
            mensiDataSelectuHodnota0 = mensiDataSelectu[rM][0];
 
            //vychozi hodnota, ktera se prepisuje
            shodnyRadekNalezen = false;
            
            //index rV udava cislo radku vetsiDataSelectu
            for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {
                
                //vychozi hodnota, ktera se prepisuje
                shodnyRadek = true;
                
                //v okamziku, kdy shodny radek byl jiz nalezen
                if (shodnyRadekNalezen == true){
                    break;
                }
               
                //vyhledava, kde je shoda == true v 0-tem sloupci
                shoda0 = poleShody[rV][0];
                if (shoda0 == true){
                    
                    //pokud je shoda v 0-tem sloupci, 
                    //pak porovna hodnotu mensiDataSelectu a vetsiDataSelectu
                    //ve sloupci 0
                    
                    vetsiDataSelectHodnota0 = vetsiDataSelectu[rV][0];
                    if (mensiDataSelectuHodnota0.equals(vetsiDataSelectHodnota0) == true){
                        //pokud hodnoty mensiho a vetsiho Selectu
                        //jsou stejne - uvazovane pro stejny sloupec, ale jiny radek
                        //pak se porovnaji hodnoty i pro ostatni sloupce
                        
                        for (int s = 1; s < mensiDataSelectu[0].length; s++) {
                            mensiDataSelectuHodnota = mensiDataSelectu[rM][s];
                            vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];
                            
                            if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false){
                                //pokud nejaka hodnota neni stejna (z nejakeho sloupce),
                                //pak se nastavi na false a dal uz se nepokracuje
                                shodnyRadek = false;
                                break;
                            }
                        }
                        
                    } else {
                        shodnyRadek = false;
                    }
                    
                } else {
                    //(shoda0 == false) 
                    //shodnyRadek = false muze nabit hodnoty(false) vicero zpusoby
                    shodnyRadek = false;
                }
                
                
                if (shodnyRadek == true){
                    shodnyRadekNalezen = true;
                    posledniRV = rV + 1;
                }
                
                if (shodnyRadek == false){
                    for (int s = 0; s < poleShody[0].length; s++) {
                        poleShody[rV][s] = false;
                    }
                }
                
           
//                for (int s = 0; s < mensiDataSelectu[0].length; s++) {
//                    mensiDataSelectuHodnota = mensiDataSelectu[rM][s];
//                
//                
//                    shoda = poleShody[rV][s];
//                    if (shoda == true){
//                        vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];
//                        if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false) {
//                      //  if (mensiDataSelectuHodnota != vetsiDataSelectHodnota){
//                            shodnyRadek = false;
//                            break;
//                        }
//                    }
//                }
            }
            
//            int d = poleShody[0].length;

            //nejedna-li se o shodny radek 
            //tzn. radek mensiDataSelectu != radku vetsiDataSelectu
            //pak prepise vsechny true na danem radku na false
            //(to je taky cilem opravy, jelikoz v puvodnim poleShody tomu tak nemusi byt)
//            if (shodnyRadek == false){
//                for (int s = 0; s < poleShody[0].length; s++) {
//                    poleShody[r][s] = false;
//                }
//            }
//            d = poleShody[0].length;
        }
    }
    
    
    public JTextPane getBarevnyText(){
    //public JScrollPane getBarevnyText(){    
        //return (jTextPane1);
        //return (jTextPane2);
        return (jTextPane3);
    }
    
    
    private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka){
        
        String polozkaPole;
        boolean nalezenaShoda = false;
        
        if (HledanaPolozka != null){
        
            for (int s = 0; s < Pole[0].length; s++) {
                if(nalezenaShoda == true){
                    break;
                }
                
                for (int r = 0; r < Pole.length; r++) {
                    polozkaPole = Pole[r][s];
                    
                    if (polozkaPole != null){
                        
                        if (polozkaPole.equals(HledanaPolozka) == true){
                            rPol = r;
                            sPol = s;
                            nalezenaShoda = true;
                            break;
                        }
                        
                    }
                }
            }
        }
        
        return (nalezenaShoda);

    }
    
            
    private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2){
        //obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty
        //metoda zjisti ve kterem poli je vice null
        
        int pocetNullDataSelectu1;
        int pocetNullDataSelectu2;
        
        boolean jeDelsiDataSelectu2;
        
        pocetNullDataSelectu1 = 0;
        pocetNullDataSelectu2 = 0;
        
        for (int i = 0; i < DataSelectu1.length; i++) {
            
            if (DataSelectu1[i] == null){
                pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;
            }
            if (DataSelectu2[i] == null){
                pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;
            }
            
        }
        
        if (pocetNullDataSelectu2 > pocetNullDataSelectu1){
            jeDelsiDataSelectu2 = true;
        } else {
            jeDelsiDataSelectu2 = false;
        }
        
        return (jeDelsiDataSelectu2);
        
    }
    
    
     private String vratStringHlavicky(){
      
        String NazevSloupce;
        String HlavickaStr;
        int pocetZnakuVeSloupci;
        String ZbyvajiciMezery;
        
        HlavickaStr = "";
        
        for (int s = 1; s <= NazvySloupcu.length; s++) {
            NazevSloupce = NazvySloupcu[s-1];
            pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s-1];
            
            ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, NazevSloupce);
            HlavickaStr = HlavickaStr + "  " + ZbyvajiciMezery;
            
        }
        
        return(HlavickaStr);
    }
     
     
    private String doplnZbyvajiciMezery(int pocetZnakuSloupce, String Hodnota)
    {
        String ZbyvajiciMezery;
        int pocetZnakuMezer;
        
        if (Hodnota != null){
               
            pocetZnakuMezer = pocetZnakuSloupce - Hodnota.length();
            ZbyvajiciMezery = Hodnota;

            //doplni retezec o mezery
            for (int i = 0; i < pocetZnakuMezer; i++) {
                 ZbyvajiciMezery = ZbyvajiciMezery + " "; 
            }
        
        } 
        else
        {
            ZbyvajiciMezery = "";
        }    
        
        return (ZbyvajiciMezery);
        
    }
     
     
    private int[] vratPocetZnakuProVsechnySloupce()
    {
        int pocetSloupcu;
        pocetSloupcu = NazvySloupcu.length;
        int pocetZnaku;
        int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];
        
        for (int s = 0; s < pocetSloupcu; s++){
            pocetZnaku = vratPocetZnakuProDanySloupec(s);
            pocetZnakuVeSloupcich[s] = pocetZnaku;
        }
        
        return (pocetZnakuVeSloupcich);
    }
     
     
    private int vratPocetZnakuProDanySloupec(int sloupec)
    { //vrati pole s poctem znaku v jednotlivych sloupcich
      //to proto aby sloupce krasne zarovnal   
    
        String Hodnota;
        int nejvicPocetZnakuHodnoty;
        int pocetZnakuHodnoty;
        
        //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce
        nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();
        
        for (int r = 1; r < DataSelectuStredni.length; r++) {
            Hodnota = DataSelectuStredni[r][sloupec];
            if (Hodnota != null)
            {
                pocetZnakuHodnoty = Hodnota.length();
                if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){
                    nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;
                }
            }
        }
        
        return nejvicPocetZnakuHodnoty;
        
    }
    
            
    
    private void vratBarevnyText(String[][] DataSelectu, boolean zvyraznujPolozky){
        
        String hodnota;
        String mezera;
        String hodnotaM;
        int delkaDoc;
        boolean shoda;
        
        String ZbyvajiciMezery;
        int pocetZnakuVeSloupci;
        
        //StyledDocument doc = jTextPane2.getStyledDocument();
        StyledDocument doc = jTextPane3.getStyledDocument();
        
        SimpleAttributeSet keyWord = new SimpleAttributeSet();
        StyleConstants.setForeground(keyWord, Color.RED);
        
        hodnota = "xxx";
        mezera = "  ";
        hodnotaM = "";
        
        delkaDoc = 0;
        
        try
        {
            //jTextPane2.setText(""); 
            jTextPane3.setText("                                                                                                                           \n"); 
            
            //doc.insertString(0, "<html>                                             </html>", keyWord );
            
            //index r = -1 plati pro hlavicku
            for (int r = -1; r < DataSelectu.length; r++) { 
             
                for (int s = 0; s < DataSelectu[0].length; s++) {    
                    
                    if (r == -1){
                    //jedna se o hlavicku    
                        shoda = false;
                        hodnota = NazvySloupcu[s];
                    } else {
                    //jedna se o tabulku    
                       
                        //Zvyraznuje polozky jeb v pripade, pokud zvyraznujPolozky == true
                        if (zvyraznujPolozky == true){
                            shoda = PoleShody[r][s];
                        } else {
                            shoda = false;
                        }
                        
                        hodnota = DataSelectu[r][s];
                    }
                    
                    delkaDoc = doc.getLength();

                    pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s];
                    ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, hodnota);

                    hodnotaM = ZbyvajiciMezery + "   ";
    
                    //oznaci danou bunku v zavislosti na tom, zda nalezl shodu ci nikoliv
                    if (shoda == true){
                        doc.insertString(doc.getLength(), hodnotaM, keyWord );
                    } else {
                        doc.insertString(doc.getLength(), hodnotaM, null );
                    }
                }  
                
                if (r == -1){
                    //za hlavicku vlozi prazdny radek + novy rasek   
                    doc.insertString(doc.getLength(), "\n\n", null );
                } else {
                    //janak vklada pouze novy radek
                    doc.insertString(doc.getLength(), "\n", null );
                }
            }
        }
        
        catch(Exception e) { System.out.println(e); }
        
    }
    
    
    //pokud je NejvetsiDotaz = true, pak vraci nejvetsi dotaz, jinak stredni dotaz
    public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)
    {
        
        
        //String originalniSelect;    //napr.          Select * FROM ... WHERE ...
        String plnySelect;            //z toho vychazi Select * FROM 
       
        String castZaFrom;
        String castPredFrom;
        String NazevTabulky;
        String[] castZaFromArr;
        String[] stringArr;
        int indexOfFROM;
        
        indexOfFROM = originalniSelect.indexOf("FROM");
        castZaFrom = originalniSelect.substring(indexOfFROM);
        
        if (NejvetsiDotaz == true){
            castPredFrom = "SELECT * ";
        } else {
            castPredFrom = originalniSelect.substring(0, indexOfFROM);
        }
       
        castZaFromArr = castZaFrom.split(" ");
        NazevTabulky = castZaFromArr[1];
        stringArr = NazevTabulky.split("\n");
        if (stringArr.length > 0)
        {
            NazevTabulky = stringArr[0];
        }
        
        plnySelect = castPredFrom + "FROM " + NazevTabulky;
        
        
        return(plnySelect);
                
    }
    
    
    
    
    
    
    
    
    
    
    
    
    //nepotrebne
    
    private void vratBarevnyText2(){
        
        //jTextPane2.setText( "original text" );
        jTextPane3.setText( "original text" );
        //StyledDocument doc = jTextPane2.getStyledDocument();
        StyledDocument doc = jTextPane3.getStyledDocument();

        //  Define a keyword attribute

        SimpleAttributeSet keyWord = new SimpleAttributeSet();
        StyleConstants.setForeground(keyWord, Color.RED);
        StyleConstants.setBackground(keyWord, Color.YELLOW);
        StyleConstants.setBold(keyWord, true);

        //  Add some text
        try
        {
            doc.insertString(0, "Start of text\n", null );
            doc.insertString(doc.getLength(), "\nEnd of text", keyWord );
        }
        catch(Exception e) { System.out.println(e); }
       

    }

}
