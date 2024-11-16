# def vyhledejAdresuSrc(self):

### list of variables
adresaZdroj   
adresaZdrojNew   
nazevSlozky   

### code of method
```
    def vyhledejAdresuSrc(self):

        adresaZdroj = Path.cwd().parent.parent.parts
        adresaZdrojNew = ""

        for i in range(0, len(adresaZdroj)):
            nazevSlozky = adresaZdroj[i]
            adresaZdrojNew = adresaZdrojNew + nazevSlozky + '\\'

        adresaZdrojNew = adresaZdrojNew + "srcJAVA\\src"

        return (adresaZdrojNew)
```
