/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package PridejTabulku;

import NactiTxt.NactiData;
import java.io.IOException;
import static java.lang.reflect.Array.set;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;


public final class VytvorDB {
    
    private String[] HlavickaTabulky;
    private String[] DatoveTypySloupcu;
    private String[][] DataTabulky;
    
    public VytvorDB() throws IOException, ClassNotFoundException, SQLException{
        
        String QueryCreateTable;
        String AdresaKTabulce;
        
        String NazvyTabulek[];
        String NazevTabulky;
        
        
        //Dropne vsechny tabulky
        DropTable Drop = new DropTable();
        
        AdresaKTabulce = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\DataBase-Zdroje\\";
        
        //Pripravi seznam tabulek podle nazvu txt ve slozce
        NazvyTabulek = SeznamTabulekZTxt(AdresaKTabulce);
        
        //Vytvori jednotlive tabulky
        for (int i = 0; i < NazvyTabulek.length; i++) {
            NazevTabulky = NazvyTabulek[i];
            PridejTabulkuDoDB(AdresaKTabulce, NazevTabulky);
        }
    
    }
    
    private void PridejTabulkuDoDB(String AdresaKTabulce, String NazevTabulky) throws SQLException, ClassNotFoundException, IOException
    {
        
        //nacte data z txt
        NactiData Data = new NactiData(NazevTabulky, AdresaKTabulce);
        
        HlavickaTabulky = Data.getTabulkaHlavicka();
        DataTabulky = Data.getTabulkaData();
        DatoveTypySloupcu = Data.getDatoveTypySloupcu();
        
        //Dropne vsechny jiz existujici tabulky
        //DropTable Drop = new DropTable();
        
        //vytvori tabulku v DB
        CreateTable VytvorTabulku = new CreateTable(HlavickaTabulky, DatoveTypySloupcu, NazevTabulky);
        
        //vlozi vsechny radky do tabulky
        pridejRadek vsechnyNoveRadky = new pridejRadek(NazevTabulky,DatoveTypySloupcu, DataTabulky, HlavickaTabulky);
        
    }
    
    private String[] SeznamTabulekZTxt(String AdresaKTabulce) throws IOException {
        
        String ObsahSlozky[];
        String NazevSouboru;
        String NazevTabulky = null;
        int indexOfPripony;
        
        ObsahSlozky = VratObsahSlozky(AdresaKTabulce);
        
        ArrayList<String> NazvyTabulek = new ArrayList<String>();
        
        //Jen ty soubory s priponou txt vypise jako Tabulky
        for (int i = 0; i < ObsahSlozky.length; i++) {
            NazevSouboru = ObsahSlozky[i];
            indexOfPripony = NazevSouboru.indexOf(".txt");
            if (indexOfPripony > -1)
            {
                NazevTabulky = NazevSouboru.substring(0, indexOfPripony);
                NazvyTabulek.add(NazevTabulky);
            }
        }
        
        //Preverde ArrayList na pole
        String[] NazvyTabulekArr = new String[NazvyTabulek.size()]; 
        NazvyTabulekArr = NazvyTabulek.toArray(NazvyTabulekArr); 
        
        return NazvyTabulekArr;
        
    }
    
    
    private String[] VratObsahSlozky(String dir) throws IOException {
        Set<String> fileList = new HashSet<>();
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get(dir))) {
            for (Path path : stream) {
                if (!Files.isDirectory(path)) {
                    fileList.add(path.getFileName()
                        .toString());
                }
            }
        }

        String[] myArray = new String[fileList.size()];
        fileList.toArray(myArray);
    
        return myArray;
    }
    
   
    
    
}
