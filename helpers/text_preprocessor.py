import nltk
from nltk.corpus import stopwords
import string

class PreProcessor:
    @staticmethod
    def processText(text):
        text = text.lower()
        tokens = nltk.word_tokenize(text)
        # print(tokens)
        stop = stopwords.words('english') + list(string.punctuation)
        woorden = []
        for token in tokens:
            if token not in stop:
                woorden.append(token)
        # print(woorden)
        stemmer = nltk.stem.PorterStemmer()
        singles = [stemmer.stem(woord) for woord in woorden]
        # print(singles)
        return singles
