# def vratZdrojovaData(self, zdrojovaTrida, dataPozadovaneTridy):

### list of variables
zdrojovaTrida   
dataZdrojoveTridy   
nazevSouboru   

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
### links

