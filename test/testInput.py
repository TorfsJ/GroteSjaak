import unittest
from hamcrest import *

from manager.input_service import InputService
from input.xml_reader import XmlReader
from input.formatter import XmlFormatter

class TestReader(unittest.TestCase):
    def test_reader(self):
        fileuris = ["kakhoofd", "u mama"]
        service = InputService()
        service.create_collection(fileuris)
        # reader = XmlReader()
        # xmlfile = reader.readfile()
        # formatter = XmlFormatter()
        # formatter.converttothreads(xmlfile)
