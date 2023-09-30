class testujData():

    def __init__(self, data):

        self.tiskniDataAll(data)
        print()


    def tiskniDataAll(self, data):

        self.vytvorCsvDataAll(data)
        dataKTisku = data.jeTotoKod

        print()


    def vytvorCsvDataAll(self, data):

        csvData = []

        jeTotoKod = data.jeTotoKod
        klicoveSlovo = data.klicoveSlovo
        koncovyStrednik = data.koncovyStrednik
        konecBloku = data.konecBloku
        nazevInstance = data.nazevInstance
        nazevMetody = data.nazevMetody
        nazevTridy = data.nazevTridy
        poleRadku = data.poleRadku
        slozenaZavorka = data.slozenaZavorka
        volanaInstance = data.volanaInstance
        volanaMetoda = data.volanaMetoda
        volanaTrida = data.volanaTrida
        zacatekBloku = data.zacatekBloku

        prvniRadek = self.vytvorPrvniRadek()

        csvData = self.pridejSloupecDoCsv(csvData, poleRadku)
        csvData = self.pridejSloupecDoCsv(csvData, jeTotoKod)
        csvData = self.pridejSloupecDoCsv(csvData, klicoveSlovo)
        csvData = self.pridejSloupecDoCsv(csvData, koncovyStrednik)
        csvData = self.pridejSloupecDoCsv(csvData, konecBloku)
        csvData = self.pridejSloupecDoCsv(csvData, nazevInstance)
        csvData = self.pridejSloupecDoCsv(csvData, nazevMetody)
        csvData = self.pridejSloupecDoCsv(csvData, nazevTridy)
        csvData = self.pridejSloupecDoCsv(csvData, slozenaZavorka)
        csvData = self.pridejSloupecDoCsv(csvData, volanaInstance)
        csvData = self.pridejSloupecDoCsv(csvData, volanaMetoda)
        csvData = self.pridejSloupecDoCsv(csvData, volanaTrida)
        csvData = self.pridejSloupecDoCsv(csvData, zacatekBloku)

        csvData.insert(0, prvniRadek)

        nazevSouboruJava = data.nazevSouboru
        nazevSouboruCsv = nazevSouboruJava.replace('.java', '.csv')

        self.tiskniData(csvData, nazevSouboruCsv)

        print()


    def vytvorPrvniRadek(self):

        prvniRadek = 'poleRadku, jeTotoKod, klicoveSlovo, koncovyStrednik, konecBloku, nazevInstance, nazevMetody, nazevTridy, slozenaZavorka, volanaInstance, volanaMetoda, volanaTrida, zacatekBloku'

        return(prvniRadek)


    def pridejSloupecDoCsv(self, csvData, sloupec):

        pridavejPrvniSloupec = False

        if not csvData:
            csvData = ['' for i in range(len(sloupec)+1)]
            pridavejPrvniSloupec = True

        for i in range(0, len(sloupec)):
            radek = str(sloupec[i])
            radek = radek.replace(',', '?')

            if(pridavejPrvniSloupec == False):
                radek0 = csvData[i]
            else:
                radek0 = ''

            radekNew = radek0 + str(radek) + ', '
            radekNew = radekNew.replace('\n', '')
            csvData[i] = radekNew

        return(csvData)


    def tiskniData(self, poleRadkuN, nazevSouboru):

        #adresa = "C:\\Users\\jonas\\OneDrive\\Počítač\\PhD\\dekod.txt"
        adresa = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\KORONA_PROGRAMMING\\Dekoding\\Python\\All Data\\Testing pythonu\\ExportDat\\" + nazevSouboru

        # file = open("testfile.txt", "w")
        file = open(adresa, "w")

        for i in range(0, len(poleRadkuN)):
            radek = poleRadkuN[i]
            file.write(radek + "\n")

        file.close()



