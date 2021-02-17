import math

# This should ask for a val and for how many roots (or more) a value should be revealed

chosen = input("What number? ")
rootCount = input("How many Roots? ")

rootArr = []
primeArr = []

def getMod(x, y):
    return x % y

def loopOverPrimeArr(x):
    x = int(x)
    for p in range(len(primeArr)):
        y = int(primeArr[p])
        if (getMod(x, y)) == 0:
            rootArr.append(y)
            x = x / y
    return x

def loopOverAll(x):
    x = int(x)
    for a in range(x):
        y = a + 1
        if y == x and len(rootArr) > 0:
            rootArr.append(y)
            break
        elif y > (x * 0.51):
            break
        elif y > 1 and getMod(x, y) == 0:   
            rootArr.append(y)
            x = x / y
            loopOverAll(x)
    return x

def determineRoots(val):
    x = int(val)
    x2 = int(loopOverPrimeArr(val))
    if x2 > 1:
        loopOverAll(x2)
        if len(rootArr) == 0:
            primeArr.append(x)
        else:
            if len(rootArr) >= int(rootCount):
                print(x, "has", rootCount,"or more roots. Here they are:",rootArr)

def primeLooper(val):
    x = int(val)
    for i in range(x):
        rootArr.clear()
        determineRoots(i + 1)

primeLooper(chosen)