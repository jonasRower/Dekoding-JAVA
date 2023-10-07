
package sql_gui;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;


public class Select {
    
    private Connection conn;
    private Statement st;
    private ResultSet rs;
    private ResultSetMetaData rsmd;
    
    private String[][] DataSelectu;
    private String[] NazvySloupcu;
   
    private String[] SubSelecty;
    private String[] SubTabulky;
    
    private String query;
    private String nazevTabulky;
    private String dotazBezNazvuTabulky;
    
    
    Select(String query) throws SQLException, ClassNotFoundException
    {
        
        //Registering the driver
        Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
        conn = DriverManager.getConnection("jdbc:derby://localhost:1527/SimpleDBDemo", "demo", "demo");

        this.query = query;
        ziskejNazevTabulkyZDotazu();
        
        int pocetRadku = 0;
        int pocetSloupcu = 0;
        
        if (nazevTabulky != null)
        {
            pocetRadku = vratPocetRadku();
            pocetSloupcu = vratPocetSloupcu();
        
            //naplni pole String[][] DataSelectu
            DataSelectu = vratObsahTabulky(pocetRadku, pocetSloupcu);
            NazvySloupcu = vratNazvySloupcu(pocetSloupcu);
        }
    }
    
    
    public String[][] getDataSelectu(){
        return (DataSelectu);
    }
    
    public String[] getNazvySloupcu(){
        return (NazvySloupcu);
    }
    
    
    private void ziskejNazevTabulkyZDotazu()
    {
    //SJEDNOTIT KOD V TETO METODE
    //s metodou vratSubSelecty, kde nazev tabulky se ziskava stejnym zpusobem
        
        int pocetSelectu;
        String[] arrOfStr = query.split("FROM"); 
        String[] arrOfStr2;
        if (arrOfStr.length > 2){
            //pokud je pocet "splitu" v selectu vetsi nez 2 pak se pocita pocet SELECTU
            //a pro kazdy select se vraci nazev tabulky
            pocetSelectu = vratPocetSubStringu("SELECT", query);
            vratSubSelecty(pocetSelectu);
            nazevTabulky = SubTabulky[0];
            
            dotazBezNazvuTabulky = arrOfStr[0].trim() + " FROM ";
        }
        
        if (arrOfStr.length == 2){
            nazevTabulky = arrOfStr[1].trim();
            arrOfStr2 = nazevTabulky.split("\n"); 
            if (arrOfStr2.length > 0){
                nazevTabulky = arrOfStr2[0];
            }
            dotazBezNazvuTabulky = arrOfStr[0].trim() + " FROM ";
        }
    }  
    
    
    private int vratPocetSubStringu(String SubString, String Dotaz) {
        
        int count = 0, fromIndex = 0;
        while ((fromIndex = Dotaz.indexOf(SubString, fromIndex)) != -1 ){
 
            System.out.println("Found at index: " + fromIndex);
            count++;
            fromIndex++;
            
        }
        
        return count;
    }
    
    private void vratSubSelecty(int pocetSubSelectu){
    //vraci cast Selectu pocinaje klicovim slovem "SELECT"
    
        int OdIndexu;
        int indexNalezenehoSelectu;
        String nazevSubTabulky;
        
        String[] arrOfStr; 
        String[] arrOfStr2; 
        
        SubSelecty = new String[pocetSubSelectu];
        SubTabulky = new String[pocetSubSelectu];
        String CastRetezceZaSelectem;
        
        OdIndexu = 0;
        indexNalezenehoSelectu = -1;
        
        for (int i = 0; i < pocetSubSelectu; i++) {
            
            CastRetezceZaSelectem = "";
            
            indexNalezenehoSelectu = query.indexOf("SELECT", indexNalezenehoSelectu + 1);
            CastRetezceZaSelectem = query.substring(indexNalezenehoSelectu, query.length());

            //zjisti NazevTabulky pro SubDotaz
            arrOfStr = CastRetezceZaSelectem.split("FROM"); 
            nazevSubTabulky = arrOfStr[1].trim();
            arrOfStr2 = nazevSubTabulky.split("\n"); 
            if (arrOfStr2.length > 0){
                nazevSubTabulky = arrOfStr2[0].trim();
            }

            //Zapise nazev SubDotazu do pole
            SubSelecty[i] = CastRetezceZaSelectem;

            //Zapise nazev SubTabulky do pole
            SubTabulky[i] = nazevSubTabulky;
        
//        OdIndexu = indexNalezenehoSelectu + 1; 
//        indexNalezenehoSelectu = query.indexOf("SELECT", OdIndexu);
//        CastRetezceZaSelectem = query.substring(indexNalezenehoSelectu, query.length());
//        SubSelecty[1] = CastRetezceZaSelectem;

        }
        
        System.out.println("");
        
    }
    
    
    private int vratPocetRadku() throws SQLException
    {
        ResultSet rs;
        String Dotaz;
        
        Dotaz = "SELECT COUNT(*) FROM " + nazevTabulky;
        
        //odstrani koncovy strednik
        Dotaz = Dotaz.replace(";", "");
        
        st = conn.createStatement();
        //rs = st.executeQuery("SELECT COUNT(*) FROM STUDENT");
        rs = st.executeQuery(Dotaz);
        rs.next();
        
        int rowCount = rs.getInt(1);
        System.out.println(rowCount);
        
        return (rowCount);
    }
    
    
    private int vratPocetSloupcu() throws SQLException
    {
        //odstrani koncovy strednik
        String Dotaz;
        Dotaz = query.replace(";", "");
        

        
 
        
        
        st = conn.createStatement();
        rs = st.executeQuery(Dotaz);
        rsmd = rs.getMetaData();
        
        int columnCount; 
        columnCount = rsmd.getColumnCount();
        
        return (columnCount);
    }
    
    
    private String[][] vratObsahTabulky(int pocetRadku, int pocetSloupcu) throws SQLException
    {
        
       // String query;
        String[][] DataSelectu = new String[pocetRadku][pocetSloupcu]; 
        String hodnota;
        
        //query = dotazBezNazvuTabulky + nazevTabulky;
        
        //odstrani koncovy strednik
        String Dotaz;
        Dotaz = query.replace(";", "");
        
        
        st = conn.createStatement();
        rs = st.executeQuery(Dotaz);

        int r;
        r = -1;
        
        //predelat na arrayList
        while(rs.next())
        {
            r = r + 1;
            for (int s = 1; s <= pocetSloupcu; s++) {
                hodnota = rs.getString(s);
                DataSelectu[r][s-1] = hodnota;
            }
        }  
        
        return (DataSelectu);
           
    }
    
    
    private String[] vratNazvySloupcu(int pocetSloupcu) throws SQLException
    {
        
        //odstrani koncovy strednik
        String Dotaz;
        
        Dotaz = dotazBezNazvuTabulky + nazevTabulky;
        Dotaz = Dotaz.replace(";", "");
        
        Dotaz = "SELECT * FROM item_mast";
        
        Statement statement = conn.createStatement();
        ResultSet resultSet = statement.executeQuery(Dotaz);

        ResultSetMetaData metadata = resultSet.getMetaData();
        int columnCount = metadata.getColumnCount();

        ArrayList<String> columns = new ArrayList<String>();
        
        for (int i = 1; i <= columnCount; i++) {
            String columnName = metadata.getColumnName(i);
            columns.add(columnName);
        }
        
        String[] SeznamSloupcu = new String[columns.size()]; 
        SeznamSloupcu = columns.toArray(SeznamSloupcu); 
        
        return (SeznamSloupcu);
        
    }
    
}
