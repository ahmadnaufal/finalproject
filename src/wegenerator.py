import sys
import os

from models import Dataset
from feature_extractor import WordEmbeddingFeatureExtractor
# DEFAULT PATHS


def main(train_set, output_path):

    # LOAD TRAIN SET
    dataset_train = Dataset.DatasetReview()
    dataset_train.load_review_from_csv(train_set)

    # LOAD TEST SET
    # dataset_test = Dataset.DatasetReview()
    # dataset_test.load_review_from_csv(test_set)

    # preprocessor = DatasetPreprocessor()
    # dataset = preprocessor.fold_cases_d(dataset)
    # dataset = preprocessor.remove_punctuations_d(dataset)
    # dataset = preprocessor.convert_numbers_d(dataset)

    # dataset.export_only_contents("../Test/dataset.txt")

    # fe = BagFeatureExtractor(dataset.get_contents())
    # fe.build()
    # fe.save_vocab("../Test/vocab.txt")

    # dataset.export_formatted_dataset("formatted_dataset_wow.tsv")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    fe = WordEmbeddingFeatureExtractor(dataset_train.get_contents(), dimen=300)
    fe.save_model_to_file(output_path + "vectors_full_300.txt", vocabfile=output_path + "vocab_full_300.txt", binary=False)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
