"""
Paginates the entire dictionary
Now with concurrency!
"""
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from broth import Page
from writer import read_alphabet_list, write_page_dict


def letter_template(letter):
    '''
    Template for link making
    '''
    return f"https://www.english-bangla.com/browse/bntobn/{letter}"


def get_page_num(letter: str):
    '''
    Returns the page number of a letter
    '''
    letter_page = Page(letter_template(letter))
    main_unordered_list = letter_page.find_id('cat_page')[0].find('ul')
    # match the ul for No match found
    if "No word" in main_unordered_list.text:
        # lINK https://stackoverflow.com/questions/38542543/functionality-of-python-in-vs-contains/38542777?noredirect=1#comment64477339_38542543
        # print("No words found")
        return {}
    else:
        # print([i.text for i in main_unordered_list.find_all('a')])
        # find the pagination div and
        pagination = letter_page.find_class('pagination')[0]
        # print(pagination.text)
        if pagination.findChildren('a') == []:
            # number of pages
            return {letter: 1}
        else:
            last_page_link = int(pagination.find_all('a')
                                 [-1]['href'].split('/')[-1])
            # number of pages
            return {letter: int(last_page_link)}


def collect_pages():
    """
    Collects all the pagination data into pickle
    """
    dictionary = {}
    alphabet = read_alphabet_list()
    with ThreadPoolExecutor(5) as executor:
        for dictionary_part in tqdm(executor.map(get_page_num, alphabet), leave=False, unit="Letter", desc="Pagination", total=len(alphabet)):
            dictionary.update(dictionary_part)

    write_page_dict(dictionary)
