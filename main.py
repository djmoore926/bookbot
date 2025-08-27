from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_book_words(text)
    stats = format_char_num(get_book_chars(text))
    # print(f"{num_words} words found in the document")
    # print(get_book_chars(text))
    stats.sort(key=get_num, reverse=True)
    trimmed_stats = trim_stats(stats)
    print(f"""
===============BOOKBOT===============
Analyzing book found at {path}...
------------ Word Count -------------
Found {num_words} total words
---------- Character Count ----------""")
    pull_values(trimmed_stats)
    print("=================END================="
)



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def pull_values(stats):
    for item in stats:
        print(f'{item["char"]}: {item["num"]}')

if __name__ == "__main__":

    main()
