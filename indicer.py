"""
Fetches all the links to all the words
Now with concurrency!
"""
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm, trange
from broth import Page
from writer import read_page_dict, write_wordlist_links



def get_list(commonargs):
    '''
    Returns a list based on page number and letter
    '''
    letter, last_page_number_str = commonargs
    last_page = int(last_page_number_str)
    for page_number in trange(1, last_page+1, leave=False, unit="Pages"):
        def letter_template(_letter, page_num):
            """
            Template for the letteing linkss
            """
            return f"https://www.english-bangla.com/browse/bntobn/{_letter}/{page_num}"
        word_page = Page(letter_template(letter, page_number))
        main_unordered_list = word_page.find_id('cat_page')[0].find('ul')
        list_li_ul = [i['href'] for i in main_unordered_list.find_all('a')]
        return list_li_ul


def collect_word_index():
    """
    Collect all the word links
    """
    link_list = []
    dictionary = read_page_dict()
    with ThreadPoolExecutor(30) as executor:
        link_list = list(tqdm(executor.map(get_list, dictionary.items()),
                        leave=False, unit="Letters", total=len(dictionary)))

    write_wordlist_links(link_list)
