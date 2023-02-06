class vykresliStromFolder{
  constructor(inputTreeJson){
        var jsTreeDataJson = {
            "core": {
                "data": [
{
"id": "row_10",
"parent": "#",
"text": "public NactiDotazy() throws IOException{"
},
{
"id": "row_11",
"parent": "#",
"text": ""
},
{
"id": "row_12",
"parent": "#",
"text": "String Adresa;"
},
{
"id": "row_13",
"parent": "#",
"text": "String ZdrojDotazuVlevo;"
},
{
"id": "row_14",
"parent": "#",
"text": "String ZdrojDotazuVpravo;"
},
{
"id": "row_15",
"parent": "#",
"text": ""
},
{
"id": "row_16",
"parent": "#",
"text": "Adresa = |C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\EXAMPLES-w3resource\\|;"
},
{
"id": "row_17",
"parent": "#",
"text": "ZdrojDotazuVlevo = |RetrieveDataFromTablesCZ.txt|;"
},
{
"id": "row_18",
"parent": "#",
"text": "ZdrojDotazuVpravo = |RetrieveDataFromTablesCZvpravo.txt|;"
},
{
"id": "row_19",
"parent": "#",
"text": ""
},
{
"id": "row_20",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_21",
"parent": "#",
"text": "SubDotazyPopis[0][0] = |SubDotazyPopis[0][0]|;"
},
{
"id": "row_22",
"parent": "#",
"text": "SubDotazyPopis[0][1] = |SubDotazyPopis[0][1]|;"
},
{
"id": "row_23",
"parent": "#",
"text": "SubDotazyPopis[0][2] = |SubDotazyPopis[0][2]|;"
},
{
"id": "row_24",
"parent": "#",
"text": ""
},
{
"id": "row_25",
"parent": "#",
"text": "SubDotazyPopis[1][0] = |SubDotazyPopis[1][0]|;"
},
{
"id": "row_26",
"parent": "#",
"text": "SubDotazyPopis[1][1] = |SubDotazyPopis[1][1]|;"
},
{
"id": "row_27",
"parent": "#",
"text": "SubDotazyPopis[1][2] = |SubDotazyPopis[1][2]|;"
},
{
"id": "row_28",
"parent": "#",
"text": ""
},
{
"id": "row_29",
"parent": "#",
"text": "SubDotazyPopis[2][0] = |SubDotazyPopis[2][0]|;"
},
{
"id": "row_30",
"parent": "#",
"text": "SubDotazyPopis[2][1] = |SubDotazyPopis[2][1]|;"
},
{
"id": "row_31",
"parent": "#",
"text": "SubDotazyPopis[2][2] = |SubDotazyPopis[2][2]|;"
},
{
"id": "row_32",
"parent": "#",
"text": ""
},
{
"id": "row_33",
"parent": "#",
"text": ""
},
{
"id": "row_34",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_35",
"parent": "#",
"text": "SubDotazySQL[0][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_36",
"parent": "#",
"text": "SubDotazySQL[0][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_37",
"parent": "#",
"text": "SubDotazySQL[0][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_38",
"parent": "#",
"text": ""
},
{
"id": "row_39",
"parent": "#",
"text": "SubDotazySQL[1][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_40",
"parent": "#",
"text": "SubDotazySQL[1][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_41",
"parent": "#",
"text": "SubDotazySQL[1][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_42",
"parent": "#",
"text": ""
},
{
"id": "row_43",
"parent": "#",
"text": "SubDotazySQL[2][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_44",
"parent": "#",
"text": "SubDotazySQL[2][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_45",
"parent": "#",
"text": "SubDotazySQL[2][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_46",
"parent": "#",
"text": ""
},
{
"id": "row_47",
"parent": "#",
"text": "//Ziska data vlevo"
},
{
"id": "row_48",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVlevo);"
},
{
"id": "row_49",
"parent": "#",
"text": "DotazySQLVlevo = DotazySQL;"
},
{
"id": "row_50",
"parent": "row_48",
"text": "{"
},
{
"id": "row_51",
"parent": "row_48",
"text": ""
},
{
"id": "row_52",
"parent": "row_48",
"text": "String Radek;"
},
{
"id": "row_53",
"parent": "row_48",
"text": "String PrvniZnak = null;"
},
{
"id": "row_54",
"parent": "row_48",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_55",
"parent": "row_48",
"text": "String Dotaz = null;"
},
{
"id": "row_56",
"parent": "row_48",
"text": ""
},
{
"id": "row_57",
"parent": "row_48",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_58",
"parent": "row_48",
"text": ""
},
{
"id": "row_59",
"parent": "row_48",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_60",
"parent": "row_48",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_61",
"parent": "row_48",
"text": "String PlnaCesta;"
},
{
"id": "row_62",
"parent": "row_48",
"text": ""
},
{
"id": "row_63",
"parent": "row_48",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_64",
"parent": "row_48",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_65",
"parent": "row_48",
"text": ""
},
{
"id": "row_66",
"parent": "row_48",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_67",
"parent": "row_48",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_68",
"parent": "row_48",
"text": ""
},
{
"id": "row_69",
"parent": "row_48",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_70",
"parent": "row_48",
"text": ""
},
{
"id": "row_71",
"parent": "row_48",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_72",
"parent": "row_48",
"text": ""
},
{
"id": "row_73",
"parent": "row_48",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_74",
"parent": "row_48",
"text": "{"
},
{
"id": "row_75",
"parent": "row_48",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_76",
"parent": "row_48",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_77",
"parent": "row_48",
"text": "//Dotaz = ||;"
},
{
"id": "row_78",
"parent": "row_48",
"text": ""
},
{
"id": "row_79",
"parent": "row_48",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_80",
"parent": "row_48",
"text": "{"
},
{
"id": "row_81",
"parent": "row_48",
"text": ""
},
{
"id": "row_82",
"parent": "row_48",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_83",
"parent": "row_48",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_84",
"parent": "row_48",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_85",
"parent": "row_48",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_86",
"parent": "row_48",
"text": ""
},
{
"id": "row_87",
"parent": "row_48",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_88",
"parent": "row_48",
"text": ""
},
{
"id": "row_89",
"parent": "row_48",
"text": "}"
},
{
"id": "row_90",
"parent": "row_48",
"text": "}"
},
{
"id": "row_91",
"parent": "row_48",
"text": "}"
},
{
"id": "row_92",
"parent": "row_48",
"text": ""
},
{
"id": "row_93",
"parent": "row_48",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_94",
"parent": "row_48",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_95",
"parent": "row_48",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_96",
"parent": "row_48",
"text": ""
},
{
"id": "row_97",
"parent": "row_48",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_98",
"parent": "row_48",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_99",
"parent": "row_48",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_100",
"parent": "row_48",
"text": ""
},
{
"id": "row_101",
"parent": "row_48",
"text": ""
},
{
"id": "row_102",
"parent": "#",
"text": "}"
},
{
"id": "row_103",
"parent": "#",
"text": "DotazyPopisVlevo = DotazyPopis;"
},
{
"id": "row_104",
"parent": "#",
"text": "cislaPopisuVlevo = oddelCisloDotazuOdTextuVlevo();"
},
{
"id": "row_105",
"parent": "#",
"text": ""
},
{
"id": "row_106",
"parent": "#",
"text": ""
},
{
"id": "row_107",
"parent": "row_104",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_108",
"parent": "row_104",
"text": ""
},
{
"id": "row_109",
"parent": "row_104",
"text": "String CisloStr;"
},
{
"id": "row_110",
"parent": "row_104",
"text": "int CisloInt = 0;"
},
{
"id": "row_111",
"parent": "row_104",
"text": "String[] stringArr;"
},
{
"id": "row_112",
"parent": "row_104",
"text": "int[] cislaPopisu;"
},
{
"id": "row_113",
"parent": "row_104",
"text": "String DotazPopis;"
},
{
"id": "row_114",
"parent": "row_104",
"text": ""
},
{
"id": "row_115",
"parent": "row_104",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_116",
"parent": "row_104",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_117",
"parent": "row_104",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_118",
"parent": "row_104",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_119",
"parent": "row_104",
"text": ""
},
{
"id": "row_120",
"parent": "row_104",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_121",
"parent": "row_104",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_122",
"parent": "row_104",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_123",
"parent": "row_104",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_124",
"parent": "row_104",
"text": "}"
},
{
"id": "row_125",
"parent": "row_104",
"text": ""
},
{
"id": "row_126",
"parent": "row_104",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_127",
"parent": "row_104",
"text": "}"
},
{
"id": "row_128",
"parent": "row_104",
"text": ""
},
{
"id": "row_129",
"parent": "row_104",
"text": "return (cislaPopisu);"
},
{
"id": "row_130",
"parent": "row_104",
"text": ""
},
{
"id": "row_131",
"parent": "#",
"text": "}"
},
{
"id": "row_132",
"parent": "#",
"text": "//Ziska data vpravo"
},
{
"id": "row_133",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVpravo);"
},
{
"id": "row_134",
"parent": "#",
"text": "DotazySQLVpravo = DotazySQL;"
},
{
"id": "row_135",
"parent": "row_133",
"text": "{"
},
{
"id": "row_136",
"parent": "row_133",
"text": ""
},
{
"id": "row_137",
"parent": "row_133",
"text": "String Radek;"
},
{
"id": "row_138",
"parent": "row_133",
"text": "String PrvniZnak = null;"
},
{
"id": "row_139",
"parent": "row_133",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_140",
"parent": "row_133",
"text": "String Dotaz = null;"
},
{
"id": "row_141",
"parent": "row_133",
"text": ""
},
{
"id": "row_142",
"parent": "row_133",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_143",
"parent": "row_133",
"text": ""
},
{
"id": "row_144",
"parent": "row_133",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_145",
"parent": "row_133",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_146",
"parent": "row_133",
"text": "String PlnaCesta;"
},
{
"id": "row_147",
"parent": "row_133",
"text": ""
},
{
"id": "row_148",
"parent": "row_133",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_149",
"parent": "row_133",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_150",
"parent": "row_133",
"text": ""
},
{
"id": "row_151",
"parent": "row_133",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_152",
"parent": "row_133",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_153",
"parent": "row_133",
"text": ""
},
{
"id": "row_154",
"parent": "row_133",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_155",
"parent": "row_133",
"text": ""
},
{
"id": "row_156",
"parent": "row_133",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_157",
"parent": "row_133",
"text": ""
},
{
"id": "row_158",
"parent": "row_133",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_159",
"parent": "row_133",
"text": "{"
},
{
"id": "row_160",
"parent": "row_133",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_161",
"parent": "row_133",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_162",
"parent": "row_133",
"text": "//Dotaz = ||;"
},
{
"id": "row_163",
"parent": "row_133",
"text": ""
},
{
"id": "row_164",
"parent": "row_133",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_165",
"parent": "row_133",
"text": "{"
},
{
"id": "row_166",
"parent": "row_133",
"text": ""
},
{
"id": "row_167",
"parent": "row_133",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_168",
"parent": "row_133",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_169",
"parent": "row_133",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_170",
"parent": "row_133",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_171",
"parent": "row_133",
"text": ""
},
{
"id": "row_172",
"parent": "row_133",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_173",
"parent": "row_133",
"text": ""
},
{
"id": "row_174",
"parent": "row_133",
"text": "}"
},
{
"id": "row_175",
"parent": "row_133",
"text": "}"
},
{
"id": "row_176",
"parent": "row_133",
"text": "}"
},
{
"id": "row_177",
"parent": "row_133",
"text": ""
},
{
"id": "row_178",
"parent": "row_133",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_179",
"parent": "row_133",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_180",
"parent": "row_133",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_181",
"parent": "row_133",
"text": ""
},
{
"id": "row_182",
"parent": "row_133",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_183",
"parent": "row_133",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_184",
"parent": "row_133",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_185",
"parent": "row_133",
"text": ""
},
{
"id": "row_186",
"parent": "row_133",
"text": ""
},
{
"id": "row_187",
"parent": "#",
"text": "}"
},
{
"id": "row_188",
"parent": "#",
"text": "DotazyPopisVpravo = DotazyPopis;"
},
{
"id": "row_189",
"parent": "#",
"text": "cislaPopisuVPravo = oddelCisloDotazuOdTextuVpravo();"
},
{
"id": "row_190",
"parent": "#",
"text": ""
},
{
"id": "row_191",
"parent": "#",
"text": ""
},
{
"id": "row_192",
"parent": "row_189",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_193",
"parent": "row_189",
"text": ""
},
{
"id": "row_194",
"parent": "row_189",
"text": "String CisloStr1;"
},
{
"id": "row_195",
"parent": "row_189",
"text": "String CisloStr2;"
},
{
"id": "row_196",
"parent": "row_189",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_197",
"parent": "row_189",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_198",
"parent": "row_189",
"text": ""
},
{
"id": "row_199",
"parent": "row_189",
"text": "String[] stringArr;"
},
{
"id": "row_200",
"parent": "row_189",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_201",
"parent": "row_189",
"text": "String DotazPopis;"
},
{
"id": "row_202",
"parent": "row_189",
"text": ""
},
{
"id": "row_203",
"parent": "row_189",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_204",
"parent": "row_189",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_205",
"parent": "row_189",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_206",
"parent": "row_189",
"text": ""
},
{
"id": "row_207",
"parent": "row_189",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_208",
"parent": "row_189",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_209",
"parent": "row_189",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_210",
"parent": "row_189",
"text": ""
},
{
"id": "row_211",
"parent": "row_189",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_212",
"parent": "row_189",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_213",
"parent": "row_189",
"text": "}"
},
{
"id": "row_214",
"parent": "row_189",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_215",
"parent": "row_189",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_216",
"parent": "row_189",
"text": "}"
},
{
"id": "row_217",
"parent": "row_189",
"text": ""
},
{
"id": "row_218",
"parent": "row_189",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_219",
"parent": "row_189",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_220",
"parent": "row_189",
"text": "System.out.println(||);"
},
{
"id": "row_221",
"parent": "row_189",
"text": "}"
},
{
"id": "row_222",
"parent": "row_189",
"text": ""
},
{
"id": "row_223",
"parent": "row_189",
"text": "return (cislaPopisu);"
},
{
"id": "row_224",
"parent": "#",
"text": "}"
},
{
"id": "row_225",
"parent": "#",
"text": "preusporadejDataVPravoDo2D();"
},
{
"id": "row_279",
"parent": "#",
"text": ""
},
{
"id": "row_280",
"parent": "#",
"text": ""
},
{
"id": "row_281",
"parent": "#",
"text": "}"
},
{
"id": "row_282",
"parent": "#",
"text": "public NactiDotazy() throws IOException{"
},
{
"id": "row_283",
"parent": "#",
"text": ""
},
{
"id": "row_284",
"parent": "#",
"text": "String Adresa;"
},
{
"id": "row_285",
"parent": "#",
"text": "String ZdrojDotazuVlevo;"
},
{
"id": "row_286",
"parent": "#",
"text": "String ZdrojDotazuVpravo;"
},
{
"id": "row_287",
"parent": "#",
"text": ""
},
{
"id": "row_288",
"parent": "#",
"text": "Adresa = |C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\EXAMPLES-w3resource\\|;"
},
{
"id": "row_289",
"parent": "#",
"text": "ZdrojDotazuVlevo = |RetrieveDataFromTablesCZ.txt|;"
},
{
"id": "row_290",
"parent": "#",
"text": "ZdrojDotazuVpravo = |RetrieveDataFromTablesCZvpravo.txt|;"
},
{
"id": "row_291",
"parent": "#",
"text": ""
},
{
"id": "row_292",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_293",
"parent": "#",
"text": "SubDotazyPopis[0][0] = |SubDotazyPopis[0][0]|;"
},
{
"id": "row_294",
"parent": "#",
"text": "SubDotazyPopis[0][1] = |SubDotazyPopis[0][1]|;"
},
{
"id": "row_295",
"parent": "#",
"text": "SubDotazyPopis[0][2] = |SubDotazyPopis[0][2]|;"
},
{
"id": "row_296",
"parent": "#",
"text": ""
},
{
"id": "row_297",
"parent": "#",
"text": "SubDotazyPopis[1][0] = |SubDotazyPopis[1][0]|;"
},
{
"id": "row_298",
"parent": "#",
"text": "SubDotazyPopis[1][1] = |SubDotazyPopis[1][1]|;"
},
{
"id": "row_299",
"parent": "#",
"text": "SubDotazyPopis[1][2] = |SubDotazyPopis[1][2]|;"
},
{
"id": "row_300",
"parent": "#",
"text": ""
},
{
"id": "row_301",
"parent": "#",
"text": "SubDotazyPopis[2][0] = |SubDotazyPopis[2][0]|;"
},
{
"id": "row_302",
"parent": "#",
"text": "SubDotazyPopis[2][1] = |SubDotazyPopis[2][1]|;"
},
{
"id": "row_303",
"parent": "#",
"text": "SubDotazyPopis[2][2] = |SubDotazyPopis[2][2]|;"
},
{
"id": "row_304",
"parent": "#",
"text": ""
},
{
"id": "row_305",
"parent": "#",
"text": ""
},
{
"id": "row_306",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_307",
"parent": "#",
"text": "SubDotazySQL[0][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_308",
"parent": "#",
"text": "SubDotazySQL[0][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_309",
"parent": "#",
"text": "SubDotazySQL[0][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_310",
"parent": "#",
"text": ""
},
{
"id": "row_311",
"parent": "#",
"text": "SubDotazySQL[1][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_312",
"parent": "#",
"text": "SubDotazySQL[1][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_313",
"parent": "#",
"text": "SubDotazySQL[1][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_314",
"parent": "#",
"text": ""
},
{
"id": "row_315",
"parent": "#",
"text": "SubDotazySQL[2][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_316",
"parent": "#",
"text": "SubDotazySQL[2][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_317",
"parent": "#",
"text": "SubDotazySQL[2][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_318",
"parent": "#",
"text": ""
},
{
"id": "row_319",
"parent": "#",
"text": "//Ziska data vlevo"
},
{
"id": "row_320",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVlevo);"
},
{
"id": "row_321",
"parent": "#",
"text": "DotazySQLVlevo = DotazySQL;"
},
{
"id": "row_322",
"parent": "row_320",
"text": "{"
},
{
"id": "row_323",
"parent": "row_320",
"text": ""
},
{
"id": "row_324",
"parent": "row_320",
"text": "String Radek;"
},
{
"id": "row_325",
"parent": "row_320",
"text": "String PrvniZnak = null;"
},
{
"id": "row_326",
"parent": "row_320",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_327",
"parent": "row_320",
"text": "String Dotaz = null;"
},
{
"id": "row_328",
"parent": "row_320",
"text": ""
},
{
"id": "row_329",
"parent": "row_320",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_330",
"parent": "row_320",
"text": ""
},
{
"id": "row_331",
"parent": "row_320",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_332",
"parent": "row_320",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_333",
"parent": "row_320",
"text": "String PlnaCesta;"
},
{
"id": "row_334",
"parent": "row_320",
"text": ""
},
{
"id": "row_335",
"parent": "row_320",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_336",
"parent": "row_320",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_337",
"parent": "row_320",
"text": ""
},
{
"id": "row_338",
"parent": "row_320",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_339",
"parent": "row_320",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_340",
"parent": "row_320",
"text": ""
},
{
"id": "row_341",
"parent": "row_320",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_342",
"parent": "row_320",
"text": ""
},
{
"id": "row_343",
"parent": "row_320",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_344",
"parent": "row_320",
"text": ""
},
{
"id": "row_345",
"parent": "row_320",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_346",
"parent": "row_320",
"text": "{"
},
{
"id": "row_347",
"parent": "row_320",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_348",
"parent": "row_320",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_349",
"parent": "row_320",
"text": "//Dotaz = ||;"
},
{
"id": "row_350",
"parent": "row_320",
"text": ""
},
{
"id": "row_351",
"parent": "row_320",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_352",
"parent": "row_320",
"text": "{"
},
{
"id": "row_353",
"parent": "row_320",
"text": ""
},
{
"id": "row_354",
"parent": "row_320",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_355",
"parent": "row_320",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_356",
"parent": "row_320",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_357",
"parent": "row_320",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_358",
"parent": "row_320",
"text": ""
},
{
"id": "row_359",
"parent": "row_320",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_360",
"parent": "row_320",
"text": ""
},
{
"id": "row_361",
"parent": "row_320",
"text": "}"
},
{
"id": "row_362",
"parent": "row_320",
"text": "}"
},
{
"id": "row_363",
"parent": "row_320",
"text": "}"
},
{
"id": "row_364",
"parent": "row_320",
"text": ""
},
{
"id": "row_365",
"parent": "row_320",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_366",
"parent": "row_320",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_367",
"parent": "row_320",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_368",
"parent": "row_320",
"text": ""
},
{
"id": "row_369",
"parent": "row_320",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_370",
"parent": "row_320",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_371",
"parent": "row_320",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_372",
"parent": "row_320",
"text": ""
},
{
"id": "row_373",
"parent": "row_320",
"text": ""
},
{
"id": "row_374",
"parent": "row_320",
"text": "}"
},
{
"id": "row_375",
"parent": "row_320",
"text": "{"
},
{
"id": "row_376",
"parent": "row_320",
"text": ""
},
{
"id": "row_377",
"parent": "row_320",
"text": "String Radek;"
},
{
"id": "row_378",
"parent": "row_320",
"text": "String PrvniZnak = null;"
},
{
"id": "row_379",
"parent": "row_320",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_380",
"parent": "row_320",
"text": "String Dotaz = null;"
},
{
"id": "row_381",
"parent": "row_320",
"text": ""
},
{
"id": "row_382",
"parent": "row_320",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_383",
"parent": "row_320",
"text": ""
},
{
"id": "row_384",
"parent": "row_320",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_385",
"parent": "row_320",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_386",
"parent": "row_320",
"text": "String PlnaCesta;"
},
{
"id": "row_387",
"parent": "row_320",
"text": ""
},
{
"id": "row_388",
"parent": "row_320",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_389",
"parent": "row_320",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_390",
"parent": "row_320",
"text": ""
},
{
"id": "row_391",
"parent": "row_320",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_392",
"parent": "row_320",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_393",
"parent": "row_320",
"text": ""
},
{
"id": "row_394",
"parent": "row_320",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_395",
"parent": "row_320",
"text": ""
},
{
"id": "row_396",
"parent": "row_320",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_397",
"parent": "row_320",
"text": ""
},
{
"id": "row_398",
"parent": "row_320",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_399",
"parent": "row_320",
"text": "{"
},
{
"id": "row_400",
"parent": "row_320",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_401",
"parent": "row_320",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_402",
"parent": "row_320",
"text": "//Dotaz = ||;"
},
{
"id": "row_403",
"parent": "row_320",
"text": ""
},
{
"id": "row_404",
"parent": "row_320",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_405",
"parent": "row_320",
"text": "{"
},
{
"id": "row_406",
"parent": "row_320",
"text": ""
},
{
"id": "row_407",
"parent": "row_320",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_408",
"parent": "row_320",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_409",
"parent": "row_320",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_410",
"parent": "row_320",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_411",
"parent": "row_320",
"text": ""
},
{
"id": "row_412",
"parent": "row_320",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_413",
"parent": "row_320",
"text": ""
},
{
"id": "row_414",
"parent": "row_320",
"text": "}"
},
{
"id": "row_415",
"parent": "row_320",
"text": "}"
},
{
"id": "row_416",
"parent": "row_320",
"text": "}"
},
{
"id": "row_417",
"parent": "row_320",
"text": ""
},
{
"id": "row_418",
"parent": "row_320",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_419",
"parent": "row_320",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_420",
"parent": "row_320",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_421",
"parent": "row_320",
"text": ""
},
{
"id": "row_422",
"parent": "row_320",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_423",
"parent": "row_320",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_424",
"parent": "row_320",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_425",
"parent": "row_320",
"text": ""
},
{
"id": "row_426",
"parent": "row_320",
"text": ""
},
{
"id": "row_427",
"parent": "#",
"text": "}"
},
{
"id": "row_428",
"parent": "#",
"text": "DotazyPopisVlevo = DotazyPopis;"
},
{
"id": "row_429",
"parent": "#",
"text": "cislaPopisuVlevo = oddelCisloDotazuOdTextuVlevo();"
},
{
"id": "row_430",
"parent": "#",
"text": ""
},
{
"id": "row_431",
"parent": "#",
"text": ""
},
{
"id": "row_432",
"parent": "row_429",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_433",
"parent": "row_429",
"text": ""
},
{
"id": "row_434",
"parent": "row_429",
"text": "String CisloStr;"
},
{
"id": "row_435",
"parent": "row_429",
"text": "int CisloInt = 0;"
},
{
"id": "row_436",
"parent": "row_429",
"text": "String[] stringArr;"
},
{
"id": "row_437",
"parent": "row_429",
"text": "int[] cislaPopisu;"
},
{
"id": "row_438",
"parent": "row_429",
"text": "String DotazPopis;"
},
{
"id": "row_439",
"parent": "row_429",
"text": ""
},
{
"id": "row_440",
"parent": "row_429",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_441",
"parent": "row_429",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_442",
"parent": "row_429",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_443",
"parent": "row_429",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_444",
"parent": "row_429",
"text": ""
},
{
"id": "row_445",
"parent": "row_429",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_446",
"parent": "row_429",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_447",
"parent": "row_429",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_448",
"parent": "row_429",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_449",
"parent": "row_429",
"text": "}"
},
{
"id": "row_450",
"parent": "row_429",
"text": ""
},
{
"id": "row_451",
"parent": "row_429",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_452",
"parent": "row_429",
"text": "}"
},
{
"id": "row_453",
"parent": "row_429",
"text": ""
},
{
"id": "row_454",
"parent": "row_429",
"text": "return (cislaPopisu);"
},
{
"id": "row_455",
"parent": "row_429",
"text": ""
},
{
"id": "row_456",
"parent": "row_429",
"text": "}"
},
{
"id": "row_457",
"parent": "row_429",
"text": ""
},
{
"id": "row_458",
"parent": "row_429",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_459",
"parent": "row_429",
"text": ""
},
{
"id": "row_460",
"parent": "row_429",
"text": "String CisloStr;"
},
{
"id": "row_461",
"parent": "row_429",
"text": "int CisloInt = 0;"
},
{
"id": "row_462",
"parent": "row_429",
"text": "String[] stringArr;"
},
{
"id": "row_463",
"parent": "row_429",
"text": "int[] cislaPopisu;"
},
{
"id": "row_464",
"parent": "row_429",
"text": "String DotazPopis;"
},
{
"id": "row_465",
"parent": "row_429",
"text": ""
},
{
"id": "row_466",
"parent": "row_429",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_467",
"parent": "row_429",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_468",
"parent": "row_429",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_469",
"parent": "row_429",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_470",
"parent": "row_429",
"text": ""
},
{
"id": "row_471",
"parent": "row_429",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_472",
"parent": "row_429",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_473",
"parent": "row_429",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_474",
"parent": "row_429",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_475",
"parent": "row_429",
"text": "}"
},
{
"id": "row_476",
"parent": "row_429",
"text": ""
},
{
"id": "row_477",
"parent": "row_429",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_478",
"parent": "row_429",
"text": "}"
},
{
"id": "row_479",
"parent": "row_429",
"text": ""
},
{
"id": "row_480",
"parent": "row_429",
"text": "return (cislaPopisu);"
},
{
"id": "row_481",
"parent": "row_429",
"text": ""
},
{
"id": "row_482",
"parent": "#",
"text": "}"
},
{
"id": "row_483",
"parent": "#",
"text": "//Ziska data vpravo"
},
{
"id": "row_484",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVpravo);"
},
{
"id": "row_485",
"parent": "#",
"text": "DotazySQLVpravo = DotazySQL;"
},
{
"id": "row_486",
"parent": "row_484",
"text": "{"
},
{
"id": "row_487",
"parent": "row_484",
"text": ""
},
{
"id": "row_488",
"parent": "row_484",
"text": "String Radek;"
},
{
"id": "row_489",
"parent": "row_484",
"text": "String PrvniZnak = null;"
},
{
"id": "row_490",
"parent": "row_484",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_491",
"parent": "row_484",
"text": "String Dotaz = null;"
},
{
"id": "row_492",
"parent": "row_484",
"text": ""
},
{
"id": "row_493",
"parent": "row_484",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_494",
"parent": "row_484",
"text": ""
},
{
"id": "row_495",
"parent": "row_484",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_496",
"parent": "row_484",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_497",
"parent": "row_484",
"text": "String PlnaCesta;"
},
{
"id": "row_498",
"parent": "row_484",
"text": ""
},
{
"id": "row_499",
"parent": "row_484",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_500",
"parent": "row_484",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_501",
"parent": "row_484",
"text": ""
},
{
"id": "row_502",
"parent": "row_484",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_503",
"parent": "row_484",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_504",
"parent": "row_484",
"text": ""
},
{
"id": "row_505",
"parent": "row_484",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_506",
"parent": "row_484",
"text": ""
},
{
"id": "row_507",
"parent": "row_484",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_508",
"parent": "row_484",
"text": ""
},
{
"id": "row_509",
"parent": "row_484",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_510",
"parent": "row_484",
"text": "{"
},
{
"id": "row_511",
"parent": "row_484",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_512",
"parent": "row_484",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_513",
"parent": "row_484",
"text": "//Dotaz = ||;"
},
{
"id": "row_514",
"parent": "row_484",
"text": ""
},
{
"id": "row_515",
"parent": "row_484",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_516",
"parent": "row_484",
"text": "{"
},
{
"id": "row_517",
"parent": "row_484",
"text": ""
},
{
"id": "row_518",
"parent": "row_484",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_519",
"parent": "row_484",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_520",
"parent": "row_484",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_521",
"parent": "row_484",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_522",
"parent": "row_484",
"text": ""
},
{
"id": "row_523",
"parent": "row_484",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_524",
"parent": "row_484",
"text": ""
},
{
"id": "row_525",
"parent": "row_484",
"text": "}"
},
{
"id": "row_526",
"parent": "row_484",
"text": "}"
},
{
"id": "row_527",
"parent": "row_484",
"text": "}"
},
{
"id": "row_528",
"parent": "row_484",
"text": ""
},
{
"id": "row_529",
"parent": "row_484",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_530",
"parent": "row_484",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_531",
"parent": "row_484",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_532",
"parent": "row_484",
"text": ""
},
{
"id": "row_533",
"parent": "row_484",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_534",
"parent": "row_484",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_535",
"parent": "row_484",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_536",
"parent": "row_484",
"text": ""
},
{
"id": "row_537",
"parent": "row_484",
"text": ""
},
{
"id": "row_538",
"parent": "row_484",
"text": "}"
},
{
"id": "row_539",
"parent": "row_484",
"text": "{"
},
{
"id": "row_540",
"parent": "row_484",
"text": ""
},
{
"id": "row_541",
"parent": "row_484",
"text": "String Radek;"
},
{
"id": "row_542",
"parent": "row_484",
"text": "String PrvniZnak = null;"
},
{
"id": "row_543",
"parent": "row_484",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_544",
"parent": "row_484",
"text": "String Dotaz = null;"
},
{
"id": "row_545",
"parent": "row_484",
"text": ""
},
{
"id": "row_546",
"parent": "row_484",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_547",
"parent": "row_484",
"text": ""
},
{
"id": "row_548",
"parent": "row_484",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_549",
"parent": "row_484",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_550",
"parent": "row_484",
"text": "String PlnaCesta;"
},
{
"id": "row_551",
"parent": "row_484",
"text": ""
},
{
"id": "row_552",
"parent": "row_484",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_553",
"parent": "row_484",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_554",
"parent": "row_484",
"text": ""
},
{
"id": "row_555",
"parent": "row_484",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_556",
"parent": "row_484",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_557",
"parent": "row_484",
"text": ""
},
{
"id": "row_558",
"parent": "row_484",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_559",
"parent": "row_484",
"text": ""
},
{
"id": "row_560",
"parent": "row_484",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_561",
"parent": "row_484",
"text": ""
},
{
"id": "row_562",
"parent": "row_484",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_563",
"parent": "row_484",
"text": "{"
},
{
"id": "row_564",
"parent": "row_484",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_565",
"parent": "row_484",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_566",
"parent": "row_484",
"text": "//Dotaz = ||;"
},
{
"id": "row_567",
"parent": "row_484",
"text": ""
},
{
"id": "row_568",
"parent": "row_484",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_569",
"parent": "row_484",
"text": "{"
},
{
"id": "row_570",
"parent": "row_484",
"text": ""
},
{
"id": "row_571",
"parent": "row_484",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_572",
"parent": "row_484",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_573",
"parent": "row_484",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_574",
"parent": "row_484",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_575",
"parent": "row_484",
"text": ""
},
{
"id": "row_576",
"parent": "row_484",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_577",
"parent": "row_484",
"text": ""
},
{
"id": "row_578",
"parent": "row_484",
"text": "}"
},
{
"id": "row_579",
"parent": "row_484",
"text": "}"
},
{
"id": "row_580",
"parent": "row_484",
"text": "}"
},
{
"id": "row_581",
"parent": "row_484",
"text": ""
},
{
"id": "row_582",
"parent": "row_484",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_583",
"parent": "row_484",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_584",
"parent": "row_484",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_585",
"parent": "row_484",
"text": ""
},
{
"id": "row_586",
"parent": "row_484",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_587",
"parent": "row_484",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_588",
"parent": "row_484",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_589",
"parent": "row_484",
"text": ""
},
{
"id": "row_590",
"parent": "row_484",
"text": ""
},
{
"id": "row_591",
"parent": "#",
"text": "}"
},
{
"id": "row_592",
"parent": "#",
"text": "DotazyPopisVpravo = DotazyPopis;"
},
{
"id": "row_593",
"parent": "#",
"text": "cislaPopisuVPravo = oddelCisloDotazuOdTextuVpravo();"
},
{
"id": "row_594",
"parent": "#",
"text": ""
},
{
"id": "row_595",
"parent": "#",
"text": ""
},
{
"id": "row_596",
"parent": "row_593",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_597",
"parent": "row_593",
"text": ""
},
{
"id": "row_598",
"parent": "row_593",
"text": "String CisloStr1;"
},
{
"id": "row_599",
"parent": "row_593",
"text": "String CisloStr2;"
},
{
"id": "row_600",
"parent": "row_593",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_601",
"parent": "row_593",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_602",
"parent": "row_593",
"text": ""
},
{
"id": "row_603",
"parent": "row_593",
"text": "String[] stringArr;"
},
{
"id": "row_604",
"parent": "row_593",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_605",
"parent": "row_593",
"text": "String DotazPopis;"
},
{
"id": "row_606",
"parent": "row_593",
"text": ""
},
{
"id": "row_607",
"parent": "row_593",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_608",
"parent": "row_593",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_609",
"parent": "row_593",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_610",
"parent": "row_593",
"text": ""
},
{
"id": "row_611",
"parent": "row_593",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_612",
"parent": "row_593",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_613",
"parent": "row_593",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_614",
"parent": "row_593",
"text": ""
},
{
"id": "row_615",
"parent": "row_593",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_616",
"parent": "row_593",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_617",
"parent": "row_593",
"text": "}"
},
{
"id": "row_618",
"parent": "row_593",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_619",
"parent": "row_593",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_620",
"parent": "row_593",
"text": "}"
},
{
"id": "row_621",
"parent": "row_593",
"text": ""
},
{
"id": "row_622",
"parent": "row_593",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_623",
"parent": "row_593",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_624",
"parent": "row_593",
"text": "System.out.println(||);"
},
{
"id": "row_625",
"parent": "row_593",
"text": "}"
},
{
"id": "row_626",
"parent": "row_593",
"text": ""
},
{
"id": "row_627",
"parent": "row_593",
"text": "return (cislaPopisu);"
},
{
"id": "row_628",
"parent": "row_593",
"text": "}"
},
{
"id": "row_629",
"parent": "row_593",
"text": ""
},
{
"id": "row_630",
"parent": "row_593",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_631",
"parent": "row_593",
"text": ""
},
{
"id": "row_632",
"parent": "row_593",
"text": "String CisloStr1;"
},
{
"id": "row_633",
"parent": "row_593",
"text": "String CisloStr2;"
},
{
"id": "row_634",
"parent": "row_593",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_635",
"parent": "row_593",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_636",
"parent": "row_593",
"text": ""
},
{
"id": "row_637",
"parent": "row_593",
"text": "String[] stringArr;"
},
{
"id": "row_638",
"parent": "row_593",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_639",
"parent": "row_593",
"text": "String DotazPopis;"
},
{
"id": "row_640",
"parent": "row_593",
"text": ""
},
{
"id": "row_641",
"parent": "row_593",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_642",
"parent": "row_593",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_643",
"parent": "row_593",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_644",
"parent": "row_593",
"text": ""
},
{
"id": "row_645",
"parent": "row_593",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_646",
"parent": "row_593",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_647",
"parent": "row_593",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_648",
"parent": "row_593",
"text": ""
},
{
"id": "row_649",
"parent": "row_593",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_650",
"parent": "row_593",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_651",
"parent": "row_593",
"text": "}"
},
{
"id": "row_652",
"parent": "row_593",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_653",
"parent": "row_593",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_654",
"parent": "row_593",
"text": "}"
},
{
"id": "row_655",
"parent": "row_593",
"text": ""
},
{
"id": "row_656",
"parent": "row_593",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_657",
"parent": "row_593",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_658",
"parent": "row_593",
"text": "System.out.println(||);"
},
{
"id": "row_659",
"parent": "row_593",
"text": "}"
},
{
"id": "row_660",
"parent": "row_593",
"text": ""
},
{
"id": "row_661",
"parent": "row_593",
"text": "return (cislaPopisu);"
},
{
"id": "row_662",
"parent": "#",
"text": "}"
},
{
"id": "row_663",
"parent": "#",
"text": "preusporadejDataVPravoDo2D();"
},
{
"id": "row_769",
"parent": "#",
"text": ""
},
{
"id": "row_770",
"parent": "#",
"text": ""
},
{
"id": "row_771",
"parent": "#",
"text": "}"
},
{
"id": "row_772",
"parent": "#",
"text": "public NactiDotazy() throws IOException{"
},
{
"id": "row_773",
"parent": "#",
"text": ""
},
{
"id": "row_774",
"parent": "#",
"text": "String Adresa;"
},
{
"id": "row_775",
"parent": "#",
"text": "String ZdrojDotazuVlevo;"
},
{
"id": "row_776",
"parent": "#",
"text": "String ZdrojDotazuVpravo;"
},
{
"id": "row_777",
"parent": "#",
"text": ""
},
{
"id": "row_778",
"parent": "#",
"text": "Adresa = |C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\EXAMPLES-w3resource\\|;"
},
{
"id": "row_779",
"parent": "#",
"text": "ZdrojDotazuVlevo = |RetrieveDataFromTablesCZ.txt|;"
},
{
"id": "row_780",
"parent": "#",
"text": "ZdrojDotazuVpravo = |RetrieveDataFromTablesCZvpravo.txt|;"
},
{
"id": "row_781",
"parent": "#",
"text": ""
},
{
"id": "row_782",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_783",
"parent": "#",
"text": "SubDotazyPopis[0][0] = |SubDotazyPopis[0][0]|;"
},
{
"id": "row_784",
"parent": "#",
"text": "SubDotazyPopis[0][1] = |SubDotazyPopis[0][1]|;"
},
{
"id": "row_785",
"parent": "#",
"text": "SubDotazyPopis[0][2] = |SubDotazyPopis[0][2]|;"
},
{
"id": "row_786",
"parent": "#",
"text": ""
},
{
"id": "row_787",
"parent": "#",
"text": "SubDotazyPopis[1][0] = |SubDotazyPopis[1][0]|;"
},
{
"id": "row_788",
"parent": "#",
"text": "SubDotazyPopis[1][1] = |SubDotazyPopis[1][1]|;"
},
{
"id": "row_789",
"parent": "#",
"text": "SubDotazyPopis[1][2] = |SubDotazyPopis[1][2]|;"
},
{
"id": "row_790",
"parent": "#",
"text": ""
},
{
"id": "row_791",
"parent": "#",
"text": "SubDotazyPopis[2][0] = |SubDotazyPopis[2][0]|;"
},
{
"id": "row_792",
"parent": "#",
"text": "SubDotazyPopis[2][1] = |SubDotazyPopis[2][1]|;"
},
{
"id": "row_793",
"parent": "#",
"text": "SubDotazyPopis[2][2] = |SubDotazyPopis[2][2]|;"
},
{
"id": "row_794",
"parent": "#",
"text": ""
},
{
"id": "row_795",
"parent": "#",
"text": ""
},
{
"id": "row_796",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_797",
"parent": "#",
"text": "SubDotazySQL[0][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_798",
"parent": "#",
"text": "SubDotazySQL[0][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_799",
"parent": "#",
"text": "SubDotazySQL[0][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_800",
"parent": "#",
"text": ""
},
{
"id": "row_801",
"parent": "#",
"text": "SubDotazySQL[1][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_802",
"parent": "#",
"text": "SubDotazySQL[1][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_803",
"parent": "#",
"text": "SubDotazySQL[1][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_804",
"parent": "#",
"text": ""
},
{
"id": "row_805",
"parent": "#",
"text": "SubDotazySQL[2][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_806",
"parent": "#",
"text": "SubDotazySQL[2][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_807",
"parent": "#",
"text": "SubDotazySQL[2][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_808",
"parent": "#",
"text": ""
},
{
"id": "row_809",
"parent": "#",
"text": "//Ziska data vlevo"
},
{
"id": "row_810",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVlevo);"
},
{
"id": "row_811",
"parent": "#",
"text": "DotazySQLVlevo = DotazySQL;"
},
{
"id": "row_812",
"parent": "row_810",
"text": "{"
},
{
"id": "row_813",
"parent": "row_810",
"text": ""
},
{
"id": "row_814",
"parent": "row_810",
"text": "String Radek;"
},
{
"id": "row_815",
"parent": "row_810",
"text": "String PrvniZnak = null;"
},
{
"id": "row_816",
"parent": "row_810",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_817",
"parent": "row_810",
"text": "String Dotaz = null;"
},
{
"id": "row_818",
"parent": "row_810",
"text": ""
},
{
"id": "row_819",
"parent": "row_810",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_820",
"parent": "row_810",
"text": ""
},
{
"id": "row_821",
"parent": "row_810",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_822",
"parent": "row_810",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_823",
"parent": "row_810",
"text": "String PlnaCesta;"
},
{
"id": "row_824",
"parent": "row_810",
"text": ""
},
{
"id": "row_825",
"parent": "row_810",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_826",
"parent": "row_810",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_827",
"parent": "row_810",
"text": ""
},
{
"id": "row_828",
"parent": "row_810",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_829",
"parent": "row_810",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_830",
"parent": "row_810",
"text": ""
},
{
"id": "row_831",
"parent": "row_810",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_832",
"parent": "row_810",
"text": ""
},
{
"id": "row_833",
"parent": "row_810",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_834",
"parent": "row_810",
"text": ""
},
{
"id": "row_835",
"parent": "row_810",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_836",
"parent": "row_810",
"text": "{"
},
{
"id": "row_837",
"parent": "row_810",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_838",
"parent": "row_810",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_839",
"parent": "row_810",
"text": "//Dotaz = ||;"
},
{
"id": "row_840",
"parent": "row_810",
"text": ""
},
{
"id": "row_841",
"parent": "row_810",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_842",
"parent": "row_810",
"text": "{"
},
{
"id": "row_843",
"parent": "row_810",
"text": ""
},
{
"id": "row_844",
"parent": "row_810",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_845",
"parent": "row_810",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_846",
"parent": "row_810",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_847",
"parent": "row_810",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_848",
"parent": "row_810",
"text": ""
},
{
"id": "row_849",
"parent": "row_810",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_850",
"parent": "row_810",
"text": ""
},
{
"id": "row_851",
"parent": "row_810",
"text": "}"
},
{
"id": "row_852",
"parent": "row_810",
"text": "}"
},
{
"id": "row_853",
"parent": "row_810",
"text": "}"
},
{
"id": "row_854",
"parent": "row_810",
"text": ""
},
{
"id": "row_855",
"parent": "row_810",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_856",
"parent": "row_810",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_857",
"parent": "row_810",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_858",
"parent": "row_810",
"text": ""
},
{
"id": "row_859",
"parent": "row_810",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_860",
"parent": "row_810",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_861",
"parent": "row_810",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_862",
"parent": "row_810",
"text": ""
},
{
"id": "row_863",
"parent": "row_810",
"text": ""
},
{
"id": "row_864",
"parent": "row_810",
"text": "}"
},
{
"id": "row_865",
"parent": "row_810",
"text": "{"
},
{
"id": "row_866",
"parent": "row_810",
"text": ""
},
{
"id": "row_867",
"parent": "row_810",
"text": "String Radek;"
},
{
"id": "row_868",
"parent": "row_810",
"text": "String PrvniZnak = null;"
},
{
"id": "row_869",
"parent": "row_810",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_870",
"parent": "row_810",
"text": "String Dotaz = null;"
},
{
"id": "row_871",
"parent": "row_810",
"text": ""
},
{
"id": "row_872",
"parent": "row_810",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_873",
"parent": "row_810",
"text": ""
},
{
"id": "row_874",
"parent": "row_810",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_875",
"parent": "row_810",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_876",
"parent": "row_810",
"text": "String PlnaCesta;"
},
{
"id": "row_877",
"parent": "row_810",
"text": ""
},
{
"id": "row_878",
"parent": "row_810",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_879",
"parent": "row_810",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_880",
"parent": "row_810",
"text": ""
},
{
"id": "row_881",
"parent": "row_810",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_882",
"parent": "row_810",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_883",
"parent": "row_810",
"text": ""
},
{
"id": "row_884",
"parent": "row_810",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_885",
"parent": "row_810",
"text": ""
},
{
"id": "row_886",
"parent": "row_810",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_887",
"parent": "row_810",
"text": ""
},
{
"id": "row_888",
"parent": "row_810",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_889",
"parent": "row_810",
"text": "{"
},
{
"id": "row_890",
"parent": "row_810",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_891",
"parent": "row_810",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_892",
"parent": "row_810",
"text": "//Dotaz = ||;"
},
{
"id": "row_893",
"parent": "row_810",
"text": ""
},
{
"id": "row_894",
"parent": "row_810",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_895",
"parent": "row_810",
"text": "{"
},
{
"id": "row_896",
"parent": "row_810",
"text": ""
},
{
"id": "row_897",
"parent": "row_810",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_898",
"parent": "row_810",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_899",
"parent": "row_810",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_900",
"parent": "row_810",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_901",
"parent": "row_810",
"text": ""
},
{
"id": "row_902",
"parent": "row_810",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_903",
"parent": "row_810",
"text": ""
},
{
"id": "row_904",
"parent": "row_810",
"text": "}"
},
{
"id": "row_905",
"parent": "row_810",
"text": "}"
},
{
"id": "row_906",
"parent": "row_810",
"text": "}"
},
{
"id": "row_907",
"parent": "row_810",
"text": ""
},
{
"id": "row_908",
"parent": "row_810",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_909",
"parent": "row_810",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_910",
"parent": "row_810",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_911",
"parent": "row_810",
"text": ""
},
{
"id": "row_912",
"parent": "row_810",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_913",
"parent": "row_810",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_914",
"parent": "row_810",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_915",
"parent": "row_810",
"text": ""
},
{
"id": "row_916",
"parent": "row_810",
"text": ""
},
{
"id": "row_917",
"parent": "row_810",
"text": "}"
},
{
"id": "row_918",
"parent": "row_810",
"text": "{"
},
{
"id": "row_919",
"parent": "row_810",
"text": ""
},
{
"id": "row_920",
"parent": "row_810",
"text": "String Radek;"
},
{
"id": "row_921",
"parent": "row_810",
"text": "String PrvniZnak = null;"
},
{
"id": "row_922",
"parent": "row_810",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_923",
"parent": "row_810",
"text": "String Dotaz = null;"
},
{
"id": "row_924",
"parent": "row_810",
"text": ""
},
{
"id": "row_925",
"parent": "row_810",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_926",
"parent": "row_810",
"text": ""
},
{
"id": "row_927",
"parent": "row_810",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_928",
"parent": "row_810",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_929",
"parent": "row_810",
"text": "String PlnaCesta;"
},
{
"id": "row_930",
"parent": "row_810",
"text": ""
},
{
"id": "row_931",
"parent": "row_810",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_932",
"parent": "row_810",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_933",
"parent": "row_810",
"text": ""
},
{
"id": "row_934",
"parent": "row_810",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_935",
"parent": "row_810",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_936",
"parent": "row_810",
"text": ""
},
{
"id": "row_937",
"parent": "row_810",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_938",
"parent": "row_810",
"text": ""
},
{
"id": "row_939",
"parent": "row_810",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_940",
"parent": "row_810",
"text": ""
},
{
"id": "row_941",
"parent": "row_810",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_942",
"parent": "row_810",
"text": "{"
},
{
"id": "row_943",
"parent": "row_810",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_944",
"parent": "row_810",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_945",
"parent": "row_810",
"text": "//Dotaz = ||;"
},
{
"id": "row_946",
"parent": "row_810",
"text": ""
},
{
"id": "row_947",
"parent": "row_810",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_948",
"parent": "row_810",
"text": "{"
},
{
"id": "row_949",
"parent": "row_810",
"text": ""
},
{
"id": "row_950",
"parent": "row_810",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_951",
"parent": "row_810",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_952",
"parent": "row_810",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_953",
"parent": "row_810",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_954",
"parent": "row_810",
"text": ""
},
{
"id": "row_955",
"parent": "row_810",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_956",
"parent": "row_810",
"text": ""
},
{
"id": "row_957",
"parent": "row_810",
"text": "}"
},
{
"id": "row_958",
"parent": "row_810",
"text": "}"
},
{
"id": "row_959",
"parent": "row_810",
"text": "}"
},
{
"id": "row_960",
"parent": "row_810",
"text": ""
},
{
"id": "row_961",
"parent": "row_810",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_962",
"parent": "row_810",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_963",
"parent": "row_810",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_964",
"parent": "row_810",
"text": ""
},
{
"id": "row_965",
"parent": "row_810",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_966",
"parent": "row_810",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_967",
"parent": "row_810",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_968",
"parent": "row_810",
"text": ""
},
{
"id": "row_969",
"parent": "row_810",
"text": ""
},
{
"id": "row_970",
"parent": "#",
"text": "}"
},
{
"id": "row_971",
"parent": "#",
"text": "DotazyPopisVlevo = DotazyPopis;"
},
{
"id": "row_972",
"parent": "#",
"text": "cislaPopisuVlevo = oddelCisloDotazuOdTextuVlevo();"
},
{
"id": "row_973",
"parent": "#",
"text": ""
},
{
"id": "row_974",
"parent": "#",
"text": ""
},
{
"id": "row_975",
"parent": "row_972",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_976",
"parent": "row_972",
"text": ""
},
{
"id": "row_977",
"parent": "row_972",
"text": "String CisloStr;"
},
{
"id": "row_978",
"parent": "row_972",
"text": "int CisloInt = 0;"
},
{
"id": "row_979",
"parent": "row_972",
"text": "String[] stringArr;"
},
{
"id": "row_980",
"parent": "row_972",
"text": "int[] cislaPopisu;"
},
{
"id": "row_981",
"parent": "row_972",
"text": "String DotazPopis;"
},
{
"id": "row_982",
"parent": "row_972",
"text": ""
},
{
"id": "row_983",
"parent": "row_972",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_984",
"parent": "row_972",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_985",
"parent": "row_972",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_986",
"parent": "row_972",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_987",
"parent": "row_972",
"text": ""
},
{
"id": "row_988",
"parent": "row_972",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_989",
"parent": "row_972",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_990",
"parent": "row_972",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_991",
"parent": "row_972",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_992",
"parent": "row_972",
"text": "}"
},
{
"id": "row_993",
"parent": "row_972",
"text": ""
},
{
"id": "row_994",
"parent": "row_972",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_995",
"parent": "row_972",
"text": "}"
},
{
"id": "row_996",
"parent": "row_972",
"text": ""
},
{
"id": "row_997",
"parent": "row_972",
"text": "return (cislaPopisu);"
},
{
"id": "row_998",
"parent": "row_972",
"text": ""
},
{
"id": "row_999",
"parent": "row_972",
"text": "}"
},
{
"id": "row_1000",
"parent": "row_972",
"text": ""
},
{
"id": "row_1001",
"parent": "row_972",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_1002",
"parent": "row_972",
"text": ""
},
{
"id": "row_1003",
"parent": "row_972",
"text": "String CisloStr;"
},
{
"id": "row_1004",
"parent": "row_972",
"text": "int CisloInt = 0;"
},
{
"id": "row_1005",
"parent": "row_972",
"text": "String[] stringArr;"
},
{
"id": "row_1006",
"parent": "row_972",
"text": "int[] cislaPopisu;"
},
{
"id": "row_1007",
"parent": "row_972",
"text": "String DotazPopis;"
},
{
"id": "row_1008",
"parent": "row_972",
"text": ""
},
{
"id": "row_1009",
"parent": "row_972",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_1010",
"parent": "row_972",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_1011",
"parent": "row_972",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1012",
"parent": "row_972",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_1013",
"parent": "row_972",
"text": ""
},
{
"id": "row_1014",
"parent": "row_972",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1015",
"parent": "row_972",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_1016",
"parent": "row_972",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_1017",
"parent": "row_972",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_1018",
"parent": "row_972",
"text": "}"
},
{
"id": "row_1019",
"parent": "row_972",
"text": ""
},
{
"id": "row_1020",
"parent": "row_972",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_1021",
"parent": "row_972",
"text": "}"
},
{
"id": "row_1022",
"parent": "row_972",
"text": ""
},
{
"id": "row_1023",
"parent": "row_972",
"text": "return (cislaPopisu);"
},
{
"id": "row_1024",
"parent": "row_972",
"text": ""
},
{
"id": "row_1025",
"parent": "row_972",
"text": "}"
},
{
"id": "row_1026",
"parent": "row_972",
"text": ""
},
{
"id": "row_1027",
"parent": "row_972",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_1028",
"parent": "row_972",
"text": ""
},
{
"id": "row_1029",
"parent": "row_972",
"text": "String CisloStr;"
},
{
"id": "row_1030",
"parent": "row_972",
"text": "int CisloInt = 0;"
},
{
"id": "row_1031",
"parent": "row_972",
"text": "String[] stringArr;"
},
{
"id": "row_1032",
"parent": "row_972",
"text": "int[] cislaPopisu;"
},
{
"id": "row_1033",
"parent": "row_972",
"text": "String DotazPopis;"
},
{
"id": "row_1034",
"parent": "row_972",
"text": ""
},
{
"id": "row_1035",
"parent": "row_972",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_1036",
"parent": "row_972",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_1037",
"parent": "row_972",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1038",
"parent": "row_972",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_1039",
"parent": "row_972",
"text": ""
},
{
"id": "row_1040",
"parent": "row_972",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1041",
"parent": "row_972",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_1042",
"parent": "row_972",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_1043",
"parent": "row_972",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_1044",
"parent": "row_972",
"text": "}"
},
{
"id": "row_1045",
"parent": "row_972",
"text": ""
},
{
"id": "row_1046",
"parent": "row_972",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_1047",
"parent": "row_972",
"text": "}"
},
{
"id": "row_1048",
"parent": "row_972",
"text": ""
},
{
"id": "row_1049",
"parent": "row_972",
"text": "return (cislaPopisu);"
},
{
"id": "row_1050",
"parent": "row_972",
"text": ""
},
{
"id": "row_1051",
"parent": "#",
"text": "}"
},
{
"id": "row_1052",
"parent": "#",
"text": "//Ziska data vpravo"
},
{
"id": "row_1053",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVpravo);"
},
{
"id": "row_1054",
"parent": "#",
"text": "DotazySQLVpravo = DotazySQL;"
},
{
"id": "row_1055",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1056",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1057",
"parent": "row_1053",
"text": "String Radek;"
},
{
"id": "row_1058",
"parent": "row_1053",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1059",
"parent": "row_1053",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1060",
"parent": "row_1053",
"text": "String Dotaz = null;"
},
{
"id": "row_1061",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1062",
"parent": "row_1053",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1063",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1064",
"parent": "row_1053",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1065",
"parent": "row_1053",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1066",
"parent": "row_1053",
"text": "String PlnaCesta;"
},
{
"id": "row_1067",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1068",
"parent": "row_1053",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1069",
"parent": "row_1053",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1070",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1071",
"parent": "row_1053",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1072",
"parent": "row_1053",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1073",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1074",
"parent": "row_1053",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1075",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1076",
"parent": "row_1053",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1077",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1078",
"parent": "row_1053",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1079",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1080",
"parent": "row_1053",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1081",
"parent": "row_1053",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1082",
"parent": "row_1053",
"text": "//Dotaz = ||;"
},
{
"id": "row_1083",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1084",
"parent": "row_1053",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1085",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1086",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1087",
"parent": "row_1053",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1088",
"parent": "row_1053",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1089",
"parent": "row_1053",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1090",
"parent": "row_1053",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1091",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1092",
"parent": "row_1053",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1093",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1094",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1095",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1096",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1097",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1098",
"parent": "row_1053",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1099",
"parent": "row_1053",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1100",
"parent": "row_1053",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1101",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1102",
"parent": "row_1053",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1103",
"parent": "row_1053",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1104",
"parent": "row_1053",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1105",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1106",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1107",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1108",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1109",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1110",
"parent": "row_1053",
"text": "String Radek;"
},
{
"id": "row_1111",
"parent": "row_1053",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1112",
"parent": "row_1053",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1113",
"parent": "row_1053",
"text": "String Dotaz = null;"
},
{
"id": "row_1114",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1115",
"parent": "row_1053",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1116",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1117",
"parent": "row_1053",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1118",
"parent": "row_1053",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1119",
"parent": "row_1053",
"text": "String PlnaCesta;"
},
{
"id": "row_1120",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1121",
"parent": "row_1053",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1122",
"parent": "row_1053",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1123",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1124",
"parent": "row_1053",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1125",
"parent": "row_1053",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1126",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1127",
"parent": "row_1053",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1128",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1129",
"parent": "row_1053",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1130",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1131",
"parent": "row_1053",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1132",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1133",
"parent": "row_1053",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1134",
"parent": "row_1053",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1135",
"parent": "row_1053",
"text": "//Dotaz = ||;"
},
{
"id": "row_1136",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1137",
"parent": "row_1053",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1138",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1139",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1140",
"parent": "row_1053",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1141",
"parent": "row_1053",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1142",
"parent": "row_1053",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1143",
"parent": "row_1053",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1144",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1145",
"parent": "row_1053",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1146",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1147",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1148",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1149",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1150",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1151",
"parent": "row_1053",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1152",
"parent": "row_1053",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1153",
"parent": "row_1053",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1154",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1155",
"parent": "row_1053",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1156",
"parent": "row_1053",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1157",
"parent": "row_1053",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1158",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1159",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1160",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1161",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1162",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1163",
"parent": "row_1053",
"text": "String Radek;"
},
{
"id": "row_1164",
"parent": "row_1053",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1165",
"parent": "row_1053",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1166",
"parent": "row_1053",
"text": "String Dotaz = null;"
},
{
"id": "row_1167",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1168",
"parent": "row_1053",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1169",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1170",
"parent": "row_1053",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1171",
"parent": "row_1053",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1172",
"parent": "row_1053",
"text": "String PlnaCesta;"
},
{
"id": "row_1173",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1174",
"parent": "row_1053",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1175",
"parent": "row_1053",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1176",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1177",
"parent": "row_1053",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1178",
"parent": "row_1053",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1179",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1180",
"parent": "row_1053",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1181",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1182",
"parent": "row_1053",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1183",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1184",
"parent": "row_1053",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1185",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1186",
"parent": "row_1053",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1187",
"parent": "row_1053",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1188",
"parent": "row_1053",
"text": "//Dotaz = ||;"
},
{
"id": "row_1189",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1190",
"parent": "row_1053",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1191",
"parent": "row_1053",
"text": "{"
},
{
"id": "row_1192",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1193",
"parent": "row_1053",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1194",
"parent": "row_1053",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1195",
"parent": "row_1053",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1196",
"parent": "row_1053",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1197",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1198",
"parent": "row_1053",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1199",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1200",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1201",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1202",
"parent": "row_1053",
"text": "}"
},
{
"id": "row_1203",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1204",
"parent": "row_1053",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1205",
"parent": "row_1053",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1206",
"parent": "row_1053",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1207",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1208",
"parent": "row_1053",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1209",
"parent": "row_1053",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1210",
"parent": "row_1053",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1211",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1212",
"parent": "row_1053",
"text": ""
},
{
"id": "row_1213",
"parent": "#",
"text": "}"
},
{
"id": "row_1214",
"parent": "#",
"text": "DotazyPopisVpravo = DotazyPopis;"
},
{
"id": "row_1215",
"parent": "#",
"text": "cislaPopisuVPravo = oddelCisloDotazuOdTextuVpravo();"
},
{
"id": "row_1216",
"parent": "#",
"text": ""
},
{
"id": "row_1217",
"parent": "#",
"text": ""
},
{
"id": "row_1218",
"parent": "row_1215",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_1219",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1220",
"parent": "row_1215",
"text": "String CisloStr1;"
},
{
"id": "row_1221",
"parent": "row_1215",
"text": "String CisloStr2;"
},
{
"id": "row_1222",
"parent": "row_1215",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_1223",
"parent": "row_1215",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_1224",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1225",
"parent": "row_1215",
"text": "String[] stringArr;"
},
{
"id": "row_1226",
"parent": "row_1215",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_1227",
"parent": "row_1215",
"text": "String DotazPopis;"
},
{
"id": "row_1228",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1229",
"parent": "row_1215",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_1230",
"parent": "row_1215",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1231",
"parent": "row_1215",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_1232",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1233",
"parent": "row_1215",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1234",
"parent": "row_1215",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_1235",
"parent": "row_1215",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_1236",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1237",
"parent": "row_1215",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_1238",
"parent": "row_1215",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_1239",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1240",
"parent": "row_1215",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_1241",
"parent": "row_1215",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_1242",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1243",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1244",
"parent": "row_1215",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_1245",
"parent": "row_1215",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_1246",
"parent": "row_1215",
"text": "System.out.println(||);"
},
{
"id": "row_1247",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1248",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1249",
"parent": "row_1215",
"text": "return (cislaPopisu);"
},
{
"id": "row_1250",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1251",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1252",
"parent": "row_1215",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_1253",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1254",
"parent": "row_1215",
"text": "String CisloStr1;"
},
{
"id": "row_1255",
"parent": "row_1215",
"text": "String CisloStr2;"
},
{
"id": "row_1256",
"parent": "row_1215",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_1257",
"parent": "row_1215",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_1258",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1259",
"parent": "row_1215",
"text": "String[] stringArr;"
},
{
"id": "row_1260",
"parent": "row_1215",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_1261",
"parent": "row_1215",
"text": "String DotazPopis;"
},
{
"id": "row_1262",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1263",
"parent": "row_1215",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_1264",
"parent": "row_1215",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1265",
"parent": "row_1215",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_1266",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1267",
"parent": "row_1215",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1268",
"parent": "row_1215",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_1269",
"parent": "row_1215",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_1270",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1271",
"parent": "row_1215",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_1272",
"parent": "row_1215",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_1273",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1274",
"parent": "row_1215",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_1275",
"parent": "row_1215",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_1276",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1277",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1278",
"parent": "row_1215",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_1279",
"parent": "row_1215",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_1280",
"parent": "row_1215",
"text": "System.out.println(||);"
},
{
"id": "row_1281",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1282",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1283",
"parent": "row_1215",
"text": "return (cislaPopisu);"
},
{
"id": "row_1284",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1285",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1286",
"parent": "row_1215",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_1287",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1288",
"parent": "row_1215",
"text": "String CisloStr1;"
},
{
"id": "row_1289",
"parent": "row_1215",
"text": "String CisloStr2;"
},
{
"id": "row_1290",
"parent": "row_1215",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_1291",
"parent": "row_1215",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_1292",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1293",
"parent": "row_1215",
"text": "String[] stringArr;"
},
{
"id": "row_1294",
"parent": "row_1215",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_1295",
"parent": "row_1215",
"text": "String DotazPopis;"
},
{
"id": "row_1296",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1297",
"parent": "row_1215",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_1298",
"parent": "row_1215",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1299",
"parent": "row_1215",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_1300",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1301",
"parent": "row_1215",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1302",
"parent": "row_1215",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_1303",
"parent": "row_1215",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_1304",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1305",
"parent": "row_1215",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_1306",
"parent": "row_1215",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_1307",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1308",
"parent": "row_1215",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_1309",
"parent": "row_1215",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_1310",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1311",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1312",
"parent": "row_1215",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_1313",
"parent": "row_1215",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_1314",
"parent": "row_1215",
"text": "System.out.println(||);"
},
{
"id": "row_1315",
"parent": "row_1215",
"text": "}"
},
{
"id": "row_1316",
"parent": "row_1215",
"text": ""
},
{
"id": "row_1317",
"parent": "row_1215",
"text": "return (cislaPopisu);"
},
{
"id": "row_1318",
"parent": "#",
"text": "}"
},
{
"id": "row_1319",
"parent": "#",
"text": "preusporadejDataVPravoDo2D();"
},
{
"id": "row_1477",
"parent": "#",
"text": ""
},
{
"id": "row_1478",
"parent": "#",
"text": ""
},
{
"id": "row_1479",
"parent": "#",
"text": "}"
},
{
"id": "row_1480",
"parent": "#",
"text": "public NactiDotazy() throws IOException{"
},
{
"id": "row_1481",
"parent": "#",
"text": ""
},
{
"id": "row_1482",
"parent": "#",
"text": "String Adresa;"
},
{
"id": "row_1483",
"parent": "#",
"text": "String ZdrojDotazuVlevo;"
},
{
"id": "row_1484",
"parent": "#",
"text": "String ZdrojDotazuVpravo;"
},
{
"id": "row_1485",
"parent": "#",
"text": ""
},
{
"id": "row_1486",
"parent": "#",
"text": "Adresa = |C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\EXAMPLES-w3resource\\|;"
},
{
"id": "row_1487",
"parent": "#",
"text": "ZdrojDotazuVlevo = |RetrieveDataFromTablesCZ.txt|;"
},
{
"id": "row_1488",
"parent": "#",
"text": "ZdrojDotazuVpravo = |RetrieveDataFromTablesCZvpravo.txt|;"
},
{
"id": "row_1489",
"parent": "#",
"text": ""
},
{
"id": "row_1490",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_1491",
"parent": "#",
"text": "SubDotazyPopis[0][0] = |SubDotazyPopis[0][0]|;"
},
{
"id": "row_1492",
"parent": "#",
"text": "SubDotazyPopis[0][1] = |SubDotazyPopis[0][1]|;"
},
{
"id": "row_1493",
"parent": "#",
"text": "SubDotazyPopis[0][2] = |SubDotazyPopis[0][2]|;"
},
{
"id": "row_1494",
"parent": "#",
"text": ""
},
{
"id": "row_1495",
"parent": "#",
"text": "SubDotazyPopis[1][0] = |SubDotazyPopis[1][0]|;"
},
{
"id": "row_1496",
"parent": "#",
"text": "SubDotazyPopis[1][1] = |SubDotazyPopis[1][1]|;"
},
{
"id": "row_1497",
"parent": "#",
"text": "SubDotazyPopis[1][2] = |SubDotazyPopis[1][2]|;"
},
{
"id": "row_1498",
"parent": "#",
"text": ""
},
{
"id": "row_1499",
"parent": "#",
"text": "SubDotazyPopis[2][0] = |SubDotazyPopis[2][0]|;"
},
{
"id": "row_1500",
"parent": "#",
"text": "SubDotazyPopis[2][1] = |SubDotazyPopis[2][1]|;"
},
{
"id": "row_1501",
"parent": "#",
"text": "SubDotazyPopis[2][2] = |SubDotazyPopis[2][2]|;"
},
{
"id": "row_1502",
"parent": "#",
"text": ""
},
{
"id": "row_1503",
"parent": "#",
"text": ""
},
{
"id": "row_1504",
"parent": "#",
"text": "//Provizorne naplnuji pole"
},
{
"id": "row_1505",
"parent": "#",
"text": "SubDotazySQL[0][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_1506",
"parent": "#",
"text": "SubDotazySQL[0][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_1507",
"parent": "#",
"text": "SubDotazySQL[0][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_1508",
"parent": "#",
"text": ""
},
{
"id": "row_1509",
"parent": "#",
"text": "SubDotazySQL[1][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_1510",
"parent": "#",
"text": "SubDotazySQL[1][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_1511",
"parent": "#",
"text": "SubDotazySQL[1][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_1512",
"parent": "#",
"text": ""
},
{
"id": "row_1513",
"parent": "#",
"text": "SubDotazySQL[2][0] = |SELECT name,city\n FROM salesman|;"
},
{
"id": "row_1514",
"parent": "#",
"text": "SubDotazySQL[2][1] = |SELECT winner\n FROM nobel_win|;"
},
{
"id": "row_1515",
"parent": "#",
"text": "SubDotazySQL[2][2] = |SELECT pro_name, pro_price FROM item_mast|;"
},
{
"id": "row_1516",
"parent": "#",
"text": ""
},
{
"id": "row_1517",
"parent": "#",
"text": "//Ziska data vlevo"
},
{
"id": "row_1518",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVlevo);"
},
{
"id": "row_1519",
"parent": "#",
"text": "DotazySQLVlevo = DotazySQL;"
},
{
"id": "row_1520",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1521",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1522",
"parent": "row_1518",
"text": "String Radek;"
},
{
"id": "row_1523",
"parent": "row_1518",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1524",
"parent": "row_1518",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1525",
"parent": "row_1518",
"text": "String Dotaz = null;"
},
{
"id": "row_1526",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1527",
"parent": "row_1518",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1528",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1529",
"parent": "row_1518",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1530",
"parent": "row_1518",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1531",
"parent": "row_1518",
"text": "String PlnaCesta;"
},
{
"id": "row_1532",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1533",
"parent": "row_1518",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1534",
"parent": "row_1518",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1535",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1536",
"parent": "row_1518",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1537",
"parent": "row_1518",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1538",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1539",
"parent": "row_1518",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1540",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1541",
"parent": "row_1518",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1542",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1543",
"parent": "row_1518",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1544",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1545",
"parent": "row_1518",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1546",
"parent": "row_1518",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1547",
"parent": "row_1518",
"text": "//Dotaz = ||;"
},
{
"id": "row_1548",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1549",
"parent": "row_1518",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1550",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1551",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1552",
"parent": "row_1518",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1553",
"parent": "row_1518",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1554",
"parent": "row_1518",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1555",
"parent": "row_1518",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1556",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1557",
"parent": "row_1518",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1558",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1559",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1560",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1561",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1562",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1563",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1564",
"parent": "row_1518",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1565",
"parent": "row_1518",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1566",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1567",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1568",
"parent": "row_1518",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1569",
"parent": "row_1518",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1570",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1571",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1572",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1573",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1574",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1575",
"parent": "row_1518",
"text": "String Radek;"
},
{
"id": "row_1576",
"parent": "row_1518",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1577",
"parent": "row_1518",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1578",
"parent": "row_1518",
"text": "String Dotaz = null;"
},
{
"id": "row_1579",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1580",
"parent": "row_1518",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1581",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1582",
"parent": "row_1518",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1583",
"parent": "row_1518",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1584",
"parent": "row_1518",
"text": "String PlnaCesta;"
},
{
"id": "row_1585",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1586",
"parent": "row_1518",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1587",
"parent": "row_1518",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1588",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1589",
"parent": "row_1518",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1590",
"parent": "row_1518",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1591",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1592",
"parent": "row_1518",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1593",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1594",
"parent": "row_1518",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1595",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1596",
"parent": "row_1518",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1597",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1598",
"parent": "row_1518",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1599",
"parent": "row_1518",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1600",
"parent": "row_1518",
"text": "//Dotaz = ||;"
},
{
"id": "row_1601",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1602",
"parent": "row_1518",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1603",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1604",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1605",
"parent": "row_1518",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1606",
"parent": "row_1518",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1607",
"parent": "row_1518",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1608",
"parent": "row_1518",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1609",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1610",
"parent": "row_1518",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1611",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1612",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1613",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1614",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1615",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1616",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1617",
"parent": "row_1518",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1618",
"parent": "row_1518",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1619",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1620",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1621",
"parent": "row_1518",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1622",
"parent": "row_1518",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1623",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1624",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1625",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1626",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1627",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1628",
"parent": "row_1518",
"text": "String Radek;"
},
{
"id": "row_1629",
"parent": "row_1518",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1630",
"parent": "row_1518",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1631",
"parent": "row_1518",
"text": "String Dotaz = null;"
},
{
"id": "row_1632",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1633",
"parent": "row_1518",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1634",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1635",
"parent": "row_1518",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1636",
"parent": "row_1518",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1637",
"parent": "row_1518",
"text": "String PlnaCesta;"
},
{
"id": "row_1638",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1639",
"parent": "row_1518",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1640",
"parent": "row_1518",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1641",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1642",
"parent": "row_1518",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1643",
"parent": "row_1518",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1644",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1645",
"parent": "row_1518",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1646",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1647",
"parent": "row_1518",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1648",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1649",
"parent": "row_1518",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1650",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1651",
"parent": "row_1518",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1652",
"parent": "row_1518",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1653",
"parent": "row_1518",
"text": "//Dotaz = ||;"
},
{
"id": "row_1654",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1655",
"parent": "row_1518",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1656",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1657",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1658",
"parent": "row_1518",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1659",
"parent": "row_1518",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1660",
"parent": "row_1518",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1661",
"parent": "row_1518",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1662",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1663",
"parent": "row_1518",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1664",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1665",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1666",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1667",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1668",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1669",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1670",
"parent": "row_1518",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1671",
"parent": "row_1518",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1672",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1673",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1674",
"parent": "row_1518",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1675",
"parent": "row_1518",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1676",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1677",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1678",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1679",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1680",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1681",
"parent": "row_1518",
"text": "String Radek;"
},
{
"id": "row_1682",
"parent": "row_1518",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1683",
"parent": "row_1518",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1684",
"parent": "row_1518",
"text": "String Dotaz = null;"
},
{
"id": "row_1685",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1686",
"parent": "row_1518",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1687",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1688",
"parent": "row_1518",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1689",
"parent": "row_1518",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1690",
"parent": "row_1518",
"text": "String PlnaCesta;"
},
{
"id": "row_1691",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1692",
"parent": "row_1518",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1693",
"parent": "row_1518",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1694",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1695",
"parent": "row_1518",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1696",
"parent": "row_1518",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1697",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1698",
"parent": "row_1518",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1699",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1700",
"parent": "row_1518",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1701",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1702",
"parent": "row_1518",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1703",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1704",
"parent": "row_1518",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1705",
"parent": "row_1518",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1706",
"parent": "row_1518",
"text": "//Dotaz = ||;"
},
{
"id": "row_1707",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1708",
"parent": "row_1518",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1709",
"parent": "row_1518",
"text": "{"
},
{
"id": "row_1710",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1711",
"parent": "row_1518",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1712",
"parent": "row_1518",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1713",
"parent": "row_1518",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1714",
"parent": "row_1518",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1715",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1716",
"parent": "row_1518",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1717",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1718",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1719",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1720",
"parent": "row_1518",
"text": "}"
},
{
"id": "row_1721",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1722",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1723",
"parent": "row_1518",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1724",
"parent": "row_1518",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1725",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1726",
"parent": "row_1518",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1727",
"parent": "row_1518",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1728",
"parent": "row_1518",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1729",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1730",
"parent": "row_1518",
"text": ""
},
{
"id": "row_1731",
"parent": "#",
"text": "}"
},
{
"id": "row_1732",
"parent": "#",
"text": "DotazyPopisVlevo = DotazyPopis;"
},
{
"id": "row_1733",
"parent": "#",
"text": "cislaPopisuVlevo = oddelCisloDotazuOdTextuVlevo();"
},
{
"id": "row_1734",
"parent": "#",
"text": ""
},
{
"id": "row_1735",
"parent": "#",
"text": ""
},
{
"id": "row_1736",
"parent": "row_1733",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_1737",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1738",
"parent": "row_1733",
"text": "String CisloStr;"
},
{
"id": "row_1739",
"parent": "row_1733",
"text": "int CisloInt = 0;"
},
{
"id": "row_1740",
"parent": "row_1733",
"text": "String[] stringArr;"
},
{
"id": "row_1741",
"parent": "row_1733",
"text": "int[] cislaPopisu;"
},
{
"id": "row_1742",
"parent": "row_1733",
"text": "String DotazPopis;"
},
{
"id": "row_1743",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1744",
"parent": "row_1733",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_1745",
"parent": "row_1733",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_1746",
"parent": "row_1733",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1747",
"parent": "row_1733",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_1748",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1749",
"parent": "row_1733",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1750",
"parent": "row_1733",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_1751",
"parent": "row_1733",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_1752",
"parent": "row_1733",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_1753",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1754",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1755",
"parent": "row_1733",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_1756",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1757",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1758",
"parent": "row_1733",
"text": "return (cislaPopisu);"
},
{
"id": "row_1759",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1760",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1761",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1762",
"parent": "row_1733",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_1763",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1764",
"parent": "row_1733",
"text": "String CisloStr;"
},
{
"id": "row_1765",
"parent": "row_1733",
"text": "int CisloInt = 0;"
},
{
"id": "row_1766",
"parent": "row_1733",
"text": "String[] stringArr;"
},
{
"id": "row_1767",
"parent": "row_1733",
"text": "int[] cislaPopisu;"
},
{
"id": "row_1768",
"parent": "row_1733",
"text": "String DotazPopis;"
},
{
"id": "row_1769",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1770",
"parent": "row_1733",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_1771",
"parent": "row_1733",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_1772",
"parent": "row_1733",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1773",
"parent": "row_1733",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_1774",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1775",
"parent": "row_1733",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1776",
"parent": "row_1733",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_1777",
"parent": "row_1733",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_1778",
"parent": "row_1733",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_1779",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1780",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1781",
"parent": "row_1733",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_1782",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1783",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1784",
"parent": "row_1733",
"text": "return (cislaPopisu);"
},
{
"id": "row_1785",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1786",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1787",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1788",
"parent": "row_1733",
"text": "private int[] oddelCisloDotazuOdTextuVlevo(){"
},
{
"id": "row_1789",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1790",
"parent": "row_1733",
"text": "String CisloStr;"
},
{
"id": "row_1791",
"parent": "row_1733",
"text": "int CisloInt = 0;"
},
{
"id": "row_1792",
"parent": "row_1733",
"text": "String[] stringArr;"
},
{
"id": "row_1793",
"parent": "row_1733",
"text": "int[] cislaPopisu;"
},
{
"id": "row_1794",
"parent": "row_1733",
"text": "String DotazPopis;"
},
{
"id": "row_1795",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1796",
"parent": "row_1733",
"text": "//Oddeli cislo dotazu od textu dotazu"
},
{
"id": "row_1797",
"parent": "row_1733",
"text": "cislaPopisu = new int[DotazyPopisVlevo.length];"
},
{
"id": "row_1798",
"parent": "row_1733",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1799",
"parent": "row_1733",
"text": "DotazPopis = DotazyPopisVlevo[i];"
},
{
"id": "row_1800",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1801",
"parent": "row_1733",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1802",
"parent": "row_1733",
"text": "CisloStr = stringArr[0];"
},
{
"id": "row_1803",
"parent": "row_1733",
"text": "if (isNumeric(CisloStr) == true){"
},
{
"id": "row_1804",
"parent": "row_1733",
"text": "CisloInt = Integer.parseInt(CisloStr);"
},
{
"id": "row_1805",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1806",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1807",
"parent": "row_1733",
"text": "cislaPopisu[i] = CisloInt;"
},
{
"id": "row_1808",
"parent": "row_1733",
"text": "}"
},
{
"id": "row_1809",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1810",
"parent": "row_1733",
"text": "return (cislaPopisu);"
},
{
"id": "row_1811",
"parent": "row_1733",
"text": ""
},
{
"id": "row_1812",
"parent": "#",
"text": "}"
},
{
"id": "row_1813",
"parent": "#",
"text": "//Ziska data vpravo"
},
{
"id": "row_1814",
"parent": "#",
"text": "vratSQLDotazy(Adresa, ZdrojDotazuVpravo);"
},
{
"id": "row_1815",
"parent": "#",
"text": "DotazySQLVpravo = DotazySQL;"
},
{
"id": "row_1816",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1817",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1818",
"parent": "row_1814",
"text": "String Radek;"
},
{
"id": "row_1819",
"parent": "row_1814",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1820",
"parent": "row_1814",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1821",
"parent": "row_1814",
"text": "String Dotaz = null;"
},
{
"id": "row_1822",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1823",
"parent": "row_1814",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1824",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1825",
"parent": "row_1814",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1826",
"parent": "row_1814",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1827",
"parent": "row_1814",
"text": "String PlnaCesta;"
},
{
"id": "row_1828",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1829",
"parent": "row_1814",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1830",
"parent": "row_1814",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1831",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1832",
"parent": "row_1814",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1833",
"parent": "row_1814",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1834",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1835",
"parent": "row_1814",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1836",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1837",
"parent": "row_1814",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1838",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1839",
"parent": "row_1814",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1840",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1841",
"parent": "row_1814",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1842",
"parent": "row_1814",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1843",
"parent": "row_1814",
"text": "//Dotaz = ||;"
},
{
"id": "row_1844",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1845",
"parent": "row_1814",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1846",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1847",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1848",
"parent": "row_1814",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1849",
"parent": "row_1814",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1850",
"parent": "row_1814",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1851",
"parent": "row_1814",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1852",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1853",
"parent": "row_1814",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1854",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1855",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1856",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1857",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1858",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1859",
"parent": "row_1814",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1860",
"parent": "row_1814",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1861",
"parent": "row_1814",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1862",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1863",
"parent": "row_1814",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1864",
"parent": "row_1814",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1865",
"parent": "row_1814",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1866",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1867",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1868",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1869",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1870",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1871",
"parent": "row_1814",
"text": "String Radek;"
},
{
"id": "row_1872",
"parent": "row_1814",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1873",
"parent": "row_1814",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1874",
"parent": "row_1814",
"text": "String Dotaz = null;"
},
{
"id": "row_1875",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1876",
"parent": "row_1814",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1877",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1878",
"parent": "row_1814",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1879",
"parent": "row_1814",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1880",
"parent": "row_1814",
"text": "String PlnaCesta;"
},
{
"id": "row_1881",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1882",
"parent": "row_1814",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1883",
"parent": "row_1814",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1884",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1885",
"parent": "row_1814",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1886",
"parent": "row_1814",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1887",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1888",
"parent": "row_1814",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1889",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1890",
"parent": "row_1814",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1891",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1892",
"parent": "row_1814",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1893",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1894",
"parent": "row_1814",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1895",
"parent": "row_1814",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1896",
"parent": "row_1814",
"text": "//Dotaz = ||;"
},
{
"id": "row_1897",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1898",
"parent": "row_1814",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1899",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1900",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1901",
"parent": "row_1814",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1902",
"parent": "row_1814",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1903",
"parent": "row_1814",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1904",
"parent": "row_1814",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1905",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1906",
"parent": "row_1814",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1907",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1908",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1909",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1910",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1911",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1912",
"parent": "row_1814",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1913",
"parent": "row_1814",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1914",
"parent": "row_1814",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1915",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1916",
"parent": "row_1814",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1917",
"parent": "row_1814",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1918",
"parent": "row_1814",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1919",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1920",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1921",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1922",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1923",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1924",
"parent": "row_1814",
"text": "String Radek;"
},
{
"id": "row_1925",
"parent": "row_1814",
"text": "String PrvniZnak = null;"
},
{
"id": "row_1926",
"parent": "row_1814",
"text": "boolean jePrvniZnakCislo = false;"
},
{
"id": "row_1927",
"parent": "row_1814",
"text": "String Dotaz = null;"
},
{
"id": "row_1928",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1929",
"parent": "row_1814",
"text": "String[] SeznamRadkuArr;"
},
{
"id": "row_1930",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1931",
"parent": "row_1814",
"text": "int prvniRadekDotazu;"
},
{
"id": "row_1932",
"parent": "row_1814",
"text": "int posledniRadekDotazu;"
},
{
"id": "row_1933",
"parent": "row_1814",
"text": "String PlnaCesta;"
},
{
"id": "row_1934",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1935",
"parent": "row_1814",
"text": "PlnaCesta = Adresa + NazevSouboru;"
},
{
"id": "row_1936",
"parent": "row_1814",
"text": "SeznamRadkuArr = NactiSoubor(PlnaCesta);"
},
{
"id": "row_1937",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1938",
"parent": "row_1814",
"text": "ArrayList<String> DotazyPopisList = new ArrayList<String>();"
},
{
"id": "row_1939",
"parent": "row_1814",
"text": "ArrayList<String> DotazySQLList = new ArrayList<String>();"
},
{
"id": "row_1940",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1941",
"parent": "row_1814",
"text": "for (int i = 0; i < SeznamRadkuArr.length; i++) {"
},
{
"id": "row_1942",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1943",
"parent": "row_1814",
"text": "Radek = SeznamRadkuArr[i];"
},
{
"id": "row_1944",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1945",
"parent": "row_1814",
"text": "if (Radek.isEmpty() == false)"
},
{
"id": "row_1946",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1947",
"parent": "row_1814",
"text": "PrvniZnak = Radek.substring(0, 1);"
},
{
"id": "row_1948",
"parent": "row_1814",
"text": "jePrvniZnakCislo = isNumeric(PrvniZnak);"
},
{
"id": "row_1949",
"parent": "row_1814",
"text": "//Dotaz = ||;"
},
{
"id": "row_1950",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1951",
"parent": "row_1814",
"text": "if (jePrvniZnakCislo == true)"
},
{
"id": "row_1952",
"parent": "row_1814",
"text": "{"
},
{
"id": "row_1953",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1954",
"parent": "row_1814",
"text": "DotazyPopisList.add(Radek);"
},
{
"id": "row_1955",
"parent": "row_1814",
"text": "prvniRadekDotazu = i + 1;"
},
{
"id": "row_1956",
"parent": "row_1814",
"text": "posledniRadekDotazu = vratPosledniRadekDotazu(prvniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1957",
"parent": "row_1814",
"text": "Dotaz = vratStringDotazu(prvniRadekDotazu, posledniRadekDotazu, SeznamRadkuArr);"
},
{
"id": "row_1958",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1959",
"parent": "row_1814",
"text": "DotazySQLList.add(Dotaz);"
},
{
"id": "row_1960",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1961",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1962",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1963",
"parent": "row_1814",
"text": "}"
},
{
"id": "row_1964",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1965",
"parent": "row_1814",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1966",
"parent": "row_1814",
"text": "DotazyPopis = new String[DotazyPopisList.size()];"
},
{
"id": "row_1967",
"parent": "row_1814",
"text": "DotazyPopis = DotazyPopisList.toArray(DotazyPopis);"
},
{
"id": "row_1968",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1969",
"parent": "row_1814",
"text": "//Prekonvertuje na pole Stringu"
},
{
"id": "row_1970",
"parent": "row_1814",
"text": "DotazySQL = new String[DotazySQLList.size()];"
},
{
"id": "row_1971",
"parent": "row_1814",
"text": "DotazySQL = DotazySQLList.toArray(DotazySQL);"
},
{
"id": "row_1972",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1973",
"parent": "row_1814",
"text": ""
},
{
"id": "row_1974",
"parent": "#",
"text": "}"
},
{
"id": "row_1975",
"parent": "#",
"text": "DotazyPopisVpravo = DotazyPopis;"
},
{
"id": "row_1976",
"parent": "#",
"text": "cislaPopisuVPravo = oddelCisloDotazuOdTextuVpravo();"
},
{
"id": "row_1977",
"parent": "#",
"text": ""
},
{
"id": "row_1978",
"parent": "#",
"text": ""
},
{
"id": "row_1979",
"parent": "row_1976",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_1980",
"parent": "row_1976",
"text": ""
},
{
"id": "row_1981",
"parent": "row_1976",
"text": "String CisloStr1;"
},
{
"id": "row_1982",
"parent": "row_1976",
"text": "String CisloStr2;"
},
{
"id": "row_1983",
"parent": "row_1976",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_1984",
"parent": "row_1976",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_1985",
"parent": "row_1976",
"text": ""
},
{
"id": "row_1986",
"parent": "row_1976",
"text": "String[] stringArr;"
},
{
"id": "row_1987",
"parent": "row_1976",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_1988",
"parent": "row_1976",
"text": "String DotazPopis;"
},
{
"id": "row_1989",
"parent": "row_1976",
"text": ""
},
{
"id": "row_1990",
"parent": "row_1976",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_1991",
"parent": "row_1976",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_1992",
"parent": "row_1976",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_1993",
"parent": "row_1976",
"text": ""
},
{
"id": "row_1994",
"parent": "row_1976",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_1995",
"parent": "row_1976",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_1996",
"parent": "row_1976",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_1997",
"parent": "row_1976",
"text": ""
},
{
"id": "row_1998",
"parent": "row_1976",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_1999",
"parent": "row_1976",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_2000",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2001",
"parent": "row_1976",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_2002",
"parent": "row_1976",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_2003",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2004",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2005",
"parent": "row_1976",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_2006",
"parent": "row_1976",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_2007",
"parent": "row_1976",
"text": "System.out.println(||);"
},
{
"id": "row_2008",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2009",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2010",
"parent": "row_1976",
"text": "return (cislaPopisu);"
},
{
"id": "row_2011",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2012",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2013",
"parent": "row_1976",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_2014",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2015",
"parent": "row_1976",
"text": "String CisloStr1;"
},
{
"id": "row_2016",
"parent": "row_1976",
"text": "String CisloStr2;"
},
{
"id": "row_2017",
"parent": "row_1976",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_2018",
"parent": "row_1976",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_2019",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2020",
"parent": "row_1976",
"text": "String[] stringArr;"
},
{
"id": "row_2021",
"parent": "row_1976",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_2022",
"parent": "row_1976",
"text": "String DotazPopis;"
},
{
"id": "row_2023",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2024",
"parent": "row_1976",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_2025",
"parent": "row_1976",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_2026",
"parent": "row_1976",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_2027",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2028",
"parent": "row_1976",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_2029",
"parent": "row_1976",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_2030",
"parent": "row_1976",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_2031",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2032",
"parent": "row_1976",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_2033",
"parent": "row_1976",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_2034",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2035",
"parent": "row_1976",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_2036",
"parent": "row_1976",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_2037",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2038",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2039",
"parent": "row_1976",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_2040",
"parent": "row_1976",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_2041",
"parent": "row_1976",
"text": "System.out.println(||);"
},
{
"id": "row_2042",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2043",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2044",
"parent": "row_1976",
"text": "return (cislaPopisu);"
},
{
"id": "row_2045",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2046",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2047",
"parent": "row_1976",
"text": "private int[][] oddelCisloDotazuOdTextuVpravo(){"
},
{
"id": "row_2048",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2049",
"parent": "row_1976",
"text": "String CisloStr1;"
},
{
"id": "row_2050",
"parent": "row_1976",
"text": "String CisloStr2;"
},
{
"id": "row_2051",
"parent": "row_1976",
"text": "int CisloInt1 = 0;"
},
{
"id": "row_2052",
"parent": "row_1976",
"text": "int CisloInt2 = 0;"
},
{
"id": "row_2053",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2054",
"parent": "row_1976",
"text": "String[] stringArr;"
},
{
"id": "row_2055",
"parent": "row_1976",
"text": "int[][] cislaPopisu;"
},
{
"id": "row_2056",
"parent": "row_1976",
"text": "String DotazPopis;"
},
{
"id": "row_2057",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2058",
"parent": "row_1976",
"text": "cislaPopisu = new int[DotazyPopisVpravo.length][2];"
},
{
"id": "row_2059",
"parent": "row_1976",
"text": "for (int i = 0; i < cislaPopisu.length; i++) {"
},
{
"id": "row_2060",
"parent": "row_1976",
"text": "DotazPopis = DotazyPopisVpravo[i];"
},
{
"id": "row_2061",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2062",
"parent": "row_1976",
"text": "stringArr = DotazPopis.split(|\\.|);"
},
{
"id": "row_2063",
"parent": "row_1976",
"text": "CisloStr1 = stringArr[0];"
},
{
"id": "row_2064",
"parent": "row_1976",
"text": "CisloStr2 = stringArr[1];"
},
{
"id": "row_2065",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2066",
"parent": "row_1976",
"text": "if (isNumeric(CisloStr1) == true){"
},
{
"id": "row_2067",
"parent": "row_1976",
"text": "CisloInt1 = Integer.parseInt(CisloStr1);"
},
{
"id": "row_2068",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2069",
"parent": "row_1976",
"text": "if (isNumeric(CisloStr2) == true){"
},
{
"id": "row_2070",
"parent": "row_1976",
"text": "CisloInt2 = Integer.parseInt(CisloStr2);"
},
{
"id": "row_2071",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2072",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2073",
"parent": "row_1976",
"text": "cislaPopisu[i][0] = CisloInt1;"
},
{
"id": "row_2074",
"parent": "row_1976",
"text": "cislaPopisu[i][1] = CisloInt2;"
},
{
"id": "row_2075",
"parent": "row_1976",
"text": "System.out.println(||);"
},
{
"id": "row_2076",
"parent": "row_1976",
"text": "}"
},
{
"id": "row_2077",
"parent": "row_1976",
"text": ""
},
{
"id": "row_2078",
"parent": "row_1976",
"text": "return (cislaPopisu);"
},
{
"id": "row_2079",
"parent": "#",
"text": "}"
},
{
"id": "row_2080",
"parent": "#",
"text": "preusporadejDataVPravoDo2D();"
},
{
"id": "row_2238",
"parent": "#",
"text": ""
},
{
"id": "row_2239",
"parent": "#",
"text": ""
},
{
"id": "row_2299",
"parent": "#",
"text": "public VytvorDB() throws IOException, ClassNotFoundException, SQLException{"
},
{
"id": "row_2300",
"parent": "#",
"text": ""
},
{
"id": "row_2301",
"parent": "#",
"text": "String QueryCreateTable;"
},
{
"id": "row_2302",
"parent": "#",
"text": "String AdresaKTabulce;"
},
{
"id": "row_2303",
"parent": "#",
"text": ""
},
{
"id": "row_2304",
"parent": "#",
"text": "String NazvyTabulek[];"
},
{
"id": "row_2305",
"parent": "#",
"text": "String NazevTabulky;"
},
{
"id": "row_2306",
"parent": "#",
"text": ""
},
{
"id": "row_2307",
"parent": "#",
"text": ""
},
{
"id": "row_2308",
"parent": "#",
"text": "//Dropne vsechny tabulky"
},
{
"id": "row_2309",
"parent": "#",
"text": "DropTable Drop = new DropTable();"
},
{
"id": "row_2345",
"parent": "#",
"text": "AdresaKTabulce = |C:\\Users\\jonas\\OneDrive\\Dokumenty\\JAVA\\Pokusy\\DataBase\\DataBase-Zdroje\\|;"
},
{
"id": "row_2346",
"parent": "#",
"text": ""
},
{
"id": "row_2347",
"parent": "#",
"text": "//Pripravi seznam tabulek podle nazvu txt ve slozce"
},
{
"id": "row_2348",
"parent": "#",
"text": "NazvyTabulek = SeznamTabulekZTxt(AdresaKTabulce);"
},
{
"id": "row_2349",
"parent": "#",
"text": ""
},
{
"id": "row_2350",
"parent": "#",
"text": ""
},
{
"id": "row_2351",
"parent": "#",
"text": "private String[] SeznamTabulekZTxt(String AdresaKTabulce) throws IOException {"
},
{
"id": "row_2352",
"parent": "#",
"text": ""
},
{
"id": "row_2353",
"parent": "#",
"text": "String ObsahSlozky[];"
},
{
"id": "row_2354",
"parent": "#",
"text": "String NazevSouboru;"
},
{
"id": "row_2355",
"parent": "#",
"text": "String NazevTabulky = null;"
},
{
"id": "row_2356",
"parent": "#",
"text": "int indexOfPripony;"
},
{
"id": "row_2357",
"parent": "#",
"text": ""
},
{
"id": "row_2358",
"parent": "#",
"text": "ObsahSlozky = VratObsahSlozky(AdresaKTabulce);"
},
{
"id": "row_2359",
"parent": "#",
"text": ""
},
{
"id": "row_2360",
"parent": "#",
"text": "ArrayList<String> NazvyTabulek = new ArrayList<String>();"
},
{
"id": "row_2361",
"parent": "#",
"text": ""
},
{
"id": "row_2362",
"parent": "#",
"text": "//Jen ty soubory s priponou txt vypise jako Tabulky"
},
{
"id": "row_2363",
"parent": "#",
"text": "for (int i = 0; i < ObsahSlozky.length; i++) {"
},
{
"id": "row_2364",
"parent": "#",
"text": "NazevSouboru = ObsahSlozky[i];"
},
{
"id": "row_2365",
"parent": "#",
"text": "indexOfPripony = NazevSouboru.indexOf(|.txt|);"
},
{
"id": "row_2366",
"parent": "#",
"text": "if (indexOfPripony > -1)"
},
{
"id": "row_2367",
"parent": "#",
"text": "{"
},
{
"id": "row_2368",
"parent": "#",
"text": "NazevTabulky = NazevSouboru.substring(0, indexOfPripony);"
},
{
"id": "row_2369",
"parent": "#",
"text": "NazvyTabulek.add(NazevTabulky);"
},
{
"id": "row_2370",
"parent": "#",
"text": "}"
},
{
"id": "row_2371",
"parent": "#",
"text": "}"
},
{
"id": "row_2372",
"parent": "#",
"text": ""
},
{
"id": "row_2373",
"parent": "#",
"text": "//Preverde ArrayList na pole"
},
{
"id": "row_2374",
"parent": "#",
"text": "String[] NazvyTabulekArr = new String[NazvyTabulek.size()];"
},
{
"id": "row_2375",
"parent": "#",
"text": "NazvyTabulekArr = NazvyTabulek.toArray(NazvyTabulekArr);"
},
{
"id": "row_2376",
"parent": "#",
"text": ""
},
{
"id": "row_2377",
"parent": "#",
"text": "return NazvyTabulekArr;"
},
{
"id": "row_2378",
"parent": "#",
"text": ""
},
{
"id": "row_2379",
"parent": "#",
"text": "}"
},
{
"id": "row_2380",
"parent": "#",
"text": "//Vytvori jednotlive tabulky"
},
{
"id": "row_2381",
"parent": "#",
"text": "for (int i = 0; i < NazvyTabulek.length; i++) {"
},
{
"id": "row_2382",
"parent": "#",
"text": "NazevTabulky = NazvyTabulek[i];"
},
{
"id": "row_2383",
"parent": "#",
"text": "PridejTabulkuDoDB(AdresaKTabulce, NazevTabulky);"
},
                ]
            }
        }
        //odebere predchozi strom
        $('#usingJsonTree').remove();
        //prida strom novy
        $('.tree').append('<div id="usingJsonTree"></div>');
        var myTree = $('#usingJsonTree').jstree(jsTreeDataJson);
    }
}
$(document).ready(function(){
var xxx = new vykresliStromFolder();
});
