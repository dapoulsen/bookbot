from stats import amount_of_words, amount_of_chars
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

    
def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_amount = amount_of_words(book_text)
    print(f'{word_amount} words found in the document')
    print(amount_of_chars(book_text))
    
main()