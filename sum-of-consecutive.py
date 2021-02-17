def solution(N):
    count = 0
    n = 2    #needs 2+ consecutive numbers
    while 2*N + n-n**2 > 0:
        a = (2*N + n-n**2) / (2*n)
        if a - int(a)==0:
            print(a, n) #start of consec num and num of consec. nums to cross verify
            count += 1
        n+=1
    return count
print("number of ways to reach 100 is %d "%solution(100))
