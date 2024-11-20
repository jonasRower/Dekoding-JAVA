# def zjistiZdaRadekKoduObsahujeKlicoveSlovo(self, radekKodu):

### list of variables
klicoveSlovoNalezeno   

### code of method
```
    def zjistiZdaRadekKoduObsahujeKlicoveSlovo(self, radekKodu):

        # metoda je umistena v tride OstatniMetody,
        # to proto ze je soucasne i volana od jinud - z tohoto modulu (z jinych metod)
        klicoveSlovoNalezeno = self.__InjectedObj().detekujPritomnostKlicovehoSlova(radekKodu)

        return (klicoveSlovoNalezeno)
```
### links
[klicoveSlovoNalezeno=self.__InjectedObj().detekujPritomnostKlicovehoSlova(radekKodu)](../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_MetodyJednohoRadku()/def___InjectedObj(self).md)  
