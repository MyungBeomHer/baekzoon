def DP(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return DP(n - 1) + DP(n - 2) + DP(n - 3)

for _ in range(int(input())):
    print(DP(int(input())))
