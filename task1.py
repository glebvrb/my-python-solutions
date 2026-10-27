def f(a):
    e=[]
    while a%2==0:
        e.append(2)
        a//=2
    d=3
    while d*d<=a:
        while a%d==0:
            e.append(d)
            a//=d
        d+=1
    if a>1:
        e.append(a)
    return e
N=int(input())
v=f(N)
m=0
for e in v:
    if v.count(e)>m:
        m=v.count(e)
print(m)