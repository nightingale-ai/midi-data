#http://web.archive.org/web/20190525163802/http://www.profesordepiano.com/Real%20Book/Realbook.htm/

import requests
import urllib
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver

USER_AGENT = 'curl/7.54.0'
HEADERS = {'user-agent': USER_AGENT}

PATH_TO_ADBLOCK = "/home/josh/.config/chromium/Default/Extensions/cjpalhdlnbpafiamejdnhcphjbkeiagm/1.33.2_2"
DOWNLOAD_DIR = "/home/josh/midi-data/realbook/jazz"

WEBDRIVER_OPTIONS = webdriver.ChromeOptions()
WEBDRIVER_OPTIONS.add_argument("-load-extension=" + PATH_TO_ADBLOCK)
WEBDRIVER_OPTIONS.add_argument("-page_load_strategy=eager")
WEBDRIVER_OPTIONS.add_argument("--headless")
WEBDRIVER_OPTIONS.add_experimental_option("prefs",
	{"download.default_directory" : DOWNLOAD_DIR})

WEBDRIVER = webdriver.Chrome(options=WEBDRIVER_OPTIONS)

n = 0
url2 = "http://web.archive.org/web/20160424140513/http://profesordepiano.com/Real%20Book/"

url = "http://web.archive.org/web/20190525163802/http://www.profesordepiano.com/Real%20Book/Realbook.htm/"
response = requests.get(url, headers=HEADERS)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')
for link in links:
	suffix = link.get('href')[-3:]
	if suffix == "MID":
		try:
			WEBDRIVER.get(url2 + link.get('href'))
			print("Downloading " + str(n) + ".mid", end="\r", flush=True)
			n += 1
		except urllib.error.HTTPError:
			print(link.text, " not found", flush=True)
			continue
print("Downloaded ", str(n), " midi files")
