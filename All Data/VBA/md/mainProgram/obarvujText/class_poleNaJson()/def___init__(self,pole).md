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
### links
[self.poleRadkuJson=self.prevedVsechnyRadky(pole)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_pole)/poleRadkuJson_=_[].md)  
