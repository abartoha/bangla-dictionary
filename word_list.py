'''
Fixing the silly mistakes in my word list
'''
from writer import read_wordlist_links, write_wordlist_links

list = read_wordlist_links()

new_list = []

for i in list:
    new_list += i

write_wordlist_links(new_list)