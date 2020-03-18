import os
import pprint
import xml.sax
import xml.sax.handler
import sys


class ProfileHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = 0
        self.mapping = {}

    def startElement(self, name, attrs):
        print("Start element called.........")
        print(name)
        if name == 'userid':
            print(attrs['admin'])
            for k, v in attrs.items():
                print(k, v)
        # if name == "book":
        #     self.buffer = ""
        #     self.isbn = attrs['isbn']
        # elif name == "title":
        #     self.inTitle = 1

    def characters(self, content):
        print("Content characters called.........")
        print(content)
        # if self.inTitle:
        #     print(content)
        #     self.buffer += content

    def endElement(self, name):
        print("End element called.........")
        print(name)
        # if name == "title":
        #     self.inTitle = 0
        #     self.mapping[self.isbn] = self.buffer

print(sys.stdin)
print(os.getcwd())
parser = xml.sax.make_parser()
handler = ProfileHandler()
parser.setContentHandler(handler)

parser.parse("./data/profile.xml")
# saxparser.parse(sys.stdin)
pprint.pprint(handler.mapping)
