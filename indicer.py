"""
Fetches all the links to all the words
Now with concurrency!
"""
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm, trange
from broth import Page
from writer import read_page_dict, write_wordlist_links


def letter_template(_letter, page_num):
    """
    Template for the letteing linkss
    """
    return f"https://www.english-bangla.com/browse/bntobn/{_letter}/{page_num}"


def get_list(commonargs):
    '''
    Returns a list based on page number and letter
    '''
    aggregate_list = []
    letter, last_page_number_str = commonargs
    last_page = int(last_page_number_str)
    for page_number in trange(1, last_page+1, leave=False, unit="Page", desc=f"{letter} Collection"):
        word_page = Page(letter_template(letter, page_number))
        main_unordered_list = word_page.find_id('cat_page')[0].find('ul')
        list_li_ul = [i['href'] for i in main_unordered_list.find_all('a')]
        aggregate_list.extend(list_li_ul)
    return aggregate_list


def collect_word_index():
    """
    Collect all the word links
    """
    link_list = []
    dictionary = read_page_dict()
    with ThreadPoolExecutor(5) as executor:
        for list_part in tqdm(executor.map(get_list, dictionary.items()), leave=False, unit="Letters", total=len(dictionary), desc="Indexing"):
            link_list.extend(list_part)

    write_wordlist_links(link_list)


# collect_word_index()
