# def dopisujIndexyOtevrenychAZavrenychZavorek():

### list of variables
i   
radekObsahujeKlicoveSlovo   
indexNejblizsiOtevreneZavorky   
indexNejblizsiZavreneZavorky   
if (radekObsahujeKlicoveSlovo   
if (nazevMetodyHodnota !  
vyhledejOdRadku   
radekVolaneMetody   
data.zacatekBloku[radekVolaneMetody]   
data.konecBloku[radekVolaneMetody]   

### code of method
```
def dopisujIndexyOtevrenychAZavrenychZavorek():
    # dopisuje indexy otevrenych a zavrenych zavorek ( "{", "}" ) na radek v Data, kde je volana metoda
    # proto je potreba vyhledavat volanou metodu

    i = -1

    for nazevMetodyHodnota in data.nazevMetody:
        i = i + 1
        radekObsahujeKlicoveSlovo = data.klicoveSlovo[i]

        indexNejblizsiOtevreneZavorky = -1
        indexNejblizsiZavreneZavorky = -1

        #zapisuje zacatek a konec bloku, v pripadech, kdy se nejedna o klicove slovo, tedy for, if, catch ...
        if (radekObsahujeKlicoveSlovo == False):

            if (nazevMetodyHodnota != ""):
                vyhledejOdRadku = i - 1
                indexNejblizsiOtevreneZavorky = vratNejblizsiRadekSOtevrenouZavorkou(vyhledejOdRadku)
                indexNejblizsiZavreneZavorky = vratCisloRadkuSKoncemBloku(indexNejblizsiOtevreneZavorky)

                radekVolaneMetody = najdiRadekVolaneMetody(nazevMetodyHodnota)
                if (radekVolaneMetody > -1):
                    data.zacatekBloku[radekVolaneMetody] = indexNejblizsiOtevreneZavorky
                    data.konecBloku[radekVolaneMetody] = indexNejblizsiZavreneZavorky
```
