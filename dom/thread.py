class Thread:
    def __init__(self, question):
        # document
        self.comments = []
        self.question = question

    def add_comment(self, comment):
        self.comments.append(comment)
