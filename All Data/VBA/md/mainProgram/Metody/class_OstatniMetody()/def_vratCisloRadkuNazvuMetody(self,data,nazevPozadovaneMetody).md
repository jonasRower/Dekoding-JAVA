# def vratCisloRadkuNazvuMetody(self, data, nazevPozadovaneMetody):

### list of variables
i   
cisloRadkuMetody   
nazevMetody   
if (nazevMetody   

### code of method
```
    def vratCisloRadkuNazvuMetody(self, data, nazevPozadovaneMetody):
        i = -1
        cisloRadkuMetody = -1
        for x in data.nazevMetody:
            i = i + 1
            nazevMetody = data.nazevMetody[i]
            if (nazevMetody == nazevPozadovaneMetody):
                cisloRadkuMetody = i
                break

        return(cisloRadkuMetody)
```
