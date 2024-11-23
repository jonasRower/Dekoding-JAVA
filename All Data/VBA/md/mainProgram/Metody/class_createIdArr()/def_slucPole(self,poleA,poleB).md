# def slucPole(self, poleA, poleB):

### list of variables
list1   
x   
poleUniq   

### code of method
<pre>
 <code>
    def slucPole(self, poleA, poleB):

        list1 = poleA + poleB
        x = np.array(list1)
        poleUniq = np.unique(x)

        return(poleUniq)
 <code>
<pre>
