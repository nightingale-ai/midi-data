#https://www.mfiles.co.uk/midi-traditional.htm/

import requests
import urllib
from bs4 import BeautifulSoup
import os

USER_AGENT = 'curl/7.54.0'
HEADERS = {'user-agent': USER_AGENT}

n = 0

url = "https://www.mfiles.co.uk/midi-traditional.htm/"
url2 = "https://www.mfiles.co.uk/"
response = requests.get(url, headers=HEADERS)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
categories = soup.find_all("div", {"class" : "cnt_inr"})
for category in categories:
	h2 = category.find("h2").text
	os.mkdir("./" + h2)
	links = category.find_all("a")
	for link in links:
		suffix = link.get('href')[-3:]
		if suffix == "mid" and link.text != "edit/play midi file":
			try:
				urllib.request.urlretrieve(url2 + link.get('href'), h2 + "/" + str(n) + ".mid")
				print("Downloading " + str(n) + ".mid / " + str(len(links)), end="\r")
				n += 1
			except urllib.error.HTTPError:
				print(link.text, " not found")
				continue
