import sys
from stats import get_number_of_words, get_character_frequency, get_sorted_character_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_number_of_words(book_text)
    char_freq = get_character_frequency(book_text)
    sorted_chars = get_sorted_character_list(char_freq)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ==============")

main()