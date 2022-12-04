# 2752 / 1550
# Just realized why my first solution of (low >= low2 and high >= high2) or (low <= low2 and high <= high2) didn't work because I forgot to parse the ints 💀
with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

count = 0
count2 = 0
for line in IN:
    pair1, pair2 = line.split(',')
    low, high = pair1.split('-')
    low2, high2 = pair2.split('-')
    if all(x in range(int(low), int(high) + 1) for x in range(int(low2), int(high2) + 1)) \
        or all(x in range(int(low2), int(high2) + 1) for x in range(int(low), int(high) + 1)):
        count += 1
    if any(x in range(int(low), int(high) + 1) for x in range(int(low2), int(high2) + 1)) \
       or any(x in range(int(low2), int(high2) + 1) for x in range(int(low), int(high) + 1)):
        count2 += 1
print(count, count2)
