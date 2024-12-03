import re
lines = open("input.txt", "r").read()

x = re.findall("mul\([0-9]*,[0-9]*\)", lines)

sum = 0
for i in x:
    sum += int((i[4:len(i)-1]).split(',')[0]) * int((i[4:len(i)-1]).split(',')[1])

print(sum)
