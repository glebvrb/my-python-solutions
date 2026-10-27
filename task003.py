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
        d+=2
    if a>1:
        e.append(a)
    return e
N=int(input())
v=f(N)
m=v[-1]
print(v.count(m))


