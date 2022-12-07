# I spent 40 minutes doing this
import collections

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

curr_dir = []
sizes = collections.defaultdict(lambda: 0)
for cmd in IN:
    if cmd[0] == "$":
        name = cmd.split(' ')[1]
        if name == "cd":
            arg = cmd.split(' ')[2]
            # if arg == "/":
            #     curr_dir = []
            if arg == "..":
                curr_dir.pop()
            else:
                curr_dir.append(arg)
    else:
        a, b = cmd.split()
        if a == 'dir':
            ...
        else:
            for i in range(len(curr_dir)):
                # add to parent dirs too
                sizes[''.join(x for x in curr_dir[:i+1])] += int(a)

print(sum([v for v in sizes.values() if v <= 100000]))

total_size = sizes['/']
# print(total_size)
needed = total_size - (70000000 - 30000000)

min_size = 999999999999999
for v in sizes.values():
    if v >= needed:
        min_size = min(min_size, v)

print(min_size)
