# def dohledejCisloRadkuKDaneMetode(self, hledanaMetoda, nazvyMetod):

### list of variables
i   
cisloRadkuDaneMetody   
if(nazevMetody   

### code of method
```
    def dohledejCisloRadkuKDaneMetode(self, hledanaMetoda, nazvyMetod):
        i = - 1
        cisloRadkuDaneMetody = -1
        for nazevMetody in nazvyMetod:
            i = i + 1
            if(nazevMetody == hledanaMetoda):
                cisloRadkuDaneMetody = i
                break

        return(cisloRadkuDaneMetody)
```
