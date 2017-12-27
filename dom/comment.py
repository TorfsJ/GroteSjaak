from model.document_model import DocumentModel


class Comment:
    def __init__(self, relevance, text, comment_id):
        self.document_model = 0
        self.comment_id = comment_id
        if relevance.lower() == "good":
            self.relevance = "good"
        else:
            self.relevance = "bad"
        self.text = text
        self.rankvalue = -1

    def make_model(self):
        self.document_model = DocumentModel(self.text)
