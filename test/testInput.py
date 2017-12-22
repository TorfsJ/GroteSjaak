import unittest
from hamcrest import *

from helpers.data_convertor import Xml_convertor


class TestReader(unittest.TestCase):
    def test_reader(self):
        fileuris = ["kakhoofd", "u mama"]
        forum = Xml_convertor.convert_data("dfss")
        forum.make_models()
        print(forum.collection_model.corpus)
        assert_that(len(forum.threads), equal_to(379))
