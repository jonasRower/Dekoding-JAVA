import folderStructProgram.nactiDataZLogu
import folderStructProgram.vykonavejProgram
import folderStructProgram.upravDataProStrom
import folderStructProgram.tiskniTxt

import genHtmlProgram.genStart
import log.generujLog

class vytvarejStrukturuCest():

    def __init__(self, poleRadkuLog):

        # pokud chci nacitat z logu, odkomentovat tyto radky
        #adresaLog = "C:\\Users\\jonas\\OneDrive\\Dokumenty\\2023\\Python\\dekod3.txt"
        #dataZLogu = folderStructProgram.nactiDataZLogu.nactiLog(adresaLog)
        #poleRadkuLog = dataZLogu.getDataLog()

        hlavProgram = folderStructProgram.vykonavejProgram.hlavniProgram(poleRadkuLog)
        poleDat = hlavProgram.getPoleDat()

        upravenaData = folderStructProgram.upravDataProStrom.upravData(poleDat)
        poleRadkuNew = upravenaData.getPoleRadkuNew()


        folderStructProgram.tiskniTxt.tiskniDoTxt(poleRadkuNew)
        log.generujLog.loguData("pathTree.txt", poleRadkuNew)

        # program tiskne vystup do txt
        genHtmlProgram.genStart.generujHtml(poleRadkuNew)



