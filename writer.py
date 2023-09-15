"""
Writes some output to a local file or testing purpose
"""
import pickle

def write_file(text: str) -> None:
    """
    Writes some output to a file
    """
    with open('example.txt', 'w+', encoding="utf-8") as file:
        file.write(text)

def write_alphabet_list(_list:list) -> None :
    """
    Writes the list of alphabet
    """
    with open('alphabet.pkl', 'wb') as f:
        pickle.dump(_list, f)