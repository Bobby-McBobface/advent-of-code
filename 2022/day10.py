# Easy one today, CRT a bit hard to understand 408 / 1185
with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

X = 1
clock = 0

sigs = []

screen = [['.' for _ in range(40)] for _ in range(6)]

for line in IN:
    if line == "noop":
        sprite_pos = [(X), (X-1), (X+1)]
        if clock % 40 in sprite_pos:
            screen[clock//40][clock%40] = "#"
        clock += 1
        if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
            sigs.append(X*clock)
        
    else:
        _, num = line.split(' ')
        num = int(num)

        sprite_pos = [(X), (X-1), (X+1)]
        if clock % 40 in sprite_pos:
            screen[clock//40][clock%40] = "#"
        clock += 1
        if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
             sigs.append(X*clock)

        sprite_pos = [(X), (X-1), (X+1)]
        if clock % 40 in sprite_pos:
            screen[clock//40][clock%40] = "#"
        clock += 1
        if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
            sigs.append(X*clock)

        X += num
 
print(sum(sigs))
for x in screen:
    print(''.join(x))
