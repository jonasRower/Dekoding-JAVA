
from pathlib import Path

class loguData:

    def __init__(self, nazevSouboru, dataKTisku, opravitData):

        adresaLogu = self.vyhledejAdresuLogu()
        adresaUplna = adresaLogu + '\\' + nazevSouboru

        if(opravitData == True):
            dataKTisku = self.opravJsonData(dataKTisku)


        self.tiskniDataDoTxt(dataKTisku, adresaUplna)


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


    def vyhledejAdresuLogu(self):

        adresaProjektu = Path.cwd().parent.parent.parts
        adresaProjektuNew = ""

        for i in range(0, len(adresaProjektu)):
            nazevSlozky = adresaProjektu[i]
            adresaProjektuNew = adresaProjektuNew + nazevSlozky + '\\'

        adresaProjektuNew = adresaProjektuNew + "log_output"

        return(adresaProjektuNew)


    def opravJsonData(self, jsonData):

        posledniRadek = jsonData[len(jsonData)-1]
        lastChar = posledniRadek[-1]

        if(lastChar == ','):
            posledniRadek = posledniRadek[:-1]

        jsonData[len(jsonData) - 1] = posledniRadek


        jsonDataNew = []
        jsonDataNew.append('[')
        jsonDataNew = jsonDataNew + jsonData
        jsonDataNew.append(']')

        return(jsonDataNew)