# def zjistiZdaSeJednaOCatch(radekKodu):

### list of variables
radekKodu   
jednotlivaSlovaNaRadku   
catch   
if (slovo   

### code of method
```
def zjistiZdaSeJednaOCatch(radekKodu):
    radekKodu = "      catch(Exception e) {System.out.println(e);}"
    jednotlivaSlovaNaRadku = radekKodu.split()
    catch = False
    for slovo in jednotlivaSlovaNaRadku:
        if (slovo == 'catch'):
            catch = True
            break

    return (catch)
```
