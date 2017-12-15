from hamcrest import *
from model.collection_model import CollectionModel
from model.document_model import DocumentModel
from helpers.data_convertor import Xml_convertor
from unittest import TestCase

from model.query_model import QueryModel


class TestCollectionModel(TestCase):
    def test_prob_term(self):
        forum = Xml_convertor.convert_data("dfss")
        collection = CollectionModel(forum)
        question = forum.threads[0].question
        query = QueryModel(question.text)
        doubles = []
        for term in query.query_terms:
            double = collection.prob_term(term)
            doubles.append(double)
        print(doubles)
