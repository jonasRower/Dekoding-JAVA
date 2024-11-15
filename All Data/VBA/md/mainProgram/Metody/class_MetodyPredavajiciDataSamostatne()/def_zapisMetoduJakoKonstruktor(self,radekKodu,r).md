# def zapisMetoduJakoKonstruktor(self, radekKodu, r):

### list of variables
indexZavorkyOtevrene   
metodaPredZavorkou   
indexNew   
nazevKonstruktoru   
self.__data.volanaMetoda[r]   

### code of method
```
    def zapisMetoduJakoKonstruktor(self, radekKodu, r):
        try:
            indexZavorkyOtevrene = radekKodu.index('(')
            metodaPredZavorkou = radekKodu[0:(indexZavorkyOtevrene)]
            try:
                indexNew = metodaPredZavorkou.index('new')
                nazevKonstruktoru = metodaPredZavorkou[(indexNew + 3):(len(metodaPredZavorkou))]
                nazevKonstruktoru = nazevKonstruktoru.replace(" ", "")

                self.__data.volanaMetoda[r] = nazevKonstruktoru
            except:
                pass
        except:
            pass
```
