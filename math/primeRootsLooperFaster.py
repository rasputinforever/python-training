import math

# starts from 1 and builds up the prime arr as it goes which is used for reference on the rest of the values
chosen = input("What number?")

rootArr = []
primeArr = []

def getMod(x, y):
    return x % y

# does this first, checking through each found prime BEFORE moving onto the slower method of finding roots.
def loopOverPrimeArr(x):
    x = int(x)
    for p in range(len(primeArr)):
        y = int(primeArr[p])
        if (getMod(x, y)) == 0:
            rootArr.append(y)
            x = x / y
    return x

# can this go faster?
def loopOverAll(x):
    x = int(x)
    for a in range(x):
        y = a + 1
        if y == x and len(rootArr) > 0:
            rootArr.append(y)
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
            print(x,"is a prime!")
            primeArr.append(x)
        else:
            print("all roots of",x,":",rootArr)

def primeLooper(val):
    x = int(val)
    for i in range(x):
        rootArr.clear()
        determineRoots(i + 1)
    print("All primes from 1 to",x,":",primeArr)

primeLooper(chosen)

## very slow as it manually checks every single divisor
