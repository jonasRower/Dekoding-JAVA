# def __init__(self, vsechnaSlovaAId):

### list of variables
<a href  
poleID   
slovaAId   

### code of method
<pre>
 <code>
    def __init__(self, vsechnaSlovaAId):

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/poleSlov = [].md">poleSlov=self.vratPole1D(vsechnaSlovaAId,0)</a>
        poleID = self.vratPole1D(vsechnaSlovaAId, 1)
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/poleSlovUniq = self.unique(poleSlov).md">seznamIndexuSlovUniq=self.vratPoleIndexuVsechVyskytu(poleSlov)</a>

        slovaAId = self.prevedIndexySlovNaId(seznamIndexuSlovUniq, poleID)
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/obarvujText/def___init__(self,_vsechnaSlovaAId)/jsonRadekArr = [].md">self.jsonRadekArr=self.prevedSlovaAIdNaJson(slovaAId)</a>

        print()
 <code>
<pre>


