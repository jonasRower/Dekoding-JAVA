# def vratNejblizsiRadekSOtevrenouZavorkou(self, fromIndex, dataSlozenaZavorka):

### list of variables
i   
cisloRadkuSOtevrenouZavorkou   
radek   
if (radek   
if (i >  

### code of method
```
    def vratNejblizsiRadekSOtevrenouZavorkou(self, fromIndex, dataSlozenaZavorka):

        #jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

        i = fromIndex
        cisloRadkuSOtevrenouZavorkou = -1
        for x in dataSlozenaZavorka:

            radek = dataSlozenaZavorka[i]
            if (radek == "{"):
                cisloRadkuSOtevrenouZavorkou = i
                break

            i = i + 1
            if (i >= len(dataSlozenaZavorka)):
                break

        return (cisloRadkuSOtevrenouZavorkou)
```
