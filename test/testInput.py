import unittest
from hamcrest import *

from input.xml_reader import XmlReader
from input.formatter import XmlFormatter

class TestReader(unittest.TestCase):
    def test_reader(self):
        reader = XmlReader()
        xmlfile = reader.readfile()
        formatter = XmlFormatter()
        formatter.converttothreads(xmlfile)
