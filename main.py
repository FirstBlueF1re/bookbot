from stats import get_num_words, get_characters, sorted_output

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    #get_book_text("frankenstein.txt")
    #get_num_words()
    #print(get_characters())

	print(f"============ BOOKBOT ============")
	print(f"Analyzing book found at books/frankenstein.txt...")
	print(f"----------- Word Count ----------")
	print(f"Found {get_num_words()} total words")
	print(f"--------- Character Count -------")
	sorted_output(get_characters())
main()
