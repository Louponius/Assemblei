import sys

if len(sys.argv) == 1:
    print("Usage: python3 encoder.py [FILE]")
    quit(0)

with open(sys.argv[1], 'r') as F:
    while 1:
        ch = F.read(1)
        if not ch:
            break
        if ch == '\n':
            print('@', end='')
            continue
        for x in '{0:08b}'.format(ord(ch), 'b'):
            print('!', end='')
            if x == '1':
                print('+', end='')
        print('$,', end='')
