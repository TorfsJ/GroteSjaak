from lxml import objectify

from dom.thread import Thread


class XmlFormatter:
    def converttothreads(self, xmlobject):
        obj = objectify.fromstring(xmlobject)
        print(obj.object1[0])
        thread = Thread()
