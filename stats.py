def get_string_from_file_path(path):
    content=""
    with open(path) as f:
        content = f.read()
    return content

def get_word_number_count(path):
    text = ""
    text = get_string_from_file_path(path)
    return len(text.split())

def get_character_number_count(path):
    s1 = get_string_from_file_path(path)  
    s2 = lambda func: func.lower()
    list_text = list(s2(s1))
    dic_char = []
    for chara in set(list_text):
        dic_char.append({"character":chara,"num":list_text.count(chara)})
    return dic_char

def sort_on(dict):
    return dict["num"]

def sort_dict(dict_char):
    dict_char.sort(reverse=True, key=sort_on)
    return dict_char