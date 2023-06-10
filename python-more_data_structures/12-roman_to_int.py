#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if not roman_string or type(roman_string) is not str:
        return 0
    iT = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    newlist = [iT.get(x) for x in roman_string]
    for idx, char in enumerate(newlist):
        if (idx < len(newlist) - 1):
            if newlist[idx + 1] > char:
                sum -= char
            else:
                sum += char
        else:
            sum += char
    return (sum)
