for tc in range(int(input())): #이렇게 input으로 몇번 반복하는지 알 수 있음 
    n,m = map(int,input().split()) #n 행 ,m 은 열
    array = list(map(int,input().split()))

    # 한 줄로 리스트 입력을 받은 후  행렬 만들기
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1,m): # 1번 열부터 시작
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0 : left_up = 0
            else : left_up = dp[i-1][j-1]
            #왼쪽 아래에서 오는 경우
            if i == n - 1 : left_down = 0
            else: left_down = dp[i + 1][j - 1]
            #왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)

    result  = 0
    for i in range(n):
        result = max(result,dp[i][m-1])

    print(result)





