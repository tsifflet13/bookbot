import sys
from stats import count_words_in_text, count_characters_in_text, sorted_list_of_dicts

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(count_words_in_text(text))
        print("--------- Character Count -------")
        char_count_dict = count_characters_in_text(text)
        sorted_chars = sorted_list_of_dicts(char_count_dict)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()