"""
Writes the list of alphabets into a pickle file
"""
from broth import Page
from writer import write_alphabet_list

ALPLHABET_LINK = "https://www.english-bangla.com/browse/"

# print(Page(ALPLHABET_LINK).find_class('a-z'))

# print(alphabet_list)
# alphabet_list = [link.text for link in alphabet_list.find_all('a')]


def collect_alphabet():
    """
    Collects all the alphabets from the website
    """
    alphabet_list = Page(ALPLHABET_LINK).find_class('a-z')[0]
    alphabet_list = alphabet_list.find_all('a')
    alphabet_list = [x.text for x in alphabet_list]
    alphabet_list.reverse()
    write_alphabet_list(alphabet_list)
