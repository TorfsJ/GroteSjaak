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
        tempCorpus = ""
        for word in temp:
            tempCorpus += word + " "
        self.corpus = tempCorpus

    def prob_term(self, term):
        return self.tfidx.get(term)
