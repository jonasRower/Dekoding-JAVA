# def vratNazevVolaneInstanceAMetody(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo, r):

### list of variables
volanaInstance   
volanaMetoda   
if (koncovyStrednik   
if (radekObsahujeKlicoveSlovo   
jednaSeOMetodu   
if (jednaSeOMetodu   
indexZavorkyOtevrene   
kodRadkuPredZavorkou   
slovaNaRadku   
InstanceAMetoda   
InstanceAMetodaArr   
if (len(InstanceAMetodaArr)   
jeInstanceKlicoveSlovo   
jeMetodaKlicoveSlovo   
if (jeInstanceKlicoveSlovo   
if (jeMetodaKlicoveSlovo   

### code of method
```
    def vratNazevVolaneInstanceAMetody(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo, r):

        volanaInstance = ""
        volanaMetoda = ""

        # Test: radekKodu = "indexOfFROM = originalniSelect.indexOf(FROM);"

        # kod ma vyznam vykonavat pouze tehdy, pokud radek obsahuje strednik
        if (koncovyStrednik == True):

            # a pokud radek neobsahuje klicove slovo jako napr. for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
                jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

                if (jednaSeOMetodu == True):
                    indexZavorkyOtevrene = radekKodu.index('(')
                    kodRadkuPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
                    slovaNaRadku = kodRadkuPredZavorkou.split()
                    InstanceAMetoda = slovaNaRadku[-1]
                    InstanceAMetodaArr = InstanceAMetoda.split(".")

                    if (len(InstanceAMetodaArr) == 2):
                        volanaInstance = InstanceAMetodaArr[0]
                        volanaMetoda = InstanceAMetodaArr[1]

                        jeInstanceKlicoveSlovo = self.__InjectedObj().detekujPritomnostKlicovehoSlova(volanaInstance)
                        jeMetodaKlicoveSlovo = self.__InjectedObj().detekujPritomnostKlicovehoSlova(volanaMetoda)

                        # proveri, zda se nahodnou nejedna o klicove slovo, pokud ano, pak jej prepise na""
                        if (jeInstanceKlicoveSlovo == True):
                            volanaInstance = ""
                            volanaMetoda = ""

                        if (jeMetodaKlicoveSlovo == True):
                            volanaInstance = ""
                            volanaMetoda = ""

        self.__data.add_volanaInstance(volanaInstance)
        self.__data.add_volanaMetoda(volanaMetoda)
```
