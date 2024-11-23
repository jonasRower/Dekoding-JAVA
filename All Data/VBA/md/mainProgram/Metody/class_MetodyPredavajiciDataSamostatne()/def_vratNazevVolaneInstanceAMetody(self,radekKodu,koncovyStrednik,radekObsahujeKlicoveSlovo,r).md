# def vratNazevVolaneInstanceAMetody(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo, r):

### list of variables
volanaInstance   
volanaMetoda   
koncovyStrednik   
radekObsahujeKlicoveSlovo   
<a href  
jednaSeOMetodu   
indexZavorkyOtevrene   
kodRadkuPredZavorkou   
slovaNaRadku   
InstanceAMetoda   
InstanceAMetodaArr   
len(InstanceAMetodaArr)   
jeInstanceKlicoveSlovo   
jeMetodaKlicoveSlovo   

### code of method
<pre>
 <code>
    def vratNazevVolaneInstanceAMetody(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo, r):

        volanaInstance = ""
        volanaMetoda = ""

        # Test: radekKodu = "indexOfFROM = originalniSelect.indexOf(FROM);"

        # kod ma vyznam vykonavat pouze tehdy, pokud radek obsahuje strednik
        if (koncovyStrednik == True):

            # a pokud radek neobsahuje klicove slovo jako napr. for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
                  <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_MetodyPredavajiciDataSamostatne()\def __InjectedObj(self)">jednaSeOMetodu=self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)</a>

                if (jednaSeOMetodu == True):
                    indexZavorkyOtevrene = radekKodu.index('(')
                    kodRadkuPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
                    slovaNaRadku = kodRadkuPredZavorkou.split()
                    InstanceAMetoda = slovaNaRadku[-1]
                    InstanceAMetodaArr = InstanceAMetoda.split(".")

                    if (len(InstanceAMetodaArr) == 2):
                        volanaInstance = InstanceAMetodaArr[0]
                        volanaMetoda = InstanceAMetodaArr[1]

                          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_MetodyPredavajiciDataSamostatne()\def __InjectedObj(self)">jeInstanceKlicoveSlovo=self.__InjectedObj().detekujPritomnostKlicovehoSlova(volanaInstance)</a>
                          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_MetodyPredavajiciDataSamostatne()\def __InjectedObj(self)">jeMetodaKlicoveSlovo=self.__InjectedObj().detekujPritomnostKlicovehoSlova(volanaMetoda)</a>

                        # proveri, zda se nahodnou nejedna o klicove slovo, pokud ano, pak jej prepise na""
                        if (jeInstanceKlicoveSlovo == True):
                            volanaInstance = ""
                            volanaMetoda = ""

                        if (jeMetodaKlicoveSlovo == True):
                            volanaInstance = ""
                            volanaMetoda = ""

          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_MetodyPredavajiciDataSamostatne()\def __InjectedObj(self)">self.__data.add_volanaInstance(volanaInstance)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\Metody\class_MetodyPredavajiciDataSamostatne()\def __InjectedObj(self)">self.__data.add_volanaMetoda(volanaMetoda)</a>
 <code>
<pre>




