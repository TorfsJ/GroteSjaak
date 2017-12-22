from model.query_model import QueryModel


class Question:
    def __init__(self, question_id, question_body):
        self.question_id = question_id,
        self.text = question_body
        self.query_model = 0

    def make_model(self):
        self.query_model = QueryModel(self.text)
