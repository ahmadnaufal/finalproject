import sys
import os
import re


class DocumentCombiner(object):
	"""docstring for DocumentCombiner"""
	def __init__(self, dirname):
		super(DocumentCombiner, self).__init__()
		self.dirname = dirname

	def do_combine(self, outfile):
		with open(outfile, "wb") as combined:
			for dirs in os.listdir(self.dirname):
				print dirs
				for fname in os.listdir(os.path.join(self.dirname, dirs)):
					with open(os.path.join(self.dirname, dirs, fname), "rb") as lines:
						for line in lines:
							if line[0] != '<' and line[0] != '\'' and line != "\n" and line[0] != '[':
								line = re.sub(r'<.*?>', "", line)
								combined.write(line)


def main(infile):
	dc = DocumentCombiner(infile)
	dc.do_combine(infile + "_out.txt")


if __name__ == '__main__':
	main(sys.argv[1])
