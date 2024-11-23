# def vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, hledejOdIndexu):

### list of variables
delkaDatVolanaMetodaN   
nazVolMetody   
nazVolMetody !  
cisloRadkuNasledujiciMetody   

### code of method
<pre>
 <code>
def vratCisloRadkuDalsiVolaneMetody(volanaMetodaN, hledejOdIndexu):
    delkaDatVolanaMetodaN = len(volanaMetodaN)

    #Nalezne prvni volanou metodu v poliRadku (resp. poli volanaMetodaN) za danym indexem
    for i in range(hledejOdIndexu, delkaDatVolanaMetodaN):
        nazVolMetody = volanaMetodaN[i]

        if (nazVolMetody != ""):
            cisloRadkuNasledujiciMetody = i
            break

        #vrati cislo radku odkazujici na radek, kde se nalezne zacatek a konec Bloku
        #if (nazVolMetody != ""):
        #    cisloRadkuData = vratCisloRadkuMetody(nazVolMetody)
        #    break

    return (cisloRadkuNasledujiciMetody)
 <code>
<pre>
