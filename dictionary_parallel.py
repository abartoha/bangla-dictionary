"""
Bangla Dictionary scraper but with concurrency!
"""
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from broth import Page
from writer import read_wordlist_links, dictionary_to_json, write_to_log

MAX_WORKERS = 25

# LINK https://stackoverflow.com/questions/51601756/use-tqdm-with-concurrent-futures
# LINK https://stackoverflow.com/questions/68919990/why-using-concurrent-futures-in-python-and-bs4-is-not-optimize-my-running-time


def get_word(link: str) -> dict:
    """
    Definition for Executor
    """
    try:
        word_page = Page(link)
        word_meaning_div = word_page.find_id('w_info')[0]
        word = word_meaning_div.find('strong').text.strip()
        meaning = word_meaning_div.find(
            'span', attrs={'class': 'format1'}).text.strip()
        # print(type(meaning))
        return {word: meaning}

    except Exception as _err:  # pylint: disable=broad-except
        # LINK https://stackoverflow.com/questions/756180/pylint-warning-on-except-exception
        write_to_log(f'Failed at {link} {_err}')
        return {}


def collect_words():
    """
    Collects all the words
    """
    page_list = read_wordlist_links()
    print(len(page_list))
    word_meanings = {}
    with ThreadPoolExecutor(MAX_WORKERS) as executor:
        # the argument 'total' is absolutely essential for aesthetic reasons
        for link_word in tqdm(executor.map(get_word, page_list), leave=False, unit="Words", desc="Fetching words", total=len(page_list)):
            word_meanings.update(link_word)

    dictionary_to_json(
        word_meanings, "dictionary.json")

# collect_words()