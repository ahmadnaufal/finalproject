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
                sentence = self.formalize_sentence(row["content"])
                sentence = self.convert_numbers(sentence)
                res = {'content':sentence, 'polarity':row['polarity']} 
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

    def extract_sentences_to_file(self, ofile):
        with open(ofile, "wb") as outfile:
            with open(self.infile, "rb") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    line_t = re.sub("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", "\n", row["content"])
                    outfile.write(line_t)


def main(infile, outfile):
    ip = IndonesianPreprocessorWithNLP(infile)
    # ip.extract_sentences_to_file(ofile=outfile)
    ip.formalizefile(ofile=outfile)

    ipt = IndonesianPreprocessorWithNLP(outfile)
    ipt.extract_sentences_to_file(ofile="sentences.txt")

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
