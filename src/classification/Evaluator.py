from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

from FeatureExtractor import FeatureExtractor
from Classifier import Classifier

from models import Dataset

class Evaluator(object):
	"""docstring for Evaluator"""
	def __init__(self, model):
		super(Evaluator, self).__init__()
		if isinstance(model, Classifier):
			self.model = model
		else:
			raise Exception

	def eval_with_training_set(self, training_set):
		# training_set must be type of Dataset
		training_contents = training_set.get_contents()
		training_labels = training_set.get_labels()
		fe_bag = FeatureExtractor(training_contents)
		
		# BAG_OF_WORDS
		fe_bag.build_bag()
		training_features = fe_bag.extract_features(training_contents)

		# build training models
		self.model.classify_raw(training_features, training_labels)

		# start evaluating with training set
		test_predictions = self.model.test_raw(training_features)

		print "Evaluation method: Training set"
		self.print_evaluation(fe_bag, training_labels, test_predictions)

	def eval_with_test_set(self, training_set, test_set):
		training_contents = training_set.get_contents()
		training_labels = training_set.get_labels()
		fe_bag = FeatureExtractor(training_contents)
		
		# BAG_OF_WORDS
		fe_bag.build_bag()
		training_features = fe_bag.extract_features(training_contents)

		# build training models
		self.model.classify_raw(training_features, training_labels)

		# start evaluating with test set
		test_contents = test_set.get_contents()
		test_labels = test_set.get_labels()
		test_features = fe_bag.extract_features(test_contents)
		test_predictions = self.model.test_raw(test_features)

		print "Evaluation method: Test set"
		self.print_evaluation(fe_bag, test_labels, test_predictions)

	def print_evaluation(self, feature_extractor, test_labels, test_predictions):
		print "\n***** CLASSIFIER PROPERTIES *****"
		print "Classifier model name: %s" % (self.model.get_classifier_type())
		print "Feature Extractor: %s" % (feature_extractor.get_name())

		print "\n***** TEST SET PROPERTIES *****"
		print "Total Size: %d" % (len(test_labels))
		print "Positive instances: %d" % (sum([1 for x in test_labels if x == 'positive']))
		print "Negative instances: %d" % (sum([1 for x in test_labels if x == 'negative']))

		print "\n***** PREDICTED LABELS PROPERTIES *****"
		print "Predicted positive instances: %d" % (sum([1 for x in test_predictions if x == 'positive']))
		print "Predicted negative instances: %d" % (sum([1 for x in test_predictions if x == 'negative']))

		print "\n** EVALUATIONS **"
		print "Accuracy score: %f" % (accuracy_score(test_labels, test_predictions))

		pos_f1 = f1_score(test_labels, test_predictions, pos_label='positive')
		neg_f1 = f1_score(test_labels, test_predictions, pos_label='negative')
		print "F1 positive score: %f" % (f1_score(test_labels, test_predictions, pos_label='positive'))
		print "F1 negative score: %f" % (f1_score(test_labels, test_predictions, pos_label='negative'))
		print "Average F-measure: %f" % ((pos_f1 + neg_f1) / 2)
