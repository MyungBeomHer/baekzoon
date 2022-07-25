n = int(input())
data = list(map(int,input().split()))


def nextSqure(a,b):
    sqrt = (a*b) ** (1/2)

    if sqrt % 1 == 0:
        return True
    return False


for i in range(n-1):
	end = i + 1 #end는 i보다 뒤에 나와야된다.
	while end < n :
		if nextSqure(data[i],data[end]) == True:
			data[i],data[end] = data[end],data[i] #swap
			break
		end += 1
#탐색
def bool_search(datas):
	for i in range(len(datas)-1):
		if datas[i] > datas[i+1]:
			return "NO"
	return "YES"

print(bool_search(data))


