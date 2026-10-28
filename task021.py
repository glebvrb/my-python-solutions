import sys
def LOVE(Q,N):
    N = len(Q)
    W = [0] * (N + 1)  # за перед
    Z = [0] * (N + 1)
    sk = 0
    for i in range(N):
        if Q[i] >= 0:
            sk += 1
            n = sk
            s = Q[i]
            q = W[s]
            W[n] = q

            Z[n] = s
            W[s] = n
            if q != 0:
                Z[q] = n
        else:
            n = abs(Q[i])
            sz = W[n]  # за ним
            sp = Z[n]
            W[sp] = sz
            if sz != 0:
                Z[sz] = sp

    WW = []
    nn=W[0]
    while nn!=0:
        WW.append(nn)
        nn = W[nn]
    if not WW:
        return [0]
    return WW
def gr():
    V = sys.stdin.read().split()
    u=0
    N = int(V[0]); u+=1
    Q = [int(x) for x in V[u:u+N]]
    so=LOVE(Q,N)
    print(*so)
    #sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()


# A = [0, 1, 0, 1, 3, 5, 4, 1, 2, 7]


