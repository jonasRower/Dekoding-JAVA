# def __init__(self, dataDaneTridy, ostatniMetody, poleRadkuNOdDo):

### list of variables
self.ostatniMetody   
self.nazevInstanceAr   
self.nazevMetodyArr   
self.nazevTridyArr   
self.volanaInstanceArr   
self.volanaMetodaArr   
self.volanaTridaArr   
self.radekSlovaAtributyAll   

### code of method
```
    def __init__(self, dataDaneTridy, ostatniMetody, poleRadkuNOdDo):

        self.ostatniMetody = ostatniMetody

        #poleRadkuNOdDo = dataDaneTridy.poleRadku
        #poleRadkuNOdDo = self.vratJenPotrebnyKodPoleRadku(poleRadkuDaneTridy, vyjmiKodOdRadku, vyjmiKodDoRadku)

        self.nazevInstanceAr = self.vratJenPotrebnaData(dataDaneTridy.nazevInstance)
        self.nazevMetodyArr = self.vratJenPotrebnaData(dataDaneTridy.nazevMetody)
        self.nazevTridyArr = self.vratJenPotrebnaData(dataDaneTridy.nazevTridy)
        self.volanaInstanceArr = self.vratJenPotrebnaData(dataDaneTridy.volanaInstance)
        self.volanaMetodaArr = self.vratJenPotrebnaData(dataDaneTridy.volanaMetoda)
        self.volanaTridaArr = self.vratJenPotrebnaData(dataDaneTridy.volanaTrida)

        self.radekSlovaAtributyAll = self.rozdelRadkyNaSlova(poleRadkuNOdDo)
```
### links

