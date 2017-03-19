import csv

filename = "collective.csv"
sample_result = "sample.csv"


def main():
	max_pos = 70
	max_neg = 70
	
	with open(sample_result, "wb") as csv_sample:
		samplewriter = csv.DictWriter(csv_sample, fieldnames=['content','polarity'])
		samplewriter.writeheader()

		with open(filename, "rb") as csvfile:
			rows = csv.DictReader(csvfile)
			for row in rows:
				if row['polarity'] == 'positive' and max_pos > 0:
					samplewriter.writerow({'content':row['content'], 'polarity':row['polarity']})
					max_pos -= 1
				elif row['polarity'] == 'negative' and max_neg > 0:
					samplewriter.writerow({'content':row['content'], 'polarity':row['polarity']})
					max_neg -= 1

if __name__ == '__main__':
	main()
