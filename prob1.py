#Project Euler Problem 1


whatIsSum = 0

for i in range(3,1000):
    if i % 3 == 0:
        whatIsSum += i
    elif i % 5 == 0:
        whatIsSum += i

print(whatIsSum)
