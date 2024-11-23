# def obahujeRadekKoduKlicoveSlovoNew(radekKodu):

### list of variables
indexSlovaNew   
radekObsahujeNew   

### code of method
<pre>
 <code>
def obahujeRadekKoduKlicoveSlovoNew(radekKodu):

    indexSlovaNew = -1
    radekObsahujeNew = False
    try:
        indexSlovaNew = radekKodu.index('new')
        if(indexSlovaNew > -1):
            radekObsahujeNew = True
    except:
        pass

    return(radekObsahujeNew)
 <code>
<pre>
