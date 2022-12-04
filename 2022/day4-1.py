#!/usr/bin/python3

with open("input-4", "r") as f:

    counter = 0

    while True:
        blocks = f.readline().rstrip()
        if not blocks:
            break

        sections = blocks.split(",")

        firstStart  = int(sections[0].split('-')[0])
        secondStart = int(sections[1].split('-')[0])
        firstEnd    = int(sections[0].split('-')[1])
        secondEnd   = int(sections[1].split('-')[1])
    
        if firstStart >= secondStart and firstEnd <= secondEnd:
            counter += 1
            continue
    
        if firstStart <= secondStart and firstEnd >= secondEnd:
            counter += 1

    print(counter)
