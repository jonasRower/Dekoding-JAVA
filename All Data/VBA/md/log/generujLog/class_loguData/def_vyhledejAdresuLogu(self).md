# def vyhledejAdresuLogu(self):

### list of variables
adresaProjektu   
adresaProjektuNew   
nazevSlozky   

### code of method
```
    def vyhledejAdresuLogu(self):

        adresaProjektu = Path.cwd().parent.parent.parts
        adresaProjektuNew = ""

        for i in range(0, len(adresaProjektu)):
            nazevSlozky = adresaProjektu[i]
            adresaProjektuNew = adresaProjektuNew + nazevSlozky + '\\'

        adresaProjektuNew = adresaProjektuNew + "log_output"

        return(adresaProjektuNew)
```
### links

