import re
lines = open("input.txt", "r").read()

def findkumar(l):
    x = re.findall("mul\([0-9]*,[0-9]*\)", l)


inact = "don't()"
act = "do()"
print(lines.index(act))
print(lines.index("don't()"))


z = re.findall("don't\(\).*do\(\)", lines)

print(z)