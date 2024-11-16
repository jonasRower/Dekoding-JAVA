# def hlavni(self):

### list of variables
input   
pozadovanaTrida   
nazevMetody   

### code of method
```
    def hlavni(self):

        input = self.nactiInput()

        # nazev tridy, kde je umistena metoda, ktera se bude dokumentovat
        pozadovanaTrida = input[0]

        # nazev metody, ktera se bude dokumetovat
        nazevMetody = input[1]

        # pocatecni kod, ktery se bude teprve roztahovat
        self.vratPocatecniKod(pozadovanaTrida, nazevMetody)

        self.roztahujKod()

        print("")
```
