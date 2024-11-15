# def indikujZdaSeJednaOMetodu(self, radekKodu):

### list of variables
jednaSeOMetodu   
jednaSeOArrayList   
if(jednaSeOArrayList   
indexZavorkyOtevrene   
indexZavorkyZavrene   
nazevMetody   

### code of method
```
    def indikujZdaSeJednaOMetodu(self, radekKodu):
        # to pozna na zaklade pritomnosti zavorek "(" a ")"
        # pokud tam zavorky nejsou, pak vraci false, jinak true

        jednaSeOMetodu = False
        jednaSeOArrayList = self.jednaSeOArrayList(radekKodu)

        if(jednaSeOArrayList == False):

            # zjisti index zavorky otevrene
            indexZavorkyOtevrene = 0
            try:
                indexZavorkyOtevrene = radekKodu.index('(')
            except:
                pass

            # zjisti index zavorky zavrene
            indexZavorkyZavrene = 0
            try:
                indexZavorkyZavrene = radekKodu.index(')')
            except:
                pass

            # pokud oba indexy (otevrene a zavrene zavorky) > 0, pak se jedna o metodu
            nazevMetody = ""
            if (indexZavorkyOtevrene > 0):
                if (indexZavorkyZavrene > 0):
                    jednaSeOMetodu = True

        return (jednaSeOMetodu)
```
