# def prevedRadekNaRadekArr(self, radek):

### list of variables
radekSpl   
radekIntArr   
radekPolozka   
polozkaIntArr   
polozkaInt   

### code of method
```
    def prevedRadekNaRadekArr(self, radek):

        radekSpl = radek.split(',')
        radekIntArr = []

        for i in range(0, len(radekSpl)):
            radekPolozka = radekSpl[i]
            polozkaIntArr = re.findall(r'\d+', radekPolozka)
            polozkaInt = int(polozkaIntArr[0])

            radekIntArr.append(polozkaInt)

        return(radekIntArr)
```
### links

