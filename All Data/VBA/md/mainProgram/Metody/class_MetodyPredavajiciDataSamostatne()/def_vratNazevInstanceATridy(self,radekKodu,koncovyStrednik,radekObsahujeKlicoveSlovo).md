# def vratNazevInstanceATridy(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo):

### list of variables
nazevInstance   
nazevTridy   
jednaSeOMetodu   
if (jednaSeOMetodu   
if (koncovyStrednik   
if (radekObsahujeKlicoveSlovo   
radekObsahujeNew   
if (radekObsahujeNew   
indexRovnitka   
slovaNaRadku   

### code of method
```
    def vratNazevInstanceATridy(self, radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo):

        nazevInstance = ""
        nazevTridy = ""

        # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
        jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

        if (jednaSeOMetodu == True):

            # pokud radek neobsahuje strednik, pak se nejedna o radek typu:
            # Select selStredni = new Select(dotazStredni);
            # a tudis neni co resit a na konci funkce se zapisi data typu "" do pole
            if (koncovyStrednik == True):

                # Take radek nesmi obsahovat klicove slovo for, if, catch ...
                if (radekObsahujeKlicoveSlovo == False):

                    # zjisti index klicoveho slova 'new'
                    radekObsahujeNew = self.__InjectedObj().obahujeRadekKoduKlicoveSlovoNew(radekKodu)
                    if (radekObsahujeNew == True):

                        # pokud klicove slovo "new" je obsazeno, pak proveruje, zda radekKodu obsahuje "="
                        if (radekObsahujeNew == True):
                            indexRovnitka = 0
                            try:
                                indexRovnitka = radekKodu.index('=')
                            except:
                                pass

                            # pokud i obsahuje "=" pak pokracuje kod dal - oddeli nazev Instance a nazev Tridy
                            slovaNaRadku = radekKodu.split()
                            nazevTridy = slovaNaRadku[0]
                            nazevInstance = slovaNaRadku[1]

        # data do pole se predavaji zde
        self.__data.add_nazevInstance(nazevInstance)
        self.__data.add_nazevTridy(nazevTridy)
```
### links
[jednaSeOMetodu=self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)](../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def __InjectedObj(self))
[radekObsahujeNew=self.__InjectedObj().obahujeRadekKoduKlicoveSlovoNew(radekKodu)](../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def __InjectedObj(self))
[self.__data.add_nazevInstance(nazevInstance)](../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def __InjectedObj(self))
[self.__data.add_nazevTridy(nazevTridy)](../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def __InjectedObj(self))  

[toto je test](../../../../README.md)  
[odkaz na stejny soubor](../All%20Data/test1.md)  
[odkaz na cizi soubor](../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_kVolaneMetodeNajdiNazevTridy(self%2CdataJednohoSouboru%2CdataVsechSouboru).md)  
