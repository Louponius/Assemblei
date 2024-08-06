import sys
if len(sys.argv) == 1: print("Usage: python3 interpreterplus.py [FILE]"); quit(0)
cells = [False,False,False,False,False,False,False,False]; current_cell = -1
with open(sys.argv[1], 'r') as F:
    while 1:
        ch = F.read(1)
        if not ch: break
        match ch:
            case '!':
                if current_cell > 7: current_cell = -1
                current_cell += 1
            case '?':
                if current_cell < 1: current_cell = 9
                current_cell -= 1
            case '#':
                for cell in cells: print('1' if cell else '0', end = '')
            case '.': print("abcdefgh"[current_cell], end='')
            case ',': cells = [False,False,False,False,False,False,False,False];  current_cell = -1
            case '+': cells[current_cell] = True
            case '$':
                tmp = ""
                for cell in cells: tmp += '1' if cell else '0';
                print(chr(int(tmp, 2)), end='')
            case '@': print('\n', end='')
            case _: pass
