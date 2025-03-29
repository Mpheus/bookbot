def get_num_words(filepath):
    with open(filepath) as f:
        word_count = len(f.read().split())
    return word_count

def get_char_count(filepath):
    char_dict = {}
    with open(filepath) as f:
        text = f.read().lower()
    for char in text:
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] =1

    return char_dict

def return_dict_key_value(dictionary):
    value = list(dictionary.keys())[0]

    return dictionary[value]


def return_dict_key_name(dictionary):
    name = list(dictionary.keys())[0]

    return name


def sorted_dict_list(char_dict):
    dict_list = []
    for char in char_dict:
        if char.isalpha():
            dict_list.append({char: char_dict[char]})

    dict_list.sort(reverse=True, key=return_dict_key_value)


    return dict_list
