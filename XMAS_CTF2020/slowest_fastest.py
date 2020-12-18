from telnetlib import Telnet
from copy import copy
import math

def feedIn(n, k, p, q, v0, a, c, mod):
    slowBot = p
    fastBot = q
    numFastBots = n - k
    if p > q:
        slowBot = q
        fastBot = p
        numFastBots = k

    v = [0] * n
    v[0] = v0
    for i in range (1, n):
        v[i] = (a * v[i - 1] + c) % mod
    # return goThroughSimulation(n, numFastBots, slowBot, fastBot, copy(v))
    return minDays(n, numFastBots, slowBot, fastBot, copy(v))


def parseSlowestFastest(tn):
    line = tn.read_until(b"N = ")
    print(line)
    n = tn.read_until(b",")
    n = int(n[:-1])
    print(f"n = {n}")
    tn.read_until(b" K = ")
    k = int(tn.read_until(b"\n"))
    print(f"k = {k}")
    tn.read_until(b"P = ")
    p = tn.read_until(b",")
    p = int(p[:-1])
    print(f"p = {p}")
    tn.read_until(b" Q = ")
    q = int(tn.read_until(b"\n"))
    print(f"q = {q}")

    slowBot = p
    fastBot = q
    numFastBots = n - k
    if p > q:
        slowBot = q
        fastBot = p
        numFastBots = k

    v = [0] * n
    tn.read_until(b"v[1] = ")
    v0 = tn.read_until(b",")
    v[0] = int(v0[:-1])
    # print(f"v[0] = {v[0]}")

    tn.read_until(b"a = ")
    a = tn.read_until(b",")
    a = int(a[:-1])
    # print(f"a = {a}")

    tn.read_until(b"c = ")
    c = tn.read_until(b",")
    c = int(c[:-1])
    # print(f"c = {c}")

    tn.read_until(b"mod = ")
    mod = int(tn.read_until(b"\n"))
    # print(f"mod = {mod}")

    # Given v[0], N, compute the rest of v
    # v[i] = (a * v[i - 1] + c) % mod for all i = 2, n
    # print(f"v[0] = {v[0]}")
    for i in range (1, n):
        v[i] = (a * v[i - 1] + c) % mod
        # print(f"v[{i}] = {v[i]}")

    # print(minDays(n, numFastBots, slowBot, fastBot, v))
    # print(goThroughSimulation(n, numFastBots, slowBot, fastBot, copy(v)))
    return minDays(n, numFastBots, slowBot, fastBot, v)

def goThroughSimulation(n, numFastBots, slowBot, fastBot, v):
    days = 0
    while(v != [0] * len(v)):
        v.sort()
        days += 1
        # print(v)
        for i in range(len(v)):
            if i < n - numFastBots:
                v[i] -= slowBot
            else:
                v[i] -= fastBot
            if v[i] < 0:
                v[i] = 0

    answer = bytearray()
    answer += str(days).encode()
    answer += b"\n"
    return answer


# n rooms/bots
# k P bots, n-k Q bots
# p gifts/day for P bot
# q gifts/day for Q bot
# v[i] gifts needed in ith room
def canCompleteWork(n, numFastBots, slowBot, fastBot, v, days):
    fastBotUnits = 0
    # Assume each room has the slower bot working in it for the entire duration
    for work in v:
        work -= slowBot * days
        roomFastBotUnits = 0
        if work > 0:
            if fastBot == slowBot:
                return False
            roomFastBotUnits = math.ceil(work / (fastBot - slowBot))
        fastBotUnits += roomFastBotUnits
        if roomFastBotUnits > days:
            return False

    return fastBotUnits <= (numFastBots * days)

# Try a binary search through the number of days until we find the minimum that can complete all the work
def minDays(n, numFastBots, slowBot, fastBot, v):
    minBound = min(v) // fastBot
    maxBound = max(v) // slowBot + 1
    mid = 0

    # If the bots can complete the work in i days, try fewer days, vice versa
    # until we find the boundary between being able to complete/not complete the work
    while maxBound > minBound:
        mid = (minBound + maxBound) // 2
        # print(f"mid = {mid}")
        if canCompleteWork(n, numFastBots, slowBot, fastBot, v, mid):
            # print("true")
            maxBound = mid
        else:
            # print("false")
            minBound = mid + 1

    mid = (minBound + maxBound) // 2
    # print(mid)
    answer = bytearray()
    answer += str(mid).encode()
    answer += b"\n"
    return answer

# print(canCompleteWork(2, 1, 1, 5, [6, 1], 2))
# print(minDays(2, 1, 1, 5, [6, 1]))
# print(minDays(7, 3, 107, 111, [95056, 19876, 73969, 95875, 94902, 1495, 15801]))
# print(canCompleteWork(7, 3, 107, 111, [95056, 19876, 73969, 95875, 94902, 1495, 15801], 864))
# print(canCompleteWork(7, 3, 107, 111, [95056, 19876, 73969, 95875, 94902, 1495, 15801], 863))
with Telnet('challs.xmas.htsp.ro', 6055) as tn:
    while True:
        problem = tn.read_until(b"Test number:")
        print(problem)
        # def feedIn(n, k, p, q, v, a, c, mod):
        # print(feedIn(7, 2, 137, 210, 2769, 76090, 42886, 100001))
        answer = parseSlowestFastest(tn)
        # print(answer)
        tn.write(answer)

        line = tn.read_until(b"\n")
        print(line)
        if b'X-MAS{' in line:
            print(line)
            break
        if b'That is not the correct answer!' in line:
            print(line)
            break
