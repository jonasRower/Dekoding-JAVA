import genHtmlProgram.nactiTxt
import genHtmlProgram.vratPoleIdARodicuId
import genHtmlProgram.generujJsonData
import genHtmlProgram.generujHtml

class generujHtml:

    def __init__(self, poleRadku):

        ziskejData = genHtmlProgram.nactiTxt.nacitejTxt(poleRadku)
        adresyDlePoctuUrovniNadrazene = ziskejData.getAdresyDlePoctuUrovniNadrazene()
        dataLog = ziskejData.getDataLog()


        poleIdARodicu = genHtmlProgram.vratPoleIdARodicuId.poleIdARodicuId(adresyDlePoctuUrovniNadrazene)
        poleId = poleIdARodicu.getPoleId()
        poleRodicuId = poleIdARodicu.getPoleRodicuId()

        jsonDataTree = genHtmlProgram.generujJsonData.jsonData(adresyDlePoctuUrovniNadrazene, poleId, poleRodicuId, dataLog)
        jsonData = jsonDataTree.getPoleRadku()


        genHtmlProgram.generujHtml.novyHtml(jsonData)


        print()