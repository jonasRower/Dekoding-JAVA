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

            # do kazdeho souboru dopise (dodatecne) jeste nazvy trid, na radcich s konstruktory
            dataJednohoSouboru = self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)

            # jednotlive se pridavaji data soubor po souboru
            dataVsechSouboru.append(dataJednohoSouboru)



        # projde data jeste jednou a doplni rozsahy slozenych zavorek
        # vyhledava totiz radky i z cizich trid,
        # proto je potreba tuto metodu spustit az po naplneni vsech ostatnich dat
        for i in range(1, pocetSouboru):
            dataJednohoSouboru = dataVsechSouboru[i]
            dataJednohoSouboru = self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)
            dataVsechSouboru = self.kVolaneMetodeNajdiNazevTridy(dataJednohoSouboru, dataVsechSouboru)

        #dataVsechSouboru[6].volanaTrida[40] = "VytvorDB"

        #self.podleNazvuSouboruPredejPoleSeSlozenymiZavorkami("NactiDotazy", dataVsechSouboru)

        novyJAVAKod = mainProgram.NovyJAVAKod.RoztahujData(dataVsechSouboru)
        novyJAVAKod = mainProgram.NovyJAVAKod2.RoztahujData(dataVsechSouboru)
        novyJAVAKod.hlavni()

        self.poleRadkuN = novyJAVAKod.getPoleRadkuN()
```
### links

