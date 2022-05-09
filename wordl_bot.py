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
    char_frequency_list = list(char_frequency_dict.items())
    total_char_num = len(word_list) * 5
    relative_char_frequency_list = []
    for element in char_frequency_list:
        element_upd = (element[0], element[1]/total_char_num)
        relative_char_frequency_list.append(element_upd)
    
    char_by_relative_frequency = sorted(relative_char_frequency_list, key=lambda x: x[1], reverse=True)

    return char_by_relative_frequency

print(relative_char_frequency())

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
                score -= 0.001

    return score

def word_by_score():
    word_list_and_score = [(word, score(word)) for word in word_list]
    word_list_by_score = sorted(word_list_and_score, key = lambda x: x[1], reverse = True)
    return word_list_by_score[:20]

#print(word_by_score())

def compare_words(query_word, answer_word):
    res = []
    pos_not_found = []
    letters_not_found = []
    
    for (i, letter1), letter2 in zip(enumerate(query_word), answer_word):
        if letter1 == letter2:
            res.append('2')
        else:
            res.append('0')
            pos_not_found.append(i)
            letters_not_found.append(letter2)
    
    for i in pos_not_found:
        if query_word[i] in letters_not_found:
            res[i] = '1'
            letters_not_found.remove(query_word[i])
    
    return "".join(res)

def filter_words(possible_words, word, comparison_code):
    new_possible_words = []
    for w in possible_words:
        if compare_words(word, w) == comparison_code:
            new_possible_words.append(w)

    return new_possible_words

def solver(comparison_code, word, possible_words):
    possible_words = filter_words(possible_words, word, comparison_code)
    
    if len(possible_words) == 0:
        print('Det finns inga möjliga ord i ordlistan som uppfyller kraven')
        return "", []
    else:
        words_sorted = sorted(possible_words, key=lambda x: score(x, possible_words))
    best_guess = words_sorted[0]
    return best_guess