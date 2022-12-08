#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or len(my_list) == 0 or my_list is None:
        return 0
    score_point = 0
    total_freq = 0
    for ele in my_list:
        a, b = ele
        score_point += a * b
        total_freq += b
    return score_point / total_freq if total_freq > 0 else 0
