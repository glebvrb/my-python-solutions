N = int(input())
d=2
while d*d<=N and d<=10**6:
    if N%d==0:
        while N%d==0:
            N//=d
    d+=1
print(N)
