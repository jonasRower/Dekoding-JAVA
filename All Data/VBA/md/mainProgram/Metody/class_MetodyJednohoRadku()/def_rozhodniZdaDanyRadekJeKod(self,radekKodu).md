# def rozhodniZdaDanyRadekJeKod(self, radekKodu):

### list of variables
radekKoduBezMezery   
JeToKod   
indexKomentare   

### code of method
<pre>
 <code>
    def rozhodniZdaDanyRadekJeKod(self, radekKodu):
        # print(radekKodu)
        radekKoduBezMezery = radekKodu.replace(" ", "")
        JeToKod = True

        try:
            indexKomentare = radekKoduBezMezery.index('//')
            #kod to neni, jen v pripade, ze komentar neni na nulté pozici radku
            if (indexKomentare == 0):
                JeToKod = False
            else:
                JeToKod = True
        except:
            pass

        return (JeToKod)
 <code>
<pre>
