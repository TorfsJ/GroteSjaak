from helpers.frequency_calculator import FrequencyHelper
from helpers.text_preprocessor import PreProcessor
from functools import reduce


class CollectionModel:
    def __init__(self, forum):
        self.corpus = ""
        for thread in forum.threads:
            for comment in thread.comments:
                self.corpus += comment.text + " "
        temp = PreProcessor.processText(self.corpus)
        self.tfidx = FrequencyHelper.calculate_frequencies(temp)
        temp_corpus = ""
        for word in temp:
            temp_corpus += word + " "
        self.corpus = temp_corpus

    def prob_term(self, term):
        return self.tfidx.get(term)
