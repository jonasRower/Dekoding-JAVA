# def vratCisloRadkuSKoncemBloku(self, fromIndex, dataSlozenaZavorka):

### list of variables
i   
pocetOtevrenychZavorek   
pocetZavrenychZavorek   
posledniRadek   
radek   
ZavorkyRozdil   

### code of method
<pre>
 <code>
    def vratCisloRadkuSKoncemBloku(self, fromIndex, dataSlozenaZavorka):

        i = fromIndex
        pocetOtevrenychZavorek = 0
        pocetZavrenychZavorek = 0
        posledniRadek = -1

        for x in dataSlozenaZavorka:
            radek = dataSlozenaZavorka[i]

            if (radek == "{"):
                pocetOtevrenychZavorek = pocetOtevrenychZavorek + 1

            if (radek == "}"):
                pocetZavrenychZavorek = pocetZavrenychZavorek + 1

            ZavorkyRozdil = pocetOtevrenychZavorek - pocetZavrenychZavorek

            if (ZavorkyRozdil == 0):
                posledniRadek = i + 1
                break

            i = i + 1

        return (posledniRadek)
 <code>
<pre>
