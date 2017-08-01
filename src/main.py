from models import Dataset
from classification.Evaluator import Evaluator
from classification.Classifier import Classifier
from feature_extractor import TfidfFeatureExtractor
from feature_extractor import WordEmbeddingFeatureExtractor
from feature_extractor import SennaFeatureExtractor

from sklearn.model_selection import KFold

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

    fe_tfidf = TfidfFeatureExtractor(size=500)
    fe_w2v = WordEmbeddingFeatureExtractor(infile=w2v_vec_path, binary=False, dimen=500)
    fe_sswe_w2v = WordEmbeddingFeatureExtractor(infile=sswe_w2v, binary=False, dimen=500, sswe=1)
    fe_sswe = SennaFeatureExtractor(infile=sswe_senna_vectors, vocabfile=sswe_senna_vocabs, dimen=500)

    feature_extractors = [fe_tfidf, fe_w2v, fe_sswe_w2v, fe_sswe]

    ev = Evaluator()

    print "\n**** CROSS VALIDATION EVALUATION (CORPUS: DATASET) ****\n"
    model = Classifier(models="nn")

    kfold = KFold(n_splits=10)
    ev.eval_with_cross_validation(model, feature_extractors=feature_extractors,
                                    training_set=dataset_train, num_fold=10, cv=kfold)

    model = Classifier(models="nn")
    ev.create_evaluation_result(model, feature_extractors=feature_extractors,
                                    training_set=dataset_train, num_fold=10, cv=kfold)

    print "\n**** TEST SET EVALUATION (CORPUS: DATASET) ****\n"
    model = Classifier(models="nn")
    ev.eval_with_test_set(model, feature_extractors=feature_extractors,
                            training_set=dataset_train,
                            test_set=dataset_test)

if __name__ == '__main__':
    main()
