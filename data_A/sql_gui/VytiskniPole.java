
package sql_gui;

import java.sql.SQLException;


public class VytiskniPole {
    
    private String[][] DataSelectu;
    private String[] NazvySloupcu;
    
    int[] pocetZnakuVeSloupcich;
    private String DataTabulky;

    
    
    VytiskniPole(String[] NazvySloupcu, String[][] DataSelectu) throws SQLException, ClassNotFoundException
    {
        
        this.NazvySloupcu = NazvySloupcu;
        this.DataSelectu = DataSelectu;
        
        if (NazvySloupcu != null)
        {
            pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();

            String HlavickaStr;

            HlavickaStr = vratStringHlavicky();
            DataTabulky = vratStringTabulky(HlavickaStr);
        }
    }
    
    
    
    public String getDataTabulky(){
        return (DataTabulky);
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
    
    
    private String vratStringTabulky(String HlavickaStr)
    {
        String HodnotaTabulky;
        String RadekTabulky;
        String DataTabulky;
        
        String ZbyvajiciMezery;
        int pocetZnakuVeSloupci;
        
        DataTabulky = HlavickaStr + "\n";
        
        for (int r = 1; r < DataSelectu.length; r++) {
            //RadekTabulky = DataSelectu[r][0];
            RadekTabulky = "";
            
            for (int s = 1; s <= NazvySloupcu.length; s++) {
                HodnotaTabulky = DataSelectu[r][s-1];
                pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s-1];
                ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, HodnotaTabulky);
                
                RadekTabulky = RadekTabulky + "  " + ZbyvajiciMezery;
                
            }
            System.out.println(RadekTabulky);
            DataTabulky = DataTabulky + "\n" + RadekTabulky;
        }
        
        return (DataTabulky);
        
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
        
        for (int r = 1; r < DataSelectu.length; r++) {
            Hodnota = DataSelectu[r][sloupec];
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
    
    
            
    
}
