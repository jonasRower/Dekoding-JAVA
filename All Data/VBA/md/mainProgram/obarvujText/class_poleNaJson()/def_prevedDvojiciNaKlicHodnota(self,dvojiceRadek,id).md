# def prevedDvojiciNaKlicHodnota(self, dvojiceRadek, id):

### list of variables
dvojice   
slovo   
atribut   
jsonWordAtr   

### code of method
```
    def prevedDvojiciNaKlicHodnota(self, dvojiceRadek, id):

        dvojice = str(dvojiceRadek).split(',')

        slovo = self.odeberUvozovky(dvojice[0])
        atribut = self.odeberUvozovky(dvojice[1])

        jsonWordAtr = '{ "id": "' + str(id) + '" , "word": "' + slovo + '" , "atribute": "' + atribut + '" }'

        #prida vsechna slova a id do pole
        self.zapisVsechnaSlovaAId(slovo, id)

        return(jsonWordAtr)
```
