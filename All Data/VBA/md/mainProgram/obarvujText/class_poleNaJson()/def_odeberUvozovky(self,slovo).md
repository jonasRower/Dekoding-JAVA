# def odeberUvozovky(self, slovo):

### list of variables
slovoNew   

### code of method
```
    def odeberUvozovky(self, slovo):

        slovoNew = slovo.replace("\'", '')
        slovoNew = slovoNew.replace("\"", '')
        slovoNew = slovoNew.replace("[", '')
        slovoNew = slovoNew.replace("]", '')

        return(slovoNew)
```
### links

