import sys
import math
N=int(sys.stdin.readline())
e=[]
w=1
d=2
while d**3<=N:
    if N%d==0:
        while N%d==0:
            N//=d
            e.append(d)
    d+=1
r=int(N**0.5)
for i in range(r-1,r+2):
    if i**2==N:
        e.append(i)
        e.append(i)
t=set(e)
t=(sorted(t)[::-1])
for p in t:
    if e.count(p)>=2 :
        if e.count(p)%2==0:
            w*=p**(e.count(p))
        if e.count(p)%2!=0:
            w*=p**(e.count(p)-1)
print(w)
