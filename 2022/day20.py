with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

nums: list[tuple[int, int]] = []
for id, num in enumerate(IN):
    nums.append((id, int(num) * 811589153))

orig = nums.copy()

for _ in range(10):
    for x in orig:
        pos = nums.index(x)
        _, val = nums.pop(pos)
        newpos = (pos + val) % len(nums)
        nums.insert(newpos, x)  

zeropos = 0
for index, (_, num) in enumerate(nums):
    if num == 0:
        zeropos = index
        break

# print(', '.join(str(x[1]) for x in nums))
print(nums[(zeropos + 1000) % len(nums)][1] + nums[(zeropos + 2000) % len(nums)][1] + nums[(zeropos + 3000) % len(nums)][1])
