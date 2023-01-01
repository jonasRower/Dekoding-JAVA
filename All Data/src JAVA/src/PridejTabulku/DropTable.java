/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package PridejTabulku;

import sql_gui.*;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;



public class DropTable {
    //dropne vsechny existujici tabulky
    
    Connection conn;
    Statement stmt;
    
    DropTable() throws SQLException, ClassNotFoundException{
        
        String[] seznamTabulek;
        
        //Registering the driver
        Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
        conn = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo");
      
        //Creating the Statement object
        stmt = conn.createStatement();
 
        
        seznamTabulek = VratSeznamTabulek();
        DropniTabulky(seznamTabulek);
     
    }
    
    private String[] VratSeznamTabulek() throws SQLException{
        
        List<String> tables = new ArrayList<String>();
        ResultSet rs = null;
        
        if(conn != null){
            try {
                    DatabaseMetaData dbMetaData = conn.getMetaData();
                    rs = dbMetaData.getTables("DEMO", null, null, new String[]{"TABLE"});
                    while(rs.next()){
                            tables.add(rs.getString("TABLE_NAME"));
                    }
            } catch (SQLException e) {
                    e.printStackTrace();
            } finally{

            }

        }
        
        String[] seznamTabulek = new String[tables.size()];
        seznamTabulek = tables.toArray(seznamTabulek);
        
        return (seznamTabulek);
        
    }
    
    private void DropniTabulky(String[]NazvyTabulek){

        String query;
        String NazevTabulky;
                
        for (int i = 0; i < NazvyTabulek.length; i++) {
             
            NazevTabulky = NazvyTabulek[i];
            query = "DROP TABLE " + NazevTabulky;
             
            try {
            stmt.execute(query);
            } catch (Exception e) {
                System.out.println(e);
            }
             
        }
        
    }
    
    
}
