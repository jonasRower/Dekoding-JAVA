# def doplnVolanouTriduKeKonstruktoru(self, dataJednohoSouboru):

### list of variables
i   
nazevTridy   
nazevTridy !  
volanaMetoda   
if(volanaMetoda !  
dataJednohoSouboru.volanaTrida[i]   
dataJednohoSouboru.volanaInstance[i]   

### code of method
```
    def doplnVolanouTriduKeKonstruktoru(self, dataJednohoSouboru):
        i = -1
        for x in dataJednohoSouboru.nazevTridy:
            i = i + 1
            nazevTridy = dataJednohoSouboru.nazevTridy[i]
            if (nazevTridy != ""):
                volanaMetoda = dataJednohoSouboru.volanaMetoda[i]
                if(volanaMetoda != ""):
                    dataJednohoSouboru.volanaTrida[i] = nazevTridy
                    dataJednohoSouboru.volanaInstance[i] = "_"      # "_" priznak indikuje, aby hledal nazev tridy na stejnem radku

        return(dataJednohoSouboru)
```
### links

