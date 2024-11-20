# def vratSlozenouZavorku(self, radekKodu):

### list of variables
indexZavorkyOtevrene   
indexZavorkyZavrene   
radekSeZavorkou   

### code of method
```
    def vratSlozenouZavorku(self, radekKodu):

        indexZavorkyOtevrene = -1
        indexZavorkyZavrene = -1
        radekSeZavorkou = ""

        try:
            indexZavorkyOtevrene = radekKodu.index('{')
        except:
            pass

        try:
            indexZavorkyZavrene = radekKodu.index('}')
        except:
            pass

        if (indexZavorkyOtevrene > -1):
            radekSeZavorkou = "{"

        if (indexZavorkyZavrene > -1):
            radekSeZavorkou = "}"

        return (radekSeZavorkou)
```
### links

