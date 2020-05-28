a, b, c, d, e, f, g, h = '00000000'
cell = ''
with open(input('What file to execute?> '), 'r') as F:
    for row in F:
      for x in str(row):
        if x == '!':
          if cell == '': cell = 'a'
          elif 'a' <= cell <= 'g': cell = chr(ord(cell) + 1)
          elif cell == 'h': cell = ''
        if x == '?':
          if cell == '': cell = 'h'
          elif cell == 'a': cell = ''
          elif 'b' <= cell <= 'h': cell = chr(ord(cell) - 1)
        if x == '#':
          print(a + b + c + d + e + f + g + h)
        if x == "+":
          if cell == 'a' and a == '0': a = '1'
          elif cell == 'b' and b == '0': b = '1'
          elif cell == 'c' and c == '0': c = '1'
          elif cell == 'd' and d == '0': d = '1'
          elif cell == 'e' and e == '0': e = '1'
          elif cell == 'f' and f == '0': f = '1'
          elif cell == 'g' and g == '0': g = '1'
          elif cell == 'h' and h == '0': h = '1'
        if x == ".":
          print(cell)
        if x == ",":
          a, b, c, d, e, f, g, h = '00000000'
          cell = ''
