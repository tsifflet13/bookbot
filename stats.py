def sort_on(items):
    return items["num"]

def sorted_list_of_dicts(dict_arg):
    sorted_list = []
    for key, value in dict_arg.items():
        little_dict = {}
        if key.isalpha() == False:
            continue
        else:            
            little_dict["char"] = key
            little_dict["num"] = value
            sorted_list.append(little_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_words_in_text(text_string):
    words = text_string.split()
    num_words = 0
    for word in words: 
        num_words += 1
    print(f"Found {num_words} total words")

def count_characters_in_text(text):
    numbers_char_dict = {}
    for character in text:
        lowered_char = character.lower()
        if lowered_char in numbers_char_dict:
            numbers_char_dict[lowered_char] += 1
        else:
            numbers_char_dict[lowered_char] = 1
    return numbers_char_dict
