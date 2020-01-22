fte = input("What file to execute?> ")

a="0"
b="0"
c="0"
d="0"
e="0"
f="0"
g="0"
h="0"
cell=""

def lts(s):  
    str1 = ""    
    for ele in s:  
        str1 += ele     
    return str1 

def Forward():
  if cell == "":
    return "a"
  if cell == "a":
    return "b"
  if cell == "b":
    return "c"
  if cell == "c":
    return "d"
  if cell == "d":
    return "e"
  if cell == "e":
    return "f"
  if cell == "f":
    return "g"
  if cell == "g":
    return "h"
  if cell == "h":
    return ""

def GetCell():
  if cell == "":
    return "nocell"
  if cell == "a":
    return "a"
  if cell == "b":
    return "b"
  if cell == "c":
    return "c"
  if cell == "d":
    return "d"
  if cell == "e":
    return "e"
  if cell == "f":
    return "f"
  if cell == "g":
    return "g"
  if cell == "h":
    return "h"

def Backward():
  if cell == "":
    return "h"
  if cell == "a":
    return ""
  if cell == "b":
    return "a"
  if cell == "c":
    return "b"
  if cell == "d":
    return "c"
  if cell == "e":
    return "d"
  if cell == "f":
    return "e"
  if cell == "g":
    return "f"
  if cell == "h":
    return "g"

with open(fte, 'r') as fte2:
    for row in fte2:
      for x in str(row):
        if x == "!":
          cell = Forward()
        if x == "?":
          cell = Backward()
        if x == "#":
          x2 = str(a + b + c + d + e + f + g + h)
          x3 = lts(x2)
          print(x3)
        if x == "+":
          if cell == "a":
            if a == "0":
              a = "1"
          if cell == "b":
            if b == "0":
             b = "1"
          if cell == "c":
            if c == "0":
             c = "1"
          if cell == "d":
            if d == "0":
             d = "1"
          if cell == "e":
            if e == "0":
             e = "1"
          if cell == "f":
            if f == "0":
             f = "1"
          if cell == "g":
            if g == "0":
             g = "1"
          if cell == "h":
            if h == "0":
             h = "1"
        if x == ".":
          print(cell)
        if x == ",":
          a = "0"
          b = "0"
          c = "0"
          d = "0"
          e = "0"
          f = "0"
          g = "0"
          h = "0"
          cell = ""
