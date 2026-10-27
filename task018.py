import sys
def VIKA(T,W,S,N):
    L=1
    R = S+10**60
    while L<=R:
        SS=0
        M = (L+R)//2
        for i in range(0,len(T)):
            SS+=M//T[i]*W[i]
        if SS>=S:
            TT=M
            R=M-1
        else:
            L = M+1
    QQ=0

    for p in range(0,len(T)):
        if T[p]>TT:
            QQ+=W[p]
        elif T[p]<TT and TT%T[p]!=0:
            #if TT%T[p]!=0:
            QQ+=(TT//T[p]+1)*W[p]
        elif T[p] < TT and TT%T[p]==0 :
            QQ+=(TT//T[p]*W[p])
        elif T[p] == TT:
            QQ+=W[p]

    return QQ
def gr():
    V = sys.stdin.read().split()
    u=0
    so=[]
    N = int(V[u]); u+=1
    S = int(V[u]); u+=1
    T=[]; W=[]
    #print(V)
    for _ in range(N):
        T.append(int(V[u])); u+=1
        W.append(int(V[u])); u+=1
    so=[]
    so.append(str(VIKA(T, W, S, N)))
    sys.stdout.write(" ".join(so)+'\n')
if __name__ == '__main__':
    gr()

