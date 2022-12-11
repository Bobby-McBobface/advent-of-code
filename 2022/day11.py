import re
import collections
import math

def ints(line: str, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

with open("in.txt") as _:
    f = _.read().split("\n\n")
    IN = [x for x in f]


class Monkey:
    def __init__(self, monk) -> None:
        self.id = monk[0]
        self.items = collections.deque(ints(monk[1]))
        self.operation = lambda o: eval(monk[2].split('=')[1], {'old': o})
        self.test_divisible_by = ints(monk[3])[0]
        self.if_true = ints(monk[4])[0]
        self.if_false = ints(monk[5])[0]
        self.playtime = 0

    def __repr__(self) -> str:
        return f"{self.id} {self.playtime}"

    def play(self):
        for item in self.items:
            self.playtime += 1
            playing = item
            # print("Monkey inspects an item with a worry level of", playing)
            worry = self.operation(playing)
            # print("Worry level is", new_worry)
            # worry = worry // 3
            worry = worry % lcm
            # print("Monkey gets bored with item. ", worry)
            if worry % self.test_divisible_by == 0:
                # print("Item", worry, "divisible by", self.test_divisible_by)
                # print("Item thrown to", self.if_true)
                monkeys[self.if_true].items.append(worry)
            else:
                # print("Item", worry, "NOT divisible by", self.test_divisible_by)
                # print("Item thrown to", self.if_false)
                monkeys[self.if_false].items.append(worry)
        self.items = []

        
monkeys: list[Monkey] = []

for monkey in IN:
    monk = monkey.split('\n')
    monkeys.append(Monkey(monk))

# Had to get a hint about "modular arithmetic" to get this
# Couldn't even get past 100 rounds without it
lcm = math.lcm(*(x.test_divisible_by for x in monkeys))

for i in range(10000):
    if i % 1000 == 0:
        print(i)
    for j in monkeys:
        j.play()

sort = sorted(monkeys, key=lambda x: x.playtime)
print(sort[-1].playtime * sort[-2].playtime)
