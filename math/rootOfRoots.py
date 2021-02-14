# FIRST, determines if given value is a prime
# IF not, returns array of roots of the value
# IF a root has roots, returns an array of THOSE roots
# continues this until ONLY primes are returned

x = input("What number would you like to find all roots?")

rootArr = []

def findRoot(x):
    for i in range(int(x)):
        if (int(x) % (int(x) - i)) == 0 and i != (int(x) - i) and (int(x) - i) != 1:
            rootArr.append(int(x) - i)
    if len(rootArr) != 1:
        print(x, "is NOT a prime")
        # rootOfRoot(rootArr)
        print("divisors", rootArr)
    else:
        print(x, 'IS a prime!')

# creates sub-arr within main arr and calls back for each of those sub-arrs
def rootOfRoot(arr):
    for i in arr:
        rootOfRootArr = []
        rootIndex = arr.index(i)
        for j in range(i):
            if (i % (i - j)) == 0 and i != (i-j) and (i - j) != 1:
                rootOfRootArr.append(i - j)
        if len(rootOfRootArr) > 0:
            arr[rootIndex] = rootOfRootArr
            rootOfRoot(arr[rootIndex])
    
findRoot(x)
