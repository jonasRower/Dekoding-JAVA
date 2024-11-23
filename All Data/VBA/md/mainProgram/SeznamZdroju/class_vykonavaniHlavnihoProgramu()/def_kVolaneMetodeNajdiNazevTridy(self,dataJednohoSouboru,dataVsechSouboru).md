# def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru):

### list of variables
nazevTridy   
<a href  
i   
nazevMetodyHodnota   
zapisujData   
a   
if(nazevMetodyHodnota !  
nazevInstance   
if(nazevInstance   
slozeneZavorky   
nazvyMetod   
dataVsechSouboru[IndexZapisDat].zacatekBloku[i-1]   
dataVsechSouboru[IndexZapisDat].konecBloku[i-1]   
dataVsechSouboru[IndexZapisDat].volanaTrida[i-1]   

### code of method
<pre>
 <code>
    def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru):

        #Inicializuje ostatniMetody
          

        # index dataVsechSouboru ktere odpovidaji dataJednohoSouboru
        # zjistuje kvuli tomu, aby zapisoval do spravnych dat
        nazevTridy = dataJednohoSouboru.nazevSouboru
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_vratIndexDatDanehoSouboru(self,pozadovanaTrida,dataVsechSouboru).md">IndexZapisDat=self.vratIndexDatDanehoSouboru(nazevTridy,dataVsechSouboru)</a>

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
                          <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_dohledejNazevTridyKInstanci(self,dataJednohoSouboru,pozadovanaInstance,hledejDoRadku,nazevTridyOrig).md">nazevTridy=self.dohledejNazevTridyKInstanci(dataJednohoSouboru,nazevInstance,i,nazevTridy)</a>

                      <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_vratIndexDatDanehoSouboru(self,pozadovanaTrida,dataVsechSouboru).md">hledanyIndex=self.vratIndexDatDanehoSouboru(nazevTridy,dataVsechSouboru)</a>
                    if (hledanyIndex > -1):
                        slozeneZavorky = dataVsechSouboru[hledanyIndex].slozenaZavorka
                        nazvyMetod = dataVsechSouboru[hledanyIndex].nazevMetody
                    else:
                        zapisujData = False
                        # kdyz nenalezne tridu nema smysl nic zapisovat

                if (zapisujData == True):
                    # vyhleda cislo radku metody a to vzdy v datech tridy
                    # pokud je instance = "" pak se vyhledava v datech stejne tridy jako volana metoda
                      <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_dohledejCisloRadkuKDaneMetode(self,hledanaMetoda,nazvyMetod).md">cisloRadkuMetody=self.dohledejCisloRadkuKDaneMetode(nazevMetodyHodnota,nazvyMetod)</a>

                    if (cisloRadkuMetody > -1):
                        # Vyhleda index nejblizsi otevrene a zavrene zavorky
                          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_vratNejblizsiRadekSOtevrenouZavorkou(self,fromIndex,dataSlozenaZavorka).md">indexNejblizsiOtevreneZavorky=ostatniMetody.vratNejblizsiRadekSOtevrenouZavorkou(cisloRadkuMetody,slozeneZavorky)</a>
                          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_vratCisloRadkuSKoncemBloku(self,fromIndex,dataSlozenaZavorka).md">indexNejblizsiZavreneZavorky=ostatniMetody.vratCisloRadkuSKoncemBloku(indexNejblizsiOtevreneZavorky,slozeneZavorky)</a>

                        # Zapise data do Zacatek/KonecBloku
                        dataVsechSouboru[IndexZapisDat].zacatekBloku[i-1] = indexNejblizsiOtevreneZavorky
                        dataVsechSouboru[IndexZapisDat].konecBloku[i-1] = indexNejblizsiZavreneZavorky

                        # Zapise nazev tridy v ktere bude vyhledavat
                        dataVsechSouboru[IndexZapisDat].volanaTrida[i-1] = nazevTridy

        return(dataVsechSouboru)
 <code>
<pre>






