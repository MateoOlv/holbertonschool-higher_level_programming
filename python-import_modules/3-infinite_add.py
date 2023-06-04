#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sumo = 0
    for i in range(1, len(sys.argv)):
        sumo += int(sys.argv[i])
    print(sumo)
