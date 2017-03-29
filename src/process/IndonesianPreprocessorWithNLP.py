import sys
import csv
import re

sys.path.append("lib/InaNLP.jar")
sys.path.append("lib/ipostagger.jar")

from IndonesianNLP import IndonesianPOSTagger
from IndonesianNLP import IndonesianSentenceFormalization

class IndonesianPreprocessorWithNLP():

    def __init__(self, infile):
        self.infile = infile

    def formalize_sentence(self, sentence):
        formalizer = IndonesianSentenceFormalization()
        return formalizer.normalizeSentence(sentence)

    def convert_numbers(self, sentence):
        # we do convert numbers into a more general format
        # the format we are going to use is <number>
        line_t = re.sub("^\d+\s|\s\d+\s|\s\d+$", " <number> ", sentence)
        return line_t

    def formalizefile(self, ofile):
        preprocessed = []
        with open(self.infile, "rb") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                res = {'content':self.convert_numbers(self.formalize_sentence(row["content"])), 'polarity':row['polarity']} 
                preprocessed.append(res)

        with open(ofile, "wb") as csvfile:
            fieldnames = ['content', 'polarity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for rows in preprocessed:
                writer.writerow({
    				'content' : rows['content'],
    				'polarity' : rows['polarity']
    			})


def main(infile, outfile):
	ip = IndonesianPreprocessorWithNLP(infile)
	ip.formalizefile(ofile=outfile)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
