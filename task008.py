n=10**6
pk = [True]*(n+1)
d=2
while d*d<=n:
    if pk[d]:
        for i in range(d*d, n+1, d):
            pk[i]=False
    d+=1
L,R = map(int, input().split())
for i in range(L,R+1):
    if pk[i]:
        print(i, end=' ')
    else:
        d=2
        while d*d<=i:
            if i%d==0:
                print(d, end=' ')
                break
            d+=1
