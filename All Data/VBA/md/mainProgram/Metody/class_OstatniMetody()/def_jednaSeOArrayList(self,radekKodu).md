# def jednaSeOArrayList(self, radekKodu):

### list of variables
ind   
jednaSeOArrayList   

### code of method
```
    def jednaSeOArrayList(self, radekKodu):

        try:
            ind = radekKodu.index('>(')
            if(ind > 0):
                jednaSeOArrayList = True
            else:
                jednaSeOArrayList = False

        except:
            jednaSeOArrayList = False


        return(jednaSeOArrayList)
```
