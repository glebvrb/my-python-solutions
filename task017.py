import sys
def SPO(y,D,S,A,B):
    N = len(B)
    NAS=D/y
    V=NAS
    if V<=S:
        return 0
    L = 0
    fine = 0
    R = len(A) - 1
    while L <= R:
        M = (L + R) // 2
        if M == len(A) - 1:
            fine = B[-1]
            break
        if A[M] == V:
            fine = B[M]
            break
        elif A[M] < V:
            if A[M + 1] >= V:
                fine = B[M + 1]
                break
            else:
                L = M + 1
        else:
            if A[M - 1] < V:
                fine = B[M]
                break
            else:
                R = M - 1
    return fine


def gr():
    V = sys.stdin.read().split()
    u=0
    N = int(V[u]); u+=1
    M = int(V[u]); u+=1
    D = int(V[u]); u+=1
    S = int(V[u]); u+=1
    A = [int(x)+S for x in V[u:u+N-1]]; u+=N-1
    B = [int(x) for x in V[u:u+N]]; u+=N
    MA = [int(x) for x in V[u:u+M]]
    so=[]
    for y in MA:
        so.append(str(SPO(y,D,S,A,B)))
    sys.stdout.write(" ".join(so)+'\n')
if __name__ == '__main__':
    gr()

