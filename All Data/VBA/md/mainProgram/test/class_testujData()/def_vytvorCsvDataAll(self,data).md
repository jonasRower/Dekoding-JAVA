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
<a href  
nazevSouboruJava   
nazevSouboruCsv   

### code of method
<pre>
 <code>
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

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_vytvorPrvniRadek(self).md">prvniRadek=self.vytvorPrvniRadek()</a>

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,poleRadku)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,jeTotoKod)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,klicoveSlovo)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,koncovyStrednik)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,konecBloku)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,nazevInstance)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,nazevMetody)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,nazevTridy)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,slozenaZavorka)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,volanaInstance)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,volanaMetoda)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,volanaTrida)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_pridejSloupecDoCsv(self, csvData, sloupec).md">csvData=self.pridejSloupecDoCsv(csvData,zacatekBloku)</a>

        csvData.insert(0, prvniRadek)

        nazevSouboruJava = data.nazevSouboru
        nazevSouboruCsv = nazevSouboruJava.replace('.java', '.csv')

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/test/class_testujData()/def_tiskniDataAll(self, data).md">self.tiskniData(csvData,nazevSouboruCsv)</a>

        print()
 <code>
<pre>














