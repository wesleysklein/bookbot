import sys
from stats import get_word_count, get_char_count, sort_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file = f.read()
    return file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        char_count = get_char_count(text)
        sort_list = sort_chars(char_count)
        print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {get_word_count(text)} total words
--------- Character Count -------""")
        for item in sort_list:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
main()