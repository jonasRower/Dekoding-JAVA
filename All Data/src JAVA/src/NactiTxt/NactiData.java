/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package NactiTxt;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class NactiData {
    
    File file;
    ArrayList<String> SeznamRadku;
    String[] SeznamRadkuArr;
    
    private String[] HlavickaTabulky;
    private String[] DatoveTypySloupcu;
    private String[][] DataTabulky;
    
    public NactiData(String NazevTabulky, String CestaKTabulce) throws IOException{
        
        //String CestaKTabulce;
        String PlnaCesta;
        
        //CestaKTabulce = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\DataBase-Zdroje\\";  
        PlnaCesta = CestaKTabulce + NazevTabulky + ".txt"; 
        
        file = new File(PlnaCesta); 
        NactiSoubor();
        PrevedRadkyNaPole prevedData = new PrevedRadkyNaPole(SeznamRadkuArr);
         
        HlavickaTabulky = prevedData.getTabulkaHlavicka();
        DataTabulky = prevedData.getTabulkaData();
        DatoveTypySloupcu = prevedData.getDatoveTypySloupcu();
 
    }
    
    
    //Vrati data
    public String[] getTabulkaHlavicka(){
        return (HlavickaTabulky);
    }
    
    public String[][] getTabulkaData(){
        return (DataTabulky);
    }
    
    public String[] getDatoveTypySloupcu(){
        return (DatoveTypySloupcu);
    }
    
    
    void NactiSoubor() throws FileNotFoundException, IOException
    {
        String st; 
        
        BufferedReader br = new BufferedReader(new FileReader(file)); 
        SeznamRadku = new ArrayList<String>();
        
        while ((st = br.readLine()) != null) 
        {
            SeznamRadku.add(st);
        }
        
        SeznamRadkuArr = new String[SeznamRadku.size()];
        SeznamRadkuArr = SeznamRadku.toArray(SeznamRadkuArr);
        
    }
    
    String[] getSeznamRadku()
    {
        String[] SeznamRadkuArr = new String[SeznamRadku.size()];
        SeznamRadkuArr = SeznamRadku.toArray(SeznamRadkuArr);
        
        return SeznamRadkuArr;
       
    }
    
}
