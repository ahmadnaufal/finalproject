import sys
import re
from DocumentCombiner import DocumentCombiner

# sys.path.append("../../lib/InaNLP.jar")
# sys.path.append("../../lib/ipostagger.jar")

# from IndonesianNLP import IndonesianPOSTagger
# from IndonesianNLP import IndonesianSentenceFormalization

class IndonesianPreprocessor(object):
    """docstring for IndonesianPreprocessor"""
    def __init__(self):
        super(IndonesianPreprocessor, self).__init__()

    def parse_sentence(self, infile, outfile):
        # regex to parse sentence
        with open(outfile, "wb") as write_lines:
            with open(infile, "rb") as lines:
                for line in lines:
                    line_t = re.sub("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", "\n", line)
                    write_lines.write(line_t)

    def clean_file(self, infile, outfile):
        # cleaning the file:
        # remove non ascii characters
        pass

    def clean_punctuations(self, infile, outfile):
        # membersihkan tanda baca dari teks yang telah didapat
        with open(outfile, "wb") as write_lines:
            with open(infile, "rb") as lines:
                for line in lines:
                    line_t = re.sub(r'[!@#$().,?":;]', "", line)
                    write_lines.write(line_t)

    def create_plain_text(self, infile, outfile):
        # create plain text from simple format of wiki
        # do: get text inside <doc> tag removing titles
        with open(outfile, "wb") as write_lines:
            with open(infile, "rb") as lines:
                for line in lines:
                    if line.find("<doc") == -1 and line.find("</doc>") == -1:
                        if is_title is True:
                            is_title = False
                        else:
                            if len(line.split()) > 3 and line[0] != '"':
                                line_t = re.sub(r'\([^)]*\)', '', line)
                                write_lines.write(line_t)
                    elif line.find("<doc") > -1:
                        is_title = True

    def convert_numbers(self, infile, outfile):
        # we do convert numbers into a more general format
        # the format we are going to use is <number>
        with open(outfile, "wb") as write_lines:
            with open(infile, "rb") as lines:
                for line in lines:
                    line_t = re.sub("^\d+\s|\s\d+\s|\s\d+$", " <number> ", line)
                    write_lines.write(line_t)

    def fold_case(self, infile, outfile):
        # fold all cases... this is optional
        # because sometimes, we need cases for NE Tagging
        with open(outfile, "wb") as write_lines:
            with open(infile, "rb") as lines:
                for line in lines:
                    line_t = line.lower()
                    write_lines.write(line_t)


def main():
    dc = DocumentCombiner("../../output/AA")
    dc.do_combine("../../output/COMBINED.xml")

    ip = IndonesianPreprocessor()
    ip.create_plain_text("../../output/COMBINED.xml", "../../output/aftercleaned.txt")
    ip.parse_sentence("../../output/aftercleaned.txt", "../../output/aftercleaned_1.txt")
    ip.clean_punctuations("../../output/aftercleaned_1.txt", "../../output/aftercleaned_2.txt")
    ip.convert_numbers("../../output/aftercleaned_2.txt", "../../output/aftercleaned_3.txt")

if __name__ == '__main__':
    main()