from stats import count_words
from stats import count_characters
from stats import sort_dict_by_val
import sys

def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file = sys.argv[1]

    try:
        txt = get_book_text(file)
    except Exception as e:
        print(e)

    count = count_words(txt)
    chars = count_characters(txt)
    pairs = sort_dict_by_val(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for pair in pairs:
        print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")

main()
