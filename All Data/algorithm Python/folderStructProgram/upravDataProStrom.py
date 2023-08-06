import folderStructProgram.rozpoznaniRadku

class upravData:

    def __init__(self, poleRadku):

        poleRadkuNew = self.vynechRadkySLomitkemNaKonci(poleRadku)
        poleRadkuNew = self.pridejKeVsemRadkumProject(poleRadkuNew)


        # zatim nedelat vyhledejIndexyParuZavorek a udelat to tak, ze vsude kde je "\" tam by melo byt "if"
        #vyhledejIndexyParuZavorek.paryZavorek(poleRadkuNew)

        self.poleRadkuNew = poleRadkuNew


    def getPoleRadkuNew(self):
        return(self.poleRadkuNew)



    def detekujAObmenRadky(self, poleRadku):

        radkyKObmeneni = self.mainObmenovani(poleRadku)
        poleRadkuNew = self.obmenRadky(poleRadku, radkyKObmeneni)
        poleRadkuNew = self.vratPoleRadkuBezFalse(poleRadkuNew)
        poleRadkuNew = self.vymenRadkykPodIf(radkyKObmeneni, poleRadkuNew)
        poleRadkuNew = self.odmazzejDvojiteZavorky(poleRadkuNew)

        return(poleRadkuNew)



    def pridejKeVsemRadkumProject(self, poleRadku):

        poleRadkuNew = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekNew = radek.replace('{{', '{')
            radekNew = "project\\" + radekNew


            poleRadkuNew.append(radekNew)

        return(poleRadkuNew)


    def vynechRadkySLomitkemNaKonci(self, poleRadku):

        poleRadkuNew = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            posledniZnak = radek[len(radek)-1:len(radek):1]

            if(posledniZnak != '\\'):
                poleRadkuNew.append(radek)

        return(poleRadkuNew)


    def odmazzejDvojiteZavorky(self, poleRadku):

        poleRadkuNew = []

        for i in range(0, len(poleRadku)):
            radek = poleRadku[i]
            radekNew = radek.replace('{{', '{')
            radekNew = radekNew.replace('}}', '}')

            poleRadkuNew.append(radekNew)

        return(poleRadkuNew)


    # pod radky s if je treba vymenit lomitko za if
    def vymenRadkykPodIf(self, radkyKObmeneni, poleRadku):

        for i in range(1, len(radkyKObmeneni)):
            indRadku = radkyKObmeneni[i]-i
            radekDoPredposl = poleRadku[indRadku]
            radekNahrad = radekDoPredposl
            radekVzor = self.ziskejRadekBezPoslednihoNazvuAdresare(radekNahrad) + '{'

            poleRadku = self.nahradRadkyPodIndexem(poleRadku, indRadku, radekVzor, radekNahrad)
            print()

        return(poleRadku)


    def ziskejRadekBezPoslednihoNazvuAdresare(self, radek):

        radekSpl = radek.split('\\')
        radekNew = ""

        for i in range(0, len(radekSpl)-1):
            nazevSlozky = radekSpl[i]
            radekNew = radekNew + nazevSlozky + '\\'

        return(radekNew)


    def nahradRadkyPodIndexem(self, poleRadku, odIndexu, radekVzor, radekNahrad):

        for i in range(odIndexu, len(poleRadku)):

            # nahrazuje se, dokud nasledujici radek je mozne nahradit
            nahrazovatDal = self.detekujPosledniRadekKNahrazeni(poleRadku, i, radekVzor, radekNahrad)
            nahrazovatDal = True

            if(nahrazovatDal == True):
                radek = poleRadku[i]
                radekNew = radek.replace(radekVzor, radekNahrad)

                poleRadku[i] = radekNew

            else:
                break

            print()

        return(poleRadku)


    # posledni radek se jiz nebude nahrazovat, to zjistuje zde
    # je treba na posledni radek umistit uzavrenou zavorku "}"
    def detekujPosledniRadekKNahrazeni(self, poleRadku, index, radekVzor, radekNahrad):

        index1 = index + 1

        try:
            radek = poleRadku[index1]
            radekNew = radek.replace(radekVzor, radekNahrad)

            # kdyz radek jiz neni zmenen, znamena to, ze radek je jiz jiny a je potreba nastavit, ze se dal jiz nebude nahrazovat
            if(radekNew == radek):
                nahrazovatDal = False
            else:
                nahrazovatDal = True
        except:

            if(index1 == len(poleRadku)):
                nahrazovatDal = True  # pokud by to pravda nebyla, algoritmus by sem nedojel
            else:
                nahrazovatDal = False

        return(nahrazovatDal)


    def vratPoleRadkuBezFalse(self, poleRadku):

        poleRadkuNew = []

        for i in range(1, len(poleRadku)):
            radek = poleRadku[i]
            if(radek != False):
                poleRadkuNew.append(radek)

        return(poleRadkuNew)



    def obmenRadky(self, poleRadku, radkyKObmeneni):

        for i in range(1, len(radkyKObmeneni)):
            indObmen = radkyKObmeneni[i]

            if(radkyKObmeneni[0] == 'if'):
                radek = poleRadku[indObmen]
                radekNew = radek + '{'

                poleRadku[indObmen] = radekNew
                poleRadku[indObmen+1] = False

        return(poleRadku)


    def mainObmenovani(self, poleRadku):

        poleRadkuObmenit = []
        poleRadkuObmenit.append("if")

        for i in range(1, len(poleRadku)):

            radek1 = poleRadku[i-1]
            radek2 = poleRadku[i]

            jednaSeORadek = self.jednaSeORadekTypu(radek1, radek2, "if")

            if(jednaSeORadek == True):
                poleRadkuObmenit.append(i-1)

        return(poleRadkuObmenit)


    def jednaSeORadekTypu(self, radek1, radek2, podminka):

        detekujRadek = folderStructProgram.rozpoznaniRadku.dataNaRozpoznaniRadku()
        jednaSeORadek = False

        if (podminka == "if"):
            definRow1 = detekujRadek.getDefinRow1If()
            definRow2 = detekujRadek.getDefinRow2If()

            definRow1Bool = self.detekujZdaRadekObsahujeVsechnySubStringy(radek1, definRow1)
            definRow1Boo2 = self.detekujZdaRadekObsahujeVsechnySubStringy(radek2, definRow2)

            if(definRow1Bool == True):
                if (definRow1Boo2 == True):
                    jednaSeORadek = True


        return(jednaSeORadek)


    def detekujZdaRadekObsahujeVsechnySubStringy(self, radek, poleSubstr):

        poleVsechVyskytu = self.vratPoleVsechVyskytu(radek, poleSubstr)
        sizeArr = len(poleVsechVyskytu)
        sizeExp = len(poleSubstr)

        if(sizeArr == sizeExp):
            poleObsahujeSubStringy = True
        else:
            poleObsahujeSubStringy = False


        return(poleObsahujeSubStringy)


    def vratPoleVsechVyskytu(self, radek, poleSubstr):

        indFind = 0
        indSubstr = 0
        poleVsechVyskytu = []

        for i in range(0, len(radek)):

            try:
                Substr = poleSubstr[indSubstr]
                indFind = self.vratIndexFrom(radek, indFind, Substr)

                if (indFind == -1):
                    break
                else:
                    poleVsechVyskytu.append(indFind)
                    indSubstr = indSubstr + 1

            except:
                pass

        return (poleVsechVyskytu)



    def vratIndexFrom(self, arr, indexFrom, find):

        x = slice(indexFrom, len(arr))
        arrSlice = arr[x]

        try:
            indFind = indexFrom + arrSlice.index(find)
        except:
            indFind = -1

        return (indFind)