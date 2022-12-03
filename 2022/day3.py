# 1144 / 939
with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

sum = 0
for line in IN:
    fir = line[:len(line) // 2]
    snd = line[len(line) // 2:]
    com: str = list(set(fir) & set(snd))[0] 
    sum += string.ascii_letters.index(com) + 1

print(sum)

sum = 0
ite = iter(IN)
for line in ite:
    line2 = next(ite)
    line3 = next(ite)
    com: str = list(set(line) & set(line2) & set(line3))[0] 
    sum += string.ascii_letters.index(com) + 1

print(sum)
