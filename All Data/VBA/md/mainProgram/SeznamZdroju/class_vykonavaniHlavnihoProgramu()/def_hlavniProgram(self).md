# def hlavniProgram(self):

### list of variables
adresyZdrojuData   
dataVsechSouboru   
pocetSouboru   
adresaZdroj   
zdroj   
startProgramu   
dataJednohoSouboru   
novyJAVAKod   
self.poleRadkuN   

### code of method
```
    def hlavniProgram(self):

        # Do adresyZdrojuData ulozi "Nazev JAVA souboru", "adresa pred nazev souboru" a "adresu s nazvem souboru"
        adresyZdrojuData = SeznamZdroju()
        adresyZdrojuData.vratSeznamAdresZdroju()

        # zde jsou data vsech souboru
        dataVsechSouboru = []

        # kod nize, bezi ve smycce
        # jsou jednotlive volany vsechny nazvy JAVA soubory, vcetne jejich adres
        pocetSouboru = len(adresyZdrojuData.seznamZdroju)
        for i in range(0, pocetSouboru):
            # ziska adresu se zdrojem (s nazvem souboru) a nazev zdroje (souboru)
            adresaZdroj = adresyZdrojuData.seznamAdresZdroju[i]
            zdroj = adresyZdrojuData.seznamZdroju[i]

            # hlavni program pro ziskani kompletnich dat pro jeden soubor
            startProgramu = mainProgram.NactiZdroj.NactiDataProJedenZdroj()

            # data pro jeden soubor ulozi sem
            dataJednohoSouboru = startProgramu.spustProgram(adresaZdroj, zdroj)
```
              [link](../../../../../../All%20Data/VBA/md/mainProgram/NactiZdroj/class_NactiDataProJedenZdroj()/def_spustProgram(self,_adresa,_nazevSouboru).md)  

