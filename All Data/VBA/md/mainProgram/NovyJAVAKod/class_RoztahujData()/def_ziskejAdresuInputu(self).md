# def ziskejAdresuInputu(self):

### list of variables
adresaProjektu   
adresaProjektuNew   
nazevSlozky   

### code of method
<pre>
 <code>
    def ziskejAdresuInputu(self):

        adresaProjektu = Path.cwd().parent.parent.parts
        adresaProjektuNew = ""

        for i in range(0, len(adresaProjektu)):
            nazevSlozky = adresaProjektu[i]
            adresaProjektuNew = adresaProjektuNew + nazevSlozky + '\\'

        adresaProjektuNew = adresaProjektuNew + "input\\Start-class-method.txt"

        return(adresaProjektuNew)
 <code>
<pre>
