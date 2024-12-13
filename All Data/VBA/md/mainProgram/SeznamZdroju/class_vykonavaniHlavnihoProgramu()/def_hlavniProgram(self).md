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
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NactiZdroj/class_NactiDataProJedenZdroj()/def_spustProgram(self,adresa,nazevSouboru).md">dataJednohoSouboru=startProgramu.spustProgram(adresaZdroj,zdroj)</a>

            # do kazdeho souboru dopise (dodatecne) jeste nazvy trid, na radcich s konstruktory
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_doplnVolanouTriduKeKonstruktoru(self,dataJednohoSouboru).md">dataJednohoSouboru=self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)</a>

            # jednotlive se pridavaji data soubor po souboru
            dataVsechSouboru.append(dataJednohoSouboru)



        # projde data jeste jednou a doplni rozsahy slozenych zavorek
        # vyhledava totiz radky i z cizich trid,
        # proto je potreba tuto metodu spustit az po naplneni vsech ostatnich dat
        for i in range(1, pocetSouboru):
            dataJednohoSouboru = dataVsechSouboru[i]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_doplnVolanouTriduKeKonstruktoru(self,dataJednohoSouboru).md">dataJednohoSouboru=self.doplnVolanouTriduKeKonstruktoru(dataJednohoSouboru)</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_kVolaneMetodeNajdiNazevTridy(self,dataJednohoSouboru,dataVsechSouboru).md">dataVsechSouboru=self.kVolaneMetodeNajdiNazevTridy(dataJednohoSouboru,dataVsechSouboru)</a>

        #dataVsechSouboru[6].volanaTrida[40] = "VytvorDB"

        #self.podleNazvuSouboruPredejPoleSeSlozenymiZavorkami("NactiDotazy", dataVsechSouboru)

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_kVolaneMetodeNajdiNazevTridy(self,dataJednohoSouboru,dataVsechSouboru).md">novyJAVAKod=mainProgram.NovyJAVAKod.RoztahujData(dataVsechSouboru)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod/class_RoztahujData()/def_kVolaneMetodeNajdiNazevTridy(self,dataJednohoSouboru,dataVsechSouboru).md">novyJAVAKod=mainProgram.NovyJAVAKod2.RoztahujData(dataVsechSouboru)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_hlavni(self).md">novyJAVAKod.hlavni()</a>

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_getPoleRadkuN(self).md">self.poleRadkuN=novyJAVAKod.getPoleRadkuN()</a>
 <code>
<pre>


 
### This method is called from:





