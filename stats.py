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
    character_log_book = {}
    for i in opened:
        lower_only = i.lower()
        if lower_only in character_log_book:
            character_log_book[lower_only] += 1
        else:
            character_log_book[lower_only] = 1 
    sort_items = sorted(character_log_book.items())
    return character_log_book

get_characters()
