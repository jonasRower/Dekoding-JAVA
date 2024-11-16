# def vytvorCsvDataAll(self, data):

### list of variables
csvData   
jeTotoKod   
klicoveSlovo   
koncovyStrednik   
konecBloku   
nazevInstance   
nazevMetody   
nazevTridy   
poleRadku   
slozenaZavorka   
volanaInstance   
volanaMetoda   
volanaTrida   
zacatekBloku   
prvniRadek   
nazevSouboruJava   
nazevSouboruCsv   

### code of method
```
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
```
