# def pridejSloupecDoCsv(self, csvData, sloupec):

### list of variables
pridavejPrvniSloupec   
csvData   
radek   
if(pridavejPrvniSloupec   
radek0   
radekNew   
csvData[i]   

### code of method
<pre>
 <code>
    def pridejSloupecDoCsv(self, csvData, sloupec):

        pridavejPrvniSloupec = False

        if not csvData:
            csvData = ['' for i in range(len(sloupec)+1)]
            pridavejPrvniSloupec = True

        for i in range(0, len(sloupec)):
            radek = str(sloupec[i])
            radek = radek.replace(',', '?')

            if(pridavejPrvniSloupec == False):
                radek0 = csvData[i]
            else:
                radek0 = ''

            radekNew = radek0 + str(radek) + ', '
            radekNew = radekNew.replace('\n', '')
            csvData[i] = radekNew

        return(csvData)
 <code>
<pre>
