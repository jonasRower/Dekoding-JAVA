# def vratNazevVolaneMetody(self, radekKodu, koncovyStrednik, klicoveSlovo, r):

### list of variables
metodaPredZavorkou   
koncovyStrednik   
klicoveSlovo   
radekObsaheujeNew   
indexZavorkyOtevrene   
indexRovnitka   
metodaPredZavorkou !  
self.__data.volanaMetoda[r]   
indexTecky   

### code of method
```
    def vratNazevVolaneMetody(self, radekKodu, koncovyStrednik, klicoveSlovo, r):
        metodaPredZavorkou = ""

        if (koncovyStrednik == True):
            if (klicoveSlovo == False):

                # potvrdi zda radek neobsahuje klicove slovo "new"
                radekObsaheujeNew = self.__InjectedObj().obahujeRadekKoduKlicoveSlovoNew(radekKodu)

                if (radekObsaheujeNew == True):
                    # pak zapise konstruktor
                    self.zapisMetoduJakoKonstruktor(radekKodu, r)
                else:
                    # if (radekObsaheujeNew == False):
                    # aby to byla metoda musi tam byt zavorky, proto telo metody je v celem tele try:
                    try:
                        indexZavorkyOtevrene = radekKodu.index('(')
                        metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]

                        # ale nemusi tam byt = (tj. muze byt volani jak zleve tak i prave strany)
                        # protoze nemusi, pak zbytek tela je za pass
                        try:
                            # Tento kod se uplatni, pokud je volana metoda na prave strane vyrazu
                            indexRovnitka = metodaPredZavorkou.index('=')
                            metodaPredZavorkou = metodaPredZavorkou[(indexRovnitka + 1):(len(metodaPredZavorkou))]

                            # pokud kod dojde sem, pak pokracuje za pass
                        except:
                            pass

                        metodaPredZavorkou = metodaPredZavorkou.replace(" ", "")

                        # pole je jiz vytvorene (v metode vratNazevVolaneInstanceAMetody)
                        # a proto pro zapisovani se nepouziva append a zapisuji se data zde
                        # zapise se tedy volanaMetoda, pokud neobsahuje ""
                        if (metodaPredZavorkou != ""):

                            # zapisuje pouze ty data, ktere nebyly zapsany
                            if (self.__data.volanaMetoda[r] == ""):
                                # jelikoz v metode vratNazevVolaneInstanceAMetody
                                # zapisuje "" pokud metoda se jmenuje napr. indexOf,
                                # pak se prepisuje kod zde - je tedy treba odfiltrovat i napr: "originalniSelect.indexOf"
                                # to se pozna prave diky tecce
                                try:
                                    indexTecky = metodaPredZavorkou.index('.')
                                    # kdyz najde tecku, pak neprovede nic (tecka v metodaPredZavorkou, nikoliv v radekKodu)
                                except:
                                    # kdyz tecku nenajde, pak zapise data
                                    self.__data.volanaMetoda[r] = metodaPredZavorkou

                    except:
                        pass

        # Data se vraceji pro formalnost, pouze pro testovani
        return (metodaPredZavorkou)
```
### links
[radekObsaheujeNew=self.__InjectedObj().obahujeRadekKoduKlicoveSlovoNew(radekKodu)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def___InjectedObj(self).md)  
[self.zapisMetoduJakoKonstruktor(radekKodu,r)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyPredavajiciDataSamostatne()/def_zapisMetoduJakoKonstruktor(self,_radekKodu,_r).md)  
