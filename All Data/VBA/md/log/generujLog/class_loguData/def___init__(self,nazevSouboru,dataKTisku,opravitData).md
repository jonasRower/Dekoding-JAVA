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
### links
[adresaLogu=self.vyhledejAdresuLogu()](../../../../../../All%20Data/VBA/md/log/generujLog/class_loguData/def_vyhledejAdresuLogu(self).md)  
[dataKTisku=self.opravJsonData(dataKTisku)](../../../../../../All%20Data/VBA/md/log/generujLog/class_loguData/def_opravJsonData(self,_jsonData).md)  
[self.tiskniDataDoTxt(dataKTisku,adresaUplna)](../../../../../../All%20Data/VBA/md/log/generujLog/class_loguData/def_tiskniDataDoTxt(self,_dataKTisku,_adresaHtml).md)  
