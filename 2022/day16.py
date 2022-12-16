# 2.5 hours straight without breaks to solve this (with a bit of hints on python discord)
import re
import networkx as nx

def ints(line: str, negatives=1):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

g = nx.Graph()

for valve in IN:
    name = valve.split(' ')[1].strip()
    flow = ints(valve)[0]
    connected = valve.partition('valves')[2].split(",")

    g.add_node(name, flow=flow)
    for x in connected:
        if x:
            g.add_edge(name, x.strip())

def solve(totaltime):
    # name, opened, pressure
    visited: list[tuple[str, frozenset, int]] = [("AA", frozenset(), 0)]
    best: dict[tuple[str, frozenset], int] = {}

    for time in range(1, totaltime + 1):
        # do BFS
        new_visited: list[tuple[str, frozenset, int]] = []
        # For every visited node, visit another node
        for name, opened, pressure in visited:
            # Don't open if something is already better or equal
            if (name, opened) in best and pressure <= best[(name, opened)]:
                continue

            # memoize
            best[(name, opened)] = pressure

            # open this one
            if (flow := g.nodes(data='flow')[name]) > 0 and name not in opened:  # type: ignore
                newset = list(opened)
                newset.append(name)
                newset = frozenset(newset)
                new_visited.append((name, newset, pressure + flow * (totaltime - time)))  # type: ignore

            # travel to next one
            for neigh in g.neighbors(name):
                new_visited.append((neigh, opened, pressure))
            
        visited = new_visited
    return visited

visited = solve(30)
print('pt1', max(x for _,_,x in visited))

visited = solve(26)

mp = 0
mo = frozenset()
for n,o,p in visited:
    if p > mp:
        mp = p
        mo = o

for opnd in mo:
    g.remove_node(opnd)

# BFS again but with the opened nodes removed because the elephant shouldn't double open
visited = solve(26)

print("pt2", mp + max(x for _,_,x in visited))
