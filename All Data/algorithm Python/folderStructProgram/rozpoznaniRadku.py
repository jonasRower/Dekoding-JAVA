class dataNaRozpoznaniRadku:

    def __init__(self):

        self.definRow1If = self.definujIf1()
        self.definRow2If = self.definujIf2()


    def getDefinRow1If(self):
        return(self.definRow1If)

    def getDefinRow2If(self):
        return(self.definRow2If)



    def definujIf1(self):

        coObsahujeRadek1 = []

        coObsahujeRadek1.append('if')
        coObsahujeRadek1.append('(')
        coObsahujeRadek1.append(')')

        return(coObsahujeRadek1)


    def definujIf2(self):

        coObsahujeRadek2 = []

        coObsahujeRadek2.append('{')

        return (coObsahujeRadek2)