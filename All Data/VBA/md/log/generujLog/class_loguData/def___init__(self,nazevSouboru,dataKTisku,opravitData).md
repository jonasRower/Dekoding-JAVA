# def __init__(self, nazevSouboru, dataKTisku, opravitData):

### list of variables
adresaLogu   
adresaUplna   
if(opravitData   
dataKTisku   

### code of method
```
    def __init__(self, nazevSouboru, dataKTisku, opravitData):

        adresaLogu = self.vyhledejAdresuLogu()
        adresaUplna = adresaLogu + '\\' + nazevSouboru

        if(opravitData == True):
            dataKTisku = self.opravJsonData(dataKTisku)


        self.tiskniDataDoTxt(dataKTisku, adresaUplna)
```
