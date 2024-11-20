# def priradAtributyKeVsemSlovumRadku(self, radekSlova):

### list of variables
radekSlovaAtributy   
pref   
slovo   
indexAtributu   
nazevAtributu   
slovoPredZavorkou   
if(nazevAtributu   
if(indexAtributu   
slovoAAtribut   

### code of method
```
    def priradAtributyKeVsemSlovumRadku(self, radekSlova):

        radekSlovaAtributy = []
        pref = 0

        for i in range(0, len(radekSlova)):
            slovo = radekSlova[i]
            slovo = slovo.replace('\n', '')
            indexAtributu = 0

            #detekuje, zda se nejedna o zakladni typ atributu, napr. "String"
            nazevAtributu = self.vratAtributZakladni(slovo)
            slovoPredZavorkou = slovo

            #pokud nenajde, pak pokracuje dale
            if(nazevAtributu == ""):

                slovoPredZavorkou = self.odeberZeSlovaObsahZavorky(slovo)
                indexAtributu = self.vratKDanemuSlovuIndexAtributu(slovoPredZavorkou, pref)
                pref = indexAtributu

                # pokud vrati 0, pak bezi znovu na stejnem slovu
                if(indexAtributu == 0):
                    indexAtributu = self.vratKDanemuSlovuIndexAtributu(slovoPredZavorkou, pref)


            slovoAAtribut = self.vratDvojiciSlovoANazevAtributu(slovoPredZavorkou, indexAtributu, nazevAtributu)
            radekSlovaAtributy.append(slovoAAtribut)

        return(radekSlovaAtributy)
```
### links
[slovoPredZavorkou=self.odeberZeSlovaObsahZavorky(slovo)](../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)/try.md)  
