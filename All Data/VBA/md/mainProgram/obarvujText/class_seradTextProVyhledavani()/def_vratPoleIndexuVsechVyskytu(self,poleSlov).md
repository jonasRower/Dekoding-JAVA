# def vratPoleIndexuVsechVyskytu(self, poleSlov):

### list of variables
poleSlovUniq   
seznamIndexuSlovUniq   
slovo   
seznamIndexu   

### code of method
```
    def vratPoleIndexuVsechVyskytu(self, poleSlov):

        poleSlovUniq = self.unique(poleSlov)
        seznamIndexuSlovUniq = []

        for i in range(0, len(poleSlovUniq)):
            slovo = poleSlovUniq[i]
            seznamIndexu = self.vratSeznamIndexuRadkuProDaneSlovo(poleSlov, slovo)
            seznamIndexuSlovUniq.append(seznamIndexu)

        return(seznamIndexuSlovUniq)
```
