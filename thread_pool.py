'''
ThreadPool Example
'''
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from writer import write_to_log

# LINK https://stackoverflow.com/questions/68919990/why-using-concurrent-futures-in-python-and-bs4-is-not-optimize-my-running-time

def url_list_builder(num_pages):
    '''
    Builds url
    '''
    url_list = [
        f'https://quotes.toscrape.com/page/{i}/' for i in range(1, num_pages+1)]
    print('---- URL LIST SUCCESSFULLY CREATED ----')
    return url_list


# Use a Session instance:
session = requests.Session()


def get_titles(url):
    '''
    Builds title lists
    '''
    try:
        _req = session.get(url)
        soup = BeautifulSoup(_req.content, 'html.parser')
        _titles = soup.find_all("small", {"class": "author"})
        return [title.text for title in _titles]
    except Exception as _err:
        print("Issue is -->" + _err)
        write_to_log("Issue is -->" + _err)
        return []  # return empty list


url_list = url_list_builder(10)
titles = []
# Create pool size equal to number of URLs to be retrieved:
with ThreadPoolExecutor(len(url_list)) as executor:
    for title_list in executor.map(get_titles, url_list):
        titles.extend(title_list)
print(titles)
