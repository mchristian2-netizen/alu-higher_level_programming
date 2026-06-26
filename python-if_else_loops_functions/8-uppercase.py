#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print(result)
