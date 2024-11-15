# def vratPoleRozdiluAll(self, poleIndexuZavOt, poleIndexuZavZav):

### list of variables
rozdilyAll   
indexZav   
rozdilyArr   

### code of method
```
    def vratPoleRozdiluAll(self, poleIndexuZavOt, poleIndexuZavZav):

        rozdilyAll = []

        for i in range(0, len(poleIndexuZavZav)):
            indexZav = poleIndexuZavZav[i]
            rozdilyArr = self.vratPoleRozdiluKIndexuZav(poleIndexuZavOt, indexZav)

            rozdilyAll.append(rozdilyArr)

        return(rozdilyAll)
```
