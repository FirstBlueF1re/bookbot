character_log_book = {}
items_list = []

def get_book_text(file_path):
    with open(file_path) as f:
        opened = f.read()
        return opened

def get_num_words():
    book = get_book_text("frankenstein.txt")
    split_words = book.split()
    return print(f"Found {len(split_words)} total words")

def get_characters():
    opened = get_book_text("frankenstein.txt")
    for i in opened:
        lower_only = i.lower()
        if lower_only in character_log_book:
            character_log_book[lower_only] += 1
        else:
            character_log_book[lower_only] = 1
    return character_log_book

def sort_on(items):
    return items["num"]


def into_list(dict_list):
    for character, number in dict_list.items():
        items_list.append({"char": character, "num": number})
    items_list.sort(reverse=True, key=sort_on)
    return items_list
