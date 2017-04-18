import gensim

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from WordEmbeddingVectorizer import WordEmbeddingVectorizer

from process.SentenceIterator import SentenceIterator

class FeatureExtractor(object):
	"""docstring for FeatureExtractor"""
	def __init__(self, dataset):
		self.dataset = dataset
		self.vectorizer = None
		self.name = ""

	def build_bag(self):
		self.name = "Bag of Words"
		self.vectorizer = CountVectorizer()
		self.vectorizer.fit(self.dataset)

		return self

	def build_tfidf(self):
		self.name = "Term Frequency-Inverse Document Frequency"
		self.vectorizer = TfidfVectorizer()
		self.vectorizer.fit(self.dataset)

		return self

	def build_w2v_features(self, input_from='create', binary=False, infile=None):
		self.name = "Gensim Word2Vec"
		if input_from == "create":
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

	def build_sswe_features(self, input_from='create', binary=False, infile=None):
		# TODO: create model based on SSWE features
		pass

	def extract_features(self, dataset):
		return self.vectorizer.transform(dataset)

	def get_feature_size(self):
		return len(self.vectorizer.get_feature_names())

	def get_name(self):
		return self.name
