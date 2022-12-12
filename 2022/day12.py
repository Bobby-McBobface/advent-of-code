# 710 / 729, needs to manually input end and start point, and replace S with a and E with z in input file
import networkx as nx

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

# Damnit I had a undirected graph and that took 8 minutes to debug
g = nx.DiGraph()

directions = [(0,1),(1,0),(0,-1),(-1,0)]

maze = [x for x in IN]

def is_valid(x,y, nx, ny):
  if (nx < 0 or ny < 0):
    return False
  if (nx >= len(maze) or ny >= len(maze[0])):
    return False
  old = string.ascii_lowercase.index(maze[x][y])
  new = string.ascii_lowercase.index(maze[nx][ny])
  if (old + 1) >= new:
    return True
  return False

for x in range(len(maze)):
  for y in range(len(maze[0])):
    for dx, dy in directions:
      if is_valid(x,y, x+dx, y+dy):
        g.add_edge((x,y),(x+dx,y+dy))

shortest = 99999

for x in range(len(maze)):
  for y in range(len(maze[0])):
    if maze[x][y] == 'a':
        try:
            shortest = min(shortest, len(nx.dijkstra_path(g, (x,y), (20, 148))))
        except:
            pass
print(shortest)

