import sys
import os

class DocumentCombiner(object):
	"""docstring for DocumentCombiner"""
	def __init__(self, dirname):
		super(DocumentCombiner, self).__init__()
		self.dirname = dirname

	def do_combine(self, outfile):
		with open(outfile, "wb") as combined:
			for fname in os.listdir(self.dirname):
				with open(os.path.join(self.dirname, fname), "rb") as lines:
					combined.writelines(lines)
