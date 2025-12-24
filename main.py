from stats import count_words_in_text, count_characters_in_text

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    print(count_words_in_text(text))
    char_count_dict = count_characters_in_text(text)
    print(char_count_dict)

main()