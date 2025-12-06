character_log_book = {}

def get_book_text(file_path):
    with open(file_path) as f:
        opened = f.read()
        return opened

def get_num_words():
    book = get_book_text("frankenstein.txt")
    split_words = book.split()
    return len(split_words)

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

def sorted_output(character_log_book):
    temp_dictionary = {key: value for key, value in character_log_book.items() if key.isalpha()}
    for item in sorted(temp_dictionary, key=temp_dictionary.get, reverse=True):
        print(f"{item}: {temp_dictionary[item]}")


#    return items_list
#print(into_list(get_characters()))
