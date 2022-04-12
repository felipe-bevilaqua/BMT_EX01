import xml.sax

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.title = ""
        self.title_list = []
        self.record_list = []
        self.record = ""
        self.count = 0

       # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag

       # Call when a character is read
    def characters(self, content):
        if (self.CurrentData == "RECORDNUM"):
            self.record = content
            self.record_list.append(self.record)
            self.title_list.append(self.title)
            self.title = []
            self.count +=1
            if self.count > 1:
                print(' '.join(self.title_list[-1])+',', file=open('titulos.csv', "a"))
        
        elif (self.CurrentData == "TITLE"):
            self.title.append(content)
            try:
                self.title.remove('\n')
            except:
                pass
        
    # Call when an elements ends
    def endElement(self, tag):
        self.CurrentData = ""
        

# create an XMLReader
with open('titulos.csv', 'w') as f:
    parser = xml.sax.make_parser()
    Handler = XMLHandler()
    parser.setContentHandler( Handler )
    parser.parse("./CysticFibrosis2-20220328/data/cf79.xml")
