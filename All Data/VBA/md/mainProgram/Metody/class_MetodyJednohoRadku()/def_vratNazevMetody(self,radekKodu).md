# def vratNazevMetody(self, radekKodu):

### list of variables
nazevMetody   
jednaSeOMetodu   
if (jednaSeOMetodu   
indexZavorkyOtevrene   
metodaPredZavorkou   
klicovaSlova   

### code of method
```
    def vratNazevMetody(self, radekKodu):

        nazevMetody = ""

        # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
        jednaSeOMetodu = self.__InjectedObj().indikujZdaSeJednaOMetodu(radekKodu)

        if (jednaSeOMetodu == True):
            # metodaPredZavorkou uvazuje jako cast nazvu pred "("
            indexZavorkyOtevrene = radekKodu.index('(')
            metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]

            # nasledne odstrani dalsi klicova slova, ktere do nazvu nepatri + mezery
            import vstupniData
            klicovaSlova = vstupniData.definiceKlicovychSlov()

            nazevMetody = metodaPredZavorkou
            for odstranitSlovo in klicovaSlova:
                nazevMetody = nazevMetody.replace(odstranitSlovo, "")

            # odstrani jeste nejaka dalsi slova
            nazevMetody = nazevMetody.replace("private", "")
            nazevMetody = nazevMetody.replace("public", "")
            nazevMetody = nazevMetody.replace("int", "")
            nazevMetody = nazevMetody.replace("double", "")
            nazevMetody = nazevMetody.replace("String", "")
            nazevMetody = nazevMetody.replace("void", "")

            #odstrani jeste hranate zavorky
            nazevMetody = nazevMetody.replace("[", "")
            nazevMetody = nazevMetody.replace("]", "")
            nazevMetody = nazevMetody.replace(" ", "")

        return (nazevMetody)
```
