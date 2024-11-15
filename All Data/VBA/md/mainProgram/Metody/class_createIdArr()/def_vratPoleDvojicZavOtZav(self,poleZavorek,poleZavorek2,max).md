# def vratPoleDvojicZavOtZav(self, poleZavorek, poleZavorek2, max):

### list of variables
poleIndexuZavOt   
poleIndexuZavZav   
rozdilyAll   
sourRSAll   
dvojiceOtZavAll   

### code of method
```
    def vratPoleDvojicZavOtZav(self, poleZavorek, poleZavorek2, max):

        #poleIndexuZavOt1 = self.vratPoleIndexu(poleZavorek, '{')
        #poleIndexuZavZav1 = self.vratPoleIndexu(poleZavorek, '}')

        #poleIndexuZavOt2 = self.vratPoleIndexu(poleZavorek2, '{')
        #poleIndexuZavZav2 = self.vratPoleIndexu(poleZavorek2, '}')

        #poleIndexuZavOt = self.slucPole(poleIndexuZavOt1, poleIndexuZavOt2)
        #poleIndexuZavZav = self.slucPole(poleIndexuZavZav1, poleIndexuZavZav2)

        poleIndexuZavOt = self.vratPoleIndexu(poleZavorek, '{')
        poleIndexuZavZav = self.vratPoleIndexu(poleZavorek, '}')

        #muze se stat, ze nenajde vsechny zavorky, pak doplnuje indexy krajnimi hodnotami
        #poleIndexuZavOt = self.doplnChybejiciZavorkyOtZav(poleIndexuZavOt, poleIndexuZavZav, True, max)
        #poleIndexuZavZav = self.doplnChybejiciZavorkyOtZav(poleIndexuZavOt, poleIndexuZavZav, False, max)


        rozdilyAll = self.vratPoleRozdiluAll(poleIndexuZavOt, poleIndexuZavZav)
        sourRSAll = self.vyhledavejNejmensiRozdily(copy.deepcopy(rozdilyAll), len(poleZavorek))
        dvojiceOtZavAll = self.vratDvojiceIndexuZavorek(poleIndexuZavOt, poleIndexuZavZav, sourRSAll, max)


        return(dvojiceOtZavAll)
```
