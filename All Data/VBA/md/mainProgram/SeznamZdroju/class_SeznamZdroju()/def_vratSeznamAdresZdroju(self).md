# def vratSeznamAdresZdroju(self):

### list of variables
<a href  
files   

### code of method
<pre>
 <code>
    def vratSeznamAdresZdroju(self):

        #seznamZdroju = []
          <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_SeznamZdroju()/def_vyhledejAdresuSrc(self).md">adresaNadrazeneSlozky=self.vyhledejAdresuSrc()</a>


        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(adresaNadrazeneSlozky):
            for file in f:
                #print("")
                if '.java' in file:
                    files.append(os.path.join(r, file))

        for f in files:
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_SeznamZdroju()/def_add_AdresZdroju(self, adresaZdroje).md">self.add_AdresZdroju(f)</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_SeznamZdroju()/def_add_Zdroj(self, zdroj).md">self.add_Zdroj(os.path.basename(f))</a>
              <a href="../../../../../../All%20Data/VBA/md/mainProgram/SeznamZdroju/class_SeznamZdroju()/def_add_Adresa(self, adresa).md">self.add_Adresa(self.vratAdresu(f,os.path.basename(f)))</a>

        return(self)
 <code>
<pre>



