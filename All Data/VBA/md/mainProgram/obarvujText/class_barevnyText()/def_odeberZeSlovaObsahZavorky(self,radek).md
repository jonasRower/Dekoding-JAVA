# def odeberZeSlovaObsahZavorky(self, radek):

### list of variables
indexZavory   
radekPredZavorkou   

### code of method
```
    def odeberZeSlovaObsahZavorky(self, radek):

        try:
            indexZavory = radek.index('(')
            radekPredZavorkou = radek[0:indexZavory:1]
        except:
            radekPredZavorkou = radek

        return(radekPredZavorkou)
```
