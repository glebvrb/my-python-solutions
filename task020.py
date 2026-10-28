import sys
def LOVE(Q,N):
    #A = [0, 1, 0, 1, 3, 5, 4, 1, 2, 7]
    N = len(Q)
    W = [0] * (N + 1)
    for i in range(N):
        n = i + 1
        s = Q[i]
        W[n] = W[s]
        W[s] = n
    nn = 0
    WW = []
    for t in range(0, len(W)):
        WW.append(W[nn])
        nn = W[nn]
    return WW


def gr():
    V = sys.stdin.read().split()
    u=0
    N = int(V[0]); u+=1
    Q = [int(x) for x in V[u:u+N]]
    so=LOVE(Q,N)
    print(*so[0:-1])
    #sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()
