# def hlavniProgram(self):

### list of variables
adresyZdrojuData   
dataVsechSouboru   
pocetSouboru   
adresaZdroj   
zdroj   
<a href  
dataJednohoSouboru   

### code of method
<pre>
 <code>
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
              

            # data pro jeden soubor ulozi sem
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\NactiZdroj\class_NactiDataProJedenZdroj()\def spustProgram(self, adresa, nazevSouboru)">dataJednohoSouboru=startProgramu.spustProgram(adresaZdroj,zdroj)</a>

            # do kazdeho souboru dopise (dodatecne) jeste nazvy trid, na radcich s konstruktory
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\SeznamZdroju\class_vykonavaniHlavnihoProgramu()\def doplnVolanouTriduKeKonstruktoru(self, dataJednohoSouboru)">dataJednohoSouboru=self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)</a>

            # jednotlive se pridavaji data soubor po souboru
            dataVsechSouboru.append(dataJednohoSouboru)



        # projde data jeste jednou a doplni rozsahy slozenych zavorek
        # vyhledava totiz radky i z cizich trid,
        # proto je potreba tuto metodu spustit az po naplneni vsech ostatnich dat
        for i in range(1, pocetSouboru):
            dataJednohoSouboru = dataVsechSouboru[i]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\SeznamZdroju\class_vykonavaniHlavnihoProgramu()\def doplnVolanouTriduKeKonstruktoru(self, dataJednohoSouboru)">dataJednohoSouboru=self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\SeznamZdroju\class_vykonavaniHlavnihoProgramu()\def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru)">dataVsechSouboru=self.kVolaneMetodeNajdiNazevTridy(dataJednohoSouboru,dataVsechSouboru)</a>

        #dataVsechSouboru[6].volanaTrida[40] = "VytvorDB"

        #self.podleNazvuSouboruPredejPoleSeSlozenymiZavorkami("NactiDotazy", dataVsechSouboru)

          <a href="../../../../../../All%20Data/VBA/md/mainProgram\NovyJAVAKod\class_RoztahujData()\def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru)">novyJAVAKod=mainProgram.NovyJAVAKod.RoztahujData(dataVsechSouboru)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\NovyJAVAKod\class_RoztahujData()\def kVolaneMetodeNajdiNazevTridy(self, dataJednohoSouboru, dataVsechSouboru)">novyJAVAKod=mainProgram.NovyJAVAKod2.RoztahujData(dataVsechSouboru)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\NovyJAVAKod2\class_RoztahujData()\def hlavni(self)">novyJAVAKod.hlavni()</a>

          <a href="../../../../../../All%20Data/VBA/md/mainProgram\NovyJAVAKod2\class_RoztahujData()\def getPoleRadkuN(self)">self.poleRadkuN=novyJAVAKod.getPoleRadkuN()</a>
 <code>
<pre>








