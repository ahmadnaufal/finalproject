import requests
import codecs
import csv
import re
import os

from bs4 import BeautifulSoup
from review import Review

base_url = "https://www.tripadvisor.co.id"
root_url = "/Restaurants-g297704-Bandung_West_Java_Java.html"

review_hold = "Reviews"
page_hold = "g297704"	# specific for bandung only

def save_to_csv(results, filename):
	with codecs.open(filename + ".csv", "wb", encoding='utf-8') as csvfile:
		fieldnames = ['content','polarity']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for result in results:
			content = re.sub(r'[^\x00-\x7F]+',' ', result.content)
			content = content.replace("\n", " ").strip()
			content = re.sub('\.+', '.', content)
			content = ' '.join(content.split())
			writer.writerow({
				'content': content,
				'polarity': result.polarity,
			})

def main():
	r = requests.get(base_url + root_url)
	soup = BeautifulSoup(r.content, "html.parser")

	pages = int(soup.find("div", attrs={"class" : "pageNumbers"}).find_all()[-1].get("data-page-number"))

	print "Total: %d pages." % pages
	for j in xrange(pages):
		dir_name = "Review/" + str(j) + "/"
		print "restaurant in page %d:" % j
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)

		if j == 0:
			rows = soup.find_all('div', attrs={"class" : "listing"})
		else:
			pos = root_url.find(page_hold)
			new_root_url = root_url[:pos + len(review_hold)] + "-oa" + str(j*3) + "0-" + page_url[pos + len(review_hold):]
			rpg = requests.get(base_url + new_root_url)
			soup = BeautifulSoup(rpg.content, "html.parser")
			rows = soup.find_all('div', attrs={"class" : "listing"})

		for row in rows:
			list_review = []
			link = row.find("a", attrs={"class" : "property_title"})
			page_url = link.get("href")
			print page_url

			rp = requests.get(base_url + page_url)
			soup_r = BeautifulSoup(rp.content, "html.parser")

			page_div = soup_r.find("div", attrs={"class" : "pageNumbers"})
			if page_div is None:
				pagenum = 1
			else:
				pagenum = int(page_div.find_all()[-1].get("data-page-number"))
			
			for i in xrange(pagenum):
				print "page %d" % i
				if i == 0:
					reviews = soup_r.find_all('div', attrs={"class" : "review"})
				else:
					pos = page_url.find(review_hold)
					new_page_url = page_url[:pos + len(review_hold)] + "-or" + str(i) + "0-" + page_url[pos + len(review_hold):]
					rp = requests.get(base_url + new_page_url)
					soup_r = BeautifulSoup(rp.content, "html.parser")
					reviews = soup_r.find_all('div', attrs={"class" : "review"})

				for review in reviews:
					content = review.find("p", attrs={"class" : "partial_entry"}).getText()
					rating = review.find("img", attrs={"class" : "sprite-rating_s_fill"});
					num = rating.get("class")

					if num[-1] == "s50" or num[-1] == "s40" or num[-1] == "s30":
						polarity = "positive"
					elif num[-1] == "s10" or num[-1] == "s20":
						polarity = "negative"

					rev = Review(content, polarity)
					list_review.append(rev)

			save_to_csv(list_review, dir_name + page_url[1:-5])


if __name__ == '__main__':
	main()