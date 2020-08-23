README
Fix-hangul

Take in a directory of mp3 files and fix the encoding errors from the past.
In my case, I only had Korean files that were broken. Probably from old computers in the 2000s that failed in encoding due to them not support hangul at the time

Current scheme:
-create a dictionary of broken filename and the fixed filename with python's encoding tool
-rename the filenames to the corrected names..
	-if the name's already in hangul, then the program returns the text as blank. To circumvent this, I added a try except clause since it does go through an error on its own.

todo:
discovered broken ID3 attributes
	1.1: current module https://github.com/artcom-net/mp3-tagger doesn't get the year attribute correctly, when it shows up in Linux file explorer
	1.2: alt module https://eyed3.readthedocs.io/en/latest/eyed3.html is hard to parse through atm. Promising if it works.


