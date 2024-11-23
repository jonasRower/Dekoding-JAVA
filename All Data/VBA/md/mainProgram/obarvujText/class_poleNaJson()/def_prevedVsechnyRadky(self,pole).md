# def prevedVsechnyRadky(self, pole):

### list of variables
poleRadkuJson   
radek   
radekMod   
radekSpl   
jsonStejneId   

### code of method
<pre>
 <code>
    def prevedVsechnyRadky(self, pole):

        poleRadkuJson = []

        for i in range(0, len(pole)):
            radek = pole[i]

            radekMod = radek.replace('[[', '')
            radekMod = radekMod.replace(']]', '')

            radekSpl = radekMod.split('], [')

            jsonStejneId = self.prevedSlovaJednohoRadku(radekSpl, i)
            poleRadkuJson = poleRadkuJson + jsonStejneId

        return(poleRadkuJson)
 <code>
<pre>
