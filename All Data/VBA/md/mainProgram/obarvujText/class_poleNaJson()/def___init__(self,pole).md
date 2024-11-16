# def __init__(self, pole):

### list of variables
self.vsechnaSlovaAId   
self.poleRadkuJson   
vyhledavaniSlov   
self.slovaAId   

### code of method
```
    def __init__(self, pole):

        self.vsechnaSlovaAId = []
        self.poleRadkuJson = self.prevedVsechnyRadky(pole)

        vyhledavaniSlov = seradTextProVyhledavani(self.vsechnaSlovaAId)
        self.slovaAId = vyhledavaniSlov.getJsonRadekArr()
```
