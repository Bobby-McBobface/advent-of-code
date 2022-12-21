# 364 / 1042
with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

monkeys = {}
nums = {}
for monkey in IN:
    name, op = monkey.split(":")
    if op.strip().isnumeric():
        monkeys[name] = int(op)
    else:
        monkeys[name] = op.strip()

# while True: 
#     for name, op in monkeys.items():
#         if isinstance(op, int):
#             nums[name] = op
#         else:
#             m1, sign, m2 = op.split(' ')
#             if m1 in nums and m2 in nums:
#                 nums[name] = eval(f"{nums[m1]} {sign} {nums[m2]}")
#         if name == "root":
#             print(nums.get("root"))
#             sys.exit()
rootop: str
rootop = monkeys["root"]
for i in range(999):
    for monkey in rootop.split(' '):
        if monkey.strip() in monkeys:
            rootop = rootop.replace(monkey, f"( {monkeys[monkey.strip()]} )")

print(rootop.replace(' ', ''))
