# def ziskejNazevTridyProZapis(self, dataPozadovaneTridy, cisloRadku):

### list of variables
nazevSouboru   
aktualniTrida   
zapisovanaTrida   
if(aktualniTrida !  
tridaZapis   

### code of method
```
    def ziskejNazevTridyProZapis(self, dataPozadovaneTridy, cisloRadku):
        nazevSouboru = dataPozadovaneTridy.nazevSouboru
        aktualniTrida = nazevSouboru.replace(".java", "")

        try:
            zapisovanaTrida = dataPozadovaneTridy.volanaTrida[cisloRadku-1]
            if(aktualniTrida != zapisovanaTrida):
                tridaZapis = zapisovanaTrida
            else:
                tridaZapis = ""
        except:
            tridaZapis = ""

        return (tridaZapis)
```
### links

