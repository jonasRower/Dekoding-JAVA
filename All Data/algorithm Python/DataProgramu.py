
class Data:

    def __init__(self):
        self.poleRadku = []
        self.jeTotoKod = []
        self.koncovyStrednik = []
        self.nazevMetody = []
        self.nazevInstance = []

        self.nazevTridy = []
        self.volanaInstance = []
        self.volanaMetoda = []
        self.slozenaZavorka = []
        self.zacatekBloku = []
        self.konecBloku = []
        self.klicoveSlovo = []
        self.volanaTrida = []

    def add_nazevSouboru(self, nazevSouboru):
        self.nazevSouboru = nazevSouboru

    def add_radek(self, radek):
        self.poleRadku.append(radek)

    def add_jeTotoKod(self, jeTotoKod):
        self.jeTotoKod.append(jeTotoKod)

    def add_koncovyStrednik(self, koncovyStrednik):
        self.koncovyStrednik.append(koncovyStrednik)

    def add_klicoveSlovo(self, klicoveSlovo):
        self.klicoveSlovo.append(klicoveSlovo)

    def add_nazevMetody(self, nazevMetody):
        self.nazevMetody.append(nazevMetody)

    def add_nazevInstance(self, nazevInstance):
        self.nazevInstance.append(nazevInstance)

    def add_nazevTridy(self, nazevTridy):
        self.nazevTridy.append(nazevTridy)

    def add_volanaInstance(self, volanaInstance):
        self.volanaInstance.append(volanaInstance)

    def add_volanaMetoda(self, volanaMetoda):
        self.volanaMetoda.append(volanaMetoda)


    def add_slozenaZavorka(self, slozenaZavorka):
        self.slozenaZavorka.append(slozenaZavorka)

    def add_zacatekBloku(self, zacatekBloku):
        self.zacatekBloku.append(zacatekBloku)

    def add_konecBloku(self, konecBloku):
        self.konecBloku.append(konecBloku)

    def add_volanaTrida(self, volanaTrida):
        self.volanaTrida.append(volanaTrida)



