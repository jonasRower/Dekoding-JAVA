# def vratZdrojovaData(self, zdrojovaTrida, dataPozadovaneTridy):

### list of variables
zdrojovaTrida   
dataZdrojoveTridy   
nazevSouboru   
<a href  

### code of method
<pre>
 <code>
    def vratZdrojovaData(self, zdrojovaTrida, dataPozadovaneTridy):
        if (zdrojovaTrida == ""):
            dataZdrojoveTridy = dataPozadovaneTridy
        else:
            zdrojovaTrida = zdrojovaTrida.replace(".java", "")
            nazevSouboru = zdrojovaTrida + ".java"
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/NovyJAVAKod2/class_RoztahujData()/def_najdiDataPrislusneTridy2(self, pozadovanyNazevSouboru).md">dataZdrojoveTridy=self.najdiDataPrislusneTridy2(nazevSouboru)</a>
            if (dataZdrojoveTridy == ""):
                dataZdrojoveTridy = dataPozadovaneTridy

        return (dataZdrojoveTridy)
 <code>
<pre>
