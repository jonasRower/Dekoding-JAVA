# def vratIndexDatDanehoSouboru(self, pozadovanaTrida, dataVsechSouboru):

### list of variables
i   
pozadovanaTrida   
pozadovanyNazevSouboru   
hledanyIndex   
nazevSouboru   

### code of method
```
    def vratIndexDatDanehoSouboru(self, pozadovanaTrida, dataVsechSouboru):
        i = -1
        pozadovanaTrida = pozadovanaTrida.replace(".java", "")
        pozadovanyNazevSouboru = pozadovanaTrida + ".java"
        hledanyIndex = -1
        for x in dataVsechSouboru:
            i = i + 1
            nazevSouboru = dataVsechSouboru[i].nazevSouboru
            if (nazevSouboru == pozadovanyNazevSouboru):
                hledanyIndex = i
                break

        return(hledanyIndex)
```
### links

