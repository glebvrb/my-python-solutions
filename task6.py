n=10**6
pk = [True]*(n+1)
d=2
while d*d<=n:
    if pk[d]:
        for i in range(d*d, n+1, d):
            pk[i]=False
    d+=1
L,R = map(int, input().split())
w=[]
for i in range(L,R+1):
    if pk[i]==True:
        w.append(i)

if len(w)==0:
    print('empty')
else:
    print(*w)