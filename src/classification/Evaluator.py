from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

from Classifier import Classifier

from models import Dataset

class Evaluator(object):
	"""docstring for Evaluator"""
	def __init__(self):
		super(Evaluator, self).__init__()

	def eval_with_training_set(self, model, feature_extractor, training_set):
		# training_set must be type of Dataset
		training_contents = training_set.get_contents()
		training_labels = training_set.get_labels()
		
		# build features
		feature_extractor.build()
		training_features = feature_extractor.extract_features(training_contents)

		# build training models
		model.classify_raw(training_features, training_labels)

		# start evaluating with training set
		test_predictions = model.test_raw(training_features)

		print "Evaluation method: Training set"
		self.print_evaluation(model, feature_extractor, training_labels, test_predictions)

	def eval_with_test_set(self, model, feature_extractor, training_set, test_set):
		training_contents = training_set.get_contents()
		training_labels = training_set.get_labels()
		
		# build training features
		feature_extractor.build()
		training_features = fe_bag.extract_features(training_contents)

		# build training models
		model.classify_raw(training_features, training_labels)

		# start evaluating with test set
		test_contents = test_set.get_contents()
		test_labels = test_set.get_labels()
		test_features = fe_bag.extract_features(test_contents)
		test_predictions = model.test_raw(test_features)

		print "Evaluation method: Test set"
		self.print_evaluation(model, feature_extractor, test_labels, test_predictions)

	def eval_with_cross_validation(self, model, feature_extractor, training_set, num_fold=10):
		training_contents = training_set.get_contents()
		training_labels = training_set.get_labels()

		# build training features
		feature_extractor.build()
		training_features = feature_extractor.extract_features(training_contents)

		# start evaluating with cross validation and f1_score
		scores = cross_val_score(model.classifier, training_features, training_labels, cv=num_fold, scoring='f1_macro')

		print "Evaluation method: Cross Validation"
		print "Number of Folds: %d" % (num_fold)
		print "Using F1 Macro\n"

		for i in xrange(0, len(scores)):
			print "Iteration %d = %f" % (i + 1, scores[i])

		print "Average score: %f" % (scores.mean())

	def print_evaluation(self, model, feature_extractor, test_labels, test_predictions):
		print "\n***** CLASSIFIER PROPERTIES *****"
		print "Classifier model name: %s" % (model.get_classifier_type())
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

		print "F1 positive score: %f" % (f1_score(test_labels, test_predictions, pos_label='positive'))
		print "F1 negative score: %f" % (f1_score(test_labels, test_predictions, pos_label='negative'))
		print "Average F-measure: %f" % (f1_score(test_labels, test_predictions, average='macro'))

		# evaluate confusion matrix
		cnf_matrix = confusion_matrix(test_labels, test_predictions, labels=['positive', 'negative'])
		print "\nConfusion Matrix:"
		print "\t\tPositive\tNegative (predicted labels)"
		print "Positive\t%d\t\t%d" % (cnf_matrix[0][0], cnf_matrix[0][1])
		print "Negative\t%d\t\t%d" % (cnf_matrix[1][0], cnf_matrix[1][1])
		print "(actual labels)\n"
