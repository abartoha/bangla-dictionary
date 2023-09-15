"""
Writes some output to a local file or testing purpose
"""
import pickle
from json import dumps
from datetime import datetime
ALPHABET_FILE = 'alphabet.pkl'
DICT_FILE = 'page.pkl'
WORDLIST_FILE = 'words.pkl'
DICTIONARY = 'dict.pkl'
LOGFILE = 'log.txt'


def write_alphabet_list(_list: list) -> None:
    """
    Writes the list of alphabet
    """
    with open(ALPHABET_FILE, 'wb') as _file:
        pickle.dump(_list, _file)


def read_alphabet_list() -> None:
    """
    Reads the list of alphabet
    """
    with open(ALPHABET_FILE, 'rb') as _f:
        return pickle.load(_f)


def write_page_dict(__dict: dict) -> None:
    """
    Writes the dict of pages
    """
    with open(DICT_FILE, 'wb') as _file:
        pickle.dump(__dict, _file)


def read_page_dict() -> None:
    """
    Reads the dict of pages
    """
    with open(DICT_FILE, 'rb') as _f:
        return pickle.load(_f)


def write_wordlist_links(_list: list) -> None:
    """
    Writes the list of links to words
    """
    with open(WORDLIST_FILE, 'wb') as _file:
        pickle.dump(_list, _file)


def read_wordlist_links() -> None:
    """
    Reads the list of links to words
    """
    with open(WORDLIST_FILE, 'rb') as _f:
        return pickle.load(_f)


def write_dictionary(_dict: dict) -> None:
    """
    Writes the dictionary
    """
    with open(DICTIONARY, 'wb') as _file:
        pickle.dump(_dict, _file)


def dictionary_to_json(_dict: dict, filename):
    """
    Write the dictionary to a dict
    """
    with open(filename, 'w+', encoding='utf-8') as _fp:
        _fp.write(dumps(_dict))


def write_to_log(_log: str) -> None:
    '''
    writes a line to the log file
    '''
    with open(LOGFILE, 'a+') as _fp:
        _fp.write(f'{str(datetime.now())} - {_log}\n')
