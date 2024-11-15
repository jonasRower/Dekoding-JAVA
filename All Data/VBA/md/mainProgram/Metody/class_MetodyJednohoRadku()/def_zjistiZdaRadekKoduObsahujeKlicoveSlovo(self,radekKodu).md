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
