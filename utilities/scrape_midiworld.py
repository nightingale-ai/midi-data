#https://www.midiworld.com/

import requests
import urllib
from bs4 import BeautifulSoup
import sys

CATEGORIES = [
	"classic",
	"pop",
	"rock",
	"rap",
	"dance",
	"punk",
	"blues",
	"country",
	"movie themes",
	"tv themes",
	"christmas carols",
	"video game themes",
	"disney themes",
	"national anthems",
	"jazz",
	"hip-hop"
]

def error(*msg, displayGenres=False):
	print(*msg)
	if(displayGenres):
		print("Available genres:\n *", "\n * ".join(CATEGORIES))
	exit(1)

def scrape(genre):
	genre = urllib.parse.quote(genre)

	USER_AGENT = 'curl/7.54.0' # why not lmfao
	HEADERS = {'user-agent': USER_AGENT}

	i = 1
	j = 1
	pageExists = True
	while pageExists:
		url = "https://www.midiworld.com/search/" + str(i) + "/?q=" + genre
		response = requests.get(url, headers=HEADERS)
		pageExists = (response.status_code == 200)
		if not pageExists:
			continue

		html = response.text
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.find_all('a'):
			if link.text == "download":
				fn = genre + "-" + str(i) + "-" + str(j) + ".midi"
				try: urllib.request.urlretrieve(link.get('href'), fn)
				except urllib.error.HTTPError:
					continue
				print("* Downloading", fn, end="\r")
				j += 1

		print()
		i += 1
		j = 0

def main():
	if len(sys.argv) != 2:
		error("Usage:", sys.argv[0], "<genre>", displayGenres=True)
	else:
		if sys.argv[1] not in CATEGORIES:
			error("No such genre.", displayGenres=True)
		else:
			scrape(sys.argv[1])
try:
	main()
except KeyboardInterrupt:
	exit(0)
