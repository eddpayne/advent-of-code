#!/usr/bin/python3

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

duplicatedItems = []

with open("input-3", "r") as f:
    while True:
        contents = f.readline().rstrip()
        if not contents:
            break

        itemsPerCompartment = len(contents)//2
        compartments = [ contents[:itemsPerCompartment], contents[itemsPerCompartment:] ]

        for item in compartments[0]:
            if item in compartments[1]:
                duplicatedItems.append(item)
                print(f"Found a duplicated {item}")
                break

    values = list(map(lambda x: priorities.find(x)+1, duplicatedItems))

    print(sum(values))
