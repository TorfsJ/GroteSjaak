from helpers.text_preprocessor import PreProcessor
from helpers.frequency_calculator import FrequencyHelper
from functools import reduce


class DocumentModel:
    def __init__(self, text):
        self.document_terms = PreProcessor.processText(text)
        self.tfidx = FrequencyHelper.calculate_frequencies(self.document_terms)

    def prob_document_given_query(self, query_term):
        # return reduce(lambda y, z: y * z, map(lambda x: self.tfidx.get(x), query_model.query_terms))
        return self.tfidx.get(query_term, 0)
