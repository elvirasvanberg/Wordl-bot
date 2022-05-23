from ast import While
from collections import Counter

def char_frequency(list):
    dict = Counter()
    for word in list:
        word = word.lower()
        dict.update(word)

    return dict

def relative_char_frequency(possible_words):
    char_frequency_dict = char_frequency(possible_words)
    char_frequency_list = list(char_frequency_dict.items())
    total_char_num = len(possible_words) * 5
    relative_char_frequency_list = []
    for element in char_frequency_list:
        element_upd = (element[0], element[1]/total_char_num)
        relative_char_frequency_list.append(element_upd)
    
    char_by_relative_frequency = sorted(relative_char_frequency_list, key=lambda x: x[1], reverse=True)

    return char_by_relative_frequency

def score(word, possible_words):
    char_frequency_list = relative_char_frequency(possible_words)

    # remove duplicate, triplicate, etc. letters to give a more accurate score
    letter_list = []
    for c in word:
        if c not in letter_list:
            letter_list.append(c)

    score = 0
    for letter in letter_list:
        i = 0
        while letter != char_frequency_list[i][0]:
            i += 1
        score += char_frequency_list[i][1]

    return score

def word_by_score(word_list):
    word_list_and_score = [(word, score(word, word_list)) for word in word_list]
    word_list_by_score = sorted(word_list_and_score, key = lambda x: x[1], reverse = True)
    return word_list_by_score