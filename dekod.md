$\color{red}{\text{sel}}$<br>
$\color{red}{\text{sele}}$<br>
$\color{red}{\text{selec}}$<br>
$$\color{red}{\text{select}}$$<br>

$$\color{red}{\pifont{39}}$$<br>





$\color{red}{Select}$<br>

$\textcolor{red}{Important}$<br>


$\color{#FDEE00}{\char"F1}$<br>



$\color{#FDEE00}{\text{package sql\\_gui;}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{import java.awt.Color;}}$<br>
$\color{#FDEE00}{\text{import java.sql.SQLException;}}$<br>
$\color{#FDEE00}{\text{import java.util.ArrayList;}}$<br>
$\color{#FDEE00}{\text{import java.util.Arrays;}}$<br>
$\color{#FDEE00}{\text{import javax.swing.JScrollPane;}}$<br>
$\color{#FDEE00}{\text{import javax.swing.JTextPane;}}$<br>
$\color{#FDEE00}{\text{import javax.swing.text.SimpleAttributeSet;}}$<br>
$\color{#FDEE00}{\text{import javax.swing.text.StyleConstants;}}$<br>
$\color{#FDEE00}{\text{import javax.swing.text.StyledDocument;}}$<br>
$\color{#FDEE00}{\text{//}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{public class BarevnyJTextArea \\{}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private JTextPane jTextPane3;}}$<br>
$\color{#FDEE00}{\text{&emsp;private boolean[][] PoleShody;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private int rPol;}}$<br>
$\color{#FDEE00}{\text{&emsp;private int sPol;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private String[] DotazySQL;}}$<br>
$\color{#FDEE00}{\text{&emsp;int vyberDotazVlevo;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;String[][] DataSel\ectuStredni;}}$<br>
$\color{#FDEE00}{\text{&emsp;String[][] DataSelectuStredni;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;String[] NazvySloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;int[] pocetZnakuVeSloupcich;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;//Konstruktor}}$<br>
$\color{#FDEE00}{\text{&emsp;BarevnyJTextArea(JTextPane jTextPane1, String[] DotazySQL, int vyberDotazVlevo, boolean[] poleVyberu) throws SQLException, ClassNotFoundException {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;this.jTextPane3 = jTextPane1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;this.DotazySQL = DotazySQL;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;this.vyberDotazVlevo = vyberDotazVlevo;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean NejmensiSelect;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean StredniSelect;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean NejvetsiSelect;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean zvyraznujPolozky;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;zvyraznujPolozky = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;NejmensiSelect = poleVyberu[0];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StredniSelect = poleVyberu[1];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;NejvetsiSelect = poleVyberu[2];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pripravDataSelectu(NejvetsiSelect);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;  private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  String dotazNejmensi;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  String dotazStredni;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  //String dotazNejvetsi;   - zatim nevyuzito}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  //plati pro dotaz z comboboxu - DotazVpravo}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->  //&emsp;&emsp;if (vyberDotazVlevo > DotazySQL.length){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->  //&emsp;&emsp;&emsp;SQL_GUI_Frame.}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->  //&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  dotazNejmensi = DotazySQL[vyberDotazVlevo];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  //String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String castZaFrom;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String castPredFrom;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String NazevTabulky;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] castZaFromArr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] stringArr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int indexOfFROM;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  indexOfFROM = originalniSelect.indexOf("FROM");}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  castZaFrom = originalniSelect.substring(indexOfFROM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  if (NejvetsiDotaz == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  castPredFrom = "SELECT * ";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  } else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  castPredFrom = originalniSelect.substring(0, indexOfFROM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  //Vytvori Select a pripravi data}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  Select selNejmensi = new Select(dotazNejmensi);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  Select selStredni = new Select(dotazStredni);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  //Vrati data ze Selectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  DataSelectuNejmensi = selNejmensi.getDataSelectu();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  DataSelectuStredni = selStredni.getDataSelectu();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  NazvySloupcu = selStredni.getNazvySloupcu();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  private int[] vratPocetZnakuProVsechnySloupce()}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  pocetSloupcu = NazvySloupcu.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int pocetZnaku;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;&emsp;  pocetZnaku = vratPocetZnakuProDanySloupec(s);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private int vratPocetZnakuProDanySloupec(int sloupec)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  { //vrati pole s poctem znaku v jednotlivych sloupcich}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;//to proto aby sloupce krasne zarovnal   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String Hodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int nejvicPocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  for (int r = 1; r < DataSelectuStredni.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  Hodnota = DataSelectuStredni[r][sloupec];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  if (Hodnota != null)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  pocetZnakuHodnoty = Hodnota.length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;&emsp;  nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return nejvicPocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;&emsp;  pocetZnakuVeSloupcich[s] = pocetZnaku;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  return (pocetZnakuVeSloupcich);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  String HlavickaStr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  HlavickaStr = vratStringHlavicky();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//vykresli barevny text v zavislosti na druhu vyberu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (NejmensiSelect == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuNejmensi, false);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (StredniSelect == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;-->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuStredni, true);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (NejvetsiSelect == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//pole se jmenuji stejne jako u stredniho selectu (DataSelectuStredniho obsahuji data nejvetsi)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;-->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuStredni, true);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String dotazNejmensi;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String dotazStredni;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//String dotazNejvetsi;   - zatim nevyuzito}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//plati pro dotaz z comboboxu - DotazVpravo}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;if (vyberDotazVlevo > DotazySQL.length){}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;SQL_GUI_Frame.}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;dotazNejmensi = DotazySQL[vyberDotazVlevo];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;  public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;  {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  //String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String castZaFrom;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String castPredFrom;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String NazevTabulky;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] castZaFromArr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] stringArr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  int indexOfFROM;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  indexOfFROM = originalniSelect.indexOf("FROM");}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  castZaFrom = originalniSelect.substring(indexOfFROM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (NejvetsiDotaz == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  castPredFrom = "SELECT * ";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  } else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  castPredFrom = originalniSelect.substring(0, indexOfFROM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//Vytvori Select a pripravi data}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;Select selNejmensi = new Select(dotazNejmensi);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;Select selStredni = new Select(dotazStredni);}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//Vrati data ze Selectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;DataSelectuNejmensi = selNejmensi.getDataSelectu();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;DataSelectuStredni = selStredni.getDataSelectu();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;NazvySloupcu = selStredni.getNazvySloupcu();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;  private int[] vratPocetZnakuProVsechnySloupce()}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;  {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = NazvySloupcu.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  int pocetZnaku;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;&emsp;  pocetZnaku = vratPocetZnakuProDanySloupec(s);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private int vratPocetZnakuProDanySloupec(int sloupec)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  { //vrati pole s poctem znaku v jednotlivych sloupcich}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;//to proto aby sloupce krasne zarovnal   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String Hodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int nejvicPocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int r = 1; r < DataSelectuStredni.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  Hodnota = DataSelectuStredni[r][sloupec];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (Hodnota != null)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetZnakuHodnoty = Hodnota.length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return nejvicPocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;&emsp;  pocetZnakuVeSloupcich[s] = pocetZnaku;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;&emsp;  return (pocetZnakuVeSloupcich);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String HlavickaStr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;HlavickaStr = vratStringHlavicky();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;//pretizeny kontstruktor - zatim docasne}}$<br>
$\color{#FDEE00}{\text{&emsp;private boolean[][] vratPoleShody(String[][] DataSelectu1, String[][] DataSelectu2){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[][] vetsiDataSelectu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[][] mensiDataSelectu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean[][] poleShody;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean JeDelsiDataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String HodnotaVetsiSelect;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//String HodnotaMensiSelect;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean nalezenaShoda;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//Kontroluje ktere pole je vetsi}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;JeDelsiDataSelectu2 = DelsiDataSelectu2(DataSelectu1, DataSelectu2);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;  private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  //obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  //metoda zjisti ve kterem poli je vice null}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetNullDataSelectu1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetNullDataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean jeDelsiDataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetNullDataSelectu1 = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetNullDataSelectu2 = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int i = 0; i < DataSelectu1.length; i++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (DataSelectu1[i] == null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (DataSelectu2[i] == null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (pocetNullDataSelectu2 > pocetNullDataSelectu1){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  jeDelsiDataSelectu2 = true;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  } else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  jeDelsiDataSelectu2 = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (JeDelsiDataSelectu2 == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;vetsiDataSelectu = DataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;mensiDataSelectu = DataSelectu1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;vetsiDataSelectu = DataSelectu1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;mensiDataSelectu = DataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;poleShody = new boolean[vetsiDataSelectu.length][vetsiDataSelectu[0].length];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//prenastavuje polozky na nulu (pro 1. vyhledavani) - pouzito v vratRadekASloupecNalezenePolozkyVPoli}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;rPol = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;sPol = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int s = 0; s < vetsiDataSelectu[0].length; s++) {&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int r = 0; r < vetsiDataSelectu.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;HodnotaVetsiSelect = vetsiDataSelectu[r][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;nalezenaShoda = vratRadekASloupecNalezenePolozkyVPoli(mensiDataSelectu, HodnotaVetsiSelect);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String polozkaPole;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean nalezenaShoda = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (HledanaPolozka != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  for (int s = 0; s < Pole[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  if(nalezenaShoda == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  for (int r = 0; r < Pole.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  polozkaPole = Pole[r][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  if (polozkaPole != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (polozkaPole.equals(HledanaPolozka) == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  rPol = r;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  sPol = s;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  nalezenaShoda = true;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (nalezenaShoda);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;//zapisuje nalezene shody do pole}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;poleShody[r][s] = nalezenaShoda;}}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;System.out.println(rPol + "  " + sPol);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//prekontroluje pole shody, protoze nektere polozky mohou byt spatne oznacene}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;poleShody = prekontrolujPoleShody(poleShody, mensiDataSelectu, vetsiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;  private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] mensiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] vetsiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String mensiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String vetsiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean[] poleShodyRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  int delkaVetsiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  int delkaMensiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  //nastavi pole poleShodyNew jako false pro vsechny polozky}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int r = 0; r < poleShodyNew.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  for (int s = 0; s < poleShodyNew[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  poleShodyNew[r][s] = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean shodaMVData;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  //vrati dany radek vetsich Dat Selectu&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean shoda;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String vetsiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] radekVetsiDataSelectu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int s = 0; s < vetsiDataSelectu[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  shoda = poleShody[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (shoda == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekVetsiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  //vetsi radek porovnava se vsemi radky z mensich dat}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  for (int rM = 0; rM < mensiDataSelectu.length; rM++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  //metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = mensiDataSelectu[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] radekMensiDataSelectu = new String[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return (radekMensiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  //nejdrive porovna jejich delku, zda jsou stejne dlouhe}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = true;&emsp; //defaultni hodnota, ktera se prepise}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  for (int s = 0; s < mensiDataSelectuRadek.length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  mensiDataSelectuHodnota = mensiDataSelectuRadek[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (mensiDataSelectuHodnota != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud jsou hodnoty stejne, pak shodaMVData zustane true}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  } else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  if (shodaMVData == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  poleShodyRadek = vratPoleShodyRadek(poleShody, rV);&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  //metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = poleShody[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  boolean[] radekPoleShody = new boolean[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;   for (int s = 0; s < pocetSloupcu; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  radekPoleShody[s] = poleShody[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return (radekPoleShody);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  for (int s = 0; s < poleShody[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  poleShodyNew[rV][s] = poleShodyRadek[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  } }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  } else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//this.vetsiDataSelectu = vetsiDataSelectu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return(poleShody);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] mensiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] vetsiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String mensiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String vetsiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean[] poleShodyRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int delkaVetsiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int delkaMensiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//nastavi pole poleShodyNew jako false pro vsechny polozky}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int r = 0; r < poleShodyNew.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int s = 0; s < poleShodyNew[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;poleShodyNew[r][s] = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shodaMVData;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//vrati dany radek vetsich Dat Selectu&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;  //metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;  private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean shoda;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  String vetsiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] radekVetsiDataSelectu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int s = 0; s < vetsiDataSelectu[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  shoda = poleShody[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  if (shoda == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  return (radekVetsiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//vetsi radek porovnava se vsemi radky z mensich dat}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int rM = 0; rM < mensiDataSelectu.length; rM++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetSloupcu = mensiDataSelectu[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] radekMensiDataSelectu = new String[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekMensiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;//nejdrive porovna jejich delku, zda jsou stejne dlouhe}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = true;&emsp; //defaultni hodnota, ktera se prepise}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < mensiDataSelectuRadek.length; s++) {}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectuRadek[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud jsou hodnoty stejne, pak shodaMVData zustane true}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;if (shodaMVData == true){}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShodyRadek = vratPoleShodyRadek(poleShody, rV);&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetSloupcu = poleShody[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean[] radekPoleShody = new boolean[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;   for (int s = 0; s < pocetSloupcu; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  radekPoleShody[s] = poleShody[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekPoleShody);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShodyNew[rV][s] = poleShodyRadek[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;} }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (poleShodyNew);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;//metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shoda;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String vetsiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] radekVetsiDataSelectu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int s = 0; s < vetsiDataSelectu[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;shoda = poleShody[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;if (shoda == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; -->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{ }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;-->  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (radekVetsiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;//metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pocetSloupcu = mensiDataSelectu[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] radekMensiDataSelectu = new String[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int s = 0; s < pocetSloupcu; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (radekMensiDataSelectu);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;//metoda volana z prekontrolujPoleShody}}$<br>
$\color{#FDEE00}{\text{&emsp;private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pocetSloupcu = poleShody[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean[] radekPoleShody = new boolean[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; for (int s = 0; s < pocetSloupcu; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;radekPoleShody[s] = poleShody[radek][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (radekPoleShody);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private void prekontrolujPoleShody2(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] mensiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] vetsiDataSelectuRadek;}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;mensiDataSelectuRadek = new String[5];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;vetsiDataSelectuRadek = new String[5];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String mensiDataSelectuHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String mensiDataSelectuHodnota0;&emsp;//hodnota z 0-teho sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String vetsiDataSelectHodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String vetsiDataSelectHodnota0;&emsp; //hodnota z 0-teho sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shoda;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shoda0;&emsp;&emsp;&emsp;&emsp;&emsp; //shoda z 0-teho sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shodnyRadek;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shodnyRadekNalezen;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int posledniRV = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//index rM udava cislo radku mensiDataSelectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int rM = 0; rM < mensiDataSelectu.length; rM++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;mensiDataSelectuHodnota0 = mensiDataSelectu[rM][0];}}$<br>
$\color{#FDEE00}{\text{ }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//vychozi hodnota, ktera se prepisuje}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;shodnyRadekNalezen = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//index rV udava cislo radku vetsiDataSelectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;//vychozi hodnota, ktera se prepisuje}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;shodnyRadek = true;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;//v okamziku, kdy shodny radek byl jiz nalezen}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (shodnyRadekNalezen == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;//vyhledava, kde je shoda == true v 0-tem sloupci}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;shoda0 = poleShody[rV][0];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (shoda0 == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//pokud je shoda v 0-tem sloupci, }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//pak porovna hodnotu mensiDataSelectu a vetsiDataSelectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//ve sloupci 0}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota0 = vetsiDataSelectu[rV][0];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota0.equals(vetsiDataSelectHodnota0) == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud hodnoty mensiho a vetsiho Selectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//jsou stejne - uvazovane pro stejny sloupec, ale jiny radek}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pak se porovnaji hodnoty i pro ostatni sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 1; s < mensiDataSelectu[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectu[rM][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud nejaka hodnota neni stejna (z nejakeho sloupce),}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pak se nastavi na false a dal uz se nepokracuje}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//(shoda0 == false) }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//shodnyRadek = false muze nabit hodnoty(false) vicero zpusoby}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (shodnyRadek == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadekNalezen = true;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;posledniRV = rV + 1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (shodnyRadek == false){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShody[rV][s] = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < mensiDataSelectu[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectu[rM][s];}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;shoda = poleShody[rV][s];}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;if (shoda == true){}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false) {}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;  //  if (mensiDataSelectuHodnota != vetsiDataSelectHodnota){}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;int d = poleShody[0].length;}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//nejedna-li se o shodny radek }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//tzn. radek mensiDataSelectu != radku vetsiDataSelectu}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//pak prepise vsechny true na danem radku na false}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//(to je taky cilem opravy, jelikoz v puvodnim poleShody tomu tak nemusi byt)}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;if (shodnyRadek == false){}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;&emsp;poleShody[r][s] = false;}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{//&emsp;&emsp;&emsp;d = poleShody[0].length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;public JTextPane getBarevnyText(){}}$<br>
$\color{#FDEE00}{\text{&emsp;//public JScrollPane getBarevnyText(){&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//return (jTextPane1);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//return (jTextPane2);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (jTextPane3);}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String polozkaPole;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean nalezenaShoda = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (HledanaPolozka != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int s = 0; s < Pole[0].length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if(nalezenaShoda == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;for (int r = 0; r < Pole.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;polozkaPole = Pole[r][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;if (polozkaPole != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (polozkaPole.equals(HledanaPolozka) == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rPol = r;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sPol = s;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nalezenaShoda = true;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (nalezenaShoda);}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//metoda zjisti ve kterem poli je vice null}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetNullDataSelectu1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetNullDataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean jeDelsiDataSelectu2;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pocetNullDataSelectu1 = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pocetNullDataSelectu2 = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int i = 0; i < DataSelectu1.length; i++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;if (DataSelectu1[i] == null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;if (DataSelectu2[i] == null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (pocetNullDataSelectu2 > pocetNullDataSelectu1){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;jeDelsiDataSelectu2 = true;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;jeDelsiDataSelectu2 = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (jeDelsiDataSelectu2);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp; private String vratStringHlavicky(){}}$<br>
$\color{#FDEE00}{\text{&emsp;  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String NazevSloupce;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String HlavickaStr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetZnakuVeSloupci;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String ZbyvajiciMezery;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;HlavickaStr = "";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int s = 1; s <= NazvySloupcu.length; s++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;NazevSloupce = NazvySloupcu[s-1];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s-1];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, NazevSloupce);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;HlavickaStr = HlavickaStr + "  " + ZbyvajiciMezery;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return(HlavickaStr);}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;private String doplnZbyvajiciMezery(int pocetZnakuSloupce, String Hodnota)}}$<br>
$\color{#FDEE00}{\text{&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String ZbyvajiciMezery;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetZnakuMezer;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (Hodnota != null){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;pocetZnakuMezer = pocetZnakuSloupce - Hodnota.length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;ZbyvajiciMezery = Hodnota;}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//doplni retezec o mezery}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int i = 0; i < pocetZnakuMezer; i++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp; ZbyvajiciMezery = ZbyvajiciMezery + " "; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;} }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;else}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;ZbyvajiciMezery = "";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (ZbyvajiciMezery);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;private int[] vratPocetZnakuProVsechnySloupce()}}$<br>
$\color{#FDEE00}{\text{&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetSloupcu;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;pocetSloupcu = NazvySloupcu.length;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetZnaku;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int s = 0; s < pocetSloupcu; s++){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;pocetZnaku = vratPocetZnakuProDanySloupec(s);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;pocetZnakuVeSloupcich[s] = pocetZnaku;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return (pocetZnakuVeSloupcich);}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;private int vratPocetZnakuProDanySloupec(int sloupec)}}$<br>
$\color{#FDEE00}{\text{&emsp;{ //vrati pole s poctem znaku v jednotlivych sloupcich}}$<br>
$\color{#FDEE00}{\text{&emsp;  //to proto aby sloupce krasne zarovnal   }}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String Hodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int nejvicPocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;for (int r = 1; r < DataSelectuStredni.length; r++) {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;Hodnota = DataSelectuStredni[r][sloupec];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;if (Hodnota != null)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;pocetZnakuHodnoty = Hodnota.length();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return nejvicPocetZnakuHodnoty;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private void vratBarevnyText(String[][] DataSelectu, boolean zvyraznujPolozky){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String hodnota;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String mezera;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String hodnotaM;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int delkaDoc;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;boolean shoda;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String ZbyvajiciMezery;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int pocetZnakuVeSloupci;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//StyledDocument doc = jTextPane2.getStyledDocument();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StyledDocument doc = jTextPane3.getStyledDocument();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;SimpleAttributeSet keyWord = new SimpleAttributeSet();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StyleConstants.setForeground(keyWord, Color.RED);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;hodnota = "xxx";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;mezera = "  ";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;hodnotaM = "";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;delkaDoc = 0;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;try}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//jTextPane2.setText(""); }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;jTextPane3.setText("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   \n"); }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//doc.insertString(0, "<html>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; </html>", keyWord );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;//index r = -1 plati pro hlavicku}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;for (int r = -1; r < DataSelectu.length; r++) { }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp; }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < DataSelectu[0].length; s++) {&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;if (r == -1){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//jedna se o hlavicku&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hodnota = NazvySloupcu[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//jedna se o tabulku&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//Zvyraznuje polozky jeb v pripade, pokud zvyraznujPolozky == true}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (zvyraznujPolozky == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = PoleShody[r][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = false;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hodnota = DataSelectu[r][s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;delkaDoc = doc.getLength();}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, hodnota);}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;hodnotaM = ZbyvajiciMezery + "   ";}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//oznaci danou bunku v zavislosti na tom, zda nalezl shodu ci nikoliv}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;if (shoda == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), hodnotaM, keyWord );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), hodnotaM, null );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}  }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;if (r == -1){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//za hlavicku vlozi prazdny radek + novy rasek   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\n\n", null );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;//janak vklada pouze novy radek}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\n", null );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;catch(Exception e) { System.out.println(e); }}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;//pokud je NejvetsiDotaz = true, pak vraci nejvetsi dotaz, jinak stredni dotaz}}$<br>
$\color{#FDEE00}{\text{&emsp;public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)}}$<br>
$\color{#FDEE00}{\text{&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM }}$<br>
$\color{#FDEE00}{\text{&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String castZaFrom;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String castPredFrom;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String NazevTabulky;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] castZaFromArr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;String[] stringArr;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;int indexOfFROM;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;indexOfFROM = originalniSelect.indexOf("FROM");}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;castZaFrom = originalniSelect.substring(indexOfFROM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (NejvetsiDotaz == true){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;castPredFrom = "SELECT * ";}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;} else {}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;castPredFrom = originalniSelect.substring(0, indexOfFROM);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;   }}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;castZaFromArr = castZaFrom.split(" ");}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;NazevTabulky = castZaFromArr[1];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;stringArr = NazevTabulky.split("\n");}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;if (stringArr.length > 0)}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;NazevTabulky = stringArr[0];}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;plnySelect = castPredFrom + "FROM " + NazevTabulky;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;return(plnySelect);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;//nepotrebne}}$<br>
$\color{#FDEE00}{\text{&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;private void vratBarevnyText2(){}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//jTextPane2.setText( "original text" );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;jTextPane3.setText( "original text" );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//StyledDocument doc = jTextPane2.getStyledDocument();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StyledDocument doc = jTextPane3.getStyledDocument();}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//  Define a keyword attribute}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;SimpleAttributeSet keyWord = new SimpleAttributeSet();}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StyleConstants.setForeground(keyWord, Color.RED);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StyleConstants.setBackground(keyWord, Color.YELLOW);}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;StyleConstants.setBold(keyWord, true);}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;//  Add some text}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;try}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;{}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;doc.insertString(0, "Start of text\n", null );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\nEnd of text", keyWord );}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;}}}$<br>
$\color{#FDEE00}{\text{&emsp;&emsp;catch(Exception e) { System.out.println(e); }}}$<br>
$\color{#FDEE00}{\text{&emsp;   }}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{&emsp;}}}$<br>
$\color{#FDEE00}{\text{}}$<br>
$\color{#FDEE00}{\text{}}}$<br>
