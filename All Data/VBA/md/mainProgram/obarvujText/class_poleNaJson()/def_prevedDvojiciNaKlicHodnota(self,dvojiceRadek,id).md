# def prevedDvojiciNaKlicHodnota(self, dvojiceRadek, id):

### list of variables
dvojice   
slovo   
<a href  
jsonWordAtr   

### code of method
<pre>
 <code>
    def prevedDvojiciNaKlicHodnota(self, dvojiceRadek, id):

        dvojice = str(dvojiceRadek).split(',')

        slovo = self.odeberUvozovky(dvojice[0])
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\obarvujText\def___init__(self,_pole)\slovoNew = slovo.replace("\'", '')">atribut=self.odeberUvozovky(dvojice[1])</a>

        jsonWordAtr = '{ "id": "' + str(id) + '" , "word": "' + slovo + '" , "atribute": "' + atribut + '" }'

        #prida vsechna slova a id do pole
          <a href="../../../../../../All%20Data/VBA/md/mainProgram\obarvujText\def___init__(self,_pole)\if(slovo != "")">self.zapisVsechnaSlovaAId(slovo,id)</a>

        return(jsonWordAtr)
 <code>
<pre>

