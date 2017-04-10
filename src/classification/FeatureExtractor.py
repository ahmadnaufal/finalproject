from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import csv
import sys

class FeatureExtractor(object):
	"""docstring for FeatureExtractor"""
	def __init__(self, type, infile):
		super(FeatureExtractor, self).__init__()
		self.type = type
		self.dataset = []
		self.labels = []
		self.raw_labels = []
		self.infile = infile

	def load_file(self, infile):
		self.infile = infile

	def load_dataset(self, infile="", sample=-1, column_name='content', labels_column_name='polarity'):
		if infile == "":
			infile = self.infile

		with open(infile, "rb") as f:
			reader = csv.DictReader(f)
			if sample == -1:
				for rows in reader:
					self.dataset.append(rows[column_name])
					self.raw_labels.append(rows[labels_column_name])
			else:
				i = 0
				for rows in reader:
					if i >= sample:
						break;
					else:
						self.dataset.append(rows[column_name])
						self.raw_labels.append(rows[labels_column_name])
						i += 1

	def load_labels(self, infile="", column_name='polarity'):
		if infile == "":
			infile = self.infile

		with open(infile, "rb") as f:
			reader = csv.DictReader(f)
			for rows in reader:
				if self.labels.count(rows[column_name]) == 0:
					self.labels.append(rows[column_name])

	def build_bag(self):
		self.count_vect = CountVectorizer()
		bag = self.count_vect.fit_transform(self.dataset)
		print "Bag dimensions: " + str(bag.shape)
		return bag

	def build_tfidf(self):
		bag = self.build_bag()
		tfidf_transformer = TfidfTransformer()
		tfidf = tfidf_transformer.fit_transform(bag)
		print "TFIDF bag dimensions: " + str(tfidf.shape)
		return tfidf

	def get_vocab_file(self):
		if self.count_vect is not None:
			return self.count_vect.get_feature_names()
		else:
			return []

	def export_vocab_file(self, outfile):
		with open(outfile, "wb") as vocab_file:
			res = self.get_vocab_file()
			for row in res:
				vocab_file.write(row + "\n")


def main(filename):
	fe = FeatureExtractor("tfidf", filename)
	fe.load_dataset()
	fe.load_labels()

	bag = fe.build_bag()
	fe.export_vocab_file("vocab.txt")

if __name__ == '__main__':
	main(sys.argv[1])

