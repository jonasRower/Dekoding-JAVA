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
[dataZdrojoveTridy=self.najdiDataPrislusneTridy2(nazevSouboru)](../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self,_pozadovanyNazevSouboru).md)  
