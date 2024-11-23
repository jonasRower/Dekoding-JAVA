# def indikujZdaSeJednaOMetodu(self, radekKodu):

### list of variables
jednaSeOMetodu   
<a href  
if(jednaSeOArrayList   
indexZavorkyOtevrene   
indexZavorkyZavrene   
nazevMetody   

### code of method
<pre>
 <code>
    def indikujZdaSeJednaOMetodu(self, radekKodu):
        # to pozna na zaklade pritomnosti zavorek "(" a ")"
        # pokud tam zavorky nejsou, pak vraci false, jinak true

        jednaSeOMetodu = False
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_OstatniMetody()/def_jednaSeOArrayList(self, radekKodu).md">jednaSeOArrayList=self.jednaSeOArrayList(radekKodu)</a>

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
 <code>
<pre>
