# def rozdelRadkyNaSlova(self, poleRadku):

### list of variables
radekSlovaAtributyAll   
radek   
radekSpl   
radekSlova   
radekSlovaAtributy   

### code of method
```
    def rozdelRadkyNaSlova(self, poleRadku):

        radekSlovaAtributyAll = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekSpl = radek.split(' ')
            radekSlova = self.vratRadekJenSlova(radekSpl)

            radekSlovaAtributy = self.priradAtributyKeVsemSlovumRadku(radekSlova)
            radekSlovaAtributyAll.append(str(radekSlovaAtributy))

        return(radekSlovaAtributyAll)
```
