# I now hate BFS (but I can code it up easily now)
from collections import deque

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

class Blizzard:
    def __init__(self, direction, x, y) -> None:
        self.dir = direction
        self.x = x
        self.y = y
        
    @property
    def position(self):
        return (self.x, self.y)

    def move(self):
        if self.dir == ">":
            self.x += 1
            if self.x == endx:
                self.x = 1
        elif self.dir == "<":
            self.x -= 1
            if self.x == 0:
                self.x = endx-1
        elif self.dir == "v":
            self.y += 1
            if self.y == endy:
                self.y = 1
        elif self.dir == "^":
            self.y -= 1
            if self.y == 0:
                self.y = endy-1

blizzards: list[Blizzard] = []
endx, endy = 0, 0
for y, row in enumerate(IN):
    for x, val in enumerate(row):
        if val in "<>^v":
            blizzards.append(Blizzard(val, x, y))
        elif val == "#":
            endx = x
            endy = y

blizzardatmin: list[set[tuple[int,int]]] = []

def nextblizzard():
    blizzardatmin.append(set())
    for blizzard in blizzards:
        blizzard.move()
        blizzardatmin[-1].add(blizzard.position)
    return blizzardatmin[-1]

def bfs(startmin, startx, starty, targetx, targety):
    seen = set()
    q: deque[tuple[int, int, int]] = deque()
    q.append((startmin, startx, starty))
    best = 9999
    while q:
        state = q.popleft()
        if state in seen:
            continue
        minute, x, y = state
        if minute >= best:
            continue
        if (x, y) == (targetx, targety):
            best = min(minute, best)
            continue
        if (x not in range(1,endx) or y not in range(1,endy)) and (x,y) != (startx, starty):
            continue

        seen.add(state)
        try:
            currblizzard = blizzardatmin[minute]
        except IndexError:
            currblizzard = nextblizzard()

        for dx, dy in ((0,0), (1,0), (0,1), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in currblizzard:
                q.append((minute + 1, nx, ny))
    return best

print("pt1", x := bfs(0, 1, 0, endx, endy-1))
x = bfs(x,endx, endy-1, 1, 0)
print("pt2", bfs(x, 1, 0, endx, endy-1))
