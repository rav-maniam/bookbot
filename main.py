import sys

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

from stats import count_words

from stats import character_count

from stats import print_clean

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        book = get_book_text(sys.argv[1])
        count = count_words(book)

        letters = character_count(book)
        print("============= BOOKBOT ===============")
        print("Analyzing book found at books/frankenstein.txt")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        print_clean(letters,count)
main()

    
