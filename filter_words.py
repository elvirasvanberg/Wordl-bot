from word_score import word_by_score

with open('wordle-answers-alphabetical.txt', 'r') as file:
    possible_answers = file.read().splitlines()

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
    possible_words_upd = []
    for w in possible_words:
        if compare_words(word, w) == comparison_code:
            possible_words_upd.append(w)
        else:
            pass
        
    return word_by_score(possible_words_upd)