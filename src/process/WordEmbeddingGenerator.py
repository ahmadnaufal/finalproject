import gensim
import sys

from SentenceIterator import SentenceIterator

class WordEmbeddingGenerator(object):
    """
    Create a new word embedding generator
    we can use the wikipedia to sentences
    """
    def __init__(self, path_to_corpus=""):
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

    def save_model(self, filename, binary=True):
        if binary:
            self.model.save(filename)
        else:
            self.model.save_word2vec_format(filename, binary=False)

    def load_model(self, filename, binary=True):
        if binary:
            self.model = gensim.models.Word2Vec.load(filename)
        else:
            self.model = gensim.models.Word2Vec.load_word2vec_format(filename, binary=False)

def main(infile):
    we = WordEmbeddingGenerator(infile)
    we.create_word_embedding(type="w2v")
    we.save_model("w2v_model", binary=False)

    # we.load_model("w2v_model")
    # print we.model.wv.most_similar(positive=['enak'])

if __name__ == '__main__':
    main(sys.argv[1])
