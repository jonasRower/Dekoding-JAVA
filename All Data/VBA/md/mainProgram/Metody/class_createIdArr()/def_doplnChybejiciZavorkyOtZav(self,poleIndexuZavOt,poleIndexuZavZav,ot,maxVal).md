# def doplnChybejiciZavorkyOtZav(self, poleIndexuZavOt, poleIndexuZavZav, ot, maxVal):

### list of variables
pocetOt   
pocetZav   
arrNew   
if(pocetOt !  
pocetMax   
ot   
pocetChyb   
hodnota   

### code of method
<pre>
 <code>
    def doplnChybejiciZavorkyOtZav(self, poleIndexuZavOt, poleIndexuZavZav, ot, maxVal):

        pocetOt = len(poleIndexuZavOt)
        pocetZav = len(poleIndexuZavZav)

        arrNew = []

        if(pocetOt != pocetZav):

            pocetMax = max(pocetOt, pocetZav)


            for i in range(0, pocetMax):

                if (ot == True):

                    pocetChyb = pocetMax - pocetOt
                    if(i < pocetChyb):
                        hodnota = -i
                    else:
                        hodnota = poleIndexuZavOt[i - pocetChyb]

                else:

                    pocetChyb = pocetMax - pocetZav
                    if (i > pocetChyb):
                        hodnota = maxVal + i - pocetChyb - 1
                    else:
                        if(i > len(poleIndexuZavZav)-1):
                            try:
                                hodnota = poleIndexuZavZav[len(poleIndexuZavZav)-1] + 1
                            except:
                                hodnota = 0
                        else:
                            hodnota = poleIndexuZavZav[i]

                arrNew.append(hodnota)

        return(arrNew)
 <code>
<pre>
