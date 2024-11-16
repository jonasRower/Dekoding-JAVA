# def vyberDataKdeJeDanaMetoda(self, dataVsechSouboru, pozadovanyNazevMetody):

### list of variables
i   
dataObsahujiDanouMetodu   
celyZdrojSDanouMetodou   
dataJednohoSouboru   
if(dataObsahujiDanouMetodu   

### code of method
```
    def vyberDataKdeJeDanaMetoda(self, dataVsechSouboru, pozadovanyNazevMetody):
        i = -1
        dataObsahujiDanouMetodu = False
        celyZdrojSDanouMetodou = ""
        for x in dataVsechSouboru:
            i = i + 1
            dataJednohoSouboru = dataVsechSouboru[i]
            dataObsahujiDanouMetodu = self.zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(dataJednohoSouboru, pozadovanyNazevMetody)
            if(dataObsahujiDanouMetodu == True):
                celyZdrojSDanouMetodou = dataJednohoSouboru
                break

        return(celyZdrojSDanouMetodou)
```
