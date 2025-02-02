def solution():
    INF = int(1e9)
    n, m = map(int, input().split(" "))
    board = [[INF] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input().split(" "))
        board[s][e] = 1
    for i in range(1, n+1):
        board[i][i] = 0
    
    for k in range(1, n+1): 
        for i in range(1, n+1): 
            for j in range(1, n+1):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
    
    result = 0 
    print(board)
    for i in range(1, n+1): 
        cnt = 0
        for j in range(1, n+1):
            if(board[i][j] != INF or  board[j][i] != INF) :
                cnt += 1
        if cnt == n :
            result += 1 
    return result

print(solution())
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
''' 
