# Started 2.5 hr late, submitted at 3:12 and 17399th place lol
from pprint import pprint

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

visited = set()

# head = (0, 0)
# tail = (0, 0)

directions: dict[str, tuple[int, int]] = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

diagonals = [(-1,-1),(-1,1),(1,1),(1,-1)]

def tail_touching(tail, head):
    if tail == head:
        return True
    for v in directions.values():
        newtail = (tail[0] + v[0], tail[1] + v[1])
        if newtail == head:
            return True
    for v in diagonals:
        newtail = (tail[0] + v[0], tail[1] + v[1])
        if newtail == head:
            return True
    return False

visualise = [['.','.','.','.','.'] for x in range(6)]

def pprint_board(head, tail):
    visualise[head[0]][head[1]] = 'H'
    visualise[tail[0]][tail[1]] = 'T'
    pprint([[visualise[j][i] for j in range(len(visualise))] for i in range(len(visualise[0])-1,-1,-1)])
    visualise[head[0]][head[1]] = '.'
    visualise[tail[0]][tail[1]] = '.'

knots: list[tuple[int,int]] = [(0,0) for _ in range(10)]

for move in IN:
    direction, steps = move.split(' ')
    steps = int(steps)
    for _ in range(steps):
        knots[0] = (knots[0][0] + directions[direction][0], knots[0][1] + directions[direction][1])
        for knot_index in range(9):
            visited.add(knots[-1])
            # knots[knot_index + 1]
            # move head
            if not tail_touching(knots[knot_index + 1], knots[knot_index]):
                # move tail
                relx, rely = knots[knot_index + 1][0] - knots[knot_index][0], knots[knot_index + 1][1] - knots[knot_index][1]

                # straight
                if rely == 0:
                    if relx > 0:
                        knots[knot_index + 1] = (knots[knot_index + 1][0] - 1, knots[knot_index + 1][1])
                        continue
                    else:
                        knots[knot_index + 1] = (knots[knot_index + 1][0] + 1, knots[knot_index + 1][1])
                        continue

                if relx == 0:
                    if rely < 0:
                        knots[knot_index + 1] = (knots[knot_index + 1][0], knots[knot_index + 1][1] + 1)
                        continue
                    else:
                        knots[knot_index + 1] = (knots[knot_index + 1][0], knots[knot_index + 1][1] - 1)
                        continue

                # diags
                if(relx<0 and rely<0):
                    knots[knot_index + 1] = (knots[knot_index + 1][0] + 1, knots[knot_index + 1][1] + 1)
                    continue
                elif(relx<0 and rely>0):
                    knots[knot_index + 1] = (knots[knot_index + 1][0] + 1, knots[knot_index + 1][1] - 1)
                    continue
                elif(relx>0 and rely>0):
                    knots[knot_index + 1] = (knots[knot_index + 1][0] - 1, knots[knot_index + 1][1] - 1)
                    continue
                else:
                    knots[knot_index + 1] = (knots[knot_index + 1][0] - 1, knots[knot_index + 1][1] + 1)
                    continue

        visited.add(knots[-1])

print(len(visited))
