class nactiLog:

    def __init__(self, adresaLog):

        dataLog = self.nactiDataTxt(adresaLog)
        self.dataLog = self.odeberPrazdneRadky(dataLog)


    def getDataLog(self):
        return(self.dataLog)


    def odeberPrazdneRadky(self, dataLog):

        dataLogNew = []

        for i in range(0, len(dataLog)):
            radek = dataLog[i]
            radekTrim = radek.strip()

            if(radekTrim != ''):
                dataLogNew.append(radek)

        return(dataLogNew)


    def nactiDataTxt(self, adresaLog):

        pole = []

        r = -1
        with open(adresaLog, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n' ,'')
                pole.append(line)

        return (pole)