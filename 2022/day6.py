# 3005 / 4304
with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

IN = IN[0]

for i in range(len(IN)):
    nums = set(IN[i:i+4])
    if len(nums) == 4:
        print(i + 4)
        break

for i in range(len(IN)):
    nums = set(IN[i:i+14])
    if len(nums) == 14:
        print(i + 14)
        break
