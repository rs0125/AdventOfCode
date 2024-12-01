f = open("input.txt", "r")
lines = f.readlines()

list1 = []
list2 = []

for i in range(len(lines)):
    temp = lines[i].split()
    list1.append(int(temp[0]))
    list2.append(int(temp[1]))

list1.sort()
list2.sort()

sum = 0

for i in range(len(list1)):
    sum += abs(list2[i] - list1[i])

print(sum)