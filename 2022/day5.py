import re

def ints(line: str, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

#                 [V]     [C]     [M]
# [V]     [J]     [N]     [H]     [V]
# [R] [F] [N]     [W]     [Z]     [N]
# [H] [R] [D]     [Q] [M] [L]     [B]
# [B] [C] [H] [V] [R] [C] [G]     [R]
# [G] [G] [F] [S] [D] [H] [B] [R] [S]
# [D] [N] [S] [D] [H] [G] [J] [J] [G]
# [W] [J] [L] [J] [S] [P] [F] [S] [L]
#  1   2   3   4   5   6   7   8   9 

stk1 = ['W', 'D', 'G', 'B', 'H', 'R', 'V']
stk2 = ['J', 'N', 'G', 'C', 'R', 'F']
stk3 = ['L', 'S', 'F', 'H', 'D', 'N', 'J']
stk4 = ['J', 'D', 'S', 'V',]
stk5 = ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V']
stk6 = "P G H C M".split(" ")
stk7 = "F J B G L Z H C".split(' ')
stk8 = "S J R".split(' ')
stk9 = "L G S R B N V M".split(' ')
# stk1 = "Z N".split(' ')
# stk2 = "M C D".split(' ')
# stk3 = 'P'.split(' ')

for line in IN:
    amt, frm, to = ints(line)
    # for a in range(amt):
        # eval(f'stk{to}.append(stk{frm}.pop())') # p1
    exec(f'stk{to} = stk{to} + stk{frm}[-{amt}:]')
    exec(f'stk{frm} = stk{frm}[:-{amt}]')

print(stk1[-1],stk2[-1],stk3[-1],stk4[-1],stk5[-1],stk6[-1],stk7[-1],stk8[-1],stk9[-1],sep='')
