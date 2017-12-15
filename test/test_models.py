import unittest
from hamcrest import *
from model.collection_model import CollectionModel
from model.document_model import DocumentModel
from model.query_model import QueryModel
from helpers.data_convertor import Xml_convertor
from unittest import TestCase


class TestModels(TestCase):
    def test_collection(self):
        forum = Xml_convertor.convert_data("dfss")
        collection = CollectionModel(forum)
        question = forum.threads[0].question

