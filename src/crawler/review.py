class Review(object):
	"""docstring for Review"""
	def __init__(self, content, polarity):
		super(Review, self).__init__()
		self.content = content
		self.polarity = polarity

	def to_string():
		return self.content + "\t" + self.polarity