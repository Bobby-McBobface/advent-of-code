# help how to do part 2
with open("in.txt") as _:
    f = _.read().split("\n\n")
    IN = [x for x in f]

gridinput = IN[0].splitlines()
pathinput = IN[1]

grid = {}

i = 0
for row in gridinput:
    j = 0
    for val in row:
        if val == "." or val == "#":
            grid[(j,i)] = val
        j += 1
    i += 1

path = []
pathinput = pathinput.replace("R", " R ").replace("L", " R R R ")
for x in pathinput.split(' '):
    if x.isnumeric():
        path.append(int(x))
    else:
        path.append(x)

x = 50
y = 0
print(grid[x,y])
print(len(gridinput), len(gridinput[0]))
dx = 1
dy = 0

for step in path:
    if isinstance(step, int):
        for _ in range(step):
            x, y = (x + dx) % len(gridinput[0]), (y + dy) % len(gridinput)
            # wraparound
            while grid.get((x, y)) is None:
                x, y = (x + dx) % len(gridinput[0]), (y + dy) % len(gridinput)
            if grid.get((x, y)) == "#":
                x, y = (x - dx) % len(gridinput[0]), (y - dy) % len(gridinput)
                # Unwrap
                while grid.get((x, y)) is None:
                    x, y = (x - dx) % len(gridinput[0]), (y - dy) % len(gridinput)
                break
    elif step == "R":
        if (dx, dy) == (1,0):
            # print('d')
            dx, dy = 0, 1
        elif (dx, dy) == (-1,0):
            # print('u')
            dx, dy = 0, -1
        elif (dx, dy) == (0,1):
            # print('l')
            dx, dy = -1, 0
        elif (dx, dy) == (0,-1):
            # print('r')
            dx, dy = 1, 0 

print((dx,dy), 1000 * (y + 1), 4 * (x + 1))

#  00  12
#  0   3
#  0   4
# 00  56

# ????????
