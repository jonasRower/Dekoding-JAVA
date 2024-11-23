# def vratPoleZavorek(self, poleRadku):

### list of variables
poleZavorek   
radek   
met1   
slozenaZavorka   

### code of method
<pre>
 <code>
    def vratPoleZavorek(self, poleRadku):

        poleZavorek = []

        for i in range(0, len(poleRadku)):

            radek = poleRadku[i]
            met1 = MetodyJednohoRadku(False)
            slozenaZavorka = met1.vratSlozenouZavorku(radek)

            poleZavorek.append(slozenaZavorka)

        return(poleZavorek)
 <code>
<pre>
