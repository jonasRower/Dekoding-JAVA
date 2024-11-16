# def vratPole1D(self, pole2D, index):

### list of variables
poleSlov   
slovo   

### code of method
```
    def vratPole1D(self, pole2D, index):

        poleSlov = []

        for i in range(0, len(pole2D)):
            slovo = pole2D[i][index]
            poleSlov.append(slovo)

        return(poleSlov)
```
