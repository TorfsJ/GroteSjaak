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
        threadzero = forum.threads[0]
        # querytermen = threadzero.question.query_model.query_terms
        # doubles = []
        # for comment in threadzero.comments:
        #     double = comment.document_model.prob_document_given_query(querytermen)
        #     doubles.append(double)
        threadzero.calculate_ranking(forum.collection_model)
        temp = []
        for comment in threadzero.comments:
            x = [comment.rankvalue, comment.comment_id]
            temp.append(x)
        sortedcomments = sorted(temp)
        print(sortedcomments)

