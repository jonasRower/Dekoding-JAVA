# def vratSeznamAdresZdroju(self):

### list of variables
adresaNadrazeneSlozky   
files   

### code of method
```
    def vratSeznamAdresZdroju(self):

        #seznamZdroju = []
        adresaNadrazeneSlozky = self.vyhledejAdresuSrc()


        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(adresaNadrazeneSlozky):
            for file in f:
                #print("")
                if '.java' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            self.add_AdresZdroju(f)
            self.add_Zdroj(os.path.basename(f))
            self.add_Adresa(self.vratAdresu(f, os.path.basename(f)))

        return(self)
```
### links

