import sklearn
import sys

from sklearn import metrics

from FeatureExtractor import FeatureExtractor 
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

class Classifier(object):
	"""docstring for Classifier"""
	def __init__(self, models="multinomial"):
		super(Classifier, self).__init__()
		if models == "multinomial":
			self.classifier = MultinomialNB()
		elif models == "svm":
			self.classifier = SVC()

	def classify(self, dataset, labels):
		self.classifier = self.classifier.fit(dataset, labels)

	def test(self, dataset):
		predictions = self.classifier.predict(dataset)
		return predictions

def main(filename):
	fe = FeatureExtractor("tfidf", filename)
	fe.load_dataset()
	fe.load_labels()

	bow = fe.build_bag()
	bag = fe.build_tfidf()

	print "** Using Multinomial NB Models **"

	# TFIDF
	clf = Classifier(models="multinomial")
	clf.classify(bag, fe.raw_labels)

	preds = clf.test(bag)
	# for doc, cat in zip(fe.dataset, preds):
	# 	print "%r => %s" % (doc, cat)

	print "TFIDF accuracy score: %f" % (metrics.accuracy_score(fe.raw_labels, preds, normalize=True))

	# bag of words
	clf = Classifier(models="multinomial")
	clf.classify(bow, fe.raw_labels)
	preds = clf.test(bow)

	print "BOW accuracy score: %f" % (metrics.accuracy_score(fe.raw_labels, preds, normalize=True))

	print "\n** Using SVM **"

	# TFIDF
	clf = Classifier(models="svm")
	clf.classify(bag, fe.raw_labels)

	preds = clf.test(bag)
	# for doc, cat in zip(fe.dataset, preds):
	# 	print "%r => %s" % (doc, cat)

	print "TFIDF accuracy score: %f" % (metrics.accuracy_score(fe.raw_labels, preds, normalize=True))

	# bag of words
	clf = Classifier(models="svm")
	clf.classify(bow, fe.raw_labels)
	preds = clf.test(bow)

	print "BOW accuracy score: %f" % (metrics.accuracy_score(fe.raw_labels, preds, normalize=True))



if __name__ == '__main__':
	main(sys.argv[1])