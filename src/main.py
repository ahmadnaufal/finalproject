import sys

from models import Dataset

def main(infile):
	dataset = Dataset.DatasetReview()
	dataset.load_review_from_csv(infile)
	print dataset.get_dataset_size()

if __name__ == '__main__':
	main(sys.argv[1])