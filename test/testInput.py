import unittest
from hamcrest import *

from input.xml_reader import XmlReader


class TestReader(unittest.TestCase):
    def test_reader(self):
        reader = XmlReader()
        length = reader.readfile()
        assert_that(length > 0)
