def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

def amount_of_words(book_text):
    word_list = book_text.split()
    return len(word_list)
    
def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_amount = amount_of_words(book_text)
    print(f'{word_amount} words found in the document')
    
main()