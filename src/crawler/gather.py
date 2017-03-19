import os
import csv

rootdir = "Review"

pos = 0
neg = 0
total = 0

with open("collective.csv", "wb") as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=['content', 'polarity'])
	writer.writeheader()

	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			filepath = subdir + os.sep + file
			
			with open(filepath, "rb") as f:
				rows = csv.DictReader(f)
				for row in rows:
					total += 1
					writer.writerow({'content':row['content'], 'polarity':row['polarity']})
					if row['polarity'] == 'positive':
						pos += 1
					else:
						neg += 1

print "Total instances: {0}".format(total)
print "Postive instances: {0} ({1}%)".format(pos, (float(pos)/total)*100)
print "Negative instances: {0} ({1}%)".format(neg, (float(neg)/total)*100)

# preprocess