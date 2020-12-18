from pwn import *

def parseKrampusLazer(sock):
    sock.recvuntil('Your position: ')
    myx = float(sock.recvuntil(',', drop=True).decode('ascii'))
    myy = float(sock.recvuntil('\n', drop=True).decode('ascii'))
    sock.recvuntil("Krampus' position: ")
    krampusx = float(sock.recvuntil(',', drop=True).decode('ascii'))
    krampusy = float(sock.recvuntil('\n', drop=True).decode('ascii'))
    print(f"Me: ({myx}, {myy}) - Krampus: ({krampusx}, {krampusy})")

    blockersX = placeBlockers(myx, krampusx)
    blockersY = placeBlockers(myy, krampusy)

    for x in blockersX:
        for y in blockersY:
            coord = str(x) + "," + str(y)
            print(coord)
            sock.sendline(coord)

def placeBlockers(me, krampus):
    return [
        (me + krampus) / 2,
        1 - (me + krampus) / 2,
        abs(me - krampus) / 2,
        1 - abs(me - krampus) / 2
    ]

sock = remote('challs.xmas.htsp.ro', 6005)
res = sock.recv(4096,timeout=1)
print(res)
sock.sendline("a")
for _ in range(50):
    parseKrampusLazer(sock)
res = sock.recv(4096,timeout=1)
print(res)
