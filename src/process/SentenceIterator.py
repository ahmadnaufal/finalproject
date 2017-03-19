class SentenceIterator(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename) as sentences:
            for sentence in sentences:
                yield sentence.split()

