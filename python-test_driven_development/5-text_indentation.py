#!/usr/bin/python3
"""
Text indent mod
"""
def text_indentation(text):
    """
    check error
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    """check text indentation"""
    pon = 0
    for idx, i in enumerate(text):
        if i in '?:.':
            print(text[pon:idx + 1].strip() + '\n')
            pon = idx + 1
    if not pon:
        print(text, end='')
    elif pon is not len(text):
        print(text[pon:idx + 1].strip(), end='')
