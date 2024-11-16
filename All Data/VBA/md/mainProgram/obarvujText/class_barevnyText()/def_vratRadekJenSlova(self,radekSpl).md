# def vratRadekJenSlova(self, radekSpl):

### list of variables
radekSlova   
slovo   
if(slovo !  

### code of method
```
    def vratRadekJenSlova(self, radekSpl):

        radekSlova = []

        for i in range(0, len(radekSpl)):
            slovo = radekSpl[i]

            if(slovo != ""):
                radekSlova.append(slovo)

        return(radekSlova)
```
