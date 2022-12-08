#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None or len(a_dictionary) == 0:
        return None
    value = list(a_dictionary.values())
    highest_score = value[0]
    for k, v in a_dictionary.items():
        if v > highest_score:
            highest_score = v
            best = k
    return best
