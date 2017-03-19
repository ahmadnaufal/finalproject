import csv
import sys

sys.path.append("../../lib/InaNLP.jar")
sys.path.append("../../lib/ipostagger.jar")

from IndonesianNLP import IndonesianPOSTagger
from IndonesianNLP import IndonesianSentenceFormalization

def formalizeSentence(sentence):
	formalizer = IndonesianSentenceFormalization()
	return formalizer.normalizeSentence2(sentence)

def posTagger(sentence):
	InaPosTagger = IndonesianPOSTagger()
	return InaPosTagger.doPOSTag(sentence)

def main(fin="collective.csv", fout="tagged.csv"):
	pos = 0
	neg = 0
	total = 0
	with open(fout, "wb") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['content', 'adjectives', 'polarity'])
		writer.writeheader()

		with open(fin, "rb") as colls:
			rows = csv.DictReader(colls)
			for row in rows:
				adjs = []
				total += 1
				sentence = formalizeSentence(row['content'])
				sentence_pos = posTagger(sentence)
				for post in sentence_pos:
					if post[1] == "JJ":
						adjs.append(post[0])

				writer.writerow({'content':sentence, 'adjectives':adjs, 'polarity':row['polarity']})
				if row['polarity'] == 'positive':
					pos += 1
				else:
					neg += 1

	print "Total instances: {0}".format(total)
	print "Postive instances: {0} ({1}%)".format(pos, (float(pos)/total)*100)
	print "Negative instances: {0} ({1}%)".format(neg, (float(neg)/total)*100)		

if __name__ == '__main__':
	main()