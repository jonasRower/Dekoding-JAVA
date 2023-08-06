package sql_gui;


//Dodelat JScrollPane, tak aby tam byly rolovatka
//viz https://www.youtube.com/watch?v=VSC-Nm-hLWI


import PridejTabulku.VytvorDB;
import java.awt.Color;
import java.awt.Font;
import java.awt.font.TextAttribute;
import java.io.IOException;
import java.sql.SQLException;
import java.text.AttributedString;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;
import javax.swing.text.AbstractDocument;
import javax.swing.text.BadLocationException;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;


public class SQL_GUI_Frame extends javax.swing.JFrame {
    
    private boolean prvniStisknutiTlacitka = true;
    private int vyberDotazVlevo = 0;                    //index z pole dotazu vlevo
    private String[] seznamDotazu;
    
    private String[] DotazySQL;
    private String[] DotazyPopis;
    
    private int[] cislaPopisu;
    private String[][] SubDotazySQL;
    private String[][] SubDotazyPopis;
    
    //indikuje jake tlacitko bylo stisknuto
    private boolean nejUzsiVyber;
    private boolean stredniVyber;
    private boolean nejsirsiVyber;
    
    private boolean SelectVlevo;    //indikuje ze byl vybran select vlevo nebo vpravo
    private int pocetMoznosti;      //udava pocet moznosti subdotazu (velikost comboboxu)
    private int poradiSubDotazu;    //aktualne vybrany index v Comboboxu
    
    private AbstractDocument doc;
    private JScrollPane jsp;
    
//    JText textPane = new JTextPane();
//    textPane.setText( "This is regular text"");
//    StyledDocument doc = textPane.getStyledDocument();
    
    
    public SQL_GUI_Frame() throws IOException, ClassNotFoundException, SQLException {
        initComponents();
        seznamDotazu = new String[6];
        
        seznamDotazu[0] = "SELECT * FROM CUSTOMER";
        seznamDotazu[1] = "SELECT * FROM EMP_DETAILS";
        seznamDotazu[2] = "SELECT * FROM ITEM_MAST";
        seznamDotazu[3] = "SELECT * FROM NOBEL_WIN";
        seznamDotazu[4] = "SELECT * FROM ORDERS";
        seznamDotazu[5] = "SELECT * FROM SALESMAN";
        
        vyberDotazVlevo = -1;
        
    }

    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane5 = new javax.swing.JScrollPane();
        jTextArea5 = new javax.swing.JTextArea();
        SQLVpravoSPane = new javax.swing.JScrollPane();
        SQLVpravoTArea = new javax.swing.JTextArea();
        SQLVlevoSPane = new javax.swing.JScrollPane();
        SQLVlevoTArea = new javax.swing.JTextArea();
        TlacDoprava = new javax.swing.JButton();
        TlacDoleva = new javax.swing.JButton();
        NejmensiVlevoButt = new javax.swing.JButton();
        StredniVlevoButt = new javax.swing.JButton();
        NejvetsiVlevoButt = new javax.swing.JButton();
        StredniVpravoButt = new javax.swing.JButton();
        NejvetsiVpravoButt = new javax.swing.JButton();
        NejmensiVpravoButt = new javax.swing.JButton();
        popisVpravoPane = new javax.swing.JScrollPane();
        popisVpravoTArea = new javax.swing.JTextArea();
        popisVlevoSPane = new javax.swing.JScrollPane();
        popisVlevoTArea = new javax.swing.JTextArea();
        VysledekVlevoSPane = new javax.swing.JScrollPane();
        VysledekVlevoTPane = new javax.swing.JTextPane();
        VysledekVpravoSPane = new javax.swing.JScrollPane();
        VysledekVpravoTPane = new javax.swing.JTextPane();
        jLabel1 = new javax.swing.JLabel();
        jComboBox1 = new javax.swing.JComboBox<>();

        jTextArea5.setColumns(20);
        jTextArea5.setRows(5);
        jScrollPane5.setViewportView(jTextArea5);

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBounds(new java.awt.Rectangle(0, 0, 1000, 10));

        SQLVpravoTArea.setColumns(20);
        SQLVpravoTArea.setRows(5);
        SQLVpravoSPane.setViewportView(SQLVpravoTArea);

        SQLVlevoTArea.setColumns(20);
        SQLVlevoTArea.setLineWrap(true);
        SQLVlevoTArea.setRows(5);
        SQLVlevoSPane.setViewportView(SQLVlevoTArea);

