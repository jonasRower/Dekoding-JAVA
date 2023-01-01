
package sql_gui;

import NactiTxt.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class NactiDotazy {
    
    
    ArrayList<String> SeznamRadku;
    
    private String[] HlavickaTabulky;
    private String[] DatoveTypySloupcu;
    private String[][] DataTabulky;
    
    private String[] DotazySQL = null;
    private String[] DotazyPopis = null;
    
    private String[] DotazySQLVlevo;
    private String[] DotazyPopisVlevo;
    private String[] DotazySQLVpravo;
    private String[] DotazyPopisVpravo;
    
    private int[] cislaPopisuVlevo;
    private int[][] cislaPopisuVPravo;
    
    private String[][] SubDotazySQL = new String[5][10];
    private String[][] SubDotazyPopis = new String[5][10];
    
    int[][]cislaPopisuVPravo2D;
    String[][] DotazySQLVpravo2D;
    String[][] DotazyPopisVpravo2D;
    
    
    
    public NactiDotazy() throws IOException{
        
        String Adresa;
        String ZdrojDotazuVlevo;
        String ZdrojDotazuVpravo;
        
        Adresa = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\EXAMPLES-w3resource\\";
        ZdrojDotazuVlevo = "RetrieveDataFromTablesCZ.txt";
        ZdrojDotazuVpravo = "RetrieveDataFromTablesCZvpravo.txt";
        
        //Provizorne naplnuji pole
        SubDotazyPopis[0][0] = "SubDotazyPopis[0][0]";
        SubDotazyPopis[0][1] = "SubDotazyPopis[0][1]";
        SubDotazyPopis[0][2] = "SubDotazyPopis[0][2]";
        
        SubDotazyPopis[1][0] = "SubDotazyPopis[1][0]";
        SubDotazyPopis[1][1] = "SubDotazyPopis[1][1]";
        SubDotazyPopis[1][2] = "SubDotazyPopis[1][2]";
        
        SubDotazyPopis[2][0] = "SubDotazyPopis[2][0]";
        SubDotazyPopis[2][1] = "SubDotazyPopis[2][1]";
        SubDotazyPopis[2][2] = "SubDotazyPopis[2][2]";
        
        
        //Provizorne naplnuji pole
        SubDotazySQL[0][0] = "SELECT name,city\n FROM salesman";
        SubDotazySQL[0][1] = "SELECT winner\n FROM nobel_win";
        SubDotazySQL[0][2] = "SELECT pro_name, pro_price FROM item_mast";
        
        SubDotazySQL[1][0] = "SELECT name,city\n FROM salesman";
        SubDotazySQL[1][1] = "SELECT winner\n FROM nobel_win";
        SubDotazySQL[1][2] = "SELECT pro_name, pro_price FROM item_mast";
        
        SubDotazySQL[2][0] = "SELECT name,city\n FROM salesman";
        SubDotazySQL[2][1] = "SELECT winner\n FROM nobel_win";
        SubDotazySQL[2][2] = "SELECT pro_name, pro_price FROM item_mast";

        //Ziska data vlevo
        vratSQLDotazy(Adresa, ZdrojDotazuVlevo); 
        DotazySQLVlevo = DotazySQL;
        DotazyPopisVlevo = DotazyPopis;
        cislaPopisuVlevo = oddelCisloDotazuOdTextuVlevo();
        
        //Ziska data vpravo
        vratSQLDotazy(Adresa, ZdrojDotazuVpravo); 
        DotazySQLVpravo = DotazySQL;
        DotazyPopisVpravo = DotazyPopis;
        cislaPopisuVPravo = oddelCisloDotazuOdTextuVpravo();
        
        preusporadejDataVPravoDo2D();
        
        

    }
    
    
    public String[] getDotazySQL()
    {
        return(DotazySQLVlevo);
    }
    
    public String[] getDotazyPopis()
    {
        return(DotazyPopisVlevo);
    }  
    
//    public int[] getCislaPopisu()
//    {
//        return(cislaPopisu);
//    }        
    
    public String[][] getSubDotazySQL()
    {
        return(DotazySQLVpravo2D);
       // return(SubDotazySQL);
    }  
    
    public String[][] getSubDotazyPopis()
    {
        return(DotazyPopisVpravo2D);
        //return(SubDotazyPopis);
    } 
    
    private void preusporadejDataVPravoDo2D()
    {
        int popis1;
        int popis1Predchozi;
        int popis2;
        
        int radek;
        int sloupec;
        
        String DotazSQLVPravo;
        String DotazPopisVpravo;
        
        cislaPopisuVPravo2D = new int[cislaPopisuVlevo.length][10];
        DotazySQLVpravo2D = new String[DotazySQLVpravo.length][10];
        DotazyPopisVpravo2D = new String[DotazyPopisVpravo.length][10];
        popis1Predchozi = 0;
        
        radek = -1;
        sloupec = 0;
        
        for (int r = 0; r < cislaPopisuVPravo.length; r++) {
            popis1 = cislaPopisuVPravo[r][0];
            popis2 = cislaPopisuVPravo[r][1];
            
            DotazSQLVPravo = DotazySQLVpravo[r];
            DotazPopisVpravo = DotazyPopisVpravo[r];
            
            if (popis1 != popis1Predchozi){
                radek = radek + 1;
                sloupec = 1;
                cislaPopisuVPravo2D[radek][0] = popis1;
                cislaPopisuVPravo2D[radek][sloupec] = popis2;
                
                DotazySQLVpravo2D[radek][0] = "" + popis1;
                DotazySQLVpravo2D[radek][sloupec] = DotazSQLVPravo;
                
                DotazyPopisVpravo2D[radek][0] = "" + popis1;
                DotazyPopisVpravo2D[radek][sloupec] = DotazPopisVpravo;
                
                popis1Predchozi = popis1;
                
            } else {
                sloupec = sloupec + 1;
                
                cislaPopisuVPravo2D[radek][sloupec] = popis2;
                DotazySQLVpravo2D[radek][sloupec] = DotazSQLVPravo;
                DotazyPopisVpravo2D[radek][sloupec] = DotazPopisVpravo;
                
            }
            
           
        }
        
    }
    
    void vratSQLDotazy(String Adresa, String NazevSouboru) throws IOException
    {

        String Radek;
        String PrvniZnak = null;
        boolean jePrvniZnakCislo = false;
        String Dotaz = null;
        
        String[] SeznamRadkuArr;
        
        int prvniRadekDotazu;
        int posledniRadekDotazu;
        String PlnaCesta;
        
        PlnaCesta = Adresa + NazevSouboru;
        SeznamRadkuArr = NactiSoubor(PlnaCesta);
        
        ArrayList<String> DotazyPopisList = new ArrayList<String>();
        ArrayList<String> DotazySQLList = new ArrayList<String>();
        
        for (int i = 0; i < SeznamRadkuArr.length; i++) {
            
            Radek = SeznamRadkuArr[i];
            
            if (Radek.isEmpty() == false)
            {
                PrvniZnak = Radek.substring(0, 1);
                jePrvniZnakCislo = isNumeric(PrvniZnak);
                //Dotaz = "";
                
                if (jePrvniZnakCislo == true)
                {
                    
                    DotazyPopisList.add(Radek);
                    prvniRadekDotazu = i + 1;
                    posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);
                    Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);
                    
                    DotazySQLList.add(Dotaz);
                    
                }
            }
        }
        
        //Prekonvertuje na pole Stringu
        DotazyPopis = new String[DotazyPopisList.size()]; 
        DotazyPopis = DotazyPopisList.toArray(DotazyPopis); 
        
        //Prekonvertuje na pole Stringu
        DotazySQL = new String[DotazySQLList.size()]; 
        DotazySQL = DotazySQLList.toArray(DotazySQL); 
        
           
    }
    
    
    String[] NactiSoubor(String PlnaCesta) throws FileNotFoundException, IOException
    {
        String st; 
        String[] SeznamRadkuArr;
        File file;
        
        file = new File(PlnaCesta); 
        
        BufferedReader br = new BufferedReader(new FileReader(file)); 
        SeznamRadku = new ArrayList<String>();
        
        while ((st = br.readLine()) != null) 
        {
            SeznamRadku.add(st);
        }
        
        SeznamRadkuArr = new String[SeznamRadku.size()];
        SeznamRadkuArr = SeznamRadku.toArray(SeznamRadkuArr);
        
        return (SeznamRadkuArr);
        
        
    }
    
    private int[] oddelCisloDotazuOdTextuVlevo(){
        
        String CisloStr;
        int CisloInt = 0;
        String[] stringArr;
        int[] cislaPopisu;
        String DotazPopis;
        
        //Oddeli cislo dotazu od textu dotazu
        cislaPopisu = new int[DotazyPopisVlevo.length];
        for (int i = 0; i < cislaPopisu.length; i++) { 
            DotazPopis = DotazyPopisVlevo[i];
            
            stringArr = DotazPopis.split("\\.");
            CisloStr = stringArr[0];
            if (isNumeric(CisloStr) == true){
                CisloInt = Integer.parseInt(CisloStr);
            }
            
            cislaPopisu[i] = CisloInt;
        }
        
        return (cislaPopisu);
        
    }
    
    
    private int[][] oddelCisloDotazuOdTextuVpravo(){  
        
        String CisloStr1;
        String CisloStr2;
        int CisloInt1 = 0;
        int CisloInt2 = 0;
        
        String[] stringArr;
        int[][] cislaPopisu;
        String DotazPopis;
        
        cislaPopisu = new int[DotazyPopisVpravo.length][2];
        for (int i = 0; i < cislaPopisu.length; i++) { 
            DotazPopis = DotazyPopisVpravo[i];
            
            stringArr = DotazPopis.split("\\.");
            CisloStr1 = stringArr[0];
            CisloStr2 = stringArr[1];
            
            if (isNumeric(CisloStr1) == true){
                CisloInt1 = Integer.parseInt(CisloStr1);
            }
            if (isNumeric(CisloStr2) == true){
                CisloInt2 = Integer.parseInt(CisloStr2);
            }
            
            cislaPopisu[i][0] = CisloInt1;
            cislaPopisu[i][1] = CisloInt2;
            System.out.println("");
        }
        
        return (cislaPopisu);
    }
            

    private int vratPosledniRadekDotazu(int prvniRadekDotazu, String[] SeznamRadkuArr)
    {
        String Radek = null;
        int PosledniZnakASCII = 0;
        int posledniRadekDotazu = 0;
        int[] poleASCII = null;
        
        for (int i = prvniRadekDotazu; i < SeznamRadkuArr.length; i++) 
        {
            Radek = SeznamRadkuArr[i];
            Radek = Radek.trim();
            if (Radek.isEmpty() == false)
            {
                poleASCII = vratPoleASCII(Radek);
                PosledniZnakASCII = poleASCII[poleASCII.length-1];
                if (PosledniZnakASCII == 59)
                {
                    posledniRadekDotazu = i;
                    break;
                }
            } 
        }
        
        return posledniRadekDotazu;
    }
    
        public int[] vratPoleASCII(String str) {
        int[] ASCII = new int[str.length()];
        for (int i = 0; i < ASCII.length; i++) {
            ASCII[i] = str.charAt(i);
        }
        return (ASCII);
    }
        
        
    private String vratStringDotazu(int prvniRadek, int posledniRadek, String[] SeznamRadkuArr)
    {
        String CelyDotaz;
        String DotazRadek;
        CelyDotaz = "";
        
        for (int i = prvniRadek; i <= posledniRadek; i++) 
        {
            DotazRadek = SeznamRadkuArr[i];
            CelyDotaz = CelyDotaz + DotazRadek + "\n";
            
        }   
        
        return(CelyDotaz);
    }
    
    
    private boolean isNumeric(String str) 
    { 
        try 
        {  
            Double.parseDouble(str);  
            return true;
        } catch(NumberFormatException e){  
            return false;  
        }  
    } 
}
            
            
            
    
    
    
    

