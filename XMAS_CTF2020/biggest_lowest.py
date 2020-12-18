from telnetlib import Telnet
import ast

# Assume passed in tn is in this state such that it will pass bytearrays like so:
# b"Test number: 1/50\n"
# b"array = [1, 5, 7, 3, 1]\n"
# b"k1 = 4\n"
# b"k2 = 2\n"
def parseBiggestLowest(tn):
    array = []
    k1 = 0
    k2 = 0
    answer = bytearray()

    # Read in the next line, b"array = []\n"
    line = tn.read_until(b"\n")
    if b'array = ' in line:
        # Parse the bytearray into an integer array, then sort it
        array = ast.literal_eval(line.decode("utf-8").split('array = ')[1])
        array.sort()
        # Read in the next line, b"k1 = x\n"
        line = tn.read_until(b"\n")
        k1 = int(line.decode("utf-8").split('k1 = ')[1])
        # Read in the next line, b"k2 = y\n"
        line = tn.read_until(b"\n")
        k2 = int(line.decode("utf-8").split('k2 = ')[1])

    # Assemble answer of a comma separated list of first k1 elements increasing,
    # a semicolon, then a comma separated list of the last k2 elements decreasing
    for i in range(0, k1):
        answer.extend(str(array[i]).encode())
        if i != (k1 - 1):
            answer += b", "
    answer += b"; "

    for i in range(0, k2):
        index = i * (-1) - 1
        answer.extend(str(array[index]).encode())
        if i != (k2 - 1):
            answer += b", "

    answer += b"\n"
    return answer

with Telnet('challs.xmas.htsp.ro', 6051) as tn:
    while True:
        line = tn.read_until(b"\n")
        if b'Test number: ' in line:
            answer = parseBiggestLowest(tn)
            tn.write(answer)
        # Print out the flag when we're done solving
        if b'X-MAS{' in line:
            print(line)
            break
