import json
import os, sys
import random
from word_score import score
from collections import Counter

with open('wordle-answers-alphabetical.txt', 'r') as file:
    possible_answers = file.read().splitlines()

with open('wordle-allowed-guesses.txt', 'r') as file:
    allowed_guesses = file.read().splitlines()

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