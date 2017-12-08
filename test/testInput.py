import unittest
from hamcrest import *
from input.formatter import XmlFormatter


class TestReader(unittest.TestCase):
    def test_reader(self):
        fileuris = ["kakhoofd", "u mama"]
        reader = XmlFormatter("sgdsdg")
        reader.convert_data()
