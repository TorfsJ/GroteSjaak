from dom.relevance import Relevance


class Comment:
    def __init__(self, relevance, comment_id, date, text):
        if relevance not in (Relevance.GOOD, Relevance.BAD):
            raise ValueError('Relevance is not valid!')
        self.relevance = relevance
        self.comment_id = comment_id
        self.date = date
        self.text = text
