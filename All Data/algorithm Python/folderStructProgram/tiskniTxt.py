class tiskniDoTxt:

    def __init__(self, poleRadku):

        adresaHtml = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\2023\\Python\\DoLinuxuData\\stromDekod3.txt"
        self.tiskniDataDoTxt(poleRadku, adresaHtml)


    def tiskniDataDoTxt(self, dataKTisku, adresaHtml):
        dataWrite = ""

        f = open(adresaHtml, 'w')

        for i in range(0, len(dataKTisku)):

            radek = dataKTisku[i]

            if(radek != False):
                radekStr = str(radek)
                dataWrite = dataWrite + radekStr + '\n'


        f.write(dataWrite)
        f.close()

