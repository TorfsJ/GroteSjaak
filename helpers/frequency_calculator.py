import collections


class FrequencyHelper:
    @staticmethod
    def calculate_frequencies(wordlist):
        frequency_dict = collections.Counter(wordlist)
        d = dict(frequency_dict)
        wordcount = len(d)
        d2 = {}
        for k, v in d.items():
            d2[k] = v/wordcount
        return d2
