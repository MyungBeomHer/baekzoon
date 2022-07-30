
N = int(input())
count = 0
for i in range(1,N+1):

    if i < 100:
        count +=1
    elif i >= 101:
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            count +=1
print(count)

