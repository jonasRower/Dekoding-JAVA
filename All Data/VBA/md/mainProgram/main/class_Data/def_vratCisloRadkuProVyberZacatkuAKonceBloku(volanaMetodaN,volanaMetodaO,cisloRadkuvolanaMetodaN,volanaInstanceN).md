# def vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN, volanaMetodaO, cisloRadkuvolanaMetodaN, volanaInstanceN):

### list of variables
cisloRadkuZacKonBloku   
nazevVolaneMetody   
nazevVolaneInstance   
i   
if(dataNazevMetody   
if (nazevVolaneInstance   

### code of method
```
def vratCisloRadkuProVyberZacatkuAKonceBloku(volanaMetodaN, volanaMetodaO, cisloRadkuvolanaMetodaN, volanaInstanceN):

    cisloRadkuZacKonBloku = -1
    nazevVolaneMetody = volanaMetodaN[cisloRadkuvolanaMetodaN]
    nazevVolaneInstance = volanaInstanceN[cisloRadkuvolanaMetodaN]

    i = -1
    for dataNazevMetody in volanaMetodaO:
        i = i + 1
        if(dataNazevMetody == nazevVolaneMetody):

            # zatim kod funguje jen pro volani pouze v ramci jedne tridy
            # kdyz tam bude instance - je potreba rozsirit kod o nacitani dat z vice souboru
            nazevVolaneInstance = volanaInstanceN[i]

            if (nazevVolaneInstance == ""):
                cisloRadkuZacKonBloku = i
                break

    return(cisloRadkuZacKonBloku)
```
