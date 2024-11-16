# def vratDvojiciSlovoANazevAtributu(self, slovo, indexAtributu, nazevAtributu):

### list of variables
slovoAAtribut   
if(nazevAtributu   
nazevAtributu   

### code of method
```
    def vratDvojiciSlovoANazevAtributu(self, slovo, indexAtributu, nazevAtributu):

        slovoAAtribut = []

        if(nazevAtributu == ""):
            if (indexAtributu > 0):
                nazevAtributu = self.priradNazevAtributu(indexAtributu)
            else:
                nazevAtributu = ""

        slovoAAtribut.append(slovo)
        slovoAAtribut.append(nazevAtributu)

        return(slovoAAtribut)
```
