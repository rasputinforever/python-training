# loops over all numbers from X (user input) to 1, delivering all roots of each and ending with an array of each of the primes found
x = input("What number?")

rootArr = []
primeArr = []

def getMod(x, y):
    return x % y

def getRoot(num):
    curNum = int(num)
    for i in range(curNum):
        if i != 0 and getMod(curNum, i + 1) == 0:
            rootArr.append(i + 1)
            curNum = int(curNum / (i + 1))
            getRoot(curNum)
            break

def allRoots(x):
    getRoot(x)
    if len(rootArr) > 1:
        print("All roots of", x, ":", rootArr)
        rootArr.clear()
    else:
        print(x, "is a PRIME number!")
        rootArr.clear()
        primeArr.append(x)


def primeLooper(val):
    j = int(val)
    for i in range(j):
        allRoots(j - i)
    print("All primes from", j, "to 1:",primeArr)
        

primeLooper(x)

## very slow as it manually checks every single divisor
