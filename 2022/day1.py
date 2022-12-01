# 455th place
with open("in.txt") as _:
    f = _.readlines()

l = [x for x in f]

a = 0
b = 0
cal = []
for x in l:
    if x == "\n":
        cal.append(b)
        b = 0
        continue
    b += int(x)

print(max(cal))
print(list(sorted(cal))[-1] + list(sorted(cal))[-2] + list(sorted(cal))[-3])
