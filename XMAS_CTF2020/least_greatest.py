from telnetlib import Telnet
from sympy.ntheory import factorint

def parseLeastGreatest(tn):
    answer = bytearray()

    # Read in the next line
    line = tn.read_until(b"\n")
    print(line)
    gcd = int(line.decode("utf-8").split('gcd(x, y) = ')[1])
    # Read in the next line, b"k1 = x\n"
    line = tn.read_until(b"\n")
    lcm = int(line.decode("utf-8").split('lcm(x, y) = ')[1])

    answer += str(numFactorPairsCooler(gcd, lcm)).encode()
    # answer += str(numFactorPairs(gcd, lcm)).encode()
    answer += b"\n"
    return answer

# lcm(x, y) = (x * y)/gcd(x, y)
# Given the prime factors of (x * y) and of gcd(x * y):
# x must have at least prime factors of gcd
def numFactorPairsCooler(gcd, lcm):
    return 2 ** len(factorint(lcm // gcd).keys())

def numFactorPairs(gcd, lcm):
    print("Started computering")
    factors = factorint(lcm * gcd)
    # lcmFactors = factorint(lcm)
    gcdFactors = factorint(gcd)
    # print(factors)
    # print(lcmFactors)
    # print(gcdFactors)
    for f in gcdFactors:
        factors[f] -= 2 * gcdFactors[f]
    stuff = 0
    for f in factors:
        if factors[f] != 0:
            stuff += 1
    answer = 2 ** stuff
    # print(answer)
    return answer

with Telnet('challs.xmas.htsp.ro', 6050) as tn:
    while True:
        line = tn.read_until(b"\n")
        print(line)
        if b'Test number: ' in line:
            answer = parseLeastGreatest(tn)
            tn.write(answer)
        # Print out the flag when we're done solving
        if b'X-MAS{' in line:
            print(line)
            break
        if b'That is not the correct answer!' in line:
            break
