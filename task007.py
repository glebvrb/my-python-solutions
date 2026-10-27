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
if len(w)<2 or( len(w)==2 and w[0]+2!=w[1]):
    print('empty')
ws = set(w)
if len(w)!=0:
    for p in w:
        if p+2 in ws:
            print(p,p+2)
