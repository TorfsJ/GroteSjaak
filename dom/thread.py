

class Thread:
    def __init__(self, question):
        # document
        self.comments = []
        self.question = question

    def add_comment(self, comment):
        self.comments.append(comment)

    def make_models(self):
        self.question.make_model()
        for comment in self.comments:
            comment.make_model()
