from helpers.text_preprocessor import PreProcessor


class QueryModel:
    def __init__(self, text):
        self.query_terms = PreProcessor.processText(text)
