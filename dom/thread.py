

class Thread:
    def __init__(self, question):
        # document
        self.comments = []
        self.sorted_comments = {}
        self.question = question

    def add_comment(self, comment):
        self.comments.append(comment)

    def make_models(self):
        self.question.make_model()
        for comment in self.comments:
            comment.make_model()

    def calculate_ranking(self, collection_model):
        weight_lambda = 0.5
        query_model = self.question.query_model
        for comment in self.comments:
            pq = 1
            for term in query_model.query_terms:
                # 0.5 * P(D) + 0.5 * P(C) (per query term, per comment)
                pd = comment.document_model.prob_document_given_query(term)
                pc = collection_model.prob_term(term)
                pqt = weight_lambda*pd + weight_lambda*pc
                pq = pq * pqt
            comment.rankvalue = pq

