"""
Writes the list of alphabets into a pickle file
"""
from broth import Page
from writer import write_file

ALPLHABET_LINK = "https://www.english-bangla.com/browse/bntobn/%E0%A6%85"

# print(Page(ALPLHABET_LINK).find_class('a-z'))
alphabet_list = Page(ALPLHABET_LINK).find_class('a-z')[0]
alphabet_list = alphabet_list.find_all('a')
alphabet_list = [x.text for x in alphabet_list]
print(alphabet_list)
# alphabet_list = [link.text for link in alphabet_list.find_all('a')]