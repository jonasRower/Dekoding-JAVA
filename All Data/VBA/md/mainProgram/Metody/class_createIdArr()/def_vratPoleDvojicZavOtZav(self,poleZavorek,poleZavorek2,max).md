# def vratPoleDvojicZavOtZav(self, poleZavorek, poleZavorek2, max):

### list of variables
<a href  

### code of method
<pre>
 <code>
    def vratPoleDvojicZavOtZav(self, poleZavorek, poleZavorek2, max):

        #poleIndexuZavOt1 = self.vratPoleIndexu(poleZavorek, '{')
        #poleIndexuZavZav1 = self.vratPoleIndexu(poleZavorek, '}')

        #poleIndexuZavOt2 = self.vratPoleIndexu(poleZavorek2, '{')
        #poleIndexuZavZav2 = self.vratPoleIndexu(poleZavorek2, '}')

        #poleIndexuZavOt = self.slucPole(poleIndexuZavOt1, poleIndexuZavOt2)
        #poleIndexuZavZav = self.slucPole(poleIndexuZavZav1, poleIndexuZavZav2)

          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleIndexu(self, poleRadku, strExp).md">poleIndexuZavOt=self.vratPoleIndexu(poleZavorek,'{')</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleIndexu(self, poleRadku, strExp).md">poleIndexuZavZav=self.vratPoleIndexu(poleZavorek,'}')</a>

        #muze se stat, ze nenajde vsechny zavorky, pak doplnuje indexy krajnimi hodnotami
        #poleIndexuZavOt = self.doplnChybejiciZavorkyOtZav(poleIndexuZavOt, poleIndexuZavZav, True, max)
        #poleIndexuZavZav = self.doplnChybejiciZavorkyOtZav(poleIndexuZavOt, poleIndexuZavZav, False, max)


          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratPoleRozdiluAll(self, poleIndexuZavOt, poleIndexuZavZav).md">rozdilyAll=self.vratPoleRozdiluAll(poleIndexuZavOt,poleIndexuZavZav)</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vyhledavejNejmensiRozdily(self, rozdilyAll, maxPol).md">sourRSAll=self.vyhledavejNejmensiRozdily(copy.deepcopy(rozdilyAll),len(poleZavorek))</a>
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/Metody/class_createIdArr()/def_vratDvojiceIndexuZavorek(self, poleIndexuZavOt, poleIndexuZavZav, sourRSAll, maxPol).md">dvojiceOtZavAll=self.vratDvojiceIndexuZavorek(poleIndexuZavOt,poleIndexuZavZav,sourRSAll,max)</a>


        return(dvojiceOtZavAll)
 <code>
<pre>




