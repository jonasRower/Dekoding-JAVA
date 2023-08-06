
import log.generujLog

class novyHtml:

    def __init__(self, jsonData):

        poleRadkuAll = self.vytvorPoleRadkuHtml(jsonData)
        log.generujLog.loguData("index.html", poleRadkuAll)



    def vytvorPoleRadkuHtml(self, jsonData):

        # oprav jen texty, nikoliv cele radky!!
        jsonData = self.opravRadkyJsonData(jsonData)

        radkyPred = self.definujRadkyPred()
        radkyZa = self.definujRadkyZa()

        poleRadkuAll = radkyPred
        poleRadkuAll = poleRadkuAll + jsonData
        poleRadkuAll = poleRadkuAll + radkyZa

        return(poleRadkuAll)


    def opravRadkyJsonData(self, jsonData):

        for i in range(0, len(jsonData)):
            radek = jsonData[i]
            radek = radek.replace('§', '/')
            radek = radek.replace('\\\"', '\\')

            jsonData[i] = radek

        return (jsonData)



    def definujRadkyPred(self):

        radkyPred = []
        radkyPred.append('<!DOCTYPE html>')
        radkyPred.append('<html lang="en" xmlns="http://www.w3.org/1999/xhtml">')
        radkyPred.append('<head>')
        radkyPred.append('    <meta charset="utf-8" />')
        radkyPred.append('    <title>Simple jsTree</title>')
        radkyPred.append('    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jstree/3.2.1/themes/default/style.min.css" />')
        radkyPred.append('    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js"></script>')
        radkyPred.append('    <script src="https://cdnjs.cloudflare.com/ajax/libs/jstree/3.2.1/jstree.min.js"></script>')
        radkyPred.append('')
        radkyPred.append('    <script type="text/javascript">')
        radkyPred.append('        $(function () {')
        radkyPred.append('')
        radkyPred.append('            var jsondata = [')

        return(radkyPred)


    def definujRadkyZa(self):

        radkyZa = []
        radkyZa.append('            ];')
        radkyZa.append('            createJSTree(jsondata);')
        radkyZa.append('        });')
        radkyZa.append('')
        radkyZa.append('        function createJSTree(jsondata) { ')
        radkyZa.append('            $(\'#SimpleJSTree\').jstree({')
        radkyZa.append('                \'core\': {')
        radkyZa.append('                    \'data\': jsondata')
        radkyZa.append('                }')
        radkyZa.append('            });')
        radkyZa.append('        }')
        radkyZa.append('    </script>')
        radkyZa.append('')
        radkyZa.append('</head>')
        radkyZa.append('<body>')
        radkyZa.append('   <div id="SimpleJSTree"></div>')
        radkyZa.append('</body>')
        radkyZa.append('</html>')

        return (radkyZa)


