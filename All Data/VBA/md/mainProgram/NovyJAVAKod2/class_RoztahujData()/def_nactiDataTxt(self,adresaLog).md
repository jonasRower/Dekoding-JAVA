# def nactiDataTxt(self, adresaLog):

### list of variables
pole   
r   
line   

### code of method
```
    def nactiDataTxt(self, adresaLog):

        pole = []

        r = -1
        with open(adresaLog, 'r') as f:
            for line in f:
                r = r + 1

                line = line.replace('\n' ,'')
                pole.append(line)

        return (pole)
```
