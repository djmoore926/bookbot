def get_book_words(string):
    return len(string.split())

def get_book_chars(string):
    chars = {}
    for i in string.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars