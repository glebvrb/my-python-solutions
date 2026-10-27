import sys

def NA(A,N,D):
    L=0
    k=0
    R = N - 1
    while L<=R:
        if A[R]+A[L]<=D:
            R-=1; L+=1; k+=1
        elif A[R]+A[L]>D:
            k+=1; R-=1
        #else:
    return k



def gr():
    V = sys.stdin.read().split()
    u=0
    N = int(V[0]); u+=1; D = int(V[u]); u+=1
    A = [int(x) for x in V[u:u+N]]
    so=[]
    so.append(str(NA(A,N,D)))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()
