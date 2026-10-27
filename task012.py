import sys
def BP(X,Y,N):
    L,R,ot = 0,2*10**8+50000,0
    while L<=R:
        M = (L+R)//2
        Q = M//X+M//Y
        if Q>=N:
            R = M-1; ot=M
        else:
            L = M + 1
    return ot


def gr():
    so=[]
    V = sys.stdin.read().split()
    u=0
    N = int(V[u]); u+=1
    X = int(V[u]); u+=1
    Y = int(V[u]); u+=1
    w0 = min(X,Y)
    so.append(str(w0+BP(X,Y,N-1)))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()




