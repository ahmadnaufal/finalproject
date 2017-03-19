import gensim

from SentenceIterator import SentenceIterator

class WordEmbeddingGenerator(object):
    """
    Create a new word embedding generator
    we can use the wikipedia to sentences
    """
    def __init__(self, path_to_corpus):
        super(WordEmbeddingGenerator, self).__init__()
        self.file_corpus = path_to_corpus

    def create_word_embedding(self, type="w2v"):
        #tokenize the sentence
        #create the word embedding using gensim's word2vec and collobert's c&w
        if type == "w2v":
            sentences = SentenceIterator(self.file_corpus)
            self.model = gensim.models.Word2Vec(sentences)
        elif type == "c&w":
            # TODO: unimplemented yet, because still cant found the C&W algo
            pass
        else:
            pass

    def save_model(self, filename):
        self.model.save(filename)
