import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys,exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def report(filepath, num_words, sorted_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        print(f"{letter['character']}: {letter['count']}")
    print("============= END ===============")
    return report


from stats import get_num_words
from stats import get_num_letters
from stats import sorted_dict

def main():
    args = sys.argv
    filepath = (args[1])
    result = get_book_text(filepath)  # Get the text from the book
    num_words = get_num_words(result)  # Count the words
    letters_result = get_num_letters(result)  # Count the letters
    sorted_letters = sorted_dict(letters_result)  # Sort the letter counts
    report(filepath, num_words, sorted_letters)  # Print the report

main()