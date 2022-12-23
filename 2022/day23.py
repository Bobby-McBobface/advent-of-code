from collections import deque

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

elfpos = set()

for y, row in enumerate(IN):
    for x, val in enumerate(row):
        if val == "#":
            elfpos.add((x,y))


def printboard():
    minx = min(x[0] for x in elfpos)
    maxx = max(x[0] for x in elfpos)
    miny = min(x[1] for x in elfpos)
    maxy = max(x[1] for x in elfpos)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            print('#' if (x,y) in elfpos else '.', end="")
        print()
    print('=============')


def firsthalf():
    for elfx, elfy in elfpos:
        hasneighbour = False
        for dx, dy in directions:
            checkx, checky = elfx + dx, elfy + dy
            if (checkx, checky) in elfpos:
                hasneighbour = True
        if not hasneighbour:
            continue

        for direction in priorities:
            if direction(elfx, elfy):
                # print(elfx, elfy, direction.__name__)
                break

def N(elfx, elfy):
    # North
    elfexists = False
    for dx, dy in ((0,-1),(1,-1),(-1,-1)):
        checkx, checky = elfx + dx, elfy + dy
        if (checkx, checky) in elfpos:
            elfexists = True
    if not elfexists:
        if (elfx, elfy - 1) in proposed:
            removepropose.add((elfx, elfy - 1))
        else:
            proposed[(elfx, elfy - 1)] = (elfx, elfy)
        return True

def S(elfx, elfy):
    elfexists = False

    for dx, dy in ((0,1),(1,1),(-1,1)):
        checkx, checky = elfx + dx, elfy + dy
        if (checkx, checky) in elfpos:
            elfexists = True
    if not elfexists:
        if (elfx, elfy + 1) in proposed:
            removepropose.add((elfx, elfy + 1))
        else:
            proposed[(elfx, elfy + 1)] = (elfx, elfy)
        return True

def E(elfx, elfy):
    elfexists = False
    for dx, dy in ((1,0),(1,1),(1,-1)):
        checkx, checky = elfx + dx, elfy + dy
        if (checkx, checky) in elfpos:
            elfexists = True
    if not elfexists:
        if (elfx + 1, elfy) in proposed:
            removepropose.add((elfx + 1, elfy))
        else:
            proposed[(elfx + 1, elfy)] = (elfx, elfy)
        return True

def W(elfx, elfy):
    elfexists = False
    for dx, dy in ((-1,0),(-1,1),(-1,-1)):
        checkx, checky = elfx + dx, elfy + dy
        if (checkx, checky) in elfpos:
            elfexists = True
    if not elfexists:
        if (elfx - 1, elfy) in proposed:
            removepropose.add((elfx - 1, elfy))
        else:
            proposed[(elfx - 1, elfy)] = (elfx, elfy)
        return True

directions = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]

priorities = deque([N, S, W, E])
amt = 0
# for _ in range(10):
while True:
    if amt % 100 == 0:
        print(amt)
    proposed = {}
    removepropose = set()

    firsthalf()
    priorities.rotate(-1)

    # Second half
    for dupe in removepropose:
        del proposed[dupe]

    if len(proposed) == 0:
        print('pt2', amt + 1)
        break
    amt += 1

    for elfto, elffrom in proposed.items():
        elfpos.remove(elffrom)
        elfpos.add(elfto)

    # printboard()

minx = min(x[0] for x in elfpos)
maxx = max(x[0] for x in elfpos)
miny = min(x[1] for x in elfpos)
maxy = max(x[1] for x in elfpos)

empty = 0
for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        if (x,y) not in elfpos:
            empty += 1

# print("pt1",empty)
