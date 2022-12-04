#!/usr/bin/python

score = 0

playNames = { 'A' : 'Rock', 'B': 'Paper', 'C': 'Scissors',
              'X' : 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }

shapePoints = { 'A': 1, 'B': 2, 'C': 3,
                'X': 1, 'Y': 2, 'Z': 3 }
winPoints   = { 'A': { 'X': 3, 'Y': 6, 'Z': 0 },
                'B': { 'X': 0, 'Y': 3, 'Z': 6 },
                'C': { 'X': 6, 'Y': 0, 'Z': 3 } }

with open("input-2", "r") as f:
    while True:
        play = f.readline()
        if not play:
            break
        plays = play.rstrip().split(" ")
        yourPlay = plays[1]

        print(f"They played {playNames[plays[0]]}, you played {playNames[plays[1]]}")
        shapeScore = shapePoints[yourPlay]
        winScore = winPoints[plays[0]][plays[1]]
        print(f"That's {shapeScore + winScore} points!")
        score += shapeScore
        score += winScore

print(score)

