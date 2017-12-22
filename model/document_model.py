from helpers.text_preprocessor import PreProcessor
from helpers.frequency_calculator import FrequencyHelper
from functools import reduce


class DocumentModel:
    def __init__(self, text):
        self.document_terms = PreProcessor.processText(text)
        self.tfidx = FrequencyHelper.calculate_frequencies(self.document_terms)
        self.rank_value = -1

    def prob_document_given_query(self, query_terms):
        # return reduce(lambda y, z: y * z, map(lambda x: self.tfidx.get(x), query_model.query_terms))
        if len(self.document_terms) < 1:
            return 0
        prob_doc = 1
        for term in query_terms:
            prob_doc = self.tfidx.get(term, 0)*prob_doc
        self.rank_value = prob_doc
        return prob_doc
