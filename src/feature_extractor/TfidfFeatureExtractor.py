from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from FeatureExtractor import FeatureExtractor


class TfidfFeatureExtractor(FeatureExtractor):
    """docstring for FeatureExtractor"""
    def __init__(self, dataset, size=0):
        super(TfidfFeatureExtractor, self).__init__(dataset)
        self.size = size

    def build(self):
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(self.dataset)
        return self

    def extract_features(self, dataset):
        features = super(TfidfFeatureExtractor, self).extract_features(dataset)
        if self.size > 0:
            svd = TruncatedSVD(n_components=self.size)
            return svd.fit_transform(features)
        else:
            return features

    def get_name(self):
        return "Term Frequency - Inverse Document Frequency"
