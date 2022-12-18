# 1120 / 1967
import re
from collections import deque

def ints(line: str, negatives=1):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

rocks = set()
sa = 0

for rock in IN:
    rockx, rocky, rockz = ints(rock)
    rocks.add((rockx, rocky, rockz))
    sa += 6
    if (rockx + 1, rocky, rockz) in rocks:
        sa -= 2
    if (rockx - 1, rocky, rockz) in rocks:
        sa -= 2
    if (rockx, rocky + 1, rockz) in rocks:
        sa -= 2
    if (rockx, rocky - 1, rockz) in rocks:
        sa -= 2
    if (rockx, rocky, rockz + 1) in rocks:
        sa -= 2
    if (rockx, rocky, rockz - 1) in rocks:
        sa -= 2

print(sa)

outside_airs = set()
q = deque()
q.append((0,0,0)) # Assume 0,0,0 is an outside air cube

while q:
    airx, airy, airz = q.pop()
    if (airx, airy, airz) not in outside_airs:
        outside_airs.add((airx, airy, airz))
        for dx, dy, dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            nairx, nairy, nairz = (airx + dx, airy + dy, airz + dz)
            if (nairx, nairy, nairz) not in rocks and nairx in range(25) and nairy in range(25) and nairz in range(25):
                q.append((nairx, nairy, nairz))

inside_airs = {(x,y,z) for x in range(25) for y in range(25) for z in range(25)}.difference(rocks).difference(outside_airs)

for rockx, rocky, rockz in inside_airs:
    if (rockx + 1, rocky, rockz) in rocks:
        sa -= 1
    if (rockx - 1, rocky, rockz) in rocks:
        sa -= 1
    if (rockx, rocky + 1, rockz) in rocks:
        sa -= 1
    if (rockx, rocky - 1, rockz) in rocks:
        sa -= 1
    if (rockx, rocky, rockz + 1) in rocks:
        sa -= 1
    if (rockx, rocky, rockz - 1) in rocks:
        sa -= 1

print(sa)
