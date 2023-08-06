/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sql_gui;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *
 * @author jonas
 */
public class ShowTables {
    
    //private Connection conn;
    private Statement st;
    private ResultSet rs;
    
    ShowTables() throws SQLException, ClassNotFoundException
    {
        
        //Registering the driver
        Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
        //conn = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo");

        int pocetRadku;
        int pocetSloupcu;
        
        ff();
        
    }
    
    private void ff() throws SQLException
    {
        //Registering the Driver
        //DriverManager.registerDriver(new com.mysql.jdbc.Driver());
        //Getting the connection
        //String url = "jdbc:derby://localhost:1527/SimpleDBDemo";
        Connection con = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo");
        System.out.println("Connection established......");
        //Retrieving the meta data object
        DatabaseMetaData metaData = con.getMetaData();
        //Retrieving the columns in the database
        ResultSet tables = metaData.getTables(null, null, "DEMO", null);
        //Printing the column name and size
        while (tables.next()) {
            System.out.println("Table name: "+tables.getString("Table_NAME"));
            System.out.println("Table type: "+tables.getString("TABLE_TYPE"));
            System.out.println("Table schema: "+tables.getString("TABLE_SCHEM"));
            System.out.println("Table catalog: "+tables.getString("TABLE_CAT"));
            System.out.println(" ");
        }
    }        
    
    private void vv()
    {
         String[] names = { "TABLE" };
         ResultSet result;
         DatabaseMetaData metadata = null;

         try {
             Connection c;
             c = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo"); 
             metadata = c.getMetaData();
             result = metadata.getTables(null, null, null, names);
             while(result.next()){
                 System.out.println(result.getString("TABLE_NAME"));
             }
         } catch(java.sql.SQLException e) {
             e.printStackTrace();
         }

    }
    
    private void vvv() throws SQLException
    {
        Connection c;
        c = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo"); 
        DatabaseMetaData dbm = c.getMetaData();
        ResultSet rs = dbm.getTables(null, null, "DEMO", null);
        if (rs.next()) {
          System.out.println("Table exists"); 
        } else {
          System.out.println("Table does not exist"); 
        }
    }
    
    
    private void vratPocetRadku() throws SQLException
    {
        /*
        String query;
        String[] DataSelectu = new String[10]; 
        String hodnota;
        query = "SHOW TABLES";
        
        st = conn.createStatement();
        rs = st.executeQuery(query);

        int r;
        r = -1;
        
        while(rs.next())
        {
            r = r + 1;
            hodnota = rs.getString(r);
                DataSelectu[r] = hodnota;
            
        }  
        System.out.println();
        
        
        
        //Z NEJAKEHO DUVODU TO NEJDE - NEVIM PROC
        
        DatabaseMetaData metadata = null;
        metadata = conn.getMetaData();
        String[] names = { "TABLE"};
        ResultSet tableNames = metadata.getTables( null, null, null, names);
        Statement stmt;
                
        String NazevTabulky;

        while( tableNames.next())
        {
            NazevTabulky = tableNames.getString("TABLE_NAME");
            System.out.println();
              
            //Creating the Statement object
            stmt = conn.createStatement();

            //Executing the query
            //String query = "DROP TABLE Employees2";
            String query = "DROP TABLE " + NazevTabulky;
            stmt.execute(query);
        }
*/
    }
    
}
