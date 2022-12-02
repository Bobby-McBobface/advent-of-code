# 3506 / 1572 place
# Started a bit late, got 2 wrong answers due to not reading fully
with open("in.txt") as _:
    f = _.read().split("\n")

l = [x for x in f]

score = 0
for game in l:
    opp, you = game.split()
    if you == "X":
        score+=1
        if opp == "C":
            score +=6
        elif opp == "A":
            score += 3
    elif you == "Y":
        score +=2
        if opp == "A":
            score += 6
        elif opp == "B":
            score += 3
    elif you == "Z":
        score +=3
        if opp == "B":
            score += 6
        elif opp == "C":
            score += 3
print(score)

score = 0
for game in l:
    opp, res = game.split()
    if res == "X":
        score += 0
        if opp == "A":
            score += 3 
        elif opp == "B":
            score += 1
        else:
            score += 2
    elif res == "Y":
        score += 3
        if opp == "A":
            score += 1
        elif opp == "B":
            score += 2
        else:
            score += 3
    else:
        score += 6
        if opp == "A":
            score += 2
        elif opp == "B":
            score += 3
        else:
            score += 1

print(score)
