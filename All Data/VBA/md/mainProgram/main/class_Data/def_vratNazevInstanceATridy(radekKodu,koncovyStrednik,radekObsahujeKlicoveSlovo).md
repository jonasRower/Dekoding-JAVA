# def vratNazevInstanceATridy(radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo):

### list of variables
nazevInstance   
nazevTridy   
jednaSeOMetodu   
koncovyStrednik   
radekObsahujeKlicoveSlovo   
radekObsaheujeNew   
indexRovnitka   
slovaNaRadku   

### code of method
<pre>
 <code>
def vratNazevInstanceATridy(radekKodu, koncovyStrednik, radekObsahujeKlicoveSlovo):
    #vraci data z typoveho radku:
    #Select selNejmensi = new Select(dotazNejmensi);

    nazevInstance = ""
    nazevTridy = ""

    # kod vykonava na zaklade zjisteni existence zavorek "(" a ")"
    jednaSeOMetodu = indikujZdaSeJednaOMetodu(radekKodu)
    if (jednaSeOMetodu == True):

        #pokud radek neobsahuje strednik, pak se nejedna o radek typu:
        #Select selStredni = new Select(dotazStredni);
        #a tudis neni co resit a na konci funkce se zapisi data typu "" do pole
        if (koncovyStrednik == True):

            #Take radek nesmi obsahovat klicove slovo for, if, catch ...
            if (radekObsahujeKlicoveSlovo == False):

                # zjisti index klicoveho slova 'new'
                radekObsaheujeNew = obahujeRadekKoduKlicoveSlovoNew(radekKodu)
                if (radekObsaheujeNew == True):

                    #pokud klicove slovo "new" je obsazeno, pak proveruje, zda radekKodu obsahuje "="
                    if (radekObsaheujeNew == True):
                        indexRovnitka = 0
                        try:
                            indexRovnitka = radekKodu.index('=')
                        except:
                            pass

                        #pokud i obsahuje "=" pak pokracuje kod dal - oddeli nazev Instance a nazev Tridy
                        slovaNaRadku = radekKodu.split()
                        nazevTridy = slovaNaRadku[0]
                        nazevInstance = slovaNaRadku[1]


    #data do pole se predavaji zde
    data.add_nazevInstance(nazevInstance)
    data.add_nazevTridy(nazevTridy)
 <code>
<pre>
