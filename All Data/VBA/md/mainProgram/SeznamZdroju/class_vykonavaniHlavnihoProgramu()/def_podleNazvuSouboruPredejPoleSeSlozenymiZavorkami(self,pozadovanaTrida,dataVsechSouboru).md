# def podleNazvuSouboruPredejPoleSeSlozenymiZavorkami(self, pozadovanaTrida, dataVsechSouboru):

### list of variables
i   
pozadovanyNazevSouboru   
nazevSouboru   
slozeneZavorky   

### code of method
<pre>
 <code>
    def podleNazvuSouboruPredejPoleSeSlozenymiZavorkami(self, pozadovanaTrida, dataVsechSouboru):
        i = -1
        pozadovanyNazevSouboru = pozadovanaTrida + ".java"
        for x in dataVsechSouboru:
            i = i + 1
            nazevSouboru = dataVsechSouboru[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                slozeneZavorky = dataVsechSouboru[i].slozenaZavorka
                break

        return (slozeneZavorky)
 <code>
<pre>
