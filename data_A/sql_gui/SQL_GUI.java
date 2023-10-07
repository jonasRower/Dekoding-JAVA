
package sql_gui;

import NactiTxt.NactiData;
import PridejTabulku.CreateTable;
import PridejTabulku.VytvorDB;
import java.io.IOException;
import java.sql.SQLException;

//#########################################################################################################################
//  Na cem dal pracovat
//  1) VytiskniPole - dodelat stejne sirky sloupcu (metoda vratStringTabulky - vraci ruzne sirky sloupcu(resp. jejich radku))
//  2) Vytisknout Pole do TextArea - pri stisku tlacitka v GUI
//  3) Umoznit aby se SQL prikazy zapisovaly z GUI
//  4) Udelat seznam prikladu v SQL
//#########################################################################################################################


//je tam chyba s nazvem souboru, jinak by to melo fungovat
public class SQL_GUI {
    
    public static void main(String args[]) throws IOException, SQLException, ClassNotFoundException {

             
        //PripravDataDoDB DataDoDB = new PripravDataDoDB(); 
        
        //NactiDotazy Dotazy = new NactiDotazy();
        
        //V tride VytvorDB dodelat nacitani vice tabulek
        SQL_GUI_Frame obj = new SQL_GUI_Frame();
        SQL_GUI_Frame.vykresliOkno();
        
        
        //NEVIM PROC TO NEJDE
        //ALE ASI NASTUDOVAT TOTO
        //ShowTables Show = new ShowTables(); 
        
        
        //NactiData Data = new NactiData();
        //CreateTable Create = new CreateTable();
        //pridejRadek NovyRadek = new pridejRadek();
        //Select sel = new Select();
        //VytiskniPole ZobrazPole = new VytiskniPole();
        //Select2 sel2 = new Select2();

        
        //VytvorDB NovaDB = new VytvorDB();
        
        /*
        NactiData Data = new NactiData();
        
        String[] HlavickaTabulky;
        String[] DatoveTypySloupcu;
        String[][] DataTabulky;
    
        HlavickaTabulky = Data.getTabulkaHlavicka();
        DataTabulky = Data.getTabulkaData();
        DatoveTypySloupcu = Data.getDatoveTypySloupcu();
        
        CreateTable Create = new CreateTable(HlavickaTabulky, DatoveTypySloupcu);
        */
        
    }
    
}
