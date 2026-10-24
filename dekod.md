$\color{red}{}$
$\color{red}{package sql\\_gui;}$
$$\color{red}{}$$
$$\color{red}{import java.awt.Color;}$$
$$\color{red}{import java.sql.SQLException;}$$
$$\color{red}{import java.util.ArrayList;}$$<br>
$$\color{red}{import java.util.Arrays;}$$<br>
$$\color{red}{import javax.swing.JScrollPane;}$$<br>
$$\color{red}{import javax.swing.JTextPane;}$$<br>
$$\color{red}{import javax.swing.text.SimpleAttributeSet;}$$<br>
$$\color{red}{import javax.swing.text.StyleConstants;}$$<br>
$$\color{red}{import javax.swing.text.StyledDocument;}$$<br>
$$\color{red}{//}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{public class BarevnyJTextArea \\{}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private JTextPane jTextPane3;}$$<br>
$$\color{red}{&emsp;private boolean[][] PoleShody;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private int rPol;}$$<br>
$$\color{red}{&emsp;private int sPol;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private String[] DotazySQL;}$$<br>
$$\color{red}{&emsp;int vyberDotazVlevo;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;String[][] DataSelectuNejmensi;}$$<br>
$$\color{red}{&emsp;String[][] DataSelectuStredni;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;String[] NazvySloupcu;}$$<br>
$$\color{red}{&emsp;int[] pocetZnakuVeSloupcich;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;//Konstruktor}$$<br>
$$\color{red}{&emsp;BarevnyJTextArea(JTextPane jTextPane1, String[] DotazySQL, int vyberDotazVlevo, boolean[] poleVyberu) throws SQLException, ClassNotFoundException \\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;this.jTextPane3 = jTextPane1;}$$<br>
$$\color{red}{&emsp;&emsp;this.DotazySQL = DotazySQL;}$$<br>
$$\color{red}{&emsp;&emsp;this.vyberDotazVlevo = vyberDotazVlevo;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean NejmensiSelect;}$$<br>
$$\color{red}{&emsp;&emsp;boolean StredniSelect;}$$<br>
$$\color{red}{&emsp;&emsp;boolean NejvetsiSelect;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean zvyraznujPolozky;}$$<br>
$$\color{red}{&emsp;&emsp;zvyraznujPolozky = false;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;NejmensiSelect = poleVyberu[0];}$$<br>
$$\color{red}{&emsp;&emsp;StredniSelect = poleVyberu[1];}$$<br>
$$\color{red}{&emsp;&emsp;NejvetsiSelect = poleVyberu[2];}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;pripravDataSelectu(NejvetsiSelect);}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;  private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException\\{&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  String dotazNejmensi;}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  String dotazStredni;}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  //String dotazNejvetsi;   - zatim nevyuzito}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  //plati pro dotaz z comboboxu - DotazVpravo}$$<br>
$$\color{red}{&emsp;&emsp; -->  //&emsp;&emsp;if (vyberDotazVlevo > DotazySQL.length)\\{}$$<br>
$$\color{red}{&emsp;&emsp; -->  //&emsp;&emsp;&emsp;SQL\\_GUI\\_Frame.}$$<br>
$$\color{red}{&emsp;&emsp; -->  //&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  dotazNejmensi = DotazySQL[vyberDotazVlevo];}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  //String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp; }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String castZaFrom;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String castPredFrom;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String NazevTabulky;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] castZaFromArr;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] stringArr;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int indexOfFROM;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  indexOfFROM = originalniSelect.indexOf("FROM");}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  castZaFrom = originalniSelect.substring(indexOfFROM);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  if (NejvetsiDotaz == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  castPredFrom = "SELECT * ";}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  } else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  castPredFrom = originalniSelect.substring(0, indexOfFROM);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  //Vytvori Select a pripravi data}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  Select selNejmensi = new Select(dotazNejmensi);}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  Select selStredni = new Select(dotazStredni);}$$<br>
$$\color{red}{&emsp;&emsp; -->  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  //Vrati data ze Selectu}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  DataSelectuNejmensi = selNejmensi.getDataSelectu();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  DataSelectuStredni = selStredni.getDataSelectu();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  NazvySloupcu = selStredni.getNazvySloupcu();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  private int[] vratPocetZnakuProVsechnySloupce()}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  pocetSloupcu = NazvySloupcu.length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int pocetZnaku;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;&emsp;  pocetZnaku = vratPocetZnakuProDanySloupec(s);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private int vratPocetZnakuProDanySloupec(int sloupec)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  \\{ //vrati pole s poctem znaku v jednotlivych sloupcich}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;//to proto aby sloupce krasne zarovnal   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String Hodnota;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int nejvicPocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  for (int r = 1; r < DataSelectuStredni.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  Hodnota = DataSelectuStredni[r][sloupec];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  if (Hodnota != null)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  pocetZnakuHodnoty = Hodnota.length();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;&emsp;  nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return nejvicPocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;&emsp;  pocetZnakuVeSloupcich[s] = pocetZnaku;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;&emsp;  return (pocetZnakuVeSloupcich);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  String HlavickaStr;}$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  HlavickaStr = vratStringHlavicky();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp; -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//vykresli barevny text v zavislosti na druhu vyberu}$$<br>
$$\color{red}{&emsp;&emsp;if (NejmensiSelect == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuNejmensi, false);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;if (StredniSelect == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;-->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuStredni, true);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;if (NejvetsiSelect == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//pole se jmenuji stejne jako u stredniho sel}\color{red}{ectu (DataSelectuStredniho obsahuji data nejvetsi)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;PoleShody = vratPoleShody(DataSelectuStredni, DataSelectuNejmensi);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;-->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;vratBarevnyText(DataSelectuStredni, true);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException\\{&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String dotazNejmensi;}$$<br>
$$\color{red}{&emsp;&emsp;String dotazStredni;}$$<br>
$$\color{red}{&emsp;&emsp;//String dotazNejvetsi;   - zatim nevyuzito}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//plati pro dotaz z comboboxu - DotazVpravo}$$<br>
$$\color{red}{//&emsp;&emsp;if (vyberDotazVlevo > DotazySQL.length)\\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;SQL\\_GUI\\_Frame.}$$<br>
$$\color{red}{//&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;dotazNejmensi = DotazySQL[vyberDotazVlevo];}$$<br>
$$\color{red}{&emsp;&emsp;dotazStredni = vratSelectyNaVetsiDotaz(dotazNejmensi, NejvetsiDotaz);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;  public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;  \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  //String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp; }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String castZaFrom;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String castPredFrom;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String NazevTabulky;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] castZaFromArr;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] stringArr;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  int indexOfFROM;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  indexOfFROM = originalniSelect.indexOf("FROM");}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  castZaFrom = originalniSelect.substring(indexOfFROM);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (NejvetsiDotaz == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  castPredFrom = "SELECT * ";}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  } else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  castPredFrom = originalniSelect.substring(0, indexOfFROM);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//Vytvori Select a pripravi data}$$<br>
$$\color{red}{&emsp;&emsp;Select selNejmensi = new Select(dotazNejmensi);}$$<br>
$$\color{red}{&emsp;&emsp;Select selStredni = new Select(dotazStredni);}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;//Vrati data ze Selectu}$$<br>
$$\color{red}{&emsp;&emsp;DataSelectuNejmensi = selNejmensi.getDataSelectu();}$$<br>
$$\color{red}{&emsp;&emsp;   -->  }$$<br>
$$\color{red}{&emsp;&emsp;DataSelectuStredni = selStredni.getDataSelectu();}$$<br>
$$\color{red}{&emsp;&emsp;   -->  }$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;NazvySloupcu = selStredni.getNazvySloupcu();}$$<br>
$$\color{red}{&emsp;&emsp;   -->  }$$<br>
$$\color{red}{&emsp;&emsp;pocetZnakuVeSloupcich = vratPocetZnakuProVsechnySloupce();}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;  private int[] vratPocetZnakuProVsechnySloupce()}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;  \\{}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = NazvySloupcu.length;}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  int pocetZnaku;}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++)\\{}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;&emsp;  pocetZnaku = vratPocetZnakuProDanySloupec(s);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private int vratPocetZnakuProDanySloupec(int sloupec)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  \\{ //vrati pole s poctem znaku v jednotlivych sloupcich}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;//to proto aby sloupce krasne zarovnal   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String Hodnota;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int nejvicPocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  //jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int r = 1; r < DataSelectuStredni.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  Hodnota = DataSelectuStredni[r][sloupec];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (Hodnota != null)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetZnakuHodnoty = Hodnota.length();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return nejvicPocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;&emsp;  pocetZnakuVeSloupcich[s] = pocetZnaku;}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;&emsp;  return (pocetZnakuVeSloupcich);}$$<br>
$$\color{red}{&emsp;&emsp;   -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String HlavickaStr;}$$<br>
$$\color{red}{&emsp;&emsp;HlavickaStr = vratStringHlavicky();}$$<br>
$$\color{red}{&emsp;&emsp;   -->  }$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;//pretizeny kontstruktor - zatim docasne}$$<br>
$$\color{red}{&emsp;private boolean[][] vratPoleShody(String[][] DataSelectu1, String[][] DataSelectu2)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String[][] vetsiDataSelectu;}$$<br>
$$\color{red}{&emsp;&emsp;String[][] mensiDataSelectu;}$$<br>
$$\color{red}{&emsp;&emsp;boolean[][] poleShody;}$$<br>
$$\color{red}{&emsp;&emsp;boolean JeDelsiDataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String HodnotaVetsiSelect;}$$<br>
$$\color{red}{&emsp;&emsp;//String HodnotaMensiSelect;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean nalezenaShoda;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//Kontroluje ktere pole je vetsi}$$<br>
$$\color{red}{&emsp;&emsp;JeDelsiDataSelectu2 = DelsiDataSelectu2(DataSelectu1, DataSelectu2);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;  private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  //obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  //metoda zjisti ve kterem poli je vice null}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetNullDataSelectu1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetNullDataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean jeDelsiDataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetNullDataSelectu1 = 0;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetNullDataSelectu2 = 0;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int i = 0; i < DataSelectu1.length; i++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (DataSelectu1[i] == null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (DataSelectu2[i] == null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (pocetNullDataSelectu2 > pocetNullDataSelectu1)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  jeDelsiDataSelectu2 = true;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  } else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  jeDelsiDataSelectu2 = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;if (JeDelsiDataSelectu2 == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;vetsiDataSelectu = DataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;mensiDataSelectu = DataSelectu1;}$$<br>
$$\color{red}{&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;vetsiDataSelectu = DataSelectu1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;mensiDataSelectu = DataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;poleShody = new boolean[vetsiDataSelectu.length][vetsiDataSelectu[0].length];}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//prenastavuje polozky na nulu (pro 1. vyhledavani) - pouzito v vratRadekASloupecNalezenePolozkyVPoli}$$<br>
$$\color{red}{&emsp;&emsp;rPol = 0;}$$<br>
$$\color{red}{&emsp;&emsp;sPol = 0;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int s = 0; s < vetsiDataSelectu[0].length; s++) \\{&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int r = 0; r < vetsiDataSelectu.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;HodnotaVetsiSelect = vetsiDataSelectu[r][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;nalezenaShoda = vratRadekASloupecNalezenePolozkyVPoli(mensiDataSelectu, HodnotaVetsiSelect);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String polozkaPole;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean nalezenaShoda = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  if (HledanaPolozka != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  for (int s = 0; s < Pole[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  if(nalezenaShoda == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  for (int r = 0; r < Pole.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  polozkaPole = Pole[r][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  if (polozkaPole != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (polozkaPole.equals(HledanaPolozka) == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  rPol = r;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  sPol = s;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  nalezenaShoda = true;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (nalezenaShoda);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;//zapisuje nalezene shody do pole}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;poleShody[r][s] = nalezenaShoda;}$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;System.out.println(rPol + "  " + sPol);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//prekontroluje pole shody, protoze nektere polozky mohou byt spatne oznacene}$$<br>
$$\color{red}{&emsp;&emsp;poleShody = prekontrolujPoleShody(poleShody, mensiDataSelectu, vetsiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;  private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] mensiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] vetsiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String mensiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  String vetsiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean[] poleShodyRadek;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  int delkaVetsiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  int delkaMensiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  //nastavi pole poleShodyNew jako false pro vsechny polozky}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int r = 0; r < poleShodyNew.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  for (int s = 0; s < poleShodyNew[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  poleShodyNew[r][s] = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean shodaMVData;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int rV = 0; rV < vetsiDataSelectu.length; rV++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  //vrati dany radek vetsich Dat Selectu&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean shoda;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String vetsiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] radekVetsiDataSelectu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int s = 0; s < vetsiDataSelectu[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  shoda = poleShody[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  if (shoda == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;&emsp;  radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekVetsiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  //vetsi radek porovnava se vsemi radky z mensich dat}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  for (int rM = 0; rM < mensiDataSelectu.length; rM++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  //metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = mensiDataSelectu[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  String[] radekMensiDataSelectu = new String[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return (radekMensiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  //nejdrive porovna jejich delku, zda jsou stejne dlouhe}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = true;&emsp; //defaultni hodnota, ktera se prepise}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  for (int s = 0; s < mensiDataSelectuRadek.length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  mensiDataSelectuHodnota = mensiDataSelectuRadek[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (mensiDataSelectuHodnota != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud jsou hodnoty stejne, pak shodaMVData zustane true}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  } else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  if (shodaMVData == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  poleShodyRadek = vratPoleShodyRadek(poleShody, rV);&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  //metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  pocetSloupcu = poleShody[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  boolean[] radekPoleShody = new boolean[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;   for (int s = 0; s < pocetSloupcu; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;&emsp;  radekPoleShody[s] = poleShody[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  return (radekPoleShody);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  for (int s = 0; s < poleShody[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  poleShodyNew[rV][s] = poleShodyRadek[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  } }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  } else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  //pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;&emsp;  shodaMVData = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//this.vetsiDataSelectu = vetsiDataSelectu;}$$<br>
$$\color{red}{&emsp;&emsp;return(poleShody);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private boolean[][] prekontrolujPoleShody(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String[] mensiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;String[] vetsiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;String mensiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;String vetsiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean[] poleShodyRadek;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;int delkaVetsiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;int delkaMensiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//nastavi pole poleShodyNew jako false pro vsechny polozky}$$<br>
$$\color{red}{&emsp;&emsp;boolean[][] poleShodyNew = new boolean[poleShody.length][poleShody[0].length];}$$<br>
$$\color{red}{&emsp;&emsp;for (int r = 0; r < poleShodyNew.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int s = 0; s < poleShodyNew[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;poleShodyNew[r][s] = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean shodaMVData;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int rV = 0; rV < vetsiDataSelectu.length; rV++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//vrati dany radek vetsich Dat Selectu&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;vetsiDataSelectuRadek = vratVetsiDataSelectuRadek(poleShody, vetsiDataSelectu, rV);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;  //metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;  private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  boolean shoda;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  String vetsiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  String[] radekVetsiDataSelectu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  for (int s = 0; s < vetsiDataSelectu[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  shoda = poleShody[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  if (shoda == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;&emsp;  radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  return (radekVetsiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;delkaVetsiDataSelectuRadek = vetsiDataSelectuRadek.length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;shodaMVData = true; //defaultne na true, pokud je neshoda, prenastavi se}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//vetsi radek porovnava se vsemi radky z mensich dat}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int rM = 0; rM < mensiDataSelectu.length; rM++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;mensiDataSelectuRadek = vratMensiDataSelectuRadek(mensiDataSelectu, rM);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetSloupcu = mensiDataSelectu[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  String[] radekMensiDataSelectu = new String[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  for (int s = 0; s < pocetSloupcu; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekMensiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;//nejdrive porovna jejich delku, zda jsou stejne dlouhe}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;delkaMensiDataSelectuRadek = mensiDataSelectuRadek.length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (delkaVetsiDataSelectuRadek == delkaMensiDataSelectuRadek) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//porovna vsechny sloupce Vetsich a Mensich dat, zda se shoduji}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = true;&emsp; //defaultni hodnota, ktera se prepise}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < mensiDataSelectuRadek.length; s++) \\{}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectuHodnota = vetsiDataSelectuRadek[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectuRadek[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp; }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud alespon jedna hodnota je odlisna, pak se nastavi shodaMVData = false}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud jsou hodnoty stejne, pak shodaMVData zustane true}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectuHodnota) == false)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//pokud nalezne shodu, pak "preplacne" poleShodyNew aktualnim radkem s booleans}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//musi preplacnout, protoze ne vsechny sloupce jsou true, nektere mohou zustat false}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//preplacnuti = prekopirovani boolean z poleShody pro dany radek prostrednictvim metody vratVetsiDataSelectuRadek}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;if (shodaMVData == true)\\{}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShodyRadek = vratPoleShodyRadek(poleShody, rV);&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  //metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  pocetSloupcu = poleShody[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  boolean[] radekPoleShody = new boolean[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;   for (int s = 0; s < pocetSloupcu; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;&emsp;  radekPoleShody[s] = poleShody[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  return (radekPoleShody);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-->&emsp;  }}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShodyNew[rV][s] = poleShodyRadek[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;} }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//pokud radky vetsich a mensich dat jsou ruzne dlouhe - neni co resit}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;shodaMVData = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return (poleShodyNew);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;//metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;private String[] vratVetsiDataSelectuRadek(boolean[][] poleShody, String[][] vetsiDataSelectu, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean shoda;}$$<br>
$$\color{red}{&emsp;&emsp;String vetsiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;ArrayList<String> radekVetsiDataSelectuList = new ArrayList<String>();}$$<br>
$$\color{red}{&emsp;&emsp;String[] radekVetsiDataSelectu;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int s = 0; s < vetsiDataSelectu[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;shoda = poleShody[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;if (shoda == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;vetsiDataSelectuHodnota = vetsiDataSelectu[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;radekVetsiDataSelectuList.add(vetsiDataSelectuHodnota);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; -->  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{ }$$<br>
$$\color{red}{&emsp;&emsp;radekVetsiDataSelectu = radekVetsiDataSelectuList.toArray(new String[radekVetsiDataSelectuList.size()]);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;-->  }$$<br>
$$\color{red}{&emsp;&emsp;return (radekVetsiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;//metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;private String[] vratMensiDataSelectuRadek(String[][] mensiDataSelectu, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;pocetSloupcu = mensiDataSelectu[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;String[] radekMensiDataSelectu = new String[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int s = 0; s < pocetSloupcu; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;radekMensiDataSelectu[s] = mensiDataSelectu[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return (radekMensiDataSelectu);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;  }$$<br>
$$\color{red}{&emsp;//metoda volana z prekontrolujPoleShody}$$<br>
$$\color{red}{&emsp;private boolean[] vratPoleShodyRadek(boolean[][] poleShody, int radek)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;pocetSloupcu = poleShody[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;boolean[] radekPoleShody = new boolean[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp; for (int s = 0; s < pocetSloupcu; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;radekPoleShody[s] = poleShody[radek][s];}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp; }$$<br>
$$\color{red}{&emsp;&emsp;return (radekPoleShody);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private void prekontrolujPoleShody2(boolean[][] poleShody, String[][] mensiDataSelectu, String[][] vetsiDataSelectu)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String[] mensiDataSelectuRadek;}$$<br>
$$\color{red}{&emsp;&emsp;String[] vetsiDataSelectuRadek;}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;mensiDataSelectuRadek = new String[5];}$$<br>
$$\color{red}{&emsp;&emsp;vetsiDataSelectuRadek = new String[5];}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String mensiDataSelectuHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;String mensiDataSelectuHodnota0;&emsp;//hodnota z 0-teho sloupce}$$<br>
$$\color{red}{&emsp;&emsp;String vetsiDataSelectHodnota;}$$<br>
$$\color{red}{&emsp;&emsp;String vetsiDataSelectHodnota0;&emsp; //hodnota z 0-teho sloupce}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;boolean shoda;}$$<br>
$$\color{red}{&emsp;&emsp;boolean shoda0;&emsp;&emsp;&emsp;&emsp;&emsp; //shoda z 0-teho sloupce}$$<br>
$$\color{red}{&emsp;&emsp;boolean shodnyRadek;}$$<br>
$$\color{red}{&emsp;&emsp;boolean shodnyRadekNalezen;}$$<br>
$$\color{red}{&emsp;&emsp;int posledniRV = 0;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//index rM udava cislo radku mensiDataSelectu}$$<br>
$$\color{red}{&emsp;&emsp;for (int rM = 0; rM < mensiDataSelectu.length; rM++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;mensiDataSelectuHodnota0 = mensiDataSelectu[rM][0];}$$<br>
$$\color{red}{ }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//vychozi hodnota, ktera se prepisuje}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;shodnyRadekNalezen = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//index rV udava cislo radku vetsiDataSelectu}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int rV = 0; rV < vetsiDataSelectu.length; rV++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;//vychozi hodnota, ktera se prepisuje}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;shodnyRadek = true;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;//v okamziku, kdy shodny radek byl jiz nalezen}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (shodnyRadekNalezen == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;//vyhledava, kde je shoda == true v 0-tem sloupci}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;shoda0 = poleShody[rV][0];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (shoda0 == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//pokud je shoda v 0-tem sloupci, }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//pak porovna hodnotu mensiDataSelectu a vetsiDataSelectu}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//ve sloupci 0}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota0 = vetsiDataSelectu[rV][0];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota0.equals(vetsiDataSelectHodnota0) == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud hodnoty mensiho a vetsiho Selectu}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//jsou stejne - uvazovane pro stejny sloupec, ale jiny radek}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pak se porovnaji hodnoty i pro ostatni sloupce}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 1; s < mensiDataSelectu[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectu[rM][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pokud nejaka hodnota neni stejna (z nejakeho sloupce),}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//pak se nastavi na false a dal uz se nepokracuje}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//(shoda0 == false) }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//shodnyRadek = false muze nabit hodnoty(false) vicero zpusoby}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (shodnyRadek == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadekNalezen = true;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;posledniRV = rV + 1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (shodnyRadek == false)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;poleShody[rV][s] = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;   }$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < mensiDataSelectu[0].length; s++) \\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;mensiDataSelectuHodnota = mensiDataSelectu[rM][s];}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;shoda = poleShody[rV][s];}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;if (shoda == true)\\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;vetsiDataSelectHodnota = vetsiDataSelectu[rV][s];}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (mensiDataSelectuHodnota.equals(vetsiDataSelectHodnota) == false) \\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;  //  if (mensiDataSelectuHodnota != vetsiDataSelectHodnota)\\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shodnyRadek = false;}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;int d = poleShody[0].length;}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//nejedna-li se o shodny radek }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//tzn. radek mensiDataSelectu != radku vetsiDataSelectu}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//pak prepise vsechny true na danem radku na false}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//(to je taky cilem opravy, jelikoz v puvodnim poleShody tomu tak nemusi byt)}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;if (shodnyRadek == false)\\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < poleShody[0].length; s++) \\{}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;&emsp;poleShody[r][s] = false;}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{//&emsp;&emsp;&emsp;d = poleShody[0].length;}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;public JTextPane getBarevnyText()\\{}$$<br>
$$\color{red}{&emsp;//public JScrollPane getBarevnyText()\\{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//return (jTextPane1);}$$<br>
$$\color{red}{&emsp;&emsp;//return (jTextPane2);}$$<br>
$$\color{red}{&emsp;&emsp;return (jTextPane3);}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private boolean vratRadekASloupecNalezenePolozkyVPoli(String[][] Pole, String HledanaPolozka)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String polozkaPole;}$$<br>
$$\color{red}{&emsp;&emsp;boolean nalezenaShoda = false;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;if (HledanaPolozka != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int s = 0; s < Pole[0].length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if(nalezenaShoda == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;for (int r = 0; r < Pole.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;polozkaPole = Pole[r][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;if (polozkaPole != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (polozkaPole.equals(HledanaPolozka) == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rPol = r;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sPol = s;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;nalezenaShoda = true;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;break;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return (nalezenaShoda);}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;private boolean DelsiDataSelectu2(String[][] DataSelectu1, String[][] DataSelectu2)\\{}$$<br>
$$\color{red}{&emsp;&emsp;//obe pole jsou stejne velke, ale to mensi obsahuje null hodnoty}$$<br>
$$\color{red}{&emsp;&emsp;//metoda zjisti ve kterem poli je vice null}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetNullDataSelectu1;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetNullDataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;boolean jeDelsiDataSelectu2;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;pocetNullDataSelectu1 = 0;}$$<br>
$$\color{red}{&emsp;&emsp;pocetNullDataSelectu2 = 0;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int i = 0; i < DataSelectu1.length; i++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;if (DataSelectu1[i] == null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;pocetNullDataSelectu1 = pocetNullDataSelectu1 + 1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;if (DataSelectu2[i] == null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;pocetNullDataSelectu2 = pocetNullDataSelectu2 + 1;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;if (pocetNullDataSelectu2 > pocetNullDataSelectu1)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;jeDelsiDataSelectu2 = true;}$$<br>
$$\color{red}{&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;jeDelsiDataSelectu2 = false;}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return (jeDelsiDataSelectu2);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp; private String vratStringHlavicky()\\{}$$<br>
$$\color{red}{&emsp;  }$$<br>
$$\color{red}{&emsp;&emsp;String NazevSloupce;}$$<br>
$$\color{red}{&emsp;&emsp;String HlavickaStr;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetZnakuVeSloupci;}$$<br>
$$\color{red}{&emsp;&emsp;String ZbyvajiciMezery;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;HlavickaStr = "";}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int s = 1; s <= NazvySloupcu.length; s++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;NazevSloupce = NazvySloupcu[s-1];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s-1];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, NazevSloupce);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;HlavickaStr = HlavickaStr + "  " + ZbyvajiciMezery;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return(HlavickaStr);}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp;private String doplnZbyvajiciMezery(int pocetZnakuSloupce, String Hodnota)}$$<br>
$$\color{red}{&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;String ZbyvajiciMezery;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetZnakuMezer;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;if (Hodnota != null)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;pocetZnakuMezer = pocetZnakuSloupce - Hodnota.length();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;ZbyvajiciMezery = Hodnota;}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//doplni retezec o mezery}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int i = 0; i < pocetZnakuMezer; i++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp; ZbyvajiciMezery = ZbyvajiciMezery + " "; }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;} }$$<br>
$$\color{red}{&emsp;&emsp;else}$$<br>
$$\color{red}{&emsp;&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;ZbyvajiciMezery = "";}$$<br>
$$\color{red}{&emsp;&emsp;}&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return (ZbyvajiciMezery);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp;private int[] vratPocetZnakuProVsechnySloupce()}$$<br>
$$\color{red}{&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;int pocetSloupcu;}$$<br>
$$\color{red}{&emsp;&emsp;pocetSloupcu = NazvySloupcu.length;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetZnaku;}$$<br>
$$\color{red}{&emsp;&emsp;int[] pocetZnakuVeSloupcich = new int[pocetSloupcu];}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int s = 0; s < pocetSloupcu; s++)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;pocetZnaku = vratPocetZnakuProDanySloupec(s);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;pocetZnakuVeSloupcich[s] = pocetZnaku;}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return (pocetZnakuVeSloupcich);}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp; }$$<br>
$$\color{red}{&emsp;private int vratPocetZnakuProDanySloupec(int sloupec)}$$<br>
$$\color{red}{&emsp;\\{ //vrati pole s poctem znaku v jednotlivych sloupcich}$$<br>
$$\color{red}{&emsp;  //to proto aby sloupce krasne zarovnal   }$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String Hodnota;}$$<br>
$$\color{red}{&emsp;&emsp;int nejvicPocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//jako vychozi hodnotu kontroluje pocet znaku nazvu sloupce}$$<br>
$$\color{red}{&emsp;&emsp;nejvicPocetZnakuHodnoty = NazvySloupcu[sloupec].length();}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;for (int r = 1; r < DataSelectuStredni.length; r++) \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;Hodnota = DataSelectuStredni[r][sloupec];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;if (Hodnota != null)}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;pocetZnakuHodnoty = Hodnota.length();}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (pocetZnakuHodnoty > nejvicPocetZnakuHodnoty)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;nejvicPocetZnakuHodnoty = pocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return nejvicPocetZnakuHodnoty;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private void vratBarevnyText(String[][] DataSelectu, boolean zvyraznujPolozky)\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String hodnota;}$$<br>
$$\color{red}{&emsp;&emsp;String mezera;}$$<br>
$$\color{red}{&emsp;&emsp;String hodnotaM;}$$<br>
$$\color{red}{&emsp;&emsp;int delkaDoc;}$$<br>
$$\color{red}{&emsp;&emsp;boolean shoda;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;String ZbyvajiciMezery;}$$<br>
$$\color{red}{&emsp;&emsp;int pocetZnakuVeSloupci;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//StyledDocument doc = jTextPane2.getStyledDocument();}$$<br>
$$\color{red}{&emsp;&emsp;StyledDocument doc = jTextPane3.getStyledDocument();}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;SimpleAttributeSet keyWord = new SimpleAttributeSet();}$$<br>
$$\color{red}{&emsp;&emsp;StyleConstants.setForeground(keyWord, Color.RED);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;hodnota = "xxx";}$$<br>
$$\color{red}{&emsp;&emsp;mezera = "  ";}$$<br>
$$\color{red}{&emsp;&emsp;hodnotaM = "";}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;delkaDoc = 0;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;try}$$<br>
$$\color{red}{&emsp;&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//jTextPane2.setText(""); }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;jTextPane3.setText("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   \n"); }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//doc.insertString(0, "<html>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; </html>", keyWord );}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;//index r = -1 plati pro hlavicku}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;for (int r = -1; r < DataSelectu.length; r++) \\{ }$$<br>
$$\color{red}{&emsp;&emsp;&emsp; }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;for (int s = 0; s < DataSelectu[0].length; s++) \\{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;if (r == -1)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//jedna se o hlavicku&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hodnota = NazvySloupcu[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//jedna se o tabulku&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//Zvyraznuje polozky jeb v pripade, pokud zvyraznujPolozky == true}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if (zvyraznujPolozky == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = PoleShody[r][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shoda = false;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hodnota = DataSelectu[r][s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;delkaDoc = doc.getLength();}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;pocetZnakuVeSloupci = pocetZnakuVeSloupcich[s];}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;ZbyvajiciMezery = doplnZbyvajiciMezery(pocetZnakuVeSloupci, hodnota);}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;hodnotaM = ZbyvajiciMezery + "   ";}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//oznaci danou bunku v zavislosti na tom, zda nalezl shodu ci nikoliv}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;if (shoda == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), hodnotaM, keyWord );}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), hodnotaM, null );}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}  }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;if (r == -1)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//za hlavicku vlozi prazdny radek + novy rasek   }$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\n\n", null );}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;//janak vklada pouze novy radek}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\n", null );}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;catch(Exception e) \\{ System.out.println(e); }}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;//pokud je NejvetsiDotaz = true, pak vraci nejvetsi dotaz, jinak stredni dotaz}$$<br>
$$\color{red}{&emsp;public String vratSelectyNaVetsiDotaz(String originalniSelect, boolean NejvetsiDotaz)}$$<br>
$$\color{red}{&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//String originalniSelect;&emsp;//napr.&emsp;&emsp;  Select * FROM ... WHERE ...}$$<br>
$$\color{red}{&emsp;&emsp;String plnySelect;&emsp;&emsp;&emsp;//z toho vychazi Select * FROM }$$<br>
$$\color{red}{&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;String castZaFrom;}$$<br>
$$\color{red}{&emsp;&emsp;String castPredFrom;}$$<br>
$$\color{red}{&emsp;&emsp;String NazevTabulky;}$$<br>
$$\color{red}{&emsp;&emsp;String[] castZaFromArr;}$$<br>
$$\color{red}{&emsp;&emsp;String[] stringArr;}$$<br>
$$\color{red}{&emsp;&emsp;int indexOfFROM;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;indexOfFROM = originalniSelect.indexOf("FROM");}$$<br>
$$\color{red}{&emsp;&emsp;castZaFrom = originalniSelect.substring(indexOfFROM);}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;if (NejvetsiDotaz == true)\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;castPredFrom = "SELECT * ";}$$<br>
$$\color{red}{&emsp;&emsp;} else \\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;castPredFrom = originalniSelect.substring(0, indexOfFROM);}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;   }$$<br>
$$\color{red}{&emsp;&emsp;castZaFromArr = castZaFrom.split(" ");}$$<br>
$$\color{red}{&emsp;&emsp;NazevTabulky = castZaFromArr[1];}$$<br>
$$\color{red}{&emsp;&emsp;stringArr = NazevTabulky.split("\n");}$$<br>
$$\color{red}{&emsp;&emsp;if (stringArr.length > 0)}$$<br>
$$\color{red}{&emsp;&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;NazevTabulky = stringArr[0];}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;plnySelect = castPredFrom + "FROM " + NazevTabulky;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;return(plnySelect);}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;//nepotrebne}$$<br>
$$\color{red}{&emsp;}$$<br>
$$\color{red}{&emsp;private void vratBarevnyText2()\\{}$$<br>
$$\color{red}{&emsp;&emsp;}$$<br>
$$\color{red}{&emsp;&emsp;//jTextPane2.setText( "original text" );}$$<br>
$$\color{red}{&emsp;&emsp;jTextPane3.setText( "original text" );}$$<br>
$$\color{red}{&emsp;&emsp;//StyledDocument doc = jTextPane2.getStyledDocument();}$$<br>
$$\color{red}{&emsp;&emsp;StyledDocument doc = jTextPane3.getStyledDocument();}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;//  Define a keyword attribute}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;SimpleAttributeSet keyWord = new SimpleAttributeSet();}$$<br>
$$\color{red}{&emsp;&emsp;StyleConstants.setForeground(keyWord, Color.RED);}$$<br>
$$\color{red}{&emsp;&emsp;StyleConstants.setBackground(keyWord, Color.YELLOW);}$$<br>
$$\color{red}{&emsp;&emsp;StyleConstants.setBold(keyWord, true);}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;&emsp;//  Add some text}$$<br>
$$\color{red}{&emsp;&emsp;try}$$<br>
$$\color{red}{&emsp;&emsp;\\{}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;doc.insertString(0, "Start of text\n", null );}$$<br>
$$\color{red}{&emsp;&emsp;&emsp;doc.insertString(doc.getLength(), "\nEnd of text", keyWord );}$$<br>
$$\color{red}{&emsp;&emsp;}}$$<br>
$$\color{red}{&emsp;&emsp;catch(Exception e) \\{ System.out.println(e); }}$$<br>
$$\color{red}{&emsp;   }$$<br>
$$\color{red}{}$$<br>
$$\color{red}{&emsp;}}$$<br>
$$\color{red}{}$$<br>
$$\color{red}{}}$$<br>
