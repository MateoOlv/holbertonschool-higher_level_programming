#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for directory in dir(hidden_4):
        if directory[0] != "_":
            print(directory)
