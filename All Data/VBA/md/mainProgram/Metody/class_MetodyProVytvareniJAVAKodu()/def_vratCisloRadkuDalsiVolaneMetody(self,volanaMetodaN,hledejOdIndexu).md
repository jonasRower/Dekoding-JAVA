# def vratCisloRadkuDalsiVolaneMetody(self, volanaMetodaN, hledejOdIndexu):

### list of variables
delkaDatVolanaMetodaN   
cisloRadkuNasledujiciMetody   
nazVolMetody   
if (nazVolMetody !  

### code of method
```
    def vratCisloRadkuDalsiVolaneMetody(self, volanaMetodaN, hledejOdIndexu):
        delkaDatVolanaMetodaN = len(volanaMetodaN)
        cisloRadkuNasledujiciMetody = -1

        # Nalezne prvni volanou metodu v poliRadku (resp. poli volanaMetodaN) za danym indexem
        for i in range(hledejOdIndexu, delkaDatVolanaMetodaN):
            nazVolMetody = volanaMetodaN[i]

            if (nazVolMetody != ""):
                cisloRadkuNasledujiciMetody = i
                break


            # vrati cislo radku odkazujici na radek, kde se nalezne zacatek a konec Bloku
            # if (nazVolMetody != ""):
            #    cisloRadkuData = vratCisloRadkuMetody(nazVolMetody)
            #    break

        return (cisloRadkuNasledujiciMetody)
```
