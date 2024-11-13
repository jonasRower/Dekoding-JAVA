# def dohledejNazevTridyKInstanci(self, dataJednohoSouboru, pozadovanaInstance, hledejDoRadku, nazevTridyOrig):

### list of variables
nazevTridy   
hledejDoRadku   
nazevInstance   
if (nazevInstance   

### code of method
```
    def dohledejNazevTridyKInstanci(self, dataJednohoSouboru, pozadovanaInstance, hledejDoRadku, nazevTridyOrig):
        # hledejDoRadku - hleda od radku smerem nahoru

        # defaultne nastavuji
        # pokud se jedna o generovanou instanci, pak trida neni a vrati nazevTridyOriginalni
        nazevTridy = nazevTridyOrig

        # pro jistotu hledam od radku jeste jednoho nize
        hledejDoRadku = hledejDoRadku + 1

        # hledam od radku smerem nahoru, protoze predpokladam,
        # ze trida bude definovana nekde ned volanou instanci
        for i in range(hledejDoRadku, 0, -1):
            #prohledava data.nazevInstance , nikoliv volanaInstance
            nazevInstance = dataJednohoSouboru.nazevInstance[i]
            if (nazevInstance == pozadovanaInstance):
                nazevTridy = dataJednohoSouboru.nazevTridy[i]
                break

        return (nazevTridy)
```
