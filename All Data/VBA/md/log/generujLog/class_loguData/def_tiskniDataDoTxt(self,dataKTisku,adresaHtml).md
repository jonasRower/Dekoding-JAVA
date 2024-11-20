# def tiskniDataDoTxt(self, dataKTisku, adresaHtml):

### list of variables
dataWrite   
f   
radek   
if(radek !  
radekStr   

### code of method
```
    def tiskniDataDoTxt(self, dataKTisku, adresaHtml):
        dataWrite = ""

        f = open(adresaHtml, 'w')

        for i in range(0, len(dataKTisku)):

            radek = dataKTisku[i]

            if(radek != False):
                radekStr = str(radek)
                dataWrite = dataWrite + radekStr + '\n'


        f.write(dataWrite)
        f.close()
```
### links

