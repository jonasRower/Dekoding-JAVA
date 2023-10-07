/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package NactiTxt;

/**
 *
 * @author jonas
 */
public class PrevedRadkyNaPole {
//prevede pole s jednim loupcem na vice sloupcu    
    
    private String[][] DataVeViceSloupcich;
    private String[] radekSHlavickouPole;
    private String[] DatoveTypySloupcu;
    
    PrevedRadkyNaPole(String[] PoleVJednomSloupci){
        
        String radekPouzeSHlavickou;
        int pocetSloupcu;
        
        radekPouzeSHlavickou = VratRadekSHlavickou(PoleVJednomSloupci);
        radekSHlavickouPole = RozdelRadekDoPole(radekPouzeSHlavickou);
        pocetSloupcu = radekSHlavickouPole.length;
        
        DataVeViceSloupcich = VratDataVeViceSloupcich(pocetSloupcu, PoleVJednomSloupci);
        DatoveTypySloupcu = vratDatoveTypy();
        
    }
    
    //Vrati data
    public String[] getTabulkaHlavicka(){
        return (radekSHlavickouPole);
    }
    
    public String[][] getTabulkaData(){
        return (DataVeViceSloupcich);
    }
    
    public String[] getDatoveTypySloupcu(){
        return (DatoveTypySloupcu);
    }
    
    
    private String VratRadekSHlavickou(String[] PoleVJednomSloupci){
        
       String radekSHlavickou; 
       radekSHlavickou = PoleVJednomSloupci[0];
       
       return(radekSHlavickou);
        
    }
    
    private String[] RozdelRadekDoPole(String radekSHlavickou){
        
        String[] radekPole;
        radekPole = radekSHlavickou.split("\\|");    
        
        //Odmaze z jednotlivych polozek mezery na koncich stringu
        for (int i = 0; i < radekPole.length; i++) {
            radekPole[i] = radekPole[i].trim();
        }
        
        return(radekPole);
                
    }
    
    private String[][] VratDataVeViceSloupcich(int pocetSloupcu, String[] PoleVJednomSloupci){
        
        String Radek;
        int pocetRadku;
        
        String[][] DataVeViceSloupcich;
        String[] radekPole;
        
        pocetRadku = PoleVJednomSloupci.length - 2;
        DataVeViceSloupcich = new String[pocetRadku][pocetSloupcu];
        
        for (int r = 0; r < pocetRadku; r++) {
            Radek = PoleVJednomSloupci[r+2];
            radekPole = RozdelRadekDoPole(Radek);
            
            for (int s = 0; s < radekPole.length; s++) {
                DataVeViceSloupcich[r][s] = radekPole[s];
            }
        }
        
        return(DataVeViceSloupcich);
        
    }
    
    //vrati pole datovych typu
    
    private String[] vratDatoveTypy()
    {
        int pocetSloupcu;
        boolean datovyTypSloupceCislo;
        boolean datovyTypSloupceInteger;
        
        pocetSloupcu = radekSHlavickouPole.length;
        String[] DatoveTypySloupcu = new String[pocetSloupcu];
        
        for (int sloupec = 0; sloupec < pocetSloupcu; sloupec++) {
            datovyTypSloupceCislo = jeDatovyTypSloupceCislo(sloupec);
            if (datovyTypSloupceCislo == true)
            {
                datovyTypSloupceInteger = jeDatovyTypSloupceInteger(sloupec);
                if (datovyTypSloupceInteger == true){
                    DatoveTypySloupcu[sloupec] = "INT";
                } 
                else
                {
                    DatoveTypySloupcu[sloupec] = "DOUBLE";
                }
            } 
            else
            {
                DatoveTypySloupcu[sloupec] = "VARCHAR(255)";
            }
        }
        
        return (DatoveTypySloupcu);
        
    }
    
    private boolean jeDatovyTypSloupceCislo(int sloupec)
    {
        String HodnotaVeSloupci;
        int pocetRadku;
        
        boolean jeHodnotaCislo;
        boolean jeSloupecCislo;
        
        pocetRadku = radekSHlavickouPole.length;
        jeSloupecCislo = true;
        
        for (int r = 0; r < pocetRadku; r++) {
            HodnotaVeSloupci = DataVeViceSloupcich[r][sloupec];
            jeHodnotaCislo = isNumeric(HodnotaVeSloupci);
            if (jeHodnotaCislo == false){
                jeSloupecCislo = false;
                break;
            }
        }
        
        return jeSloupecCislo;
    }
    
    private boolean jeDatovyTypSloupceInteger(int sloupec)
    {    
        String HodnotaVeSloupci;
        int pocetRadku;
        
        boolean jeHodnotaCislo;
        boolean jeSloupecInteger;
        
        pocetRadku = radekSHlavickouPole.length;
        jeSloupecInteger = true;
        
        for (int r = 0; r < pocetRadku; r++) {
            HodnotaVeSloupci = DataVeViceSloupcich[r][sloupec];
            if(HodnotaVeSloupci.contains(".") == true){
                jeSloupecInteger = false;
                break;
            }
        }   
        return jeSloupecInteger;
    }
    
    
    private boolean isNumeric(String strNum) {
    if (strNum == null) {
        return false;
    }
    try {
        double d = Double.parseDouble(strNum);
    } catch (NumberFormatException nfe) {
        return false;
    }
    return true;
     }       
}
