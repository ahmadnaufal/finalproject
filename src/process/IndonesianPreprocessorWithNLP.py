import sys

sys.path.append("../../lib/InaNLP.jar")
sys.path.append("../../lib/ipostagger.jar")

from IndonesianNLP import IndonesianPOSTagger
from IndonesianNLP import IndonesianSentenceFormalization

class IndonesianPreprocessorWithNLP(object):
	"""docstring for IndonesianPreprocessorWithNLP"""
	def __init__(self, arg):
		super(IndonesianPreprocessorWithNLP, self).__init__()
		self.arg = arg
	
	def formalize_sentence(self, sentence):
		formalizer = IndonesianSentenceFormalization()
		return formalizer.normalizeSentence(sentence)

	def convert_numbers(self, sentence):
        # we do convert numbers into a more general format
        # the format we are going to use is <number>
        line_t = re.sub("^\d+\s|\s\d+\s|\s\d+$", " <number> ", sentence)
        return line_t
