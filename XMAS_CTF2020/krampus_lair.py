from telnetlib import Telnet

def textAdventureLook(tn):
    tn.write(str('look').encode('ascii') + b"\n")
    line = tn.read_until(b"> ")
    print(line.decode('utf-8'))

def textAdventureDo(tn, cmd, arg):
    cmd += ' ' + arg
    print(cmd)
    tn.write(cmd.encode('ascii') + b"\n")
    line = tn.read_until(b"> ")
    print(line.decode('utf-8'))

def textAdventure(tn):
    # Starting Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'move', 'east')

    # Can/Water/Bow Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'take', 'can')

    textAdventureLook(tn)
    textAdventureDo(tn, 'use', 'can')

    textAdventureLook(tn)
    textAdventureDo(tn, 'take', 'bow')

    textAdventureLook(tn)
    textAdventureDo(tn, 'move', 'west')
    textAdventureDo(tn, 'move', 'north')

    # Krampus Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'move', 'east')

    # Wooden Sign Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'read', 'sign')
    textAdventureDo(tn, 'move', 'east')

    # Metal Sign Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'read', 'sign')
    textAdventureDo(tn, 'move', 'east')

    # Gem Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'take', 'gem')
    textAdventureDo(tn, 'move', 'west')
    textAdventureDo(tn, 'move', 'west')
    textAdventureDo(tn, 'move', 'west')
    textAdventureDo(tn, 'move', 'west')

    # Fireflies Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'use', 'can')
    textAdventureLook(tn)
    textAdventureDo(tn, 'take', 'snare')
    textAdventureLook(tn)
    textAdventureDo(tn, 'move', 'east')
    textAdventureDo(tn, 'move', 'south')
    textAdventureDo(tn, 'move', 'west')

    # Dark Room
    textAdventureLook(tn)
    textAdventureDo(tn, 'use', 'can')
    textAdventureLook(tn)
    textAdventureDo(tn, 'take', 'timer')
    textAdventureLook(tn)
    textAdventureDo(tn, 'move', 'east')
    textAdventureDo(tn, 'move', 'north')

    # All items collected, Krampus angry
    tn.interact()
     
with Telnet('challs.xmas.htsp.ro', 6001) as tn:
    while True:
        line = tn.read_until(b"> ")
        print(line.decode('utf-8'))
        textAdventure(tn)
