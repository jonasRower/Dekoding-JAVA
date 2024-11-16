# def vratSeznamIndexuRadkuProDaneSlovo(self, pole, slovoExp):

### list of variables
seznamIndexu   
slovo   
if(slovo   

### code of method
```
    def vratSeznamIndexuRadkuProDaneSlovo(self, pole, slovoExp):

        seznamIndexu = []
        seznamIndexu.append(slovoExp)

        for i in range(0, len(pole)):
            slovo = pole[i]
            if(slovo == slovoExp):
                seznamIndexu.append(i)

        return(seznamIndexu)
```
