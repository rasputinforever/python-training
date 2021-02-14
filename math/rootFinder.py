# FIRST: Takes in a user-input value and returns IF a number is prime
# IF NOT PRIME: returns all ROOTs

x = input("What number would you like to find all roots?")

rootArr = []

def findRoot(x):
    for i in range(int(x)):
        if (int(x) % (int(x) - i)) == 0:
            rootArr.append(int(x) - i)
    if len(rootArr) > 2:
        print(x, "is NOT a prime")
        print("divisors", rootArr)
    else:
        print(x, 'IS a prime!')
    
findRoot(x)