import gensim

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from src.process import WordEmbeddingGenerator

class WordEmbeddingFeatureExtractor(object):
	"""docstring for WordEmbeddingFeatureExtractor"""
	def __init__(self, dataset=None):
		super(WordEmbeddingFeatureExtractor, self).__init__()
		self.dataset = dataset

	def load_dataset(self, dataset):
		self.dataset = dataset

	def build_feature_from_file(self, inmodel):
		raw_model = WordEmbeddingGenerator()
		raw_model.load_model(inmodel, binary=False)

