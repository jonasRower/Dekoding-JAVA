def definiceKlicovychSlov():

    klicovaSlova = []
    klicovaSlova.append("for")
    klicovaSlova.append("if")
    klicovaSlova.append("while")
    klicovaSlova.append("try")
    klicovaSlova.append("catch")
    klicovaSlova.append("indexOf")
    klicovaSlova.append("substring")
    klicovaSlova.append("split")
    klicovaSlova.append("length")
    klicovaSlova.append("println")
    klicovaSlova.append("getLength")
    klicovaSlova.append("setForeground")
    klicovaSlova.append("return")

    return (klicovaSlova)


def adresaPredBalicek():
    adresaPredBalicek = "C:\\Users\\jonas\\PycharmProjects\\DokumentaceJAVY\\Kod JAVY\\src"
    return(adresaPredBalicek)


def vratPlnouAdresu(nazevBalicku, nazevSouboru):
    adr = adresaPredBalicek()
    plnaAdresa = adr + "\\" + nazevBalicku + "\\" + nazevSouboru
    return(plnaAdresa)

