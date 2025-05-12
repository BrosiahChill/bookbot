def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def number_of_words(text):
    new_text = text.split()
    return len(new_text)


def chars_in_book_text(text):
    # create empty dictionary
    char_dict = {}
    # get each character
    char_text = list(text.lower())
    for char in char_text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


def sorted_dictionary(char_dict):
    sorted_dict = {}
    for key, value in char_dict.items():
        new_key = ''.join(x for x in key if x.isalpha())
        sorted_dict[new_key] = value

    sorted_chars = [{key: value} for key, value in sorted(sorted_dict.items(), key=lambda y: y[1], reverse=True)]

    return sorted_chars