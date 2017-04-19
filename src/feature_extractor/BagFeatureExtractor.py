from sklearn.feature_extraction.text import CountVectorizer
from FeatureExtractor import FeatureExtractor

class BagFeatureExtractor(FeatureExtractor):
	"""docstring for FeatureExtractor"""
	def __init__(self, dataset):
		super(BagFeatureExtractor, self).__init__(dataset)

	def build(self):
		self.vectorizer = CountVectorizer()
		self.vectorizer.fit(self.dataset)
		return self

	def get_name(self):
		return "Bag of Words"
