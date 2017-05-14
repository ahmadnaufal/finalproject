import sys

from models import Dataset
from classification.Evaluator import Evaluator
from classification.Classifier import Classifier
from feature_extractor import BagFeatureExtractor
from feature_extractor import TfidfFeatureExtractor
from feature_extractor import WordEmbeddingFeatureExtractor
from feature_extractor import SennaFeatureExtractor

# DEFAULT PATHS
train_set = "../res/train_set/sample_train_set.csv"
test_set = "../res/test_set/processed_test_set.csv"

wiki_w2v_model = "../res/trains/wiki/w2v/wikipedia_w2v_indo_model.txt"
sswe_w2v = "../res/trains/wiki/sswe_w2v/sswe_wikipedia_w2v_indo_model.txt"
sswe_senna_vectors = "../res/trains/wiki/sswe_senna/vectors_full_wow.txt"
sswe_senna_vocabs = "../res/trains/wiki/sswe_senna/vectors_full_wow.txt"

def main(infile):

	# LOAD TRAIN SET
	dataset_train = Dataset.DatasetReview()
	dataset_train.load_review_from_csv(train_set)

	# LOAD TEST SET
	dataset_test = Dataset.DatasetReview()
	dataset_test.load_review_from_csv(test_set)

	# preprocessor = DatasetPreprocessor()
	# dataset = preprocessor.fold_cases_d(dataset)
	# dataset = preprocessor.remove_punctuations_d(dataset)
	# dataset = preprocessor.convert_numbers_d(dataset)

	# dataset.export_only_contents("../Test/dataset.txt")

	# fe = BagFeatureExtractor(dataset.get_contents())
	# fe.build()
	# fe.save_vocab("../Test/vocab.txt")

	# dataset.export_formatted_dataset("formatted_dataset_wow.tsv")

	print "\n**** CROSS VALIDATION EVALUATION (CORPUS: WIKIPEDIA) ****\n"

	fe = BagFeatureExtractor(dataset_train.get_contents())
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_cross_validation(classifier, fe, dataset_train)

	fe = TfidfFeatureExtractor(dataset_train.get_contents())
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_cross_validation(classifier, fe, dataset_train)

	fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=wiki_w2v_model, binary=False, dimen=200)
	# fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_cross_validation(classifier, fe, dataset_train)

	fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile="vectors_full_wow.txt", binary=False, dimen=200)
	# fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_cross_validation(classifier, fe, dataset_train)

	fe = SennaFeatureExtractor(dataset_train.get_contents(), infile="../senna_vectors.txt", vocabfile="../senna_vocab.txt")
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_cross_validation(classifier, fe, dataset_train)

	print "\n**** TRAINING SET EVALUATION (CORPUS: WIKIPEDIA) ****\n"

	fe = BagFeatureExtractor(dataset_train.get_contents())
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_training_set(classifier, fe, dataset_train)

	fe = TfidfFeatureExtractor(dataset_train.get_contents())
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_training_set(classifier, fe, dataset_train)

	fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=wiki_w2v_model, binary=False, dimen=200)
	# fe.save_model_to_file("vectors_full_wow.txt", vocabfile="vocab_full_wow.txt", binary=False)
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_training_set(classifier, fe, dataset_train)

	fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile="vectors_full_wow.txt", binary=False, dimen=200)
	# fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_training_set(classifier, fe, dataset_train)

	fe = SennaFeatureExtractor(dataset_train.get_contents(), infile="../senna_vectors.txt", vocabfile="../senna_vocab.txt")
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_training_set(classifier, fe, dataset_train)

	print "TEST SET EVALUATION (CORPUS: WIKIPEDIA)"

	fe = BagFeatureExtractor(dataset_train.get_contents())
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

	fe = TfidfFeatureExtractor(dataset_train.get_contents())
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

	fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=wiki_w2v_model, binary=False, dimen=200)
	# fe.save_model_to_file("vectors_full_wow.txt", vocabfile="vocab_full_wow.txt", binary=False)
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

	fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile="vectors_full_wow.txt", binary=False, dimen=200)
	# fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

	fe = SennaFeatureExtractor(dataset.get_contents(), infile="../senna_vectors.txt", vocabfile="../senna_vocab.txt")
	classifier = Classifier(models="svm")
	ev = Evaluator()
	ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

	# fe = WordEmbeddingFeatureExtractor(dataset.get_contents(), dimen=200)
	# # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
	# classifier = Classifier(models="svm")
	# ev = Evaluator()
	# ev.eval_with_cross_validation(classifier, fe, dataset)

	# fe = WordEmbeddingFeatureExtractor(dataset.get_contents(), infile="vectors_full.txt", binary=False)
	# # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
	# classifier = Classifier(models="svm")
	# ev = Evaluator()
	# ev.eval_with_cross_validation(classifier, fe, dataset)

	# fe = SennaFeatureExtractor(dataset.get_contents(), infile="../senna_vectors.txt", vocabfile="../senna_vocab.txt")
	# classifier = Classifier(models="svm")
	# ev = Evaluator()
	# ev.eval_with_cross_validation(classifier, fe, dataset)

	# train_dataset, test_dataset = dataset.split_to_ratio(ratio=0.4)
	# ev = Evaluator(classifier)
	# ev.eval_with_test_set(train_dataset, test_dataset)


if __name__ == '__main__':
	main(sys.argv[1])
