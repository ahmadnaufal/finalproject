from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from FeatureExtractor import FeatureExtractor


class BagFeatureExtractor(FeatureExtractor):
    """docstring for FeatureExtractor"""
    def __init__(self, dataset, size=0):
        super(BagFeatureExtractor, self).__init__(dataset)
        self.size = size

    def build(self):
        self.vectorizer = CountVectorizer()
        self.vectorizer.fit(self.dataset)
        return self

    def extract_features(self, dataset):
        features = super(BagFeatureExtractor, self).extract_features(dataset)
        if self.size > 0:
            svd = TruncatedSVD(n_components=self.size)
            return svd.fit_transform(features)
        else:
            return features

    def get_name(self):
        return "Bag of Words"
