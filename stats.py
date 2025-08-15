def get_num_words(text):
    split_text = text.split()
    num_words = 0
    for i in split_text:
        num_words += 1
    return num_words


def get_num_chars(text):
    dict = {}
    for i in text:
        dict[i.lower()] = 0
    for i in text:
        dict[i.lower()] += 1
    return dict


def trans_dict(dict):
    list_of_dicts = []
    for k, v in dict.items():
        if k.isalpha():
            list_of_dicts.append({"char": k, "num": v})
    return list_of_dicts


def sort_on(items):
    return items["num"]


def lom_to_string(list):
    r_list = []
    for i in list:
        r = f"{i['char']}: {i['num']}"
        r_list.append(r)
        r_joined = '\n'.join(r_list)
    return r_joined
