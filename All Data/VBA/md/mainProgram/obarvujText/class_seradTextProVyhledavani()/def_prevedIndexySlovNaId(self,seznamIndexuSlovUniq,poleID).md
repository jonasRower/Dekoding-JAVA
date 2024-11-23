# def prevedIndexySlovNaId(self, seznamIndexuSlovUniq, poleID):

### list of variables
slovaAId   
radek   
slovo   
<a href  

### code of method
<pre>
 <code>
    def prevedIndexySlovNaId(self, seznamIndexuSlovUniq, poleID):

        slovaAId = []

        for i in range(0, len(seznamIndexuSlovUniq)):
            radek = seznamIndexuSlovUniq[i]
            slovo = radek[0]
              <a href="../../../../../../All%20Data/VBA/md/mainProgram\obarvujText\def___init__(self,_vsechnaSlovaAId)\slovoAId = []">seznamId=self.vratIDDleIndexuRadku(radek,slovo,poleID)</a>

            slovaAId.append(seznamId)

        return(slovaAId)
 <code>
<pre>
