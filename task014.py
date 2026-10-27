import sys
def NA(M,NI):
    ww=0
    L=min(NI)
    R = max(NI)+M
    while L<=R:
        s=0
        E = (L + R) // 2
        for p in NI:
            s+=max(0,E-p)
        if s>M:
            R = E-1
        elif s <= M:
            ww=E; L = E+1
    return ww
def gr():
    so=[]
    V = sys.stdin.read().split()
    u=0
    N = int(V[u]); u+=1
    NI = [int(x) for x in V[u:u+N]]; u+=N
    M = int(V[u])
    so.append(str(NA(M,NI)))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()



