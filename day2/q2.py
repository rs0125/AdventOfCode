f = open("input.txt", "r")
lines = f.readlines()

def kumar(temp):
    for i in range(len(temp)-1):
        initdiff = int(temp[0]) - int(temp[1])
        diff = int(temp[i]) - int(temp[i+1])
        if diff == 0:
            return False
        diff = diff * (initdiff)/abs(initdiff)
        if diff > 3:
            return False
        if diff < 1:
            return False
    return True

def kumar2(temp):
    for i in range(len(temp)):
        temp2=temp[:i]+temp[i+1:]
        if kumar(temp2):
           return True
    return False

a =0

for i in range(len(lines)):
    temp = lines[i].split()
    if(kumar(temp) or kumar2(temp)):
        print(temp)
        a+=1

print(a)