"""
Bangla Dictionary scraper
"""
from bs4 import BeautifulSoup
import re
from broth import Page
from writer import write_file

# NOTE U+0980 – U+09FF bangla unicode range
# LINK https://stackoverflow.com/questions/150033/regular-expression-to-match-non-ascii-characters

# This should do it:

# [^\x00-\x7F]+
# It matches any character which is not contained in the ASCII character set (0-127, i.e. 0x0 to 0x7F).

# You can do the same thing with Unicode:

# [^\u0000-\u007F]+
# For unicode you can look at this 2 resources:

# Code charts list of Unicode ranges
# This tool to create a regex filtered by Unicode block.
# TODO find the list of bangla alphabets
# TODO find all the words for each letter in one page
# TODO find the final page number of every 

