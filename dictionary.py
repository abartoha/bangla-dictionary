"""
Deprecated!
Bangla Dictionary scraper
"""
#NOTE - Deprecated!!!!! Use dictionary_paralle.py instead
from tqdm import tqdm
from broth import Page
from writer import read_wordlist_links, dictionary_to_json, write_to_log

page_list = read_wordlist_links()

word_meanings = {}
COUNTER = 1

for count, link in enumerate(tqdm(page_list, leave=False, unit="Words", desc="Fetching words")):
    try:
        word_page = Page(link)
        word_meaning_div = word_page.find_id('w_info')[0]
        word = word_meaning_div.find('strong').text.strip()
        meaning = word_meaning_div.find(
            'span', attrs={'class': 'format1'}).text.strip()
        # print(type(meaning))
        word_meanings[word] = meaning
    # except AttributeError:
    #     write_to_log(f'Failed at {link}')
    except Exception:
        write_to_log(f'Failed at {link}')

    if count % 1000 == 0:
        dictionary_to_json(
            word_meanings, f"{COUNTER}dictionary_{count}.json")
        COUNTER += 1
        word_meanings = {}
