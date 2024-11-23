# def vyberDataKdeJeDanaMetoda(self, dataVsechSouboru, pozadovanyNazevMetody):

### list of variables
i   
dataObsahujiDanouMetodu   
celyZdrojSDanouMetodou   
dataJednohoSouboru   
<a href  
if(dataObsahujiDanouMetodu   

### code of method
<pre>
 <code>
    def vyberDataKdeJeDanaMetoda(self, dataVsechSouboru, pozadovanyNazevMetody):
        i = -1
        dataObsahujiDanouMetodu = False
        celyZdrojSDanouMetodou = ""
        for x in dataVsechSouboru:
            i = i + 1
            dataJednohoSouboru = dataVsechSouboru[i]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_vykonavaniHlavnihoProgramu()/def_zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(self, dataJednohoSouboru, pozadovanyNazevMetody).md">dataObsahujiDanouMetodu=self.zjistiZdaDataJednohoSouboruObsahujiDanouMetodu(dataJednohoSouboru,pozadovanyNazevMetody)</a>
            if(dataObsahujiDanouMetodu == True):
                celyZdrojSDanouMetodou = dataJednohoSouboru
                break

        return(celyZdrojSDanouMetodou)
 <code>
<pre>
