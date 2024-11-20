# def najdiRadekVolaneMetody(self, nazevMetody, dataVolanaMetoda):

### list of variables
radekVolaneMetody   
r   
nazevMetodyData   

### code of method
```
    def najdiRadekVolaneMetody(self, nazevMetody, dataVolanaMetoda):

        radekVolaneMetody = -1
        r = -1

        for nazevMetodyData in dataVolanaMetoda:
            r = r + 1
            if (nazevMetodyData == nazevMetody):
                radekVolaneMetody = r

        return (radekVolaneMetody)
```
### links

