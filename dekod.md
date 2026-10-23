<br>
package sql_gui;<br>
<br>
import java.awt.Color;<br>
import java.sql.SQLException;<br>
import java.util.ArrayList;<br>
import java.util.Arrays;<br>
import javax.swing.JScrollPane;<br>
import javax.swing.JTextPane;<br>
import javax.swing.text.SimpleAttributeSet;<br>
import javax.swing.text.StyleConstants;<br>
import javax.swing.text.StyledDocument;<br>
//<br>
<br>
<br>
public class BarevnyJTextArea {<br>
&emsp;<br>
&emsp;private JTextPane jTextPane3;<br>
&emsp;private boolean[][] PoleShody;<br>
&emsp;<br>
&emsp;private int rPol;<br>
&emsp;private int sPol;<br>
&emsp;<br>
&emsp;private String[] DotazySQL;<br>
&emsp;int vyberDotazVlevo;<br>
&emsp;<br>
&emsp;String[][] DataSelectuNejmensi;<br>
&emsp;String[][] DataSelectuStredni;<br>
&emsp;<br>
&emsp;String[] NazvySloupcu;<br>
&emsp;int[] pocetZnakuVeSloupcich;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;//Konstruktor<br>
&emsp;BarevnyJTextArea(JTextPane jTextPane1, String[] DotazySQL, int vyberDotazVlevo, boolean[] poleVyberu) throws SQLException, ClassNotFoundException {<br>
&emsp;&emsp;<br>
&emsp;&emsp;this.jTextPane3 = jTextPane1;<br>
&emsp;&emsp;this.DotazySQL = DotazySQL;<br>
&emsp;&emsp;this.vyberDotazVlevo = vyberDotazVlevo;<br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean NejmensiSelect;<br>
&emsp;&emsp;boolean StredniSelect;<br>
&emsp;&emsp;boolean NejvetsiSelect;<br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean zvyraznujPolozky;<br>
&emsp;&emsp;zvyraznujPolozky = false;<br>
&emsp;&emsp;<br>
&emsp;&emsp;NejmensiSelect = poleVyberu[0];<br>
&emsp;&emsp;StredniSelect = poleVyberu[1];<br>
&emsp;&emsp;NejvetsiSelect = poleVyberu[2];<br>
&emsp;&emsp;<br>
&emsp;&emsp;pripravDataSelectu(NejvetsiSelect);<br>
&emsp;&emsp; -->&emsp;  <br>
&emsp;&emsp; -->&emsp;  private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{&emsp;   <br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;&emsp;  String dotazNejmensi;<br>
&emsp;&emsp; -->&emsp;&emsp;  String dotazStredni;<br>
&emsp;&emsp; -->&emsp;&emsp;  //String dotazNejvetsi;   - zatim nevyuzito<br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;&emsp;  //plati pro dotaz z comboboxu - DotazVpravo<br>
&emsp;&emsp; -->  //&emsp;&emsp;if (vyberDotazVlevo > DotazySQL.length){<br>
&emsp;&emsp; -->  //&emsp;&emsp;&emsp;SQL_GUI_Frame.<br>
&emsp;&emsp; -->  //&emsp;&emsp;}<br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;&emsp;  dotazNejmensi = DotazySQL[vyberDotazVlevo];<br>
&emsp;&emsp; -->&emsp;&emsp;  dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  //String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM <br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp; <br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String castZaFrom;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String castPredFrom;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String NazevTabulky;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] castZaFromArr;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] stringArr;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int indexOfFROM;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  indexOfFROM = originalniSelect.indexOf("FROM");<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  castZaFrom = originalniSelect.substring(indexOfFROM);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  if (NejvetsiDotaz == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  castPredFrom = "SELECT * ";<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  } else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  castPredFrom = originalniSelect.substring(0, indexOfFROM);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }<br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;&emsp;  //Vytvori Select a pripravi data<br>
&emsp;&emsp; -->&emsp;&emsp;  Select selNejmensi = new Select(dotazNejmensi);<br>
&emsp;&emsp; -->&emsp;&emsp;  Select selStredni = new Select(dotazStredni);<br>
&emsp;&emsp; -->  <br>
&emsp;&emsp; -->&emsp;&emsp;  //Vrati data ze Selectu<br>
&emsp;&emsp; -->&emsp;&emsp;  DataSelectuNejmensi = selNejmensi.getDataSelectu();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp; -->&emsp;&emsp;  DataSelectuStredni = selStredni.getDataSelectu();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;&emsp;  NazvySloupcu = selStredni.getNazvySloupcu();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp; -->&emsp;&emsp;  pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  private int[] vratPocetZnakuProVsechnySloupce()<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int pocetSloupcu;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  pocetSloupcu = NazvySloupcu.length;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int pocetZnaku;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;&emsp;  pocetZnaku = vratPocetZnakuProDanySloupec(s);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private int vratPocetZnakuProDanySloupec(int sloupec)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  { //vrati pole s poctem znaku v jednotlivych sloupcich<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;//to proto aby sloupce krasne zarovnal   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String Hodnota;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int nejvicPocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  for (int r = 1; r < DataSelectuStredni.length; r++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  Hodnota = DataSelectuStredni[r][sloupec];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  if (Hodnota != null)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  pocetZnakuHodnoty = Hodnota.length();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;&emsp;  nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return nejvicPocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;&emsp;  pocetZnakuVeSloupcich[s] = pocetZnaku;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  return (pocetZnakuVeSloupcich);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  }<br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;&emsp;  String HlavickaStr;<br>
&emsp;&emsp; -->&emsp;&emsp;  HlavickaStr = vratStringHlavicky();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp; -->&emsp;  }<br>
&emsp;&emsp;<br>
&emsp;&emsp;//vykresli barevny text v zavislosti na druhu vyberu<br>
&emsp;&emsp;if (NejmensiSelect == true){<br>
&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuNejmensi, false);<br>
&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp;}<br>
&emsp;&emsp;if (StredniSelect == true){<br>
&emsp;&emsp;&emsp;PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);<br>
&emsp;&emsp;&emsp;&emsp;-->  <br>
&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuStredni, true);<br>
&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp;}<br>
&emsp;&emsp;if (NejvetsiSelect == true){<br>
&emsp;&emsp;&emsp;//pole se jmenuji stejne jako u stredniho selectu (DataSelectuStredniho obsahuji data nejvetsi)<br>
&emsp;&emsp;&emsp;PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);<br>
&emsp;&emsp;&emsp;&emsp;-->  <br>
&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuStredni, true);<br>
&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{&emsp;   <br>
&emsp;&emsp;<br>
&emsp;&emsp;String dotazNejmensi;<br>
&emsp;&emsp;String dotazStredni;<br>
&emsp;&emsp;//String dotazNejvetsi;   - zatim nevyuzito<br>
&emsp;&emsp;<br>
&emsp;&emsp;//plati pro dotaz z comboboxu - DotazVpravo<br>
//&emsp;&emsp;if (vyberDotazVlevo > DotazySQL.length){<br>
//&emsp;&emsp;&emsp;SQL_GUI_Frame.<br>
//&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;dotazNejmensi = DotazySQL[vyberDotazVlevo];<br>
&emsp;&emsp;dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);<br>
&emsp;&emsp;&emsp;-->&emsp;  public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)<br>
&emsp;&emsp;&emsp;-->&emsp;  {<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  //String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp; <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  String castZaFrom;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  String castPredFrom;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  String NazevTabulky;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] castZaFromArr;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] stringArr;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  int indexOfFROM;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  indexOfFROM = originalniSelect.indexOf("FROM");<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  castZaFrom = originalniSelect.substring(indexOfFROM);<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (NejvetsiDotaz == true){<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  castPredFrom = "SELECT * ";<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  } else {<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  castPredFrom = originalniSelect.substring(0, indexOfFROM);<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;<br>
&emsp;&emsp;//Vytvori Select a pripravi data<br>
&emsp;&emsp;Select selNejmensi = new Select(dotazNejmensi);<br>
&emsp;&emsp;Select selStredni = new Select(dotazStredni);<br>
<br>
&emsp;&emsp;//Vrati data ze Selectu<br>
&emsp;&emsp;DataSelectuNejmensi = selNejmensi.getDataSelectu();<br>
&emsp;&emsp;   -->  <br>
&emsp;&emsp;DataSelectuStredni = selStredni.getDataSelectu();<br>
&emsp;&emsp;   -->  <br>
&emsp;&emsp;<br>
&emsp;&emsp;NazvySloupcu = selStredni.getNazvySloupcu();<br>
&emsp;&emsp;   -->  <br>
&emsp;&emsp;pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();<br>
&emsp;&emsp;   -->&emsp;  private int[] vratPocetZnakuProVsechnySloupce()<br>
&emsp;&emsp;   -->&emsp;  {<br>
&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;<br>
&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = NazvySloupcu.length;<br>
&emsp;&emsp;   -->&emsp;&emsp;  int pocetZnaku;<br>
&emsp;&emsp;   -->&emsp;&emsp;  int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];<br>
&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;   -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++){<br>
&emsp;&emsp;   -->&emsp;&emsp;&emsp;  pocetZnaku = vratPocetZnakuProDanySloupec(s);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private int vratPocetZnakuProDanySloupec(int sloupec)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  { //vrati pole s poctem znaku v jednotlivych sloupcich<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;//to proto aby sloupce krasne zarovnal   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String Hodnota;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int nejvicPocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int r = 1; r < DataSelectuStredni.length; r++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  Hodnota = DataSelectuStredni[r][sloupec];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (Hodnota != null)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetZnakuHodnoty = Hodnota.length();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return nejvicPocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }<br>
&emsp;&emsp;   -->&emsp;&emsp;&emsp;  pocetZnakuVeSloupcich[s] = pocetZnaku;<br>
&emsp;&emsp;   -->&emsp;&emsp;  }<br>
&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;   -->&emsp;&emsp;  return (pocetZnakuVeSloupcich);<br>
&emsp;&emsp;   -->&emsp;  }<br>
&emsp;&emsp;<br>
&emsp;&emsp;String HlavickaStr;<br>
&emsp;&emsp;HlavickaStr = vratStringHlavicky();<br>
&emsp;&emsp;   -->  <br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;//pretizeny kontstruktor - zatim docasne<br>
&emsp;private boolean[][] vratPoleShody(String[][] DataSelectu1, String[][] DataSelectu2){<br>
&emsp;&emsp;<br>
&emsp;&emsp;String[][] vetsiDataSelectu;<br>
&emsp;&emsp;String[][] mensiDataSelectu;<br>
&emsp;&emsp;boolean[][] poleShody;<br>
&emsp;&emsp;boolean JeDelsiDataSelectu2;<br>
&emsp;&emsp;<br>
&emsp;&emsp;String HodnotaVetsiSelect;<br>
&emsp;&emsp;//String HodnotaMensiSelect;<br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean nalezenaShoda;<br>
&emsp;&emsp;<br>
&emsp;&emsp;//Kontroluje ktere pole je vetsi<br>
&emsp;&emsp;JeDelsiDataSelectu2 = DelsiDataSelectu2(DataSelectu1, DataSelectu2);<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;  private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2){<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  //obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  //metoda zjisti ve kterem poli je vice null<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetNullDataSelectu1;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetNullDataSelectu2;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean jeDelsiDataSelectu2;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetNullDataSelectu1 = 0;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetNullDataSelectu2 = 0;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int i = 0; i < DataSelectu1.length; i++) {<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (DataSelectu1[i] == null){<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (DataSelectu2[i] == null){<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (pocetNullDataSelectu2 > pocetNullDataSelectu1){<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  jeDelsiDataSelectu2 = true;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  } else {<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  jeDelsiDataSelectu2 = false;<br>
&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;<br>
&emsp;&emsp;if (JeDelsiDataSelectu2 == true){<br>
&emsp;&emsp;&emsp;vetsiDataSelectu = DataSelectu2;<br>
&emsp;&emsp;&emsp;mensiDataSelectu = DataSelectu1;<br>
&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;vetsiDataSelectu = DataSelectu1;<br>
&emsp;&emsp;&emsp;mensiDataSelectu = DataSelectu2;<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;poleShody = new boolean[vetsiDataSelectu.length][vetsiDataSelectu[0].length];<br>
&emsp;&emsp;<br>
&emsp;&emsp;//prenastavuje polozky na nulu (pro 1. vyhledavani) - pouzito v vratRadekASloupecNalezenePolozkyVPoli<br>
&emsp;&emsp;rPol = 0;<br>
&emsp;&emsp;sPol = 0;<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int s = 0; s < vetsiDataSelectu[0].length; s++) {&emsp;   <br>
&emsp;&emsp;&emsp;for (int r = 0; r < vetsiDataSelectu.length; r++) {<br>
&emsp;&emsp;&emsp;&emsp;HodnotaVetsiSelect = vetsiDataSelectu[r][s];<br>
&emsp;&emsp;&emsp;&emsp;nalezenaShoda = vratRadekASloupecNalezenePolozkyVPoli(mensiDataSelectu, HodnotaVetsiSelect);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String polozkaPole;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean nalezenaShoda = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (HledanaPolozka != null){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  for (int s = 0; s < Pole[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  if(nalezenaShoda == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  break;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  for (int r = 0; r < Pole.length; r++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  polozkaPole = Pole[r][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  if (polozkaPole != null){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (polozkaPole.equals(HledanaPolozka) == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  rPol = r;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  sPol = s;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  nalezenaShoda = true;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (nalezenaShoda);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;//zapisuje nalezene shody do pole<br>
&emsp;&emsp;&emsp;&emsp;poleShody[r][s] = nalezenaShoda;<br>
&emsp; <br>
&emsp;&emsp;&emsp;&emsp;System.out.println(rPol + "  " + sPol);<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;//prekontroluje pole shody, protoze nektere polozky mohou byt spatne oznacene<br>
&emsp;&emsp;poleShody = prekontrolujPoleShody(poleShody, mensiDataSelectu, vetsiDataSelectu);<br>
&emsp;&emsp;&emsp; -->&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;  private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] mensiDataSelectuRadek;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] vetsiDataSelectuRadek;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  String mensiDataSelectuHodnota;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  String vetsiDataSelectuHodnota;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean[] poleShodyRadek;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  int delkaVetsiDataSelectuRadek;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  int delkaMensiDataSelectuRadek;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  //nastavi pole poleShodyNew jako false pro vsechny polozky<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int r = 0; r < poleShodyNew.length; r++) {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  for (int s = 0; s < poleShodyNew[0].length; s++) {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  poleShodyNew[r][s] = false;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  }&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean shodaMVData;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  //vrati dany radek vetsich Dat Selectu&emsp;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean shoda;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String vetsiDataSelectuHodnota;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] radekVetsiDataSelectu;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int s = 0; s < vetsiDataSelectu[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  shoda = poleShody[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (shoda == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  -->  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekVetsiDataSelectu);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  //vetsi radek porovnava se vsemi radky z mensich dat<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  for (int rM = 0; rM < mensiDataSelectu.length; rM++) {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  //metoda volana z prekontrolujPoleShody<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = mensiDataSelectu[0].length;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] radekMensiDataSelectu = new String[pocetSloupcu];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return (radekMensiDataSelectu);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  //nejdrive porovna jejich delku, zda jsou stejne dlouhe<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = true;&emsp; //defaultni hodnota, ktera se prepise<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  for (int s = 0; s < mensiDataSelectuRadek.length; s++) {<br>
&emsp;&emsp;&emsp; -->  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  mensiDataSelectuHodnota = mensiDataSelectuRadek[s];<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;   <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (mensiDataSelectuHodnota != null){<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud jsou hodnoty stejne, pak shodaMVData zustane true<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false){<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  } else {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  if (shodaMVData == true){<br>
&emsp;&emsp;&emsp; -->  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  poleShodyRadek = vratPoleShodyRadek(poleShody, rV);&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  //metoda volana z prekontrolujPoleShody<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = poleShody[0].length;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  boolean[] radekPoleShody = new boolean[pocetSloupcu];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;   for (int s = 0; s < pocetSloupcu; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  radekPoleShody[s] = poleShody[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return (radekPoleShody);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }<br>
&emsp;&emsp;&emsp; -->  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  for (int s = 0; s < poleShody[0].length; s++) {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  poleShodyNew[rV][s] = poleShodyRadek[s];<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  } <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  <br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  } else {<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;<br>
&emsp;&emsp;//this.vetsiDataSelectu = vetsiDataSelectu;<br>
&emsp;&emsp;return(poleShody);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){<br>
&emsp;&emsp;<br>
&emsp;&emsp;String[] mensiDataSelectuRadek;<br>
&emsp;&emsp;String[] vetsiDataSelectuRadek;<br>
&emsp;&emsp;String mensiDataSelectuHodnota;<br>
&emsp;&emsp;String vetsiDataSelectuHodnota;<br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean[] poleShodyRadek;<br>
&emsp;&emsp;<br>
&emsp;&emsp;int delkaVetsiDataSelectuRadek;<br>
&emsp;&emsp;int delkaMensiDataSelectuRadek;<br>
&emsp;&emsp;<br>
&emsp;&emsp;//nastavi pole poleShodyNew jako false pro vsechny polozky<br>
&emsp;&emsp;boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];<br>
&emsp;&emsp;for (int r = 0; r < poleShodyNew.length; r++) {<br>
&emsp;&emsp;&emsp;for (int s = 0; s < poleShodyNew[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;poleShodyNew[r][s] = false;<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}&emsp;  <br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean shodaMVData;<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {<br>
&emsp;&emsp;&emsp;//vrati dany radek vetsich Dat Selectu&emsp;<br>
&emsp;&emsp;&emsp;vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;  //metoda volana z prekontrolujPoleShody<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;  private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean shoda;<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  String vetsiDataSelectuHodnota;<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] radekVetsiDataSelectu;<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int s = 0; s < vetsiDataSelectu[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  shoda = poleShody[radek][s];<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  if (shoda == true){<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->  <br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp; -->   <br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->  <br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  return (radekVetsiDataSelectu);<br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp; -->&emsp;  }<br>
&emsp;&emsp;&emsp;delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;//vetsi radek porovnava se vsemi radky z mensich dat<br>
&emsp;&emsp;&emsp;for (int rM = 0; rM < mensiDataSelectu.length; rM++) {<br>
&emsp;&emsp;&emsp;&emsp;mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetSloupcu;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetSloupcu = mensiDataSelectu[0].length;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] radekMensiDataSelectu = new String[pocetSloupcu];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekMensiDataSelectu);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;//nejdrive porovna jejich delku, zda jsou stejne dlouhe<br>
&emsp;&emsp;&emsp;&emsp;delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;<br>
&emsp;&emsp;&emsp;&emsp;if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji<br>
&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = true;&emsp; //defaultni hodnota, ktera se prepise<br>
&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < mensiDataSelectuRadek.length; s++) {<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectuRadek[s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp; <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota != null){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud jsou hodnoty stejne, pak shodaMVData zustane true<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek<br>
&emsp;&emsp;&emsp;&emsp;&emsp;if (shodaMVData == true){<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShodyRadek = vratPoleShodyRadek(poleShody, rV);&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetSloupcu;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetSloupcu = poleShody[0].length;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean[] radekPoleShody = new boolean[pocetSloupcu];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;   for (int s = 0; s < pocetSloupcu; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  radekPoleShody[s] = poleShody[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekPoleShody);<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShodyNew[rV][s] = poleShodyRadek[s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;} <br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit<br>
&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return (poleShodyNew);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;//metoda volana z prekontrolujPoleShody<br>
&emsp;private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek){<br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean shoda;<br>
&emsp;&emsp;String vetsiDataSelectuHodnota;<br>
&emsp;&emsp;ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();<br>
&emsp;&emsp;String[] radekVetsiDataSelectu;<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int s = 0; s < vetsiDataSelectu[0].length; s++) {<br>
&emsp;&emsp;&emsp;shoda = poleShody[radek][s];<br>
&emsp;&emsp;&emsp;if (shoda == true){<br>
&emsp;&emsp;&emsp;&emsp;vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];<br>
&emsp;&emsp;&emsp;&emsp;radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);<br>
&emsp;&emsp;&emsp;&emsp; -->  <br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}<br>
 <br>
&emsp;&emsp;radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);<br>
&emsp;&emsp;&emsp;-->  <br>
&emsp;&emsp;return (radekVetsiDataSelectu);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;//metoda volana z prekontrolujPoleShody<br>
&emsp;private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek){<br>
&emsp;&emsp;<br>
&emsp;&emsp;int pocetSloupcu;<br>
&emsp;<br>
&emsp;&emsp;pocetSloupcu = mensiDataSelectu[0].length;<br>
&emsp;&emsp;String[] radekMensiDataSelectu = new String[pocetSloupcu];<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int s = 0; s < pocetSloupcu; s++) {<br>
&emsp;&emsp;&emsp;radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return (radekMensiDataSelectu);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;&emsp;  <br>
&emsp;//metoda volana z prekontrolujPoleShody<br>
&emsp;private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek){<br>
&emsp;&emsp;<br>
&emsp;&emsp;int pocetSloupcu;<br>
&emsp;&emsp;<br>
&emsp;&emsp;pocetSloupcu = poleShody[0].length;<br>
&emsp;&emsp;boolean[] radekPoleShody = new boolean[pocetSloupcu];<br>
&emsp;&emsp;<br>
&emsp;&emsp; for (int s = 0; s < pocetSloupcu; s++) {<br>
&emsp;&emsp;&emsp;radekPoleShody[s] = poleShody[radek][s];<br>
&emsp;&emsp;}<br>
&emsp;&emsp; <br>
&emsp;&emsp;return (radekPoleShody);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;private void prekontrolujPoleShody2(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu){<br>
&emsp;&emsp;<br>
&emsp;&emsp;String[] mensiDataSelectuRadek;<br>
&emsp;&emsp;String[] vetsiDataSelectuRadek;<br>
<br>
&emsp;&emsp;mensiDataSelectuRadek = new String[5];<br>
&emsp;&emsp;vetsiDataSelectuRadek = new String[5];<br>
&emsp;&emsp;<br>
&emsp;&emsp;String mensiDataSelectuHodnota;<br>
&emsp;&emsp;String mensiDataSelectuHodnota0;&emsp;//hodnota z 0-teho sloupce<br>
&emsp;&emsp;String vetsiDataSelectHodnota;<br>
&emsp;&emsp;String vetsiDataSelectHodnota0;&emsp; //hodnota z 0-teho sloupce<br>
&emsp;&emsp;<br>
&emsp;   <br>
&emsp;&emsp;boolean shoda;<br>
&emsp;&emsp;boolean shoda0;&emsp;&emsp;&emsp;&emsp;&emsp; //shoda z 0-teho sloupce<br>
&emsp;&emsp;boolean shodnyRadek;<br>
&emsp;&emsp;boolean shodnyRadekNalezen;<br>
&emsp;&emsp;int posledniRV = 0;<br>
&emsp;&emsp;<br>
&emsp;&emsp;//index rM udava cislo radku mensiDataSelectu<br>
&emsp;&emsp;for (int rM = 0; rM < mensiDataSelectu.length; rM++) {<br>
&emsp;&emsp;&emsp;mensiDataSelectuHodnota0 = mensiDataSelectu[rM][0];<br>
 <br>
&emsp;&emsp;&emsp;//vychozi hodnota, ktera se prepisuje<br>
&emsp;&emsp;&emsp;shodnyRadekNalezen = false;<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;//index rV udava cislo radku vetsiDataSelectu<br>
&emsp;&emsp;&emsp;for (int rV = 0; rV < vetsiDataSelectu.length; rV++) {<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;//vychozi hodnota, ktera se prepisuje<br>
&emsp;&emsp;&emsp;&emsp;shodnyRadek = true;<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;//v okamziku, kdy shodny radek byl jiz nalezen<br>
&emsp;&emsp;&emsp;&emsp;if (shodnyRadekNalezen == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;   <br>
&emsp;&emsp;&emsp;&emsp;//vyhledava, kde je shoda == true v 0-tem sloupci<br>
&emsp;&emsp;&emsp;&emsp;shoda0 = poleShody[rV][0];<br>
&emsp;&emsp;&emsp;&emsp;if (shoda0 == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//pokud je shoda v 0-tem sloupci, <br>
&emsp;&emsp;&emsp;&emsp;&emsp;//pak porovna hodnotu mensiDataSelectu a vetsiDataSelectu<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//ve sloupci 0<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota0 = vetsiDataSelectu[rV][0];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota0.equals(vetsiDataSelectHodnota0) == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud hodnoty mensiho a vetsiho Selectu<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//jsou stejne - uvazovane pro stejny sloupec, ale jiny radek<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pak se porovnaji hodnoty i pro ostatni sloupce<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 1; s < mensiDataSelectu[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectu[rM][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud nejaka hodnota neni stejna (z nejakeho sloupce),<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pak se nastavi na false a dal uz se nepokracuje<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//(shoda0 == false) <br>
&emsp;&emsp;&emsp;&emsp;&emsp;//shodnyRadek = false muze nabit hodnoty(false) vicero zpusoby<br>
&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;if (shodnyRadek == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadekNalezen = true;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;posledniRV = rV + 1;<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;if (shodnyRadek == false){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShody[rV][s] = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;   <br>
//&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < mensiDataSelectu[0].length; s++) {<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectu[rM][s];<br>
//&emsp;&emsp;&emsp;&emsp;<br>
//&emsp;&emsp;&emsp;&emsp;<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;shoda = poleShody[rV][s];<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;if (shoda == true){<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false) {<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;  //  if (mensiDataSelectuHodnota != vetsiDataSelectHodnota){<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
//&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;<br>
//&emsp;&emsp;&emsp;int d = poleShody[0].length;<br>
<br>
&emsp;&emsp;&emsp;//nejedna-li se o shodny radek <br>
&emsp;&emsp;&emsp;//tzn. radek mensiDataSelectu != radku vetsiDataSelectu<br>
&emsp;&emsp;&emsp;//pak prepise vsechny true na danem radku na false<br>
&emsp;&emsp;&emsp;//(to je taky cilem opravy, jelikoz v puvodnim poleShody tomu tak nemusi byt)<br>
//&emsp;&emsp;&emsp;if (shodnyRadek == false){<br>
//&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) {<br>
//&emsp;&emsp;&emsp;&emsp;&emsp;poleShody[r][s] = false;<br>
//&emsp;&emsp;&emsp;&emsp;}<br>
//&emsp;&emsp;&emsp;}<br>
//&emsp;&emsp;&emsp;d = poleShody[0].length;<br>
&emsp;&emsp;}<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;public JTextPane getBarevnyText(){<br>
&emsp;//public JScrollPane getBarevnyText(){&emsp;<br>
&emsp;&emsp;//return (jTextPane1);<br>
&emsp;&emsp;//return (jTextPane2);<br>
&emsp;&emsp;return (jTextPane3);<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka){<br>
&emsp;&emsp;<br>
&emsp;&emsp;String polozkaPole;<br>
&emsp;&emsp;boolean nalezenaShoda = false;<br>
&emsp;&emsp;<br>
&emsp;&emsp;if (HledanaPolozka != null){<br>
&emsp;&emsp;<br>
&emsp;&emsp;&emsp;for (int s = 0; s < Pole[0].length; s++) {<br>
&emsp;&emsp;&emsp;&emsp;if(nalezenaShoda == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;for (int r = 0; r < Pole.length; r++) {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;polozkaPole = Pole[r][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;if (polozkaPole != null){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (polozkaPole.equals(HledanaPolozka) == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rPol = r;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sPol = s;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nalezenaShoda = true;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return (nalezenaShoda);<br>
<br>
&emsp;}<br>
&emsp;<br>
&emsp;&emsp;&emsp;<br>
&emsp;private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2){<br>
&emsp;&emsp;//obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty<br>
&emsp;&emsp;//metoda zjisti ve kterem poli je vice null<br>
&emsp;&emsp;<br>
&emsp;&emsp;int pocetNullDataSelectu1;<br>
&emsp;&emsp;int pocetNullDataSelectu2;<br>
&emsp;&emsp;<br>
&emsp;&emsp;boolean jeDelsiDataSelectu2;<br>
&emsp;&emsp;<br>
&emsp;&emsp;pocetNullDataSelectu1 = 0;<br>
&emsp;&emsp;pocetNullDataSelectu2 = 0;<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int i = 0; i < DataSelectu1.length; i++) {<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;if (DataSelectu1[i] == null){<br>
&emsp;&emsp;&emsp;&emsp;pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;if (DataSelectu2[i] == null){<br>
&emsp;&emsp;&emsp;&emsp;pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;if (pocetNullDataSelectu2 > pocetNullDataSelectu1){<br>
&emsp;&emsp;&emsp;jeDelsiDataSelectu2 = true;<br>
&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;jeDelsiDataSelectu2 = false;<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return (jeDelsiDataSelectu2);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp; private String vratStringHlavicky(){<br>
&emsp;  <br>
&emsp;&emsp;String NazevSloupce;<br>
&emsp;&emsp;String HlavickaStr;<br>
&emsp;&emsp;int pocetZnakuVeSloupci;<br>
&emsp;&emsp;String ZbyvajiciMezery;<br>
&emsp;&emsp;<br>
&emsp;&emsp;HlavickaStr = "";<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int s = 1; s <= NazvySloupcu.length; s++) {<br>
&emsp;&emsp;&emsp;NazevSloupce = NazvySloupcu[s-1];<br>
&emsp;&emsp;&emsp;pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s-1];<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, NazevSloupce);<br>
&emsp;&emsp;&emsp;HlavickaStr = HlavickaStr + "  " + ZbyvajiciMezery;<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return(HlavickaStr);<br>
&emsp;}<br>
&emsp; <br>
&emsp; <br>
&emsp;private String doplnZbyvajiciMezery(int pocetZnakuSloupce, String Hodnota)<br>
&emsp;{<br>
&emsp;&emsp;String ZbyvajiciMezery;<br>
&emsp;&emsp;int pocetZnakuMezer;<br>
&emsp;&emsp;<br>
&emsp;&emsp;if (Hodnota != null){<br>
&emsp;&emsp;&emsp;   <br>
&emsp;&emsp;&emsp;pocetZnakuMezer = pocetZnakuSloupce - Hodnota.length();<br>
&emsp;&emsp;&emsp;ZbyvajiciMezery = Hodnota;<br>
<br>
&emsp;&emsp;&emsp;//doplni retezec o mezery<br>
&emsp;&emsp;&emsp;for (int i = 0; i < pocetZnakuMezer; i++) {<br>
&emsp;&emsp;&emsp;&emsp; ZbyvajiciMezery = ZbyvajiciMezery + " "; <br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;} <br>
&emsp;&emsp;else<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;ZbyvajiciMezery = "";<br>
&emsp;&emsp;}&emsp;<br>
&emsp;&emsp;<br>
&emsp;&emsp;return (ZbyvajiciMezery);<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp; <br>
&emsp; <br>
&emsp;private int[] vratPocetZnakuProVsechnySloupce()<br>
&emsp;{<br>
&emsp;&emsp;int pocetSloupcu;<br>
&emsp;&emsp;pocetSloupcu = NazvySloupcu.length;<br>
&emsp;&emsp;int pocetZnaku;<br>
&emsp;&emsp;int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int s = 0; s < pocetSloupcu; s++){<br>
&emsp;&emsp;&emsp;pocetZnaku = vratPocetZnakuProDanySloupec(s);<br>
&emsp;&emsp;&emsp;pocetZnakuVeSloupcich[s] = pocetZnaku;<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return (pocetZnakuVeSloupcich);<br>
&emsp;}<br>
&emsp; <br>
&emsp; <br>
&emsp;private int vratPocetZnakuProDanySloupec(int sloupec)<br>
&emsp;{ //vrati pole s poctem znaku v jednotlivych sloupcich<br>
&emsp;  //to proto aby sloupce krasne zarovnal   <br>
&emsp;<br>
&emsp;&emsp;String Hodnota;<br>
&emsp;&emsp;int nejvicPocetZnakuHodnoty;<br>
&emsp;&emsp;int pocetZnakuHodnoty;<br>
&emsp;&emsp;<br>
&emsp;&emsp;//jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce<br>
&emsp;&emsp;nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();<br>
&emsp;&emsp;<br>
&emsp;&emsp;for (int r = 1; r < DataSelectuStredni.length; r++) {<br>
&emsp;&emsp;&emsp;Hodnota = DataSelectuStredni[r][sloupec];<br>
&emsp;&emsp;&emsp;if (Hodnota != null)<br>
&emsp;&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;&emsp;pocetZnakuHodnoty = Hodnota.length();<br>
&emsp;&emsp;&emsp;&emsp;if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;return nejvicPocetZnakuHodnoty;<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;&emsp;&emsp;<br>
&emsp;<br>
&emsp;private void vratBarevnyText(String[][] DataSelectu, boolean zvyraznujPolozky){<br>
&emsp;&emsp;<br>
&emsp;&emsp;String hodnota;<br>
&emsp;&emsp;String mezera;<br>
&emsp;&emsp;String hodnotaM;<br>
&emsp;&emsp;int delkaDoc;<br>
&emsp;&emsp;boolean shoda;<br>
&emsp;&emsp;<br>
&emsp;&emsp;String ZbyvajiciMezery;<br>
&emsp;&emsp;int pocetZnakuVeSloupci;<br>
&emsp;&emsp;<br>
&emsp;&emsp;//StyledDocument doc = jTextPane2.getStyledDocument();<br>
&emsp;&emsp;StyledDocument doc = jTextPane3.getStyledDocument();<br>
&emsp;&emsp;<br>
&emsp;&emsp;SimpleAttributeSet keyWord = new SimpleAttributeSet();<br>
&emsp;&emsp;StyleConstants.setForeground(keyWord, Color.RED);<br>
&emsp;&emsp;<br>
&emsp;&emsp;hodnota = "xxx";<br>
&emsp;&emsp;mezera = "  ";<br>
&emsp;&emsp;hodnotaM = "";<br>
&emsp;&emsp;<br>
&emsp;&emsp;delkaDoc = 0;<br>
&emsp;&emsp;<br>
&emsp;&emsp;try<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;//jTextPane2.setText(""); <br>
&emsp;&emsp;&emsp;jTextPane3.setText("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   \n"); <br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;//doc.insertString(0, "<html>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; </html>", keyWord );<br>
&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;//index r = -1 plati pro hlavicku<br>
&emsp;&emsp;&emsp;for (int r = -1; r < DataSelectu.length; r++) { <br>
&emsp;&emsp;&emsp; <br>
&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < DataSelectu[0].length; s++) {&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;if (r == -1){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//jedna se o hlavicku&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hodnota = NazvySloupcu[s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//jedna se o tabulku&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//Zvyraznuje polozky jeb v pripade, pokud zvyraznujPolozky == true<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (zvyraznujPolozky == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = PoleShody[r][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = false;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hodnota = DataSelectu[r][s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;delkaDoc = doc.getLength();<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s];<br>
&emsp;&emsp;&emsp;&emsp;&emsp;ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, hodnota);<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;hodnotaM = ZbyvajiciMezery + "   ";<br>
&emsp;<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//oznaci danou bunku v zavislosti na tom, zda nalezl shodu ci nikoliv<br>
&emsp;&emsp;&emsp;&emsp;&emsp;if (shoda == true){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), hodnotaM, keyWord );<br>
&emsp;&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), hodnotaM, null );<br>
&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;}  <br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;&emsp;&emsp;&emsp;if (r == -1){<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//za hlavicku vlozi prazdny radek + novy rasek   <br>
&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\n\n", null );<br>
&emsp;&emsp;&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;//janak vklada pouze novy radek<br>
&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\n", null );<br>
&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;catch(Exception e) { System.out.println(e); }<br>
&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;//pokud je NejvetsiDotaz = true, pak vraci nejvetsi dotaz, jinak stredni dotaz<br>
&emsp;public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)<br>
&emsp;{<br>
&emsp;&emsp;<br>
&emsp;&emsp;<br>
&emsp;&emsp;//String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...<br>
&emsp;&emsp;String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM <br>
&emsp;   <br>
&emsp;&emsp;String castZaFrom;<br>
&emsp;&emsp;String castPredFrom;<br>
&emsp;&emsp;String NazevTabulky;<br>
&emsp;&emsp;String[] castZaFromArr;<br>
&emsp;&emsp;String[] stringArr;<br>
&emsp;&emsp;int indexOfFROM;<br>
&emsp;&emsp;<br>
&emsp;&emsp;indexOfFROM = originalniSelect.indexOf("FROM");<br>
&emsp;&emsp;castZaFrom = originalniSelect.substring(indexOfFROM);<br>
&emsp;&emsp;<br>
&emsp;&emsp;if (NejvetsiDotaz == true){<br>
&emsp;&emsp;&emsp;castPredFrom = "SELECT * ";<br>
&emsp;&emsp;} else {<br>
&emsp;&emsp;&emsp;castPredFrom = originalniSelect.substring(0, indexOfFROM);<br>
&emsp;&emsp;}<br>
&emsp;   <br>
&emsp;&emsp;castZaFromArr = castZaFrom.split(" ");<br>
&emsp;&emsp;NazevTabulky = castZaFromArr[1];<br>
&emsp;&emsp;stringArr = NazevTabulky.split("\n");<br>
&emsp;&emsp;if (stringArr.length > 0)<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;NazevTabulky = stringArr[0];<br>
&emsp;&emsp;}<br>
&emsp;&emsp;<br>
&emsp;&emsp;plnySelect = castPredFrom + "FROM " + NazevTabulky;<br>
&emsp;&emsp;<br>
&emsp;&emsp;<br>
&emsp;&emsp;return(plnySelect);<br>
&emsp;&emsp;&emsp;&emsp;<br>
&emsp;}<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;<br>
&emsp;//nepotrebne<br>
&emsp;<br>
&emsp;private void vratBarevnyText2(){<br>
&emsp;&emsp;<br>
&emsp;&emsp;//jTextPane2.setText( "original text" );<br>
&emsp;&emsp;jTextPane3.setText( "original text" );<br>
&emsp;&emsp;//StyledDocument doc = jTextPane2.getStyledDocument();<br>
&emsp;&emsp;StyledDocument doc = jTextPane3.getStyledDocument();<br>
<br>
&emsp;&emsp;//  Define a keyword attribute<br>
<br>
&emsp;&emsp;SimpleAttributeSet keyWord = new SimpleAttributeSet();<br>
&emsp;&emsp;StyleConstants.setForeground(keyWord, Color.RED);<br>
&emsp;&emsp;StyleConstants.setBackground(keyWord, Color.YELLOW);<br>
&emsp;&emsp;StyleConstants.setBold(keyWord, true);<br>
<br>
&emsp;&emsp;//  Add some text<br>
&emsp;&emsp;try<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;doc.insertString(0, "Start of text\n", null );<br>
&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\nEnd of text", keyWord );<br>
&emsp;&emsp;}<br>
&emsp;&emsp;catch(Exception e) { System.out.println(e); }<br>
&emsp;   <br>
<br>
&emsp;}<br>
<br>
}<br>
