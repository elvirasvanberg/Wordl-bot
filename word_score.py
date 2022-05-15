from collections import Counter
from wordle_bot import possible_answers

def char_frequency(list):
    dict = Counter()
    for word in list:
        word = word.lower()
        dict.update(word)

    return dict

def relative_char_frequency():
    char_frequency_dict = char_frequency(possible_answers)
    char_frequency_list = list(char_frequency_dict.items())
    total_char_num = len(possible_answers) * 5
    relative_char_frequency_list = []
    for element in char_frequency_list:
        element_upd = (element[0], element[1]/total_char_num)
        relative_char_frequency_list.append(element_upd)
    
    char_by_relative_frequency = sorted(relative_char_frequency_list, key=lambda x: x[1], reverse=True)

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
    for a in range(5):
        for b in range(5):
            if word[a] == word[b] and a != b:
                score -= 0.01

    return score

def word_by_score():
    word_list_and_score = [(word, score(word)) for word in possible_answers]
    word_list_by_score = sorted(word_list_and_score, key = lambda x: x[1], reverse = True)
    return word_list_by_score[:20]

print(word_by_score())