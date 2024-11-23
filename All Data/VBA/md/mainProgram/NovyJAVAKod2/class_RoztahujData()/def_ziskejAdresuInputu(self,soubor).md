# def ziskejAdresuInputu(self, soubor):

### list of variables
adresaProjektu   
adresaProjektuNew   
nazevSlozky   

### code of method
<pre>
 <code>
    def ziskejAdresuInputu(self, soubor):

        adresaProjektu = Path.cwd().parent.parent.parts
        adresaProjektuNew = ""

        for i in range(0, len(adresaProjektu)):
            nazevSlozky = adresaProjektu[i]
            adresaProjektuNew = adresaProjektuNew + nazevSlozky + '\\'

        adresaProjektuNew = adresaProjektuNew + soubor

        return(adresaProjektuNew)
 <code>
<pre>
