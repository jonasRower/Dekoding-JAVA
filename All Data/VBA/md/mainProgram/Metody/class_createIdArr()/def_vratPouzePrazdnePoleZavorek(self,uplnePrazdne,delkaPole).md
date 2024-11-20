# def vratPouzePrazdnePoleZavorek(self, uplnePrazdne, delkaPole):

### list of variables
poleZavorek   
hodnota   
if(i   
if(uplnePrazdne   
i   
uplnePrazdne   

### code of method
```
    def vratPouzePrazdnePoleZavorek(self, uplnePrazdne, delkaPole):

        poleZavorek = []

        for i in range(0, delkaPole):
            hodnota = ""

            if(i == 1):
                if(uplnePrazdne == False):
                    hodnota = "{"

            if (i == delkaPole-2):
                if (uplnePrazdne == False):
                    hodnota = "}"

            poleZavorek.append(hodnota)

        return(poleZavorek)
```
### links

