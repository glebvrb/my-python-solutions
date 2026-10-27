import sys

def NA(A,N,D):
    A = [0]+A
    B = [0] * N
    for i in range(1, len(A)):
        B[i] = B[i-1] + A[i]
    R=1
    k=0
    for L in range(0, N-1):
        while R<N and B[R]-B[L]<D:
            R+=1
        if R==N:
            break
        k+=N-R
    return k

def gr():
    V = sys.stdin.read().split()
    u=0
    N = int(V[0]); u+=1; D = int(V[u]); u+=1
    A = [int(x) for x in V[u:u+N-1]]
    so=[]
    so.append(str(NA(A,N,D)))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()




