/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package PridejTabulku;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;


public class CreateTable {
    
    private String[] HlavickaTabulky;
    private String[] DatoveTypySloupcu;
    private String NazevTabulky;
    
    public CreateTable(String[] HlavickaTabulky, String[] DatoveTypySloupcu, String NazevTabulky) throws ClassNotFoundException, SQLException{
      
        this.HlavickaTabulky = HlavickaTabulky;
        this.DatoveTypySloupcu = DatoveTypySloupcu;
        this.NazevTabulky = NazevTabulky;
           
        VytvorDB();
        
    }

    
    private void VytvorDB() throws ClassNotFoundException, SQLException{

        String query;
        
        Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
        Connection conn = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo");
      
        //Creating the Statement object
        Statement stmt = conn.createStatement();
        
        //pripravi query pro vytvoreni tabulky
        query = VytvorQuery();
       
        stmt.execute(query);
        
    }
    
    private String VytvorQuery(){
        
        String radekQuery;
        String SloupecNazev;
        String SloupecDatovyTyp;
        String query;
        
        //prida radek do query s nazvem tabulky
        //radekQuery = "CREATE TABLE STUDENT( ";
        radekQuery = "CREATE TABLE " + NazevTabulky + "( ";
        query = radekQuery;
        
        for (int i = 0; i < HlavickaTabulky.length; i++) {
            
            //prida radek do query s nazvem sloupce a jeho dat. typem
            SloupecNazev = HlavickaTabulky[i];
            SloupecDatovyTyp = DatoveTypySloupcu[i];

            //prida radek do query
            radekQuery = "" + SloupecNazev + " " + SloupecDatovyTyp;
            if (i == HlavickaTabulky.length-1){
                radekQuery = radekQuery + ")";
            } 
            else 
            {
                radekQuery = radekQuery + ",";
            }
                
            query = query + radekQuery;
        
        }
        
        return (query);
        
    }
    
}
