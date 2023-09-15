"""
Bangla Dictionary scraper
"""

# NOTE U+0980 – U+09FF bangla unicode range
# LINK https://stackoverflow.com/questions/150033/regular-expression-to-match-non-ascii-characters

# 1 - Run the alphabet module

# This should do it:

# [^\x00-\x7F]+
# It matches any character which is not contained in the ASCII character set (0-127, i.e. 0x0 to 0x7F).

# You can do the same thing with Unicode:

# [^\u0000-\u007F]+
# For unicode you can look at this 2 resources:

# Code charts list of Unicode ranges
# This tool to create a regex filtered by Unicode block.

if __name__ == "__main__":
    print("Running main::BanglaDictionary module")
    from alphabet_collector import collect_alphabet
    from paginatior import collect_pages
    from indicer import collect_word_index
    from dictionary_parallel import collect_words

    collect_alphabet()
    collect_pages()
    collect_word_index()
    collect_words()
