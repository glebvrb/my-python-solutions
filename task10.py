import sys
def BPL(A,a):
    L,R,ot = 0, len(A)-1, 0
    while L<=R:
        M = (L+R)//2
        if A[M] == a:
            ot = L = M+1
        elif A[M] > a:
            R = M - 1
        else:
            L = M + 1
    return ot
def BPF(A,a):
    L,R,ot = 0,len(A)-1,0
    while L<=R:
        M = (L+R)//2
        if A[M]==a:
            ot,R = M+1, M-1
        elif A[M]>a:
            R = M-1
        else:
            L = M + 1
    return ot
def gr():
    VD = sys.stdin.read().split()
    so=[]
    u=0
    N = int(VD[u]); u+=1
    A = [int(x) for x in VD[u:u+N]]; u+=N; M = int(VD[u]); u+=1
    B = [int(x) for x in VD[u:u+M]]
    for p in range(0,M):
        so.append(str((BPL(A,B[p])+BPF(A, B[p]))//2))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()


