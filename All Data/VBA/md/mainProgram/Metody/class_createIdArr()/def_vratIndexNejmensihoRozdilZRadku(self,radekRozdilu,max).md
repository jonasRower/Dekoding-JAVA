# def vratIndexNejmensihoRozdilZRadku(self, radekRozdilu, max):

### list of variables
nejmensiRozdil   
index   
rozdil   
if(rozdil !  

### code of method
```
    def vratIndexNejmensihoRozdilZRadku(self, radekRozdilu, max):

        nejmensiRozdil = max
        index = 0

        for i in range(0, len(radekRozdilu)):
            rozdil = radekRozdilu[i]
            if(rozdil != False):
                if(rozdil < nejmensiRozdil):
                    nejmensiRozdil = rozdil
                    index = i

        return(index)
```
### links

