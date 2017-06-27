import sys

from models import Dataset

def main(infile):

	# LOAD TRAIN SET
	dataset_train = Dataset.DatasetReview()
	dataset_train.load_review_from_csv(infile)

	dataset_train.export_only_contents("sentences_new.txt")

	# fe = BagFeatureExtractor(dataset.get_contents())
	# fe.build()
	# fe.save_vocab("../Test/vocab.txt")

	dataset_train.export_formatted_dataset("formatted_dataset_wow.tsv")


if __name__ == '__main__':
	main(sys.argv[1])
