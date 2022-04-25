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

def relative_char_frequency():
    char_frequency_dict = char_frequency(word_list)
    values = char_frequency_dict.values()
    total_char_num = sum(values)
    
    char_frequency_list = list(char_frequency_dict.items())
    
    relative_char_frequency_list = []
    for element in char_frequency_list:
        element2 = (element[0], element[1]/total_char_num)
        relative_char_frequency_list.append(element2)
    
    char_by_relative_frequency = sorted(relative_char_frequency_list, key = lambda x: x[1], reverse = True)

    return char_by_relative_frequency

def score(word):
    char_frequency_list = relative_char_frequency()

    score = 0
    for letter in word:
        i = 0
        if letter != char_frequency_list[i][0]:
            i += 1
        score += char_frequency_list[i][1]
    
    # take points off if there are multiple of the same letter
    for a in range(word_length):
        for b in range(word_length):
            if word[a] == word[b] and a != b:
                score -= 0.05

    return score

def word_by_score():
    word_list_and_score = [(word, score(word)) for word in word_list]

    word_list_by_score = sorted(word_list_and_score, key = lambda x: x[1], reverse = True)
    return word_list_by_score[:20]