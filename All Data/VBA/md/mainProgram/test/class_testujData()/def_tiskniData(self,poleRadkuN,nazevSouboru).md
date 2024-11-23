# def tiskniData(self, poleRadkuN, nazevSouboru):

### list of variables
adresa   
file   
radek   

### code of method
<pre>
 <code>
    def tiskniData(self, poleRadkuN, nazevSouboru):

        #adresa = "C:\\Users\\jonas\\OneDrive\\Počítač\\PhD\\dekod.txt"
        adresa = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\KORONA_PROGRAMMING\\Dekoding\\Python\\All Data\\Testing pythonu\\ExportDat\\" + nazevSouboru

        # file = open("testfile.txt", "w")
        file = open(adresa, "w")

        for i in range(0, len(poleRadkuN)):
            radek = poleRadkuN[i]
            file.write(radek + "\n")

        file.close()
 <code>
<pre>
