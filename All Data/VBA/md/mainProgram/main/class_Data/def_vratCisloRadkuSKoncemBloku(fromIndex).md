# def vratCisloRadkuSKoncemBloku(fromIndex):

### list of variables
i   
pocetOtevrenychZavorek   
pocetZavrenychZavorek   
posledniRadek   
radek   
ZavorkyRozdil   

### code of method
```
def vratCisloRadkuSKoncemBloku(fromIndex):
    # vraci cislo radku, kde konci metoda
    # posledni radek pozna podle paroveho znaku }

    i = fromIndex
    pocetOtevrenychZavorek = 0
    pocetZavrenychZavorek = 0
    posledniRadek = -1

    for x in data.slozenaZavorka:
        radek = data.slozenaZavorka[i]

        if (radek == "{"):
            pocetOtevrenychZavorek = pocetOtevrenychZavorek + 1

        if (radek == "}"):
            pocetZavrenychZavorek = pocetZavrenychZavorek + 1

        ZavorkyRozdil = pocetOtevrenychZavorek - pocetZavrenychZavorek

        if (ZavorkyRozdil == 0):
            posledniRadek = i + 1
            break

        i = i + 1

    return(posledniRadek)
```
### links

