# def rozdelRadkyNaSlova(self, poleRadku):

### list of variables
radekSlovaAtributyAll   
radek   
radekSpl   
<a href  
radekSlovaAtributy   

### code of method
<pre>
 <code>
    def rozdelRadkyNaSlova(self, poleRadku):

        radekSlovaAtributyAll = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekSpl = radek.split(' ')
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\obarvujText\def___init__(self,_dataDaneTridy,_ostatniMetody,_poleRadkuNOdDo)\radekSlova = []">radekSlova=self.vratRadekJenSlova(radekSpl)</a>

            radekSlovaAtributy = self.priradAtributyKeVsemSlovumRadku(radekSlova)
            radekSlovaAtributyAll.append(str(radekSlovaAtributy))

        return(radekSlovaAtributyAll)
 <code>
<pre>
