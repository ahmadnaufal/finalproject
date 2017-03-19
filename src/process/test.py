import sys

def main(filepath, num_pages=30):
	with open("outfile.xml", "wb") as outfile:
		with open(filepath, "rb") as infile:
			i = 0
			for line in infile:
				if line.strip() == "</page>":
					i += 1
				outfile.write(line)

				if i >= num_pages:
					outfile.write("</mediawiki>")
					break

if __name__ == '__main__':
	main(sys.argv[1], int(sys.argv[2]))
