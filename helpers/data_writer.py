class DataWriter:
    @staticmethod
    def write_forum_to_file(forum, file_uri):
        file = open('./data_out/' + file_uri + '.relevancy', 'w')
        for thread in forum.threads:
            for comment in thread.comments:
                file.write("%-10s %-15s %-30s %s \n" % (thread.question.question_id, comment.comment_id,
                                                        comment.rankvalue, comment.relevance))
        file.close()
