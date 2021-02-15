# FIRST, determines if given value is a prime
# IF not, returns array of factors of the value
# IF a factor has factors, returns an array of THOSE factors
# continues this until ONLY primes are returned

x = input("What number would you like to find all factors?")

factorArr = []

def findfactor(x):
    for i in range(int(x)):
        if (int(x) % (int(x) - i)) == 0 and i != (int(x) - i) and (int(x) - i) != 1:
            factorArr.append(int(x) - i)
    if len(factorArr) != 1:
        print(x, "is NOT a prime")
        factorOffactor(factorArr)
    else:
        print(x, 'IS a prime!')

# creates sub-arr within main arr and calls back for each of those sub-arrs
def factorOffactor(arr):
    for i in arr:
        factorOffactorArr = []
        factorIndex = arr.index(i)
        for j in range(i):
            if (i % (i - j)) == 0 and i != (i-j) and (i - j) != 1:
                factorOffactorArr.append(i - j)
        if len(factorOffactorArr) > 0:
            print(arr[factorIndex], "factors:", factorOffactorArr)
            factorOffactor(factorOffactorArr)
# something worth adding: each callback should increase indent
# also, it's not exactly right

findfactor(x)
