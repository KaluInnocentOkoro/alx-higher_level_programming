#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    rom_fig = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_num = 0
    for idx in range(len(roman_string)):
        if idx > 0 and \
        rom_fig[roman_string[idx]] > rom_fig[roman_string[idx - 1]]:
            rom_num += rom_fig[roman_string[idx]] - \
            2 * rom_fig[roman_string[idx - 1]]
        else:
            rom_num += rom_fig[roman_string[idx]]
    return rom_num