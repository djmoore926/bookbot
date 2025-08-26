from stats import *

def main():
    text = get_book_text(r"books/frankenstein.txt")
    num_words = get_book_words(text)
    print(f"{num_words} words found in the document")
    print(get_book_chars(text))

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

if __name__ == "__main__":

    main()
