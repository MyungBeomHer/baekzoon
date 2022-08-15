N = int(input())

cost = 1000 - N

number = 0
for i in [500,100,50,10,5,1]:
    number += cost // i
    cost = cost % i

print(number)
