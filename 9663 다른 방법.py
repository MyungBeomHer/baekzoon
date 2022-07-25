N = int(input())

def check(row):
    for i in range(row):
        if arr[row] == arr[i] or abs(arr[row] - arr[i]) == row - i:
            return False
    return True

def dfs(row):
    global ans
    #마지막까지 왔다는 것은 된다는 것을 의미
    if row == N:
        result +=1
    else:
        for i in range(N):
            arr[row] = i
            if check(row):
                dfs(row + 1)



arr = [0] * N
ans = 0
dfs(0)
print(ans)

