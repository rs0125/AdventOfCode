import re
x = re.findall("mul\([0-9]*,[0-9]*\)", ''.join(re.findall(r"do\(\)(?:(?!don't\(\)).)*", "do()" + open("input.txt", "r").read() + "don't()", re.DOTALL)))
kumar = 0
for i in x:
    kumar += int((i[4:len(i)-1]).split(',')[0]) * int((i[4:len(i)-1]).split(',')[1])
print(kumar)