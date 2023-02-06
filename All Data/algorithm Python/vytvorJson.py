import numpy as np

class createJSON():

    def __init__(self, vnorenaDataAll, indexySRodici, poleRadkuN):

        poleRadkuJSON = self.sestavPoleRadkuJSON(vnorenaDataAll, poleRadkuN, indexySRodici)
        self.vytvorJSON(poleRadkuJSON)

        #self.vytvorJSON(poleRadkuJSON)
        #jsonDataJedneUrovne = self.vytvorJsonDataJedneUrovne(7, vnorenaDataAll, poleRadkuN)

        print()


    def vratRaduIndexuRadku(self, radaMeze):

        radaMeze0 = radaMeze[0]
        prvniIndex = radaMeze0[0]
        poslIndex = radaMeze0[1]

        radaIndexuRadku = []

        for i in range(prvniIndex, poslIndex):
            radaIndexuRadku.append(i)

        return(radaIndexuRadku)


    def vytvorJsonDataJedneUrovne(self, indexUrovne, vnorenaDataAll, poleRadkuN, indexySRodici):

        poleRadkuJedneUrovne = []
        poleRadkuUrovne = vnorenaDataAll[indexUrovne]
        indexyRadkuRodicuUrovne = indexySRodici[indexUrovne]

        jsonData = []
        posledniradek = False

        for i in range(0, len(poleRadkuUrovne)):

            indexyRadkuCeleUrovne = poleRadkuUrovne[i]
            indexyRadkuRodicu = indexyRadkuRodicuUrovne[i]
            indexyRadkuCeleUrovne0 = indexyRadkuCeleUrovne[0]
            radaMeze = poleRadkuUrovne[i]
            poleRadkuCeleUrovne = self.ziskejPoleRadkuCeleUrovne(indexyRadkuCeleUrovne0, poleRadkuN)
            radaIndexuRadku = self.vratRaduIndexuRadku(radaMeze)

            radaIndexuRodicu = self.vratRaduRodicuRadku(radaMeze, indexyRadkuRodicu)
            jsonData = self.vratPoleRadkuTelaJsonu(poleRadkuCeleUrovne, radaIndexuRadku, radaIndexuRodicu, jsonData)


        return(jsonData)


    def vratRaduRodicuRadku(self, radaMezeAll, indexyRadkuRodicu):

        pocetElementu = radaMezeAll[0][1]
        radaIndexuRodicu = np.full(pocetElementu, '#')

        # je problem s array, proto kopiruje pole pomoci jiz existujici metody
        radaIndexuRodicu = self.posunPoleOPocatecniIndex(radaIndexuRodicu, 0)


        for i in range(1, len(radaMezeAll)):
            radaMeze = radaMezeAll[i]
            rodic = indexyRadkuRodicu[i]
            parent = 'row_' + str(rodic)

            radaIndexuRodicu = self.vratRaduRodicuJednohoRodice(radaMeze, parent, radaIndexuRodicu)


        # opravi radu indexu rodicu
        radaIndexuRodicu = self.posunPoleOPocatecniIndex(radaIndexuRodicu, radaMezeAll[0][0])

        return(radaIndexuRodicu)



    def posunPoleOPocatecniIndex(self, radaIndexuRodicu, pocatecniIndex):

        radaIndexuRodicuNew = []

        for i in range(0, len(radaIndexuRodicu)):
            indexRodice = radaIndexuRodicu[i]
            if(i >= pocatecniIndex):
                radaIndexuRodicuNew.append(indexRodice)

        return(radaIndexuRodicuNew)


    def vratRaduRodicuJednohoRodice(self, radaMeze, indexRodice, radaIndexuRodicu):

        prvniIndex = radaMeze[0]
        poslIndex = radaMeze[1]

        for i in range(prvniIndex, poslIndex):
            try:
                radaIndexuRodicu[i] = indexRodice
            except:
                print("array owerflow - vytvorJson.py")

        return(radaIndexuRodicu)




    def vratPoleRadkuTelaJsonu(self, poleRadkuCeleUrovne, radaIndexuRadku, radaIndexuRodicu, jsonData):

        posledniradek = False

        for i in range(0, len(poleRadkuCeleUrovne)):
            id = str(radaIndexuRadku[i])
            text = str(poleRadkuCeleUrovne[i])
            text = text.replace('"', '|')
            parent = radaIndexuRodicu[i]

            # zatim tohle funguje natvrdo stejne - musim pak doresit
            #if(i == len(poleRadkuCeleUrovne)-1):
            #    posledniradek = True

            uzelJsonu = self.vratUzelJsonu(id, parent, text, posledniradek)
            jsonData = jsonData + uzelJsonu

        return(jsonData)



    def vratUzelJsonu(self, id, parent, text, posledniradek):

        uzelJsonu = []
        uzelJsonu.append('{')
        uzelJsonu.append('"id": "row_' + id + '",')
        uzelJsonu.append('"parent": "' + parent + '",')
        uzelJsonu.append('"text": "' + text + '"')

        zavorkaZavrena = '},'

        if(posledniradek == True):
            zavorkaZavrena = '}'

        uzelJsonu.append(zavorkaZavrena)

        return(uzelJsonu)



    def ziskejPoleRadkuCeleUrovne(self, indexyRadkuCeleUrovne, poleRadkuN):

        poleRadkuCeleUrovne = []

        indStart = indexyRadkuCeleUrovne[0]
        indEnd = indexyRadkuCeleUrovne[1]

        for i in range(indStart, indEnd):
            radek = poleRadkuN[i]
            radekBezSipky = radek.replace('-->', '')
            radekBezSipky = radekBezSipky.strip()
            poleRadkuCeleUrovne.append(radekBezSipky)

        return(poleRadkuCeleUrovne)


    def sestavPoleRadkuJSON(self, vnorenaDataAll, poleRadkuN, indexySRodici):

        # zatim mam jen jednu uroven
        jsonDataJedneUrovne = self.vytvorJsonDataJedneUrovne(7, vnorenaDataAll, poleRadkuN, indexySRodici)

        poleRadkuJSONPred = self.vratPoleRadkuJsonPred()
        poleRadkuJSON = jsonDataJedneUrovne
        poleRadkuJSONZa = self.vratPoleRadkuJsonZa()

        poleRadku = poleRadkuJSONPred + poleRadkuJSON + poleRadkuJSONZa

        return(poleRadku)



    def vratPoleRadkuJsonPred(self):

        poleRadkuJSONPred = []

        poleRadkuJSONPred.append('class vykresliStromFolder{')
        poleRadkuJSONPred.append('  constructor(inputTreeJson){')
        poleRadkuJSONPred.append('        var jsTreeDataJson = {')
        poleRadkuJSONPred.append('            "core": {')
        poleRadkuJSONPred.append('                "data": [')

        return(poleRadkuJSONPred)


    def vratPoleRadkuJsonZa(self):

        poleRadkuJSONZa = []

        poleRadkuJSONZa.append('                ]')
        poleRadkuJSONZa.append('            }')
        poleRadkuJSONZa.append('        }')
        poleRadkuJSONZa.append('        //odebere predchozi strom')
        poleRadkuJSONZa.append('        $(\'#usingJsonTree\').remove();')
        poleRadkuJSONZa.append('        //prida strom novy')
        poleRadkuJSONZa.append('        $(\'.tree\').append(\'<div id="usingJsonTree"></div>\');')
        poleRadkuJSONZa.append('        var myTree = $(\'#usingJsonTree\').jstree(jsTreeDataJson);')
        poleRadkuJSONZa.append('    }')
        poleRadkuJSONZa.append('}')
        poleRadkuJSONZa.append('$(document).ready(function(){')
        poleRadkuJSONZa.append('var xxx = new vykresliStromFolder();')
        poleRadkuJSONZa.append('});')

        return(poleRadkuJSONZa)


    def vytvorJSON(self, poleRadkuN):
        adresa = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\KORONA_PROGRAMMING\\Dekoding\\Python\\OutputTree\\script.js"

        # file = open("testfile.txt", "w")
        file = open(adresa, "w")

        for i in range(0, len(poleRadkuN)):
            radek = poleRadkuN[i]
            file.write(radek + "\n")

        file.close()

