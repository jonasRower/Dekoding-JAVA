# def najdiDataPrislusneTridy2(self, pozadovanyNazevSouboru):

### list of variables
i   
dataPozadovaneTridy   
pozadovanyNazevSouboru   
nazevSouboru   
if(i   
a   

### code of method
```
    def najdiDataPrislusneTridy2(self, pozadovanyNazevSouboru):
        i = -1
        dataPozadovaneTridy = ""
        #zajisti aby pozadovanyNazevSouboru obsahoval vzdy priponu
        pozadovanyNazevSouboru = pozadovanyNazevSouboru.replace(".java","")
        pozadovanyNazevSouboru = pozadovanyNazevSouboru + ".java"
        for x in self.__data:
            i = i + 1
            nazevSouboru = self.__data[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                dataPozadovaneTridy = self.__data[i]
                break

            if(i == 11):
                a = 5

        return(dataPozadovaneTridy)
```
### links

