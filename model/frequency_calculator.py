import collections


class FrequencyHelper:
    def __init__(self, input_text):
        self.input_text = input_text

    def chop_into_words(self, text):
        return text.split(' ')

    def count_words(self, word_list):
        return collections.Counter(word_list)

    def calculate_frequencies(self):
        words = self.chop_into_words(self.input_text)
        frequency_dict = self.count_words(words)
        return frequency_dict
