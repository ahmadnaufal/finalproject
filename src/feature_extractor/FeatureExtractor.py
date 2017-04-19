class FeatureExtractor(object):
	"""docstring for FeatureExtractor"""
	def __init__(self, dataset):
		self.dataset = dataset
		self.vectorizer = None

	def extract_features(self, dataset):
		return self.vectorizer.transform(dataset)

	def get_feature_size(self):
		return len(self.vectorizer.get_feature_names())
