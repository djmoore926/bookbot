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

def format_char_num(stats):
    formatted = []
    for k,v in stats.items():
        formatted.append({"char": k, "num": v})
    return formatted

def get_num(pair):
    return pair["num"]

def trim_stats(stats):
    trimmed = []
    for pair in stats:
        if pair["char"].isalpha():
            trimmed.append(pair)
    return trimmed