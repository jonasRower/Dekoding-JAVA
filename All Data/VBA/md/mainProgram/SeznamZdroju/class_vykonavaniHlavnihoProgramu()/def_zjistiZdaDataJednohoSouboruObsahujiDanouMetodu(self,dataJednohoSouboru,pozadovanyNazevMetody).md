# def zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(self, dataJednohoSouboru, pozadovanyNazevMetody):

### list of variables
dataZdrojeObsahujiMetodu   
if(nazevMetody   

### code of method
```
    def zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(self, dataJednohoSouboru, pozadovanyNazevMetody):
        dataZdrojeObsahujiMetodu = False
        for nazevMetody in dataJednohoSouboru.volanaMetoda:
            if(nazevMetody == pozadovanyNazevMetody):
                dataZdrojeObsahujiMetodu = True
                break

        return(dataZdrojeObsahujiMetodu)
```
### links

