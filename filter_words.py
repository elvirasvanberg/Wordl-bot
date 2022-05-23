def compare_words(query_word, answer_word):
    comparison_code = []
    pos_not_found = []
    letters_not_found = []
    
    for (i, letter1), letter2 in zip(enumerate(query_word), answer_word):
        if letter1 == letter2:
            comparison_code.append('2')
        else:
            comparison_code.append('0')
            pos_not_found.append(i)
            letters_not_found.append(letter2)
    
    for i in pos_not_found:
        if query_word[i] in letters_not_found:
            comparison_code[i] = '1'
            letters_not_found.remove(query_word[i])
    
    return "".join(comparison_code)

def filter_words(possible_words, word, comparison_code):
    possible_words_upd = []
    for w in possible_words:
        if compare_words(word, w) == comparison_code: # comparison_code ex 22001
            possible_words_upd.append(w)
        else:
            pass
        
    return possible_words_upd