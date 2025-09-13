def amount_of_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def amount_of_chars(book_text):
    lower_text = book_text.lower()
    final_dict = {}
    for char in lower_text:
        if char not in final_dict:
            final_dict[char] = 1
        else:
            final_dict[char] += 1 
    return final_dict
    