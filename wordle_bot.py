from filter_words import filter_words
from word_score import word_by_score
import json
import os, sys

with open('wordle-answers-alphabetical.txt', 'r') as file:
    possible_answers = file.read().splitlines()

with open(os.path.join(sys.path[0], 'svenska-ord.json')) as json_file:
    swedish_words = json.load(json_file)
swedish_wordle_words = list(filter(lambda x: len(x)==5 and "-" not in x and " " not in x, swedish_words))
swedish_wordle_words = list(map(lambda x: x.lower(), swedish_wordle_words))

def first_guess(possible_words):
    word_list_by_score = word_by_score(possible_words)
    return word_list_by_score[0][0]

def guess(possible_words, word, comparison_code):
    possible_words_upd = filter_words(possible_words, word, comparison_code)
    possible_words_upd_sorted = word_by_score(possible_words_upd)

    if len(possible_words_upd) == 0:
        return 'Det finns inga möjliga ord i ordlistan som uppfyller kraven'
    else:
        return possible_words_upd_sorted[0][0]

def main(word_list):
    guess_word = first_guess(word_list)
    print(f'Första gissningen: {guess_word}')
    comparison_code = input('Ange jämförelsekoden\n')

    while comparison_code != '22222':
        word_list = filter_words(word_list, guess_word, comparison_code)
        guess_word = guess(word_list, guess_word, comparison_code)
        print(f'Nästa gissning: {guess_word}')
        comparison_code = input('Ange jämförelsekoden\n')
    
    if comparison_code == '22222':
        return 'Grattis!'

print(main(swedish_wordle_words))