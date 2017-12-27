import unittest
from hamcrest import *

from helpers.data_convertor import Xml_convertor


class TestReader(unittest.TestCase):
    def test_reader(self):
        fileuris = ["./SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml"]
        forum = Xml_convertor.convert_data("SemEval2016-Task3-CQA-QL-train-part1-subtaskA.xml")
        forum.make_models()
        print(forum.collection_model.corpus)
        #assert_that(len(forum.threads), equal_to(379))
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
        print(temp)
        sortedcomments = sorted(temp)
        print(sortedcomments)
        assert_that(len(temp), equal_to(10))

