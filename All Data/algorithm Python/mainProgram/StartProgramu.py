import mainProgram.NactiZdroj
import mainProgram.SeznamZdroju
import mainProgram.NovyJAVAKod

import folderStructProgram.folderStructStart

# jeste doladit kod, jen v tom smyslu,
# aby se vstupni data zadavali sem

# zatim je potreba je vkladat do NovyJAVAKod3 - hlavni
# prejmenovat tridu a promazat testovaci tridy

# ve tride Metody a metode:
# dataNew = OstatniMetody.vlozSubKodDoKodu(self, DataOrig, dataNovy, vkladejOdRadku + 2)
# se posouvaji vlozena data - zde kokretne o 2 radky dolu
# proverit, zda je to vyhovujici
# posouva se to kvuli tomu, ze obcas jsou jinak zavorky a je tezke detekovat zacatek a konec zavorky
# pripadne by se dalo zjistt na jakem radku je nazev metody pred "{"

# neni dodelan vystup - dodelat
# zatim dat breakpoint na linku 128 v modulu NovyJAVAKod3





vykonavejHlavniProgram = mainProgram.SeznamZdroju.vykonavaniHlavnihoProgramu()
vykonavejHlavniProgram.hlavniProgram()

# ziska data
poleRadkuN = vykonavejHlavniProgram.getPoleRadkuN()

# posle data do dalsiho programu
folderStructProgram.folderStructStart.vytvarejStrukturuCest(poleRadkuN)

print()

