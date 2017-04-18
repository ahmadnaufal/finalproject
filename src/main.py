import sys

from models import Dataset
from classification.Evaluator import Evaluator
from classification.Classifier import Classifier

def main(infile):
	dataset = Dataset.DatasetReview()
	dataset.load_review_from_csv(infile)

	classifier = Classifier(models="svm")
	ev = Evaluator(classifier)
	ev.eval_with_training_set(dataset)

	train_dataset, test_dataset = dataset.split_to_ratio(ratio=0.4)
	ev = Evaluator(classifier)
	ev.eval_with_test_set(train_dataset, test_dataset)

if __name__ == '__main__':
	main(sys.argv[1])