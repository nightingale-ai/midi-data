# midi-data
collection of midi files

## Cleaning Procedure
Before being uploaded here, data is (1) scanned for non-MIDI files masquerading as MIDI files using [this homebrewed utility](https://github.com/nightingale-ai/nightingale/blob/main/utilities/rm_nonmidi.sh), and then (2) checked for duplicates using `fdupes` (which bases its decision on the checksum of files, not their names). As a rule, prefer MIDI files sorted into their genre to unsorted files (if the need to delete one or the other arises).

We continue to gather unsorted MIDI files in the hope that we will eventually find a tool capable of automatically determining their genre, at which point they will be merged with the rest of the dataset. The [Bodhidharma](http://jmir.sourceforge.net/index_Bodhidharma.html) tool by Cory McKay (2004) may be able to do this.

Currently, we are preserving the origin of all MIDI files by placing them in directories corresponding to their source, e.g. `/sorted/midiworld.com/pop`. Eventually we will consolidate the data into one flat directory structure filled with genres, e.g. `/pop`, `/folk`, etc.

**TODO:** add step of checking whether MIDI file is corrupt to cleaning procedure.

---

## UNTAPPED DATA SOURCES

### PRIORITY

- [x] [vgmusic](https://drive.google.com/drive/folders/1IW83MmH-RJ81yog6sbOUOTHimobE4FuK?usp=sharing) (28,419 songs)
- [x] [Doug McKenzie Jazz](https://drive.google.com/drive/folders/1wVVDpcov5VV6Govhn1-CT0BOifqoF-Od?usp=sharing) (297 songs)
- [x] [E-piano competition](https://drive.google.com/drive/folders/17yAGt3AR6txSZv8DBcbAbT3luTMkrkIb?usp=sharing) (1573 songs)
- [x] [The Lakh MIDI Dataset v0.1](https://colinraffel.com/projects/lmd/) (176,581 songs)
- [x] [W3F MIDI Files](http://web.archive.org/web/20080601093342/http://www.w3f.com/midi/pop) (organized by genre, few hundred songs)
- [x] [The Real Book Jazz Standards MIDI Files](http://web.archive.org/web/20190525163802/http://www.profesordepiano.com/Real%20Book/Realbook.htm)
- [x] [Mfiles Classical MIDI](https://www.mfiles.co.uk/classical-midi.htm)
- [x] [Mfiles Traditional MIDI](https://www.mfiles.co.uk/midi-traditional.htm) - ragtime, patriotic, folk, childrens songs, hymns/church, weddings, christmas, etc)
- [ ] [Classical Archives](https://www.classicalarchives.com/midi.html)
- [x] [Composing.ai Dataset](https://composing.ai/dataset)
- [x] midkar
  - [x] http://midkar.com/classical/
  - [x] http://midkar.com/country/
  - [x] http://midkar.com/gospel/
  - [x] http://midkar.com/holidays/christmas/
  - [x] http://midkar.com/holidays/easter/
  - [x] http://www.midkar.com/pat/
  - [x] http://midkar.com/holidays/thanksgiving/
  - [x] http://midkar.com/holidays/other/
  - [x] http://midkar.com/holidays/valentines/
  - [x] http://midkar.com/holidays/stpats/
  - [x] http://midkar.com/jazz/
  - [x] http://midkar.com/misc/
  - [x] http://midkar.com/original/
  - [x] http://midkar.com/poprock/
  - [x] http://midkar.com/ragtime/
  - [x] http://midkar.com/world/
  - [x] http://midkar.com/themes/
  - [x] http://midkar.com/blues/


### REGULAR
http://www.thejazzpage.de/index1.html -  scrapable ~100-200 jazz midi files (click on midi section on top)

http://web.archive.org/web/20180212230649/http://www.saxuet.qc.ca/TheSaxyPage/midi.htm - more jazz midis

http://caseyscaverns.com/xmas/midi.html - 200 christmas midi files

https://jazzycat.tripod.com/jazzcat.html - jazz midi files

https://www.angelfire.com/nm/hyhouse/lovesongs.html - midi (love songs, country, contemporary christian, 50s and 60s)

http://www.davidbmidi.com/ - midi singles, beatles, country, jazz, rock

http://web.archive.org/web/20050213015449/http://www.fortunecity.com/tinpan/bush/1092/duklis/duklis.html - midi country and pop

http://web.archive.org/web/20050129094112/http://www.geocities.com/ajsblue/blues/blues_1.html - blues midi

http://web.archive.org/web/20050124095208/http://www.geocities.com/ajsblue/classic/classic.html - classical/opera/orchesta midi

http://web.archive.org/web/20090228195215/http://www.trachtman.org/ragtime/index.htm - ragtime piano midi

https://www.mididb.com/genres/ - midi organized by genre, many genres, so-so

http://web.archive.org/web/20080216014704/http://www.cool-midi.com/free-midi-11.htm - has midi organized by genre (Rock R&B Rap/Hip Hop Pop Dance-Pop Latin Club/Dance Reggae Country Electronica Ethnic Fusion Gospel New Age Vocal Soundtrack Teen Pop Latin Pop Comedy Pop/RockVocal Pop World Dance Soul). potential to scrape

[MFiles Original MIDI](https://www.mfiles.co.uk/midi-original.htm) - partly unsorted, partly in categories like jazz, world, pop, soundtrack

http://web.archive.org/web/20070320074201/http://www.ugrad.physics.mcgill.ca/~orchard/Mirrors/midi-disco.chat.ru/disco-midi/index1.html - 100 disco midi easy download

### UNSORTED

https://web.archive.org/web/20051112054712/http://www.musicrobot.com/ - midi search engine (lots of midi files but doesnt seem to be organized)

http://www.garyrog.50megs.com/midi1.html - unsorted A-Z midi files (easy scrape)

http://www.ossh.com/midi/ - many midi files (some in genre folders, some not). can use wget

http://caseyscaverns.com/midi/midi1.html - unsorted A-Z midi files (easy scrape)

http://d21c.com/dolphinsdream/quietude.html - bunch of random A-Z midi files (easy scrape)

http://www.wtv-zone.com/MagicMan/Tunes-Midi/Midi.html - midi unsorted A-Z easy parse

http://web.archive.org/web/20060910015156/http://www18.pair.com/herbca/midiframes.html - midi mostly unsorted A-Z (mostly oldtime music) (mirror at http://web.archive.org/web/20041022023541/http://www.harari.net/midiframes.html)

https://monya1.tripod.com/index4.html - unsorted A-Z midi (country, easy listening, rock, jazz, etc)

http://web.archive.org/web/20040602204140/http://user.aol.com/accrdnmn/midi.html - eccentric midi stuff like accordion from different countries, steel drum, etc. bit disorganized

http://web.archive.org/web/20070621035244/http://midiallthebest.50webs.com/MidiAllTheBest/midiallthebest1.htm (midiallthebest 1-8, left links work right links dont work), unsorted

https://archive.org/details/sgeos_midi_collection - instant download unsorted midi mostly video game music

http://www.bun.ru/midi/ - A-Z unsorted midi (tupac, britney spears, some classical etc)

http://web.archive.org/web/20080224054800/http://www.free-midi.org/all_midi_artists.php - midi organized by artist (but only some downloads work)

http://web.archive.org/web/20080213205513/http://www.midimole.com/popular.php?page=A&order=a - A-Z midi (some links work), also has pop/classic/folk categories but doesnt seem to work well. overall so-so

http://web.archive.org/web/20080213173408/http://en.midipedia.net/midi_files.php - midi organized by artist, most seem to work

http://www.azringtones.com/ - ringtone midis A-Z (most work)

http://web.archive.org/web/*/http://www.fraserking.co.uk/midi/* - 1,019 archived unsorted midi tracks

http://web.archive.org/web/*/http://www.fortunecity.com/westwood/dolce/51* - some archived unsorted midi tracks

http://www.redsal.com/buf4a.htm - like 50 random midis easy download

http://www.redsal.com/redsalmidis.htm - 50 more random midis easy download

https://gifstogo.tripod.com/index-2.html - like 100 easy download midis, seems to be country or religious

http://www-personal.umich.edu/~bbowman/midi/ragtime/index.html - 12 ragtime songs (just click and download right away)

https://www.bestmp3links.com/midi/song-files.php - midi karaoke files (easy download) (on the right of the page)

https://alien98.tripod.com/show.htm - like 30 random midi files easy download

http://www.storth.com/midi/music-l.htm - a large amount of A-Z midi files easy download

http://www.breaktru.com/midi.html - like 50 random midi files easy download

http://web.archive.org/web/20070320095317/http://home.arcor.de/dinoandfriends/frank_midis.htm - 100 frank sinatra midis easy dl

http://web.archive.org/web/20060818070940/http://www.geocities.com/CollegePark/Dorm/4805/midi1.html - 50 midi by artist and sometimes genre (e.g. nas, michael jackson)

http://web.archive.org/web/20200126202935/http://raban.bravepages.com/collecta-m.html - A-Z (1) download on click

http://web.archive.org/web/20200126202935/http://raban.bravepages.com/collectn-z.html - A-Z (2) download on click

### SOUNDFONTS

https://web.archive.org/web/20150314191902/http://hammersound.com/ - a bunch of soundfonts (may be useful for when we need to play back midi on the frontend, i.e. the synth/instrument part)

### SPRINGBOARDS FOR FINDING OTHER SITES
* https://web.archive.org/web/20061123101626/http://www.dmoz.org/Arts/Music/Sound_Files/MIDI/
* http://caseyscaverns.com/links/MidiLinks.html
* http://aitech.ac.jp/~ckelly/SMF.html
* http://web.archive.org/web/20190303172958/http://ftp.monash.edu/pub/midi/MIRRORS/SMF/index.html
