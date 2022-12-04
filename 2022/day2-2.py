#!/usr/bin/python

score = 0

playNames = { 'A' : 'Rock', 'B': 'Paper', 'C': 'Scissors',
              'X' : 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }

shapePoints = { 'A': 1, 'B': 2, 'C': 3,
                'X': 1, 'Y': 2, 'Z': 3 }

winStrategy = { 'A': { 'X': 'C', 'Y': 'A', 'Z': 'B' },
                'B': { 'X': 'A', 'Y': 'B', 'Z': 'C' },
                'C': { 'X': 'B', 'Y': 'C', 'Z': 'A' } }

strategyPoints = { 'X': 0, 'Y': 3, 'Z': 6 }

requirement = { 'X': 'lose', 'Y': 'draw', 'Z': 'win' }


with open("input-2", "r") as f:
    while True:
        play = f.readline()
        if not play:
            break
        plays = play.rstrip().split(" ")
        yourPlay = winStrategy[plays[0]][plays[1]]
        print(f"They played {playNames[plays[0]]}, you need to {requirement[plays[1]]}, so you play {playNames[yourPlay]}")
        shapeScore = shapePoints[yourPlay]
        winScore = strategyPoints[plays[1]]
        print(f"That's {shapeScore + winScore} points!")
        score += shapeScore
        score += winScore

print(score)

