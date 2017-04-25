import re

from models.Review import Review


class Preprocessor(object):
	"""docstring for DatasetPreprocessor"""
	def convert_numbers(self, sentence):
		line_t = re.sub("^\d+\s|\s\d+\s|\s\d+$", " <number> ", sentence)
		return line_t

	def remove_punctuations(self, sentence):
		line_t = re.sub(r'[!@#$().,?":\';]', "", sentence)
		line_t = re.sub(r'\\', " per ", line_t)
		line_t = re.sub(r'/', " per ", line_t)
		line_t = re.sub(r'&', " dan ", line_t)
		line_t = re.sub(r'%', " persen ", line_t)
		line_t = " ".join(line_t.split())
		return line_t

	def fold_cases(self, sentence):
		line_t = sentence.lower()
		return line_t


class ReviewPreprocessor(Preprocessor):
	"""docstring for ReviewPreprocessor"""
	def __init__(self):
		super(ReviewPreprocessor, self).__init__()

	def remove_punctuations_r(self, review):
		new_content = self.remove_punctuations(review.content)
		new_label = review.polarity
		return Review(new_content, new_label)

	def fold_cases_r(self, review):
		new_content = self.fold_cases(review.content)
		new_label = review.polarity
		return Review(new_content, new_label)

	def convert_numbers_r(self, review):
		new_content = self.convert_numbers(review.content)
		new_label = review.polarity
		return Review(new_content, new_label)


class DatasetPreprocessor(ReviewPreprocessor):
	"""docstring for DatasetPreprocessor"""
	def __init__(self):
		super(DatasetPreprocessor, self).__init__()

	def remove_punctuations_d(self, dataset):
		reviews = []
		for review in dataset.dataset:
			new_review = self.remove_punctuations_r(review)
			reviews.append(new_review)

		dataset_new = dataset.dataset_from_array(reviews)
		return dataset_new

	def fold_cases_d(self, dataset):
		reviews = []
		for review in dataset.dataset:
			new_review = self.fold_cases_r(review)
			reviews.append(new_review)

		dataset_new = dataset.dataset_from_array(reviews)
		return dataset_new

	def convert_numbers_d(self, dataset):
		reviews = []
		for review in dataset.dataset:
			new_review = self.convert_numbers_r(review)
			reviews.append(new_review)

		dataset_new = dataset.dataset_from_array(reviews)
		return dataset_new
