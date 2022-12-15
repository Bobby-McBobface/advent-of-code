import re
import sys

def ints(line: str, negatives=1):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

positions: dict[tuple, tuple] = {}

def manhattan_distance(p, q):
    distance = 0
    for p_i,q_i in zip(p,q):
        distance += abs(p_i - q_i)
    return distance

NUM = 2000000
beacons_at_y = set()
unreachable_y = set()
newlines = []

for line in IN:
    sx, sy, bx, by = ints(line)
    newlines.append(line)

# are u fing serious my y pos was 31300000
# this took ages to run
for NUM in range(3000000,4000000):
    z = []
    if NUM % 10000 == 0:
        print(NUM)
    for line in newlines:
        sx, sy, bx, by = ints(line)
        positions[(sx, sy)] = ("S",)
        positions[(bx, by)] = ("B",)
        dist_to_beacon = manhattan_distance((sx,sy),(bx,by))
        # print(dist_to_beacon)
        if by == NUM:
            beacons_at_y.add(by)

        dist_to_y = manhattan_distance((sx, sy), (sx, NUM))

        # determine how many steps left/right of sx we can go
        squares_at_y = dist_to_beacon - dist_to_y
        #print(squares_at_y)

        if squares_at_y <= 0:
            continue

        left = sx - squares_at_y
        right = sx + squares_at_y
        z.append((left,right))

    z.sort()
    ml = z[0][0]
    mr = 0
    # Ranges should overlap because it's sorted
    # If they don't the beacon is there
    for l, r in z:
        if ml >= l:
            ml = max(ml, r)
        else:
            print("FOUND", (ml + 1) * 4000000 + NUM)
            sys.exit()
