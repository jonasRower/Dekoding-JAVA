# def pridejMezeryPredRadek(self, subKod, pocetMezer):

### list of variables
SubKodSMezerou   
mezeraPredSubKodem   
radekSubKoduSMezerou   

### code of method
<pre>
 <code>
    def pridejMezeryPredRadek(self, subKod, pocetMezer):


        SubKodSMezerou = []

        mezeraPredSubKodem = ""

        if(pocetMezer > -1):
            for i in range(0, pocetMezer):
                mezeraPredSubKodem = mezeraPredSubKodem + " "

            mezeraPredSubKodem = mezeraPredSubKodem + "-->" + "  "

        for radekSubKodu in subKod:
            radekSubKoduSMezerou = mezeraPredSubKodem + radekSubKodu
            SubKodSMezerou.append(radekSubKoduSMezerou)

        return (SubKodSMezerou)
 <code>
<pre>
