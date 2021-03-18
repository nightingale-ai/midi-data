"""
This is a very specific program, it will probably not be of use to you.

---
synopsis:

$ fdupes -rdN sorted/
$ fdupes -rdN unsorted/
$ fdupes -r sorted/ unsorted/ > dupes.txt
$ python3 parse_fdupes_output.py
$ while read line; do rm "$line"; done < unsorted_dupes.txt
---

When you run the fdupes program on multiple directories to check for
duplicates, it outputs something to this effect:

# Assuming you're comparing the directories sorted/ and unsorted/
# by running fdupes -r sorted/ unsorted/

sorted/pop/1.mid
unsorted/foo.com/abc.mid

sorted/pop/2.mid
unsorted/foo.com/def.mid
unsorted/baz.org/wow.mid

sorted/rap/HitEmUp.mid
unsorted/bar.net/EverydayStruggle.mid

...

With our constraints, we clearly prefer to keep the sorted version
of the MIDI file, but there is no clear way to do so for every match
using fdupes's interactive interface. This script roughly solves that
problem.

Assumptions:
(1) You've saved the output of fdupes into a file
(2) You have already ran fdupes -r sorted/ and fdupes -r unsorted/ --
we can allow these cases to be handled automatically by fdupes because
presumably we don't really care which unsorted dupe or sorted dupe gets
deleted, as long as we are not destroying information by removing a
sorted file and keeping an unsorted one. (To handle automatically, use
fdupes -rdN sorted/). Having done this, it is guaranteed for the output
of fdupes -r sorted/ unsorted/ to have at most one duplicate from sorted
and unsorted, e.g.

sorted/pop/1.mid
unsorted/foo.com/abc.mid

It is now safe for our script to simply remove all lines with the sorted
duplicate, leaving only the lines with the unsorted duplicate. E.g.

sorted/pop/1.mid
unsorted/foo.com/abc.mid

sorted/pop/2.mid
unsorted/foo.com/def.mid

 =>

unsorted/foo.com/abc.mid
unsorted/foo.com/def.mid

Upon the completion of the script, read the output file line-by-line and
remove each file written in it:

$ while read line; do rm "$line"; done < unsorted_dupes.txt

The result: you've removed all unsorted duplicates, retaining sorted ones.
"""

FDUPES_OUTPUT_FILE = "/home/josh/midi-data/dupes.txt"
SCRIPT_OUTPUT_FILE = "/home/josh/midi-data/unsorted_dupes.txt"

with open(FDUPES_OUTPUT_FILE, "r") as fin:
	with open(SCRIPT_OUTPUT_FILE, "w") as fout:
		for line in fin:
			if line[:8] == "unsorted":
				fout.write(line)
