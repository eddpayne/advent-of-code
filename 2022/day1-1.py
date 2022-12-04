#!/usr/bin/python

calcount = []

with open("input-1", "r") as f:
  reindeer = 0
  calcount.append(0)
  while True:
    line = f.readline()
    if not line:
        break
    if line == "\n":
      reindeer += 1
      calcount.append(0)
    else:
      calcount[reindeer] += int(line)

print(max(calcount))
