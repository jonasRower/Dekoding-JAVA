# def vratCisloRadkuNazvuMetody(self, data, nazevPozadovaneMetody):

### list of variables
i   
cisloRadkuMetody   
nazevMetody   

### code of method
<pre>
 <code>
    def vratCisloRadkuNazvuMetody(self, data, nazevPozadovaneMetody):
        i = -1
        cisloRadkuMetody = -1
        for x in data.nazevMetody:
            i = i + 1
            nazevMetody = data.nazevMetody[i]
            if (nazevMetody == nazevPozadovaneMetody):
                cisloRadkuMetody = i
                break

        return(cisloRadkuMetody)
 <code>
<pre>
