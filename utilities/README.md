#utilities
Ad-hoc utilities used to gather, clean, and organize MIDI data.

## Scraping
To scrape the data, run the python scripts with the `scrape_` prefix.

Requirements:
* `python3`
* `BeautifulSoup4` ([url](https://www.crummy.com/software/BeautifulSoup/bs4/doc/))
* `requests` ([url](https://requests.readthedocs.io/en/master/))
* `selenium`  ([url](https://www.selenium.dev/))

Only some of the scripts need selenium (it was necessary for quirky sites). You may also need to install [uBlock Origin](https://github.com/gorhill/uBlock) (or your adblocker of choice) in order for those scripts to work correctly.

## Cleaning Procedure
Note: these steps use shell scripts which are meant to be run in POSIX shells.

1. Remove non-MIDI files using `rm_nonmidi` (often the files are downloaded with a `.mid` suffix but are actually empty, an HTML file, or even some other weird file format)
2. Check for duplicate files using `fdupes` ([url](https://github.com/adrianlopezroche/fdupes)) -- if duplicates are found, prefer to keep sorted files over unsorted files.
3. Rename all files to their md5 checksum using `md5rename`.

## Useful Shell Tidbits
`rm .??*` - remove all files starting with a dot from the directory (some prepackaged datasets came with a bunch of garbage dotfiles)

`fdupes -rdN` - preserve first file from duplicates, delete all others with no prompt

`fdupes -rd` or `fdupes -rdP` - display duplicates with prompt of which to delete (sometimes `-P` plain interface is more appropriate).

`zip -r9 stuff.zip stuff/` - turn directory into a zip file, `-9` means most thorough compression

`for f in *; do ls -l "$f" | wc -l; du -h "$f"; printf "---"; done` -  get number of files and size of directory

`for f in *; do zip -r9 "$f.zip" "$f"; done` - zip all directories

`find . -mindepth 2 -type f -exec mv {} . \;` - flatten directory

`git reset --soft HEAD~` - undo latest un-pushed commit, keeping all changes

`git reset` - when run after the above, will unstage anything added with `git add`
