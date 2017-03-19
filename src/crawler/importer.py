def main():
	i = 0
	lines = []
	with open("/media/ahmadnaufal/Data/idwiki-20160407-pages-meta-history.xml")	as infile:
		for line in infile:
			lines.append(line)
			i += 1
			if i > 50000:
				break

	with open("res", "wb") as outfile:
		for line in lines:
			outfile.write(line)

if __name__ == '__main__':
	main()