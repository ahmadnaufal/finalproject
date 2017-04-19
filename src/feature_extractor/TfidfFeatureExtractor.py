from sklearn.feature_extraction.text import TfidfVectorizer
from FeatureExtractor import FeatureExtractor

class TfidfFeatureExtractor(FeatureExtractor):
	"""docstring for FeatureExtractor"""
	def __init__(self, dataset):
		super(TfidfFeatureExtractor, self).__init__(dataset)

	def build(self):
		self.vectorizer = TfidfVectorizer()
		self.vectorizer.fit(self.dataset)
		return self
		
	def get_name(self):
		return "Term Frequency - Inverse Document Frequency"
