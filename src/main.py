import sys

from models import Dataset
from classification.Evaluator import Evaluator
from classification.Classifier import Classifier
from feature_extractor import BagFeatureExtractor
from feature_extractor import TfidfFeatureExtractor
from feature_extractor import WordEmbeddingFeatureExtractor
from feature_extractor import SennaFeatureExtractor

# DEFAULT PATHS
train_set = "../new_res/2017-06-19/train_set.csv"
test_set = "../new_res/2017-06-19/test_set.csv"

sswe_w2v = "../new_res/2017-06-19/sswe/vectors_full_500.txt"
sswe_senna_vectors = "../new_res/2017-06-19/sswe_new/vectors_full_500.txt"
sswe_senna_vocabs = "../new_res/2017-06-19/sswe_new/vocab_full_500.txt"

w2v_vec_path = "../new_res/2017-06-19/w2v/vectors_full_500.txt"
w2v_vocab_path = "../new_res/2017-06-19/w2v/vocab_full_500.txt"


def main():

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

    print "\n**** CROSS VALIDATION EVALUATION (CORPUS: DATASET) ****\n"

    # fe = BagFeatureExtractor(dataset_train.get_contents(), size=500)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = TfidfFeatureExtractor(dataset_train.get_contents(), size=500)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=w2v_vec_path, binary=False, dimen=500)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    # # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = SennaFeatureExtractor(dataset_train.get_contents(), infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = BagFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = TfidfFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=w2v_vec_path, binary=False, dimen=500)
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    # # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = SennaFeatureExtractor(dataset_train.get_contents(), infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = BagFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = TfidfFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=w2v_vec_path, binary=False, dimen=500)
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    # # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # fe = SennaFeatureExtractor(dataset_train.get_contents(), infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_cross_validation(classifier, fe, dataset_train)

    # print "TEST SET EVALUATION (CORPUS: DATASET)"

    fe = BagFeatureExtractor(dataset_train.get_contents(), size=500)
    classifier = Classifier(models="svm")
    ev = Evaluator()
    ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    fe = TfidfFeatureExtractor(dataset_train.get_contents(), size=500)
    classifier = Classifier(models="svm")
    ev = Evaluator()
    ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=w2v_vec_path, binary=False, dimen=500)
    classifier = Classifier(models="svm")
    ev = Evaluator()
    ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    # # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = SennaFeatureExtractor(dataset_train.get_contents(), infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)
    # classifier = Classifier(models="svm")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = BagFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = TfidfFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=w2v_vec_path, binary=False, dimen=500)
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    # # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = SennaFeatureExtractor(dataset_train.get_contents(), infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)
    # classifier = Classifier(models="rfc")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = BagFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = TfidfFeatureExtractor(dataset_train.get_contents())
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=w2v_vec_path, binary=False, dimen=500)
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    # # fe.save_model_to_file("vectors_full.txt", vocabfile="vocab_full.txt", binary=False)
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)

    # fe = SennaFeatureExtractor(dataset_train.get_contents(), infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)
    # classifier = Classifier(models="nn")
    # ev = Evaluator()
    # ev.eval_with_test_set(classifier, fe, dataset_train, dataset_test)


if __name__ == '__main__':
    main()
