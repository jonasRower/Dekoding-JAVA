# def vratZdrojovaData(self, zdrojovaTrida, dataPozadovaneTridy):

### list of variables
if (zdrojovaTrida   
dataZdrojoveTridy   
zdrojovaTrida   
nazevSouboru   
if (dataZdrojoveTridy   

### code of method
```
    def vratZdrojovaData(self, zdrojovaTrida, dataPozadovaneTridy):
        if (zdrojovaTrida == ""):
            dataZdrojoveTridy = dataPozadovaneTridy
        else:
            zdrojovaTrida = zdrojovaTrida.replace(".java", "")
            nazevSouboru = zdrojovaTrida + ".java"
            dataZdrojoveTridy = self.najdiDataPrislusneTridy2(nazevSouboru)
            if (dataZdrojoveTridy == ""):
                dataZdrojoveTridy = dataPozadovaneTridy

        return (dataZdrojoveTridy)
```
