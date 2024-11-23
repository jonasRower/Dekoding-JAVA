# def odeberUvozovky(self, slovo):

### list of variables
slovoNew   

### code of method
<pre>
 <code>
    def odeberUvozovky(self, slovo):

        slovoNew = slovo.replace("\'", '')
        slovoNew = slovoNew.replace("\"", '')
        slovoNew = slovoNew.replace("[", '')
        slovoNew = slovoNew.replace("]", '')

        return(slovoNew)
 <code>
<pre>
