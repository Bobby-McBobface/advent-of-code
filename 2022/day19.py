# 464 / 2166 (Don't count the pt2 score, I needed to cheat for that)
import re
import collections

def ints(line: str, negatives=1):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

blueprints = []
for blueprint in IN:
    num, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = ints(blueprint)
    blueprints.append((num, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs))

p1 = 0
p2 = 1

for blueprint in blueprints[:3]:
    best_geode = 0
    num, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = blueprint
    ore_bots = 1
    clay_bots = 0
    obs_bots = 0
    geode_bots = 0
    ore = 0
    clay = 0
    obs = 0
    geode = 0

    dp = set()
    queue = collections.deque()
    times = set()
    queue.append((0, ore_bots, clay_bots, obs_bots, geode_bots, ore, clay, obs, geode))

    # Copied from solution megathread
    max_ore_cost = max(obs_ore, ore_ore, clay_ore, geode_ore)

    while queue:
        state = queue.popleft()
        # print(state)
        time, ore_bots, clay_bots, obs_bots, geode_bots, ore, clay, obs, geode = state

        # if ore > 25 or clay > 25 or obs > 25:
        #     continue

        # https://github.com/alexander-yu/adventofcode/blob/d13bcc7fb150515bf40e5eb4c0a2abb398a9d844/problems_2022/19.py#L49
        # I gave up on part 2, had to look at this explaination on what to do, good explanation though
        # I could do part 1 just by brute forcing in a few minutes though
        # In theory if I had more RAM I could have done it
        if time not in times:
            times.add(time)
            print(f'[{num}] Time left: {time:<2} | Queue size: {len(queue)}')

        ore = min(ore, max_ore_cost + (max_ore_cost - ore_bots) * ((32 - time) - 1))
        clay = min(clay, obs_clay + (obs_clay - clay_bots) * ((32 - time) - 1))
        obs = min(obs, geode_obs + (geode_obs - obs_bots) * ((32 - time) - 1))

        state = (time, ore_bots, clay_bots, obs_bots, geode_bots, ore, clay, obs, geode, time)

        if state in dp:
            continue
        dp.add(state)

        time += 1
        if time == 32:
            best_geode = max(best_geode, geode + geode_bots)
            continue

        # Build ore bot
        if ore >= ore_ore:
            queue.append((time, ore_bots + 1, clay_bots, obs_bots, geode_bots, ore - ore_ore + ore_bots, clay + clay_bots, obs + obs_bots, geode + geode_bots))
        # Build clay bot
        if ore >= clay_ore:
            queue.append((time, ore_bots, clay_bots + 1, obs_bots, geode_bots, ore - clay_ore + ore_bots, clay + clay_bots, obs + obs_bots, geode + geode_bots))
        # Build obs bot
        if ore >= obs_ore and clay >= obs_clay:
            queue.append((time, ore_bots, clay_bots, obs_bots + 1, geode_bots, ore - obs_ore + ore_bots, clay - obs_clay + clay_bots, obs + obs_bots, geode + geode_bots))
        # Build geode bot
        if ore >= geode_ore and obs >= geode_obs:
            queue.append((time, ore_bots, clay_bots, obs_bots, geode_bots + 1, ore - geode_ore + ore_bots, clay + clay_bots, obs - geode_obs + obs_bots, geode + geode_bots))

        ore += ore_bots
        clay += clay_bots
        obs += obs_bots
        geode += geode_bots

        queue.append((time, ore_bots, clay_bots, obs_bots, geode_bots, ore, clay, obs, geode))

    # print(num * best_geode)
    # p1 += (num * best_geode)
    print(best_geode)
    p2 *= best_geode

print(p2)
