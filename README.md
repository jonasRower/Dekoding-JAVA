# Dekoding-JAVA
Převádí zdrojový kód JAVA do stromové struktury.

toto je test

## Spuštění programu
Po stažení a spustíme program v IDE Pycharm

V souboru `StartProgramu.py` začíná běh programu.
Kód je následující:
```
import mainProgram.SeznamZdroju
import mainProgram.NovyJAVAKod


vykonavejHlavniProgram = mainProgram.SeznamZdroju.vykonavaniHlavnihoProgramu()
vykonavejHlavniProgram.hlavniProgram()
```

## Popis metod
### class `vykonavaniHlavnihoProgramu():`
třída je v souboru: `mainProgram.SeznamZdroju`.

#### metoda `def hlavniProgram(self):`
`adresyZdrojuData.vratSeznamAdresZdroju()` plní objekt `adresyZdrojuData` daty.  
`seznamAdres` obsahuje seznam všech adres k jednotlivým `.java` souborům - bez názvů `.java`  
`seznamAdresZdroju`obsahuje seznam všech adres k jednotlivým `.java souborům` - včetně názvů `.java`  
`seznamZdroju` obsahuje seznam názvů souborů `.java`  


