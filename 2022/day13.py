# 9676 / 9107 after 3hours. Forgot to do it at midnight EST haha rip
import functools

with open("in.txt") as _:
    f = _.read().split("\n\n")
    IN = [x for x in f]

packetpairs: list[tuple] = []

for packetpair in IN:
    packet1, packet2 = packetpair.split('\n')
    packet1 = eval(packet1)
    packet2 = eval(packet2)
    packetpairs.append((packet1, packet2))

def check(pk1, pk2, n=''):
    for left,right in zip(pk1, pk2):
        if isinstance(left, int) and isinstance(right, int):
            # print(n, 'Compare', left, 'vs', right)
            if left < right:
                # print(n, "Left side is smaller, right order")
                return 1
            elif left > right:
                # print(n, "Right side is smaller, wrong order")
                return -1

        elif isinstance(left, list) and isinstance(right, list):
            # print(n, "Compare", left, right)
            if ((x := check(left, right, n + ' -')) != 0):
                return x

        elif isinstance(left, int) and isinstance(right, list):
            # print(n, "Mixed types", left, right)
            if ((x := check([left], right, n + ' -')) != 0):
                return x

        elif isinstance(left, list) and isinstance(right, int):
            # print(n, "Mixed types", left, right)
            if ((x := check(left, [right], n + ' -')) != 0):
                return x

    if len(pk1) < len(pk2):
        # print("Left side ran out, correct order")
        return 1
    elif len(pk1) > len(pk2):
        # print("Right side ran out, wrong order")
        return -1
    return 0

corrects = []
n = 1
for pk1, pk2 in packetpairs:
    # print('== Pair', n, '==')
    if check(pk1, pk2) == 1:
        corrects.append(n)
    n += 1

print(sum(corrects))

packets = [[[2]], [[6]]]
for x, y in packetpairs:
    packets.append(x)
    packets.append(y)

packets.sort(key=functools.cmp_to_key(check), reverse=True)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
