#https://freemidi.org/genre

import requests
import urllib
from bs4 import BeautifulSoup
import sys
import time
from selenium import webdriver
import selenium

USER_AGENT = 'curl/7.54.0' # why not lmfao
HEADERS = {'user-agent': USER_AGENT}

WEBDRIVER=""
PATH_TO_ADBLOCK = "/home/josh/.config/chromium/Default/Extensions/cjpalhdlnbpafiamejdnhcphjbkeiagm/1.33.2_2"
DOWNLOAD_DIRECTORY = "/home/josh/midi-data/freemidi.org/"

CATEGORIES = [
	"rock",
	"pop",
	"hip-hop-rap",
	"rnb-soul",
	"classical",
	"country",
	"jazz",
	"blues",
	"dance-eletric",
	"folk",
	"punk",
	"newage",
	"reggae-ska",
	"metal",
	"disco",
	"bluegrass"
]

#for unique file names, e.g. "1-1.midi", "2-5.midi"
n_artist = 1
n_song = 1

def error(*msg, displayGenres=False):
	print(*msg)
	if(displayGenres):
		print("Available genres:\n *", "\n * ".join(CATEGORIES))
	exit(1)

#note that we relaunch the webdriver each time purposely, otherwise the songs
#do not download
def download(url, fn):
	global WEBDRIVER
	WEBDRIVER_OPTIONS = webdriver.ChromeOptions()
	WEBDRIVER_OPTIONS.add_argument("-load-extension=" + PATH_TO_ADBLOCK)
	WEBDRIVER_OPTIONS.add_argument("-page_load_strategy=eager")
	WEBDRIVER_OPTIONS.add_argument("--headless")
	WEBDRIVER_OPTIONS.add_experimental_option("prefs",
		{"download.default_directory" : DOWNLOAD_DIR})

	WEBDRIVER = webdriver.Chrome(options=WEBDRIVER_OPTIONS)
	WEBDRIVER.get(url)
	WEBDRIVER.execute_script('document.getElementById("downloadmidi").click();')
	time.sleep(1) #all good things take time...
	WEBDRIVER.quit()

def scrapeSong(song_page):
	url = "https://freemidi.org/" + song_page
	try:
		response = requests.get(url, headers=HEADERS)
		if response.status_code != 200:
			return
	except requests.exceptions.RequestException as e:
		print(e)
		return

	fn = str(n_artist) + "-" + str(n_song) + ".midi"
	try: download(url, fn)
	except selenium.common.exceptions.WebDriverException as e:
		print(e)
		return
	print("* Downloading", fn, end="\r")

def scrapeArtist(artist_page):
	global n_song
	global n_artist

	url = "https://freemidi.org/" + artist_page

	page = 0
	page_exists = True
	while page_exists:
		page_url = url + "-P-" + str(page)
		try:
			response = requests.get(page_url, headers=HEADERS)
		except requests.exceptions.RequestException as e:
			print(e)
			break

		html = response.text
		soup = BeautifulSoup(html, 'html.parser')
		#first two results are not songs
		songs = soup.find_all("a", itemprop="url")[2:]

		#freemidi.org doesn't return a 404, on non-existent pages,
		#rather it just loads a page with only one "song" titled
		#"Error no title", which we use to determine whether a page
		#exists.
		page_exists = (response.status_code == 200) \
			and (html.find("Error no title") == -1) \
			and (len(songs) > 1)
		if not page_exists: break

		for song in songs:
			scrapeSong(song.get("href"))
			n_song += 1

		page += 1

	n_artist += 1
	n_song = 1
	print()

def scrape(genre):
	genre = urllib.parse.quote(genre)

	url = "https://freemidi.org/genre-" + genre
	response = requests.get(url, headers=HEADERS)
	if response.status_code != 200:
		return

	html = response.text
	soup = BeautifulSoup(html, 'html.parser')

	for artist in soup.find_all("div", class_="genre-link-text"):
		scrapeArtist(artist.a.get("href"))

def main():
	if len(sys.argv) != 2:
		error("Usage:", sys.argv[0], "<genre>", displayGenres=True)
	else:
		if sys.argv[1] not in CATEGORIES:
			error("No such genre.", displayGenres=True)
		else:
			scrape(sys.argv[1])
			WEBDRIVER.quit()
try:
	main()
except KeyboardInterrupt:
	WEBDRIVER.quit()
	exit(0)
