# def zneplatniDanyRadekASloupec(self, rozdilyAll, sourR, sourS):

### list of variables
rozdilyRadek   
hodnota   
if(r   
if(s   
rozdilyAll[r][s]   

### code of method
<pre>
 <code>
    def zneplatniDanyRadekASloupec(self, rozdilyAll, sourR, sourS):

        for r in range(0, len(rozdilyAll)):
            rozdilyRadek = rozdilyAll[r]
            for s in range(0, len(rozdilyAll)):
                hodnota = rozdilyAll[r][s]
                if(r == sourR):
                    hodnota = False
                if(s == sourS):
                    hodnota = False

                rozdilyAll[r][s] = hodnota

        return(rozdilyAll)
 <code>
<pre>
