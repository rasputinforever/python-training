# All roots of a given value are returned as an array
x = input("What number? ")


rootArr = []

def getMod(x, y):
    return x % y

def getRoot(num):
    curNum = int(num)
    for i in range(curNum):
        if i != 0 and getMod(curNum, i + 1) == 0:
            print(i + 1, "is a factor of", curNum)
            rootArr.append(i + 1)
            curNum = int(curNum / (i + 1))
            getRoot(curNum)
            break

def allRoots(x):
    getRoot(x)
    if len(rootArr) > 1:
        print("All roots of", x, ":", rootArr)
        print(x,"has",len(rootArr),"roots!")
    else:
        print(x, "is a PRIME number!")

allRoots(x)