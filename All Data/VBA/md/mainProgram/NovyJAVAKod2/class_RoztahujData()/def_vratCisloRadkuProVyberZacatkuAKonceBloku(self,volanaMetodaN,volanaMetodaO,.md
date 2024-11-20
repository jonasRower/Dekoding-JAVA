# def vratCisloRadkuProVyberZacatkuAKonceBloku(self, volanaMetodaN, volanaMetodaO,

### list of variables
cisloRadkuZacKonBloku   
nazevVolaneMetody   
cisloRadkuvolanaMetodaN   
a   
i   
dataNazevMetody   
nazevVolaneInstance   

### code of method
```
    def vratCisloRadkuProVyberZacatkuAKonceBloku(self, volanaMetodaN, volanaMetodaO,
                                                 cisloRadkuvolanaMetodaN, volanaInstanceN):

        cisloRadkuZacKonBloku = -1
        nazevVolaneMetody = volanaMetodaN[cisloRadkuvolanaMetodaN]
        #nazevVolaneInstance = volanaInstanceN[cisloRadkuvolanaMetodaN]

        if (cisloRadkuvolanaMetodaN == 116):
            a = 4

        i = -1
        for dataNazevMetody in volanaMetodaO:
            i = i + 1
            if (dataNazevMetody == nazevVolaneMetody):

                # zatim kod funguje jen pro volani pouze v ramci jedne tridy
                # kdyz tam bude instance - je potreba rozsirit kod o nacitani dat z vice souboru
                try:
                    nazevVolaneInstance = volanaInstanceN[i]
                except:
                    cisloRadkuZacKonBloku = i
                    break

                #if (nazevVolaneInstance == ""):
                cisloRadkuZacKonBloku = i
                break

        return (cisloRadkuZacKonBloku)
```
### links

