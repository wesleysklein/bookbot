def get_word_count(book_string):
    words = book_string.split()
    return len(words)

def get_char_count(book_string):
    char_cout_list = {}
    lower_book = book_string.lower()

    for char in lower_book:
        if char not in char_cout_list:
            char_cout_list[f'{char}'] = 1
        elif char in char_cout_list:
            char_cout_list[f'{char}'] += 1

    return char_cout_list

def sort_on(items):
        return items["num"]

def sort_chars(char_dict):
    char_list = [] 
    
    for item in char_dict:
        new_dict = {"char": item, "num": char_dict[item]}
        char_list.append(new_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list