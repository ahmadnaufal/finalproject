class IndonesianPreprocessor(object):
    """docstring for IndonesianPreprocessor"""
    def __init__(self):
        super(IndonesianPreprocessor, self).__init__()

    def parse_sentence(self, infile, outfile):
        # regex to parse sentence

    def clean_file(self, infile, outfile):
        # cleaning the file:
        # remove non ascii characters

    def create_plain_text(self, infile, outfile):
        # create plain text from simple format of wiki
        # do: get text inside <doc> tag removing titles
    
    def convert_numbers(self, infile, outfile):
        # we do convert numbers into a more general format
        # the format we are going to use is <number>
        with open(infile, "rb") as lines:
            for line in lines:
                line_t = re.sub("^\d+\s|\s\d+\s|\s\d+$", "<number>", line)                
    
    def fold_case(self, infile, outfile):
        # fold all cases... this is optional
        # because sometimes, we need cases for NE Tagging
    

