#http://web.archive.org/web/20080601093347/http://www.w3f.com/midi/

"""
Note: a lot of the files themselves are not archived, so you will see
a lot of "Not found" messages. Some of the genres are all there, others
are entirely not there.
"""

import requests
import urllib
from bs4 import BeautifulSoup
import os

USER_AGENT = 'curl/7.54.0'
HEADERS = {'user-agent':USER_AGENT}

url = "http://web.archive.org/web/20080601093347/http://www.w3f.com/midi/"
CATEGORIES = ["christmas", "country", "new", "newyears", "rock", "pop"]

for genre in CATEGORIES:
	os.mkdir(genre)
	print("Genre:", genre)
	response = requests.get(url + genre, headers=HEADERS)
	if response.status_code != 200:
		print("Unable to get page")
		continue
	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	links = soup.find_all('a')
	for link in links:
		suffix = link.text[-3:]
		if suffix == "mid":
			try:
				urllib.request.urlretrieve(link.get('href'), "./" + genre + "/" + link.text)
				print("Downloading " + link.text, end="\r")
			except urllib.error.HTTPError:
				print(link.text, " not found")
				continue
