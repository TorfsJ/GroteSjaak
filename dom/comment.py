class Comment:
    def __init__(self, relevance, text, comment_id):
        self.comment_id = comment_id
        if relevance.lower() == "good":
            self.relevance = "good"
        else:
            self.relevance = "bad"
        self.text = text
