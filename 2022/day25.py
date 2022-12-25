with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

nums = []
for snafu in IN:
    val = 0
    place = 1
    for char in snafu[::-1]:
        if char == "-":
            char = -1
        elif char == "=":
            char = -2
        else:
            char = int(char)
        val += char * place
        place *= 5
    nums.append(val)

n = sum(nums)

# Based off googling balanced ternary after some people said balanced quinary in Discord
output = ""
    
while(n > 0):
    rem = n % 5
    if rem == 0:
        output = '0' + output
        n = n // 5
    elif rem == 1:
        output = '1' + output
        n = n // 5
    elif rem == 2:
        output = '2' + output
        n = n // 5
    elif rem == 3:
        output = '=' + output
        n += 2
        n = n // 5
    elif rem == 4:
        output = '-' + output
        n += 1
        n = n // 5

print(output)
