import sys
def STEREOMETRIA(N,A):
    A = A[::-1]
    ml = 0
    ks = 0
    for i in range(0, N):
        if i <= ml:
            ks += 1

        ml = max(i + A[i], ml)
    ks-=1
    return len(A)-ks



def gr():
    V = sys.stdin.read().split()
    N = int(V[0])
    u=1
    so=[]
    A = [int(x) for x in V[u:u+N]]
    OT = STEREOMETRIA(N,A)
    so.append(str(OT))
    sys.stdout.write(' '.join(so)+'\n')


if __name__=='__main__':
    gr()




