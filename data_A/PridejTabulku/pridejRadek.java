/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package PridejTabulku;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;


class pridejRadek {
    
    private String[] HlavickaTabulky;
    private String[] DatoveTypySloupcu;
    private String[][] DataTabulky;
    
    
    pridejRadek(String NazevTabulky, String[] DatoveTypySloupcu, String[][] DataTabulky, String[] HlavickaTabulky) throws SQLException{
        
        this.HlavickaTabulky = HlavickaTabulky;
        this.DatoveTypySloupcu = DatoveTypySloupcu;
        this.DataTabulky = DataTabulky;
        
        pridejJednotliveRadky(NazevTabulky);
        
    }
        
    private void pridejJednotliveRadky(String NazevTabulky) throws SQLException{  
        
        String datovyTyp;
        String hodnota;
        String StrPrepareStatement;
        
        StrPrepareStatement = vratPrepareStatementString(NazevTabulky);
        
        Connection con = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo");
        PreparedStatement st = con.prepareStatement(StrPrepareStatement);
        
        //prida jednotlive radky
        for (int r = 0; r < DataTabulky.length; r++) {
            
            //prida hodnoty do kazdeho radku
            for (int i = 0; i < DatoveTypySloupcu.length; i++) {

                datovyTyp = DatoveTypySloupcu[i];
                hodnota = DataTabulky[r][i];

                
                try{
                    
                
                //if (hodnota != ""){
                    if (datovyTyp=="INT") 
                    {
                        st.setInt(i+1,Integer.parseInt(hodnota));
                        System.out.println("setInt(" + (i+1) + "," + hodnota + ")");
                    }
                    else 
                    {
                        if (datovyTyp=="DOUBLE") 
                        {
                            st.setDouble(i+1, Double.parseDouble(hodnota));
                            System.out.println("setDouble(" + (i+1) + "," + hodnota + ")");
                        }
                        else
                        {
                            st.setString(i+1, hodnota);
                            System.out.println("setString(" + (i+1) + "," + hodnota + ")");
                        }

                    }
               // }   
                } catch (Exception e) {
                    System.out.println(e);
                }
            }
            
            st.executeUpdate();
        
        }
       
       
        
    }
    
    private String vratPrepareStatementString(String NazevTabulky){
        
        String StrPrepareStatement;
        String StrNazvySloupcu;         // napr = ID,Name
        String StrValues;               // napr = ?,?
        String NazevSloupce;
        
        
        StrNazvySloupcu = HlavickaTabulky[0];
        StrValues = "?";
        
        for (int i = 1; i < HlavickaTabulky.length; i++) {
            NazevSloupce = HlavickaTabulky[i];
            StrNazvySloupcu = StrNazvySloupcu + "," + NazevSloupce;
            StrValues = StrValues + ",?";
        }
            
        StrPrepareStatement = "Insert into " + NazevTabulky + "("+ StrNazvySloupcu +")values("+ StrValues +")";
        
        return StrPrepareStatement;
    }
    
    
    
    
    
}
