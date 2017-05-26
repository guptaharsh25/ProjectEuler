#Project Euler Problem 2

arr = []
arr.append(1)
arr.append(2)

i = 0

whatIsSum = 2

while arr[i+1] < 4000000:
    arr.append(arr[i] + arr[i+1])

    if arr[i+2] % 2 == 0:
        whatIsSum += arr[i+2]

    i += 1

print(whatIsSum)
