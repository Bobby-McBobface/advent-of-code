# Spent 50 mins on this, so much debugging needed

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

grid = [[int(y) for y in x] for x in IN]

visible = set()
# left
for x in range(len(grid)):
    for y in range(len(grid[x])): 
        try:
            if max(grid[x][:y]) < grid[x][y]:
                visible.add((x,y))
        except:
            # max arg is empty
            visible.add((x,y))

# right
for x in range(len(grid)):
    for y in range(len(grid[x])): 
        try:
            if max(grid[x][::-1][:y]) < grid[x][::-1][y]:
                visible.add((x,-1+(len(grid)-y)))
        except:
            # max arg is empty
            visible.add((x,y))

# rotate 90 degrees clockwise
rgrid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0])-1,-1,-1)]

# up
for x in range(len(rgrid)):
    for y in range(len(rgrid[x])): 
        # M[j][m+1-i]
        try:
            if max(rgrid[x][:y]) < rgrid[x][y]:
                visible.add((y, len(rgrid)-x-1))
        except:
            # max arg is empty
            visible.add((y, len(rgrid)-x-1))

# down
for x in range(len(rgrid)):
    for y in range(len(rgrid[x])): 
        try:
            if max(rgrid[x][::-1][:y]) < rgrid[x][::-1][y]:
                # damn that index took 5mins debugging to find, kept thinking it was [y][len(rgrid)-(-1+(len(grid)-x))-1]
                visible.add((-1+(len(grid)-y), len(rgrid)-x-1))
        except:
            # max arg is empty
            visible.add((-1+(len(grid)-y), len(rgrid)-x-1))

# edges (idk why some aren't counted)
for x in range(len(grid)):
    for y in range(len(grid[x])): 
        if x == len(grid)-1 or y == len(grid)-1:
            visible.add((x, y))

print(len(visible))

# me when the part 1 code can't be used for part 2
max_dist = 0
for x in range(len(grid)):
    for y in range(len(grid)):
        dist = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            curr_dist = 0
            start = grid[x][y]
            newx = x + dx
            newy = y + dy
            # Put a while True:, then break on IndexError; that took 30 mins to debug (idk why it's broken)
            while 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                curr_dist += 1
                if grid[newx][newy] >= start:
                    break
                newx = newx + dx
                newy = newy + dy

            dist.append(curr_dist)
        max_dist = max(max_dist, dist[0] * dist[1] * dist [2] * dist[3])

print(max_dist)
