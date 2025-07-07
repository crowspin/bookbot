def count_words(text):
    return len(text.split())

def count_characters(text):
    resp = {}
    for ch in text:
        ch = ch.lower()
        if ch not in resp:
            resp[ch] = 1
        else: resp[ch] += 1
    return resp

def sort_on(pair):
    return pair['num']

def sort_dict_by_val(dict):
    resp = []
    for pair in dict:
        resp.append({
            "char": pair,
            "num": dict[pair]
            })
    resp.sort(reverse=True, key=sort_on)
    return resp