        TlacDoprava.setText(">>");
        TlacDoprava.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                TlacDopravaActionPerformed(evt);
            }
        });

        TlacDoleva.setText("<<");
        TlacDoleva.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                TlacDolevaActionPerformed(evt);
            }
        });

        NejmensiVlevoButt.setText("( o )");
        NejmensiVlevoButt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                NejmensiVlevoButtActionPerformed(evt);
            }
        });

        StredniVlevoButt.setText("(  o  )");
        StredniVlevoButt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                StredniVlevoButtActionPerformed(evt);
            }
        });

        NejvetsiVlevoButt.setText("(   o   )");
        NejvetsiVlevoButt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                NejvetsiVlevoButtActionPerformed(evt);
            }
        });

        StredniVpravoButt.setText("(  o  )");
        StredniVpravoButt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                StredniVpravoButtActionPerformed(evt);
            }
        });

        NejvetsiVpravoButt.setText("(   o   )");
        NejvetsiVpravoButt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                NejvetsiVpravoButtActionPerformed(evt);
            }
        });

        NejmensiVpravoButt.setText("( o )");
        NejmensiVpravoButt.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                NejmensiVpravoButtActionPerformed(evt);
            }
        });

        popisVpravoTArea.setBackground(new java.awt.Color(240, 240, 240));
        popisVpravoTArea.setColumns(20);
        popisVpravoTArea.setLineWrap(true);
        popisVpravoTArea.setRows(5);
        popisVpravoPane.setViewportView(popisVpravoTArea);

        popisVlevoTArea.setBackground(new java.awt.Color(240, 240, 240));
        popisVlevoTArea.setColumns(20);
        popisVlevoTArea.setLineWrap(true);
        popisVlevoTArea.setRows(5);
        popisVlevoSPane.setViewportView(popisVlevoTArea);

        VysledekVlevoSPane.setBackground(new java.awt.Color(255, 255, 255));
        VysledekVlevoSPane.setHorizontalScrollBarPolicy(javax.swing.ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS);
        VysledekVlevoSPane.setToolTipText("");
        VysledekVlevoSPane.setVerticalScrollBarPolicy(javax.swing.ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);

        VysledekVlevoTPane.setMinimumSize(new java.awt.Dimension(100, 100));
        VysledekVlevoSPane.setViewportView(VysledekVlevoTPane);

        VysledekVpravoSPane.setHorizontalScrollBarPolicy(javax.swing.ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS);
        VysledekVpravoSPane.setVerticalScrollBarPolicy(javax.swing.ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        VysledekVpravoSPane.setViewportView(VysledekVpravoTPane);

        jLabel1.setText("Porovnat s dotazem:");
        jLabel1.setToolTipText("");

        jComboBox1.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }));
        jComboBox1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboBox1ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(NejmensiVlevoButt, javax.swing.GroupLayout.DEFAULT_SIZE, 97, Short.MAX_VALUE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(StredniVlevoButt, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(NejvetsiVlevoButt, javax.swing.GroupLayout.PREFERRED_SIZE, 109, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED))
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                        .addComponent(SQLVlevoSPane, javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(VysledekVlevoSPane, javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(popisVlevoSPane, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 353, Short.MAX_VALUE)))
                .addComponent(TlacDoleva, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(TlacDoprava, javax.swing.GroupLayout.PREFERRED_SIZE, 69, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel1)
                        .addGap(18, 18, 18)
                        .addComponent(jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, 50, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addGroup(layout.createSequentialGroup()
                            .addComponent(NejmensiVpravoButt, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                            .addComponent(StredniVpravoButt, javax.swing.GroupLayout.PREFERRED_SIZE, 89, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(18, 18, 18)
                            .addComponent(NejvetsiVpravoButt, javax.swing.GroupLayout.PREFERRED_SIZE, 111, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addComponent(VysledekVpravoSPane)
                        .addComponent(SQLVpravoSPane)
                        .addComponent(popisVpravoPane)))
                .addGap(19, 19, 19))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addComponent(popisVlevoSPane, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel1)
                            .addComponent(jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(popisVpravoPane)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(SQLVlevoSPane, javax.swing.GroupLayout.PREFERRED_SIZE, 116, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(SQLVpravoSPane, javax.swing.GroupLayout.PREFERRED_SIZE, 114, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(StredniVpravoButt)
                                .addComponent(NejmensiVpravoButt)
                                .addComponent(NejvetsiVpravoButt))
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(NejvetsiVlevoButt)
                                .addComponent(StredniVlevoButt))
                            .addComponent(NejmensiVlevoButt))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(VysledekVpravoSPane, javax.swing.GroupLayout.PREFERRED_SIZE, 298, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addGap(0, 0, Short.MAX_VALUE)
                                .addComponent(VysledekVlevoSPane, javax.swing.GroupLayout.PREFERRED_SIZE, 303, javax.swing.GroupLayout.PREFERRED_SIZE))))
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(TlacDoleva, javax.swing.GroupLayout.PREFERRED_SIZE, 466, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(TlacDoprava, javax.swing.GroupLayout.PREFERRED_SIZE, 466, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    
    // tlacitko ">>"
    private void TlacDopravaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_TlacDopravaActionPerformed
    
        try {

            if (prvniStisknutiTlacitka == true)
            {       
                
                //Nacte vsechny dotazy aby je mohl zobrazit
                NactiDotazy DotazyzTxt = new NactiDotazy();
               
                DotazySQL = DotazyzTxt.getDotazySQL();
                DotazyPopis = DotazyzTxt.getDotazyPopis();
                
               // cislaPopisu = DotazyzTxt.getCislaPopisu();
                SubDotazySQL = DotazyzTxt.getSubDotazySQL();
                SubDotazyPopis = DotazyzTxt.getSubDotazyPopis();
                
                //vytvori novou databazi, tak ze odstrani tabulky stare a vlozi nove
                VytvorDB NovaDB = new VytvorDB();
                
                //nastavi vychozi hodnoty, podle toho o jaky vyber se jedna
                nejUzsiVyber = true;
                stredniVyber = false;
                nejsirsiVyber = false;
                
                //Nastavi ze tlacitko jiz bylo stlaceno
                prvniStisknutiTlacitka = false; //indikuje, ze tlacitko jiz bylo spusteno
       
            }
           
            vyberDotazVlevo = vyberDotazVlevo + 1;
            poradiSubDotazu = 1; 
            SelectVlevo = true;
            vratPocetMoznosti();
           
            zobrazSelectVJTextArea();
            vymazHodnotyVpravo();
            jComboBox1.setSelectedIndex(0);
            
        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }    
        
    }//GEN-LAST:event_TlacDopravaActionPerformed

    private void nastavComboboxVpravo(){
        
        //vrati pocet moznosti pro ComboBox
        vratPocetMoznosti();
        
        //initComponents();
        String[] dat = new String[pocetMoznosti];
        for(int i = 0; i < pocetMoznosti; i++) {
            dat[i] = "" + i;
        }
        //jComboBox1.setModel(new javax.swing.DefaultComboBoxModel(dat));
       // jComboBox1.addItem(new ComboItem("Visible String 1", "Value 1"));
        //jComboBox1 jComboBox1 = new jComboBox1();
        //jComboBox1.addItem("asdf");
        
    }
    
    private void vratPocetMoznosti(){
        
        String hodnota;
        
        for(int i = 0; i < SubDotazySQL[0].length; i++) {
            hodnota = SubDotazySQL[vyberDotazVlevo][i];
            if (hodnota == null){
                //ulozi pocet moznosti do promenne ve tride
                pocetMoznosti = i;
                break;
            }
        }
        
    }
    
    
    // tlacitko "<<"
    private void TlacDolevaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_TlacDolevaActionPerformed
        try {
 
            if(vyberDotazVlevo > 0){
                vyberDotazVlevo = vyberDotazVlevo - 1;
                poradiSubDotazu = 1;
                SelectVlevo = true;
                vratPocetMoznosti();
                
                zobrazSelectVJTextArea();
                vymazHodnotyVpravo();
                jComboBox1.setSelectedIndex(0);
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }    
        
    }//GEN-LAST:event_TlacDolevaActionPerformed

    
    private void NejmensiVlevoButtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_NejmensiVlevoButtActionPerformed
        try {
            //tlacitko ( o ) vlevo (1. zleva)
            nejUzsiVyber = true;
            stredniVyber = false;
            nejsirsiVyber = false;
            
            SelectVlevo = true;
            
            
            zobrazSelectVJTextArea();            

        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_NejmensiVlevoButtActionPerformed

    
    private void StredniVlevoButtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_StredniVlevoButtActionPerformed
        //tlacitko (  o  ) vlevo (2. zleva)
        try { 
            
            nejUzsiVyber = false;
            stredniVyber = true;
            nejsirsiVyber = false;
            
            SelectVlevo = true;
         
            zobrazSelectVJTextArea();
        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }//GEN-LAST:event_StredniVlevoButtActionPerformed

    private void NejvetsiVlevoButtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_NejvetsiVlevoButtActionPerformed
        
        //tlacitko (  o  ) vlevo (3. zleva)
        try { 
            
            nejUzsiVyber = false;
            stredniVyber = false;
            nejsirsiVyber = true;
            
            SelectVlevo = true;
         
            zobrazSelectVJTextArea();
            
        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }//GEN-LAST:event_NejvetsiVlevoButtActionPerformed

    private void NejmensiVpravoButtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_NejmensiVpravoButtActionPerformed
       
         try {
            //tlacitko ( o ) vpravo (1. zleva)
            nejUzsiVyber = true;
            stredniVyber = false;
            nejsirsiVyber = false;
            
            SelectVlevo = false;
            
            if (poradiSubDotazu > 0){
                zobrazSelectVJTextArea();   
            }
                    

        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }//GEN-LAST:event_NejmensiVpravoButtActionPerformed

    private void StredniVpravoButtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_StredniVpravoButtActionPerformed
        
         //tlacitko (  o  ) vpravo (2. zleva)
        try { 
            
            nejUzsiVyber = false;
            stredniVyber = true;
            nejsirsiVyber = false;
            
            SelectVlevo = false;
         
            if (poradiSubDotazu > 0){
                zobrazSelectVJTextArea();   
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }//GEN-LAST:event_StredniVpravoButtActionPerformed

    private void NejvetsiVpravoButtActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_NejvetsiVpravoButtActionPerformed
        
        //tlacitko (  o  ) vpravo (3. zleva)
        try { 
            
            nejUzsiVyber = false;
            stredniVyber = false;
            nejsirsiVyber = true;
            
            SelectVlevo = false;
         
            if (poradiSubDotazu > 0){
                zobrazSelectVJTextArea();   
            }
            
        } catch (SQLException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }//GEN-LAST:event_NejvetsiVpravoButtActionPerformed

    private void jComboBox1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboBox1ActionPerformed
       
        poradiSubDotazu = jComboBox1.getSelectedIndex();
        
        if (poradiSubDotazu == 0){
           
            // pouze vymaze hodnoty a nic vic
            vymazHodnotyVpravo();
        
        } else {
            
            SelectVlevo = false;
        
            try {
                zobrazSelectVJTextArea();
            } catch (SQLException ex) {
                Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
            } catch (ClassNotFoundException ex) {
                Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }//GEN-LAST:event_jComboBox1ActionPerformed

    
    private void zobrazSelectVJTextArea() throws SQLException, ClassNotFoundException {
        
        boolean[] PoleVyberu = new boolean[3];
        
        String dotaz = "";
        String ukol = "";
        String subDotaz = "";
        String subUkol = "";
        
        String[] moznostiSubDotazuSQL = null;
        
        
        PoleVyberu[0] = nejUzsiVyber;
        PoleVyberu[1] = stredniVyber;
        PoleVyberu[2] = nejsirsiVyber;
           
        //NASTAVUJE DATA DO POLI VLEVO
        if (SelectVlevo == true){
            BarevnyJTextArea barevnyDotaz = new BarevnyJTextArea(VysledekVlevoTPane, DotazySQL, vyberDotazVlevo, PoleVyberu);
        
             //Vlevo
            dotaz = DotazySQL[vyberDotazVlevo];
            ukol = DotazyPopis[vyberDotazVlevo];
            
            //zapise popis prikladu do pole vlevo
            popisVlevoTArea.setText(ukol);
        
            //zapise SQL prikladu do pole vlevo
            SQLVlevoTArea.setText(dotaz);
            
            VysledekVlevoTPane.setFont(new Font("monospaced", Font.PLAIN, 12));
            
        }
        
        //NASTAVUJE DATA DO POLI VPRAVO
        if (SelectVlevo == false){
            moznostiSubDotazuSQL = vratPoleMoznostiSubDotazu(1);
            if (poradiSubDotazu >= moznostiSubDotazuSQL.length){      
                vymazHodnotyVpravo();
            }  
            else       
            { 
                BarevnyJTextArea barevnyDotaz = new BarevnyJTextArea(VysledekVpravoTPane, moznostiSubDotazuSQL, poradiSubDotazu, PoleVyberu);

                //Vpravo
                subDotaz = SubDotazySQL[vyberDotazVlevo][poradiSubDotazu];
                subUkol = SubDotazyPopis[vyberDotazVlevo][poradiSubDotazu];

                //zapise popis Subprikladu do pole vpravo
                popisVpravoTArea.setText(subUkol);

                //Zapise SQL SubPrikladu do pole vpravo
                SQLVpravoTArea.setText(subDotaz);
            
            }
        
            VysledekVpravoTPane.setFont(new Font("monospaced", Font.PLAIN, 12));
        }

    }
    
    //Vymazou se data v polich a popisu, pokud kliknu na >> nebo <<
    private void vymazHodnotyVpravo(){
        
        popisVpravoTArea.setText("");
        SQLVpravoTArea.setText("");
        VysledekVpravoTPane.setText("");
        
    }
    
    private String[] vratPoleMoznostiSubDotazu(int indexDotazu){
        
        String[] MoznostiSubDotazuSQL = new String[pocetMoznosti];
        
        int cisloDotazu;    //tj. cislo dle zadani napr. 19.
        //int indexDotazu;    //tj index v poli dotazu SQL
        
        indexDotazu = 0;
        
        for (int i = 0; i < pocetMoznosti; i++) { 
            MoznostiSubDotazuSQL[i] = SubDotazySQL[indexDotazu][i];
        }  
        
        return MoznostiSubDotazuSQL;
        
    }
    

    public static void vykresliOkno() {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        
        
        
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(SQL_GUI_Frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(SQL_GUI_Frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(SQL_GUI_Frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(SQL_GUI_Frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
 

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                
                
                try {
                    //System.out.println("ahoj");
                    //NactiDataZTxt Data = new NactiDataZTxt();

                    new SQL_GUI_Frame().setVisible(true);
                    //JFrame.setResizable(false);
                } catch (IOException ex) {
                    Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
                } catch (ClassNotFoundException ex) {
                    Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
                } catch (SQLException ex) {
                    Logger.getLogger(SQL_GUI_Frame.class.getName()).log(Level.SEVERE, null, ex);
                }
        
            }
        });
    }
    
    
    public String vratSelectyNaPlnouTabulku(String originalniSelect)
    {
        //String originalniSelect;    //napr.          Select * FROM ... WHERE ...
        String plnySelect;          //z toho vychazi Select * FROM 
       
        String castZaFrom;
        String castPredFrom;
        String NazevTabulky;
        String[] castZaFromArr;
        String[] stringArr;
        int indexOfFROM;
        
        indexOfFROM = originalniSelect.indexOf("FROM");
        castZaFrom = originalniSelect.substring(indexOfFROM);
        castPredFrom = originalniSelect.substring(0, indexOfFROM);
       
        castZaFromArr = castZaFrom.split(" ");
        NazevTabulky = castZaFromArr[1];
        stringArr = NazevTabulky.split("\n");
        if (stringArr.length > 0)
        {
            NazevTabulky = stringArr[0];
        }
        
        plnySelect = castPredFrom + "FROM " + NazevTabulky;
        
        
        return(plnySelect);
                
    }
    
    
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton NejmensiVlevoButt;
    private javax.swing.JButton NejmensiVpravoButt;
    private javax.swing.JButton NejvetsiVlevoButt;
    private javax.swing.JButton NejvetsiVpravoButt;
    private javax.swing.JScrollPane SQLVlevoSPane;
    private javax.swing.JTextArea SQLVlevoTArea;
    private javax.swing.JScrollPane SQLVpravoSPane;
    private javax.swing.JTextArea SQLVpravoTArea;
    private javax.swing.JButton StredniVlevoButt;
    private javax.swing.JButton StredniVpravoButt;
    private javax.swing.JButton TlacDoleva;
    private javax.swing.JButton TlacDoprava;
    private javax.swing.JScrollPane VysledekVlevoSPane;
    private javax.swing.JTextPane VysledekVlevoTPane;
    private javax.swing.JScrollPane VysledekVpravoSPane;
    private javax.swing.JTextPane VysledekVpravoTPane;
    private javax.swing.JComboBox<String> jComboBox1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JScrollPane jScrollPane5;
    private javax.swing.JTextArea jTextArea5;
    private javax.swing.JScrollPane popisVlevoSPane;
    private javax.swing.JTextArea popisVlevoTArea;
    private javax.swing.JScrollPane popisVpravoPane;
    private javax.swing.JTextArea popisVpravoTArea;
    // End of variables declaration//GEN-END:variables


}
