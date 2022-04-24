import json
import os, sys
import random

word_length = 5

with open(os.path.join(sys.path[0], 'svenska-ord.json')) as json_file:
    wordl_words = json.load(json_file)
word_list = list(filter(lambda x: len(x)==word_length and "-" not in x and " " not in x, wordl_words))

from collections import Counter

def char_frequency(list):
    dict = Counter()
    for word in list:
        word = word.lower()
        dict.update(word)

    return dict

print(char_frequency(word_list))

def relative_char_frequency():
    char_frequency_dict = char_frequency(word_list)
    values = char_frequency_dict.values()
    total_char_num = sum(values)
    
    char_frequency_list = list(char_frequency_dict.items())
    
    for c in range(len(char_frequency_list)):
        char_frequency_list[c][1] == char_frequency_list[c][1]/total_char_num
    
    return char_frequency_list

print(relative_char_frequency())