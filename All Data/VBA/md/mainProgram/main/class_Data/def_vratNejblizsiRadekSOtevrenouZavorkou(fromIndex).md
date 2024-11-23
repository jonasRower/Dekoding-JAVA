# def vratNejblizsiRadekSOtevrenouZavorkou(fromIndex):

### list of variables
i   
cisloRadkuSOtevrenouZavorkou   
radek   
i >  

### code of method
<pre>
 <code>
def vratNejblizsiRadekSOtevrenouZavorkou(fromIndex):
    # vrati cislo radku kde je "{"
    # zacne hledat od zadaneho radku smerem dolu

    i = fromIndex
    cisloRadkuSOtevrenouZavorkou = -1
    for x in data.slozenaZavorka:

        radek = data.slozenaZavorka[i]
        if (radek == "{"):
            cisloRadkuSOtevrenouZavorkou = i
            break

        i = i + 1
        if (i >= len(data.slozenaZavorka)):
            break

    return (cisloRadkuSOtevrenouZavorkou)
 <code>
<pre>
