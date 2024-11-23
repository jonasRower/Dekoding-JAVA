# def dopisujIndexyOtevrenychAZavrenychZavorek(self):

### list of variables
i   
indexNejblizsiOtevreneZavorky   
indexNejblizsiZavreneZavorky   
radekObsahujeKlicoveSlovo   
nazevMetodyHodnota !  
vyhledejOdRadku   
radekVolaneMetody   
self.__data.zacatekBloku[radekVolaneMetody]   
self.__data.konecBloku[radekVolaneMetody]   

### code of method
<pre>
 <code>
    def dopisujIndexyOtevrenychAZavrenychZavorek(self):
        # dopisuje indexy otevrenych a zavrenych zavorek ( "{", "}" ) na radek v Data, kde je volana metoda
        # proto je potreba vyhledavat volanou metodu

        i = -1

        for nazevMetodyHodnota in self.__data.nazevMetody:
            i = i + 1
              

            indexNejblizsiOtevreneZavorky = -1
            indexNejblizsiZavreneZavorky = -1

            # zapisuje zacatek a konec bloku, v pripadech, kdy se nejedna o klicove slovo, tedy for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                if (nazevMetodyHodnota != ""):
                    vyhledejOdRadku = i - 1
                    indexNejblizsiOtevreneZavorky = OstatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(self, vyhledejOdRadku, self.__data.slozenaZavorka)
                    indexNejblizsiZavreneZavorky = OstatniMetody.vratCisloRadkuSKoncemBloku(self, indexNejblizsiOtevreneZavorky, self.__data.slozenaZavorka)

                      
                    radekVolaneMetody = OstatniMetody.najdiRadekVolaneMetody(self, nazevMetodyHodnota, self.__data.volanaMetoda)
                    if (radekVolaneMetody > -1):
                        self.__data.zacatekBloku[radekVolaneMetody] = indexNejblizsiOtevreneZavorky
                        self.__data.konecBloku[radekVolaneMetody] = indexNejblizsiZavreneZavorky
 <code>
<pre>

