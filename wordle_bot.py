from filter_words import filter_words
from word_score import word_by_score

with open('wordle-answers-alphabetical.txt', 'r') as file:
    possible_answers = file.read().splitlines()

def guess(possible_words, word, comparison_code):
    guess_list = filter_words(possible_words, word, comparison_code)
    guess_list_sorted = word_by_score(guess_list)

    if len(guess_list) == 0:
        print('Det finns inga möjliga ord i ordlistan som uppfyller kraven')
        return []
    else:
        return guess_list_sorted[0][0]