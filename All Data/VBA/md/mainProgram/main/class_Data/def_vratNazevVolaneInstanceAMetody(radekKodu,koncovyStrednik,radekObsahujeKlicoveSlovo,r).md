# def vratNazevVolaneInstanceAMetody(radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo,r):

### list of variables
volanaInstance   
volanaMetoda   
koncovyStrednik   
if(radekObsahujeKlicoveSlovo   
jednaSeOMetodu   
indexZavorkyOtevrene   
kodRadkuPredZavorkou   
slovaNaRadku   
InstanceAMetoda   
InstanceAMetodaArr   
len(InstanceAMetodaArr)   
jeInstanceKlicoveSlovo   
jeMetodaKlicoveSlovo   
if(jeMetodaKlicoveSlovo   

### code of method
<pre>
 <code>
def vratNazevVolaneInstanceAMetody(radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo,r):
    # vraci data z typoveho radku:
    # DataSelectuNejmensi = selNejmensi.getDataSelectu();

    volanaInstance = ""
    volanaMetoda = ""

    #Test: radekKodu = "indexOfFROM = originalniSelect.indexOf(FROM);"

    # kod ma vyznam vykonavat pouze tehdy, pokud radek obsahuje strednik
    if (koncovyStrednik == True):

        # a pokud radek neobsahuje klicove slovo jako napr. for, if, catch ...
        if(radekObsahujeKlicoveSlovo == False):

            # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
            jednaSeOMetodu = indikujZdaSeJednaOMetodu(radekKodu)
            if (jednaSeOMetodu == True):
                indexZavorkyOtevrene = radekKodu.index('(')
                kodRadkuPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
                slovaNaRadku = kodRadkuPredZavorkou.split()
                InstanceAMetoda = slovaNaRadku[-1]
                InstanceAMetodaArr = InstanceAMetoda.split(".")

                if (len(InstanceAMetodaArr) == 2):
                    volanaInstance = InstanceAMetodaArr[0]
                    volanaMetoda = InstanceAMetodaArr[1]

                    jeInstanceKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(volanaInstance)
                    jeMetodaKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(volanaMetoda)

                    #proveri, zda se nahodnou nejedna o klicove slovo, pokud ano, pak jej prepise na""
                    if (jeInstanceKlicoveSlovo == True):
                        volanaInstance = ""
                        volanaMetoda = ""

                    if(jeMetodaKlicoveSlovo == True):
                        volanaInstance = ""
                        volanaMetoda = ""

                    #if(volanaMetoda == "indexOf"):
                    #    jeMetodaKlicoveSlovo = zjistiZdaRadekKoduObsahujeKlicoveSlovo(volanaMetoda)
                     #   print("")
                     #   volanaInstance = ""
                     #   volanaMetoda = ""

    data.add_volanaInstance(volanaInstance)
    data.add_volanaMetoda(volanaMetoda)
    print("")
 <code>
<pre>
