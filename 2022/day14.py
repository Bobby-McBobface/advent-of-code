# Had an unknown bug in part 1, but got correct answer, then got screwed in pt. 2. Took 1 hour to debug aaaaaaaaa
# 2662 / 4997
import re

def ints(line: str, negatives=1):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

import functools

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

filled: dict[tuple, str] = {}
import more_itertools

for rock in IN:
    connects = ints(rock)
    rock_iter = iter(more_itertools.chunked(connects, 2))
    x1, y1 = next(rock_iter)
    for x2, y2 in rock_iter:
        if x1 == x2:
            if y1 < y2:
                for y in range(y1, y2 + 1):
                    filled[(x1,y)] = "#"
            else:
                for y in range(y2, y1 + 1):
                    filled[(x1,y)] = "#"

        elif y1 == y2:
            if x1 < x2:
                for x in range(x1, x2 + 1):
                    filled[(x,y1)] = "#"
            else:
                for x in range(x2, x1 + 1):
                    filled[(x,y1)] = "#"
        x1 = x2
        y1 = y2

# Part 2 only
maxy = 0
for _, y in filled.keys():
    maxy = max(maxy, y)

maxy += 2

for x in range(0, 9999):
    filled[(x,maxy)] = "#"
# Part 2 only end

count = 0
while True:
    abyss_count = 0
    if filled.get((500, 0)):
        print("breaking")
        break
    sand = (500, 0)

    # print('============')
    while True:
        abyss_count += 1
        if abyss_count >= 1000:
            print(sand, 'sand in abyss')
            break

        moved = False
        # down
        if not filled.get((sand[0], sand[1] + 1)):
            # print("move down")
            sand = (sand[0], sand[1] + 1)
            moved = True
            continue

        # left and down
        if not filled.get((sand[0] - 1, sand[1] + 1)):
            # print("left down")
            sand = (sand[0] - 1, sand[1] + 1)
            moved = True
            continue

        # down right
        if not filled.get((sand[0] + 1, sand[1] + 1)):
            # print("right down")
            sand = (sand[0] + 1, sand[1] + 1)
            moved = True
            continue
            
        if moved == False:
            break

    if abyss_count >= 1000:
        break

    # print('placed', sand)
    filled[sand] = "o"
    count += 1
    # plt.scatter([k[0] for k in filled.keys()], [k[1] for k in filled.keys()])
    # plt.gca().invert_yaxis()
    # plt.ylim(top=0)
    # plt.scatter([k[0] for k,v in filled.items() if v == 'o'], [k[1] for k,v in filled.items() if v == "o"])
    # plt.show()
print(count)
