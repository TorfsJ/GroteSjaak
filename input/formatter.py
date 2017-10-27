from lxml import objectify

from dom.thread import Thread

from bs4 import BeautifulSoup


class XmlFormatter:
    def converttothreads(self, xmlobject):
        obj = objectify.fromstring(xmlobject)
        print(obj.object1[0])
        thread = Thread()

