# Returns an array of primes from 1 to USER INPUT value

loopCount = input("FInd all primes from 1 to _________:")

primeArr = []

def getMod(x, y):
    return int(x) % int(y)

def findRoot(val):
    rootArr = []
    x = int(val)

    for i in range(int(x)):
        if (int(x) % (int(x) - i)) == 0:
            rootArr.append(i + 1)
    if len(rootArr) == 2:
        primeArr.append(val)

def loopOverAll(loop):
    for i in range(loop):
        findRoot(i + 1)
    print(primeArr)
    print("There are", len(primeArr), "primes from 1 to ", loop)

loopOverAll(int(loopCount))