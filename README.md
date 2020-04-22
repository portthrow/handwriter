# handwriter
Handwriter

Simply run: `python writer.py`

# Making it your own
In the images folder, you will find:
  lowers.png
  capitals.png
  numbers.png
  special_chars.png
  
The file `create_text.py` ingests these four files and creates all of the individual character files.
The names of these files are translated in `writer.py`, so if you create your own (or the special characters are in a different order), you should look at both files.

The `height` and `width` arguments in `create_text.py` are the height and width of each individual character. The script "crops out" each letter from the aforementioned files (numbers, lowers, etc.) iterating based on the width.
