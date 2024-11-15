# def vratPoleRadkuBezZavorekNaZacatkuRadku(self, poleRadku):

### list of variables
poleRadku2   
radek   
radekBezPrvnihoZnaku   

### code of method
```
    def vratPoleRadkuBezZavorekNaZacatkuRadku(self, poleRadku):

        poleRadku2 = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radek = radek.strip()

            radekBezPrvnihoZnaku = radek[1:len(radek):1]
            poleRadku2.append(radekBezPrvnihoZnaku)

        return(poleRadku2)
```
