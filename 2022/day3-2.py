#!/usr/bin/python3

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

badges = []

with open("input-3", "r") as f:
    while True:
        rucksack1 = f.readline().rstrip()
        if not rucksack1:
            break

        rucksack2 = f.readline().rstrip()
        rucksack3 = f.readline().rstrip()

        candidates = []

        for item in rucksack1:
            if item in rucksack2:
                candidates.append(item)
                
        print(f"Found the following candidates: {candidates}")

        for item in candidates:
            if item in rucksack3:
                print(f"Found the badge! id: {item}")
                badges.append(item)
                break


    values = list(map(lambda x: priorities.find(x)+1, badges))

    print(sum(values))
