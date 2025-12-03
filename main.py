from stats import get_num_words, get_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    #get_book_text("frankenstein.txt")
    get_num_words()
    print(get_characters())

main()
