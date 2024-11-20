# def najdiRadekVolaneMetody(nazevMetody):

### list of variables
radekVolaneMetody   
r   
nazevMetodyData   

### code of method
```
def najdiRadekVolaneMetody(nazevMetody):

    radekVolaneMetody = -1
    r = -1

    for nazevMetodyData in data.volanaMetoda:
        r = r + 1
        if (nazevMetodyData == nazevMetody):
            radekVolaneMetody = r

    return(radekVolaneMetody)
```
### links

