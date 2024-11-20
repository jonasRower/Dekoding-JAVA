# def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru):

### list of variables
ostatniMetody   
nazevTridy   
IndexZapisDat   
i   
nazevMetodyHodnota   
zapisujData   
a   
if(nazevMetodyHodnota !  
nazevInstance   
if(nazevInstance   
slozeneZavorky   
nazvyMetod   
hledanyIndex   
cisloRadkuMetody   
indexNejblizsiOtevreneZavorky   
indexNejblizsiZavreneZavorky   
dataVsechSouboru[IndexZapisDat].zacatekBloku[i-1]   
dataVsechSouboru[IndexZapisDat].konecBloku[i-1]   
dataVsechSouboru[IndexZapisDat].volanaTrida[i-1]   

### code of method
```
    def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru):

        #Inicializuje ostatniMetody
        ostatniMetody = mainProgram.Metody.OstatniMetody()

        # index dataVsechSouboru ktere odpovidaji dataJednohoSouboru
        # zjistuje kvuli tomu, aby zapisoval do spravnych dat
        nazevTridy = dataJednohoSouboru.nazevSouboru
        IndexZapisDat = self.vratIndexDatDanehoSouboru(nazevTridy, dataVsechSouboru)

        i = -1
        for x in dataJednohoSouboru.nazevMetody:
            i = i + 1

            nazevMetodyHodnota = dataJednohoSouboru.volanaMetoda[i]
            zapisujData = True
            #nazevTridy = ""
            # pro testovani:
            if (i == 35):
                a = 4

            if (i == 41):
                a = 4


            if(nazevMetodyHodnota != ""):
                nazevInstance = dataJednohoSouboru.volanaInstance[i]

                if(nazevInstance == ""):
                    # nenalezne-li nazev Instance pak se jedna o metodu volanou ze stejne tridy
                    # a neni treba dohledavat nazev souboru a jejich data
                    slozeneZavorky = dataJednohoSouboru.slozenaZavorka
                    nazvyMetod = dataJednohoSouboru.nazevMetody
                    nazevTridy = dataJednohoSouboru.nazevSouboru
                    nazevTridy = nazevTridy.replace(".java", "")
                else:
                    if(nazevInstance == "_"):   #"_"
                        # pokud nazevInstance obsahuje priznak "_" pak nazev Tridy = volanaTrida (jedna se o radek konstruktoru)
                        nazevTridy = dataJednohoSouboru.volanaTrida[i]
                    else:
                        nazevTridy = self.dohledejNazevTridyKInstanci(dataJednohoSouboru, nazevInstance, i, nazevTridy)

                    hledanyIndex = self.vratIndexDatDanehoSouboru(nazevTridy, dataVsechSouboru)
                    if (hledanyIndex > -1):
                        slozeneZavorky = dataVsechSouboru[hledanyIndex].slozenaZavorka
                        nazvyMetod = dataVsechSouboru[hledanyIndex].nazevMetody
                    else:
                        zapisujData = False
                        # kdyz nenalezne tridu nema smysl nic zapisovat

                if (zapisujData == True):
                    # vyhleda cislo radku metody a to vzdy v datech tridy
                    # pokud je instance = "" pak se vyhledava v datech stejne tridy jako volana metoda
                    cisloRadkuMetody = self.dohledejCisloRadkuKDaneMetode(nazevMetodyHodnota, nazvyMetod)

                    if (cisloRadkuMetody > -1):
                        # Vyhleda index nejblizsi otevrene a zavrene zavorky
                        indexNejblizsiOtevreneZavorky = ostatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(cisloRadkuMetody, slozeneZavorky)
                        indexNejblizsiZavreneZavorky = ostatniMetody.vratCisloRadkuSKoncemBloku(indexNejblizsiOtevreneZavorky, slozeneZavorky)

                        # Zapise data do Zacatek/KonecBloku
                        dataVsechSouboru[IndexZapisDat].zacatekBloku[i-1] = indexNejblizsiOtevreneZavorky
                        dataVsechSouboru[IndexZapisDat].konecBloku[i-1] = indexNejblizsiZavreneZavorky

                        # Zapise nazev tridy v ktere bude vyhledavat
                        dataVsechSouboru[IndexZapisDat].volanaTrida[i-1] = nazevTridy

        return(dataVsechSouboru)
```
### links

