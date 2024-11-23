# def vytvorPoleRadkuHtml(self, jsonData):

### list of variables
<a href  
poleRadkuAll   

### code of method
<pre>
 <code>
    def vytvorPoleRadkuHtml(self, jsonData):

        # oprav jen texty, nikoliv cele radky!!
          <a href="../../../../../../All%20Data/VBA/md/genHtmlProgram\generujHtml\class_novyHtml\def opravRadkyJsonData(self, jsonData)">jsonData=self.opravRadkyJsonData(jsonData)</a>

          <a href="../../../../../../All%20Data/VBA/md/genHtmlProgram\generujHtml\class_novyHtml\def definujRadkyPred(self)">radkyPred=self.definujRadkyPred()</a>
          <a href="../../../../../../All%20Data/VBA/md/genHtmlProgram\generujHtml\class_novyHtml\def definujRadkyZa(self)">radkyZa=self.definujRadkyZa()</a>

        poleRadkuAll = radkyPred
        poleRadkuAll = poleRadkuAll + jsonData
        poleRadkuAll = poleRadkuAll + radkyZa

        return(poleRadkuAll)
 <code>
<pre>


