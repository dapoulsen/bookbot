import sys

from stats import amount_of_words, amount_of_chars, sort_dicts
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents    

    
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_amount = amount_of_words(book_text)
    char_dict = amount_of_chars(book_text)
    sorted_dicts = sort_dicts(char_dict)
    print("============ BOOKBOT ============ \n Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_amount} total words')
    print("--------- Character Count -------")
    for ch_dict in sorted_dicts:
        if ch_dict["char"].isalpha():
            print(f'{ch_dict["char"]}: {ch_dict["num"]}')
    print("============= END ===============")
    
main()