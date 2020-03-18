import pprint
import xml.dom.minidom
from xml.dom.minidom import Node

import os
import sys
sys.path.insert(len(sys.path)  + 1, os.getcwd())
print(os.getcwd())
doc = xml.dom.minidom.parse("./data/catelog.xml")
# print(doc)

mapping = {}
for node in doc.getElementsByTagName("book"):
    isbn =  node.getAttribute("isbn")
    print(isbn)
    L =  node.getElementsByTagName("title")
    M = node.getElementsByTagName("author")

    for node2 in L:
        title = ""
        for node3 in node2.childNodes:
            if node3.nodeType == Node.TEXT_NODE:
                title += node3.data
                print(title)

        mapping[isbn] = title

    for node2 in M:
        author =""
        for node3 in node2.childNodes:
            if node3.nodeType == Node.TEXT_NODE:
                author += node3.data
                print(author)
        mapping['author'] = author
print(mapping)