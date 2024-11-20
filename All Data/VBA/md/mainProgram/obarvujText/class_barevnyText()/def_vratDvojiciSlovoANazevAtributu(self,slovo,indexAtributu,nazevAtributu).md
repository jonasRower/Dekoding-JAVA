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
### links
[nazevAtributu=self.priradNazevAtributu(indexAtributu)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/if(indexAtributu_==_1).md)  
