# def vratNazevMetody(radekKodu):

### list of variables
nazevMetody   
jednaSeOMetodu   
if (jednaSeOMetodu   
indexZavorkyOtevrene   
metodaPredZavorkou   

### code of method
```
def vratNazevMetody(radekKodu):
#K od vraci nazev metody z typoveho kodu:
# private void pripravDataSelectu(boolean NejvetsiDotaz) throws SQLException, ClassNotFoundException{

    nazevMetody = ""

    # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
    jednaSeOMetodu = indikujZdaSeJednaOMetodu(radekKodu)
    if (jednaSeOMetodu == True):

        # metodaPredZavorkou uvazuje jako cast nazvu pred "("
        indexZavorkyOtevrene = radekKodu.index('(')
        metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]

        #nasledne odstrani dalsi klicova slova, ktere do nazvu nepatri + mezery
        nazevMetody = metodaPredZavorkou.replace("private", "")
        nazevMetody = nazevMetody.replace("public", "")
        nazevMetody = nazevMetody.replace("boolean", "")
        nazevMetody = nazevMetody.replace("String", "")
        nazevMetody = nazevMetody.replace("int", "")
        nazevMetody = nazevMetody.replace("double", "")
        nazevMetody = nazevMetody.replace("void", "")
        nazevMetody = nazevMetody.replace("indexOf", "")
        nazevMetody = nazevMetody.replace("substring", "")
        nazevMetody = nazevMetody.replace("split", "")
        nazevMetody = nazevMetody.replace("length", "")
        nazevMetody = nazevMetody.replace("println", "")
        nazevMetody = nazevMetody.replace("getLength", "")
        nazevMetody = nazevMetody.replace("setForeground", "")
        nazevMetody = nazevMetody.replace("return", "")
        nazevMetody = nazevMetody.replace("[", "")
        nazevMetody = nazevMetody.replace("]", "")
        nazevMetody = nazevMetody.replace(" ", "")


    return(nazevMetody)
```
