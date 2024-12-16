
def count_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()
    
def count_char(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        else:
            continue
    return characters

def sort(letters):
    max_count = 0
    new_letters = {}
    while len(letters) > 0:
        for count in letters:
            if letters[count] > max_count:
                max_letter = count
                max_count = letters[count]
        new_letters[max_letter] = max_count
        del letters[max_letter]
        max_count = 0
    return new_letters

def print_report(path, words, letters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in this document")
    for char in letters:
        print(f"The '{char}' character was found {letters[char]} times")
    print("--- End report ---")

def main():
    path = "books/Frankenstein.txt"
    text = get_book(path)
    word_count = count_words(text)
    letter_count = count_char(text)
    sorted_count = sort(letter_count)

    print_report(path, word_count, sorted_count)


main()
