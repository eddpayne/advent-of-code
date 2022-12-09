#!/usr/bin/python3

def getMessageStart(message, headerlength):
    start = 0

    while True:
        candidate = message[start:start+headerlength]
        if len(set([x for x in candidate])) == headerlength:
            return start+headerlength
        
        start += 1
        if start+headerlength > len(message):
            return False


with open("input-6", "r") as f:

    message = f.readline().rstrip()

    print(f"Part 1: {getMessageStart(message, 4)}")
    print(f"Part 2: {getMessageStart(message, 14)}")
