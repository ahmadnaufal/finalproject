import gensim

from FeatureExtractor import FeatureExtractor
from vectorizer.WordEmbeddingVectorizer import WordEmbeddingVectorizer

from models.SentenceIterator import SentenceIterator

class WordEmbeddingFeatureExtractor(FeatureExtractor):
	"""docstring for FeatureExtractor"""
	def __init__(self, dataset, infile=None, binary=False):
		super(WordEmbeddingFeatureExtractor, self).__init__(dataset)
		self.model_file = infile
		self.binary = binary

	def build(self):
		if not self.model_file:
			sentences = SentenceIterator(self.dataset)
			w2v = gensim.models.Word2Vec(sentences)
		elif input_from == "file":
			w2v = gensim.models.Word2Vec.load_word2vec_format(infile, binary)

		# build our word embedding model vectorizer
		w2v_dict = dict(zip(w2v.index2word, w2v.syn0))
		sentences = SentenceIterator(self.dataset)

		self.vectorizer = WordEmbeddingVectorizer(w2v_dict)
		self.vectorizer.fit(sentences)

		return self

	def save_model_to_file(self, outfile, vocabfile=None, binary=True):
		sentences = SentenceIterator(self.dataset)
		w2v = gensim.models.Word2Vec(sentences)

		w2v.save_word2vec_format(outfile, fvocab=vocabfile, binary=binary)
		
	def get_name(self):
		return "Gensim Word2Vec"
