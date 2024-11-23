# def najdiDataPrislusneTridy(self, pozadovanyNazevSouboru, dataZdrojoveTridy):

### list of variables
i   
dataPozadovaneTridy   
pozadovanyNazevSouboru   
nazevSouboru   

### code of method
<pre>
 <code>
    def najdiDataPrislusneTridy(self, pozadovanyNazevSouboru, dataZdrojoveTridy):
        i = -1
        dataPozadovaneTridy = ""
        # zajisti aby pozadovanyNazevSouboru obsahoval vzdy priponu
        pozadovanyNazevSouboru = pozadovanyNazevSouboru.replace(".java", "")
        pozadovanyNazevSouboru = pozadovanyNazevSouboru + ".java"
        for x in dataZdrojoveTridy:
            i = i + 1
            nazevSouboru = dataZdrojoveTridy[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                dataPozadovaneTridy = dataZdrojoveTridy[i]
                break

        return (dataPozadovaneTridy)
 <code>
<pre>
