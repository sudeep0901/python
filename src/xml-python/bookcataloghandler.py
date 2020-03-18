import os
import pprint
import xml.sax
import xml.sax.handler


class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = 0
        self.mapping = {}

    def startElement(self, name, attrs):
        print("Start element called.........")

        if name == "book":
            self.buffer = ""
            self.isbn = attrs['isbn']
        elif name == "title":
            self.inTitle = 1

    def characters(self, content):
        print("End characters called.........")

        if self.inTitle:
            print(content)
            self.buffer += content

    def endElement(self, name):
        print("End element called.........")
        print(name)
        if name == "title":
            self.inTitle = 0
            self.mapping[self.isbn] = self.buffer


print(os.getcwd())
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)

parser.parse("/home/sudeep/sources/github/pythongithub/src/xml-python/data/catelog.xml")
pprint.pprint(handler.mapping)
