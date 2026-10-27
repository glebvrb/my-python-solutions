import sys
def VIKA(ND,D,N):
    q1=[]
    # if N==2:
    #     if ND[0] == D:
    #         q1.append(1); q1.append(2)
    #         return q1

    B = [0] * (len(ND) + 1)
    for i in range(1, len(B)):
        B[i] = B[i - 1] + ND[i - 1]

    R = 1
    for L in range(0, len(B) - 1):
        while R <= len(B) - 1:
            if B[R] - B[L] == D:
                w1 = L + 1
                w2 = R + 1
                q1.append(w1)
                q1.append(w2)
                return q1

            if R == N or B[R] - B[L] > D:
                break
            R += 1

def gr():
    V = sys.stdin.read().split()
    u=0
    N = int(V[u]); u+=1
    D = int(V[u]); u+=1
    ND = [int(x) for x in V[u:u+N-1]]
    so=[]
    w1=VIKA(ND,D,N)
    so.append(str(w1[0])); so.append(str(w1[1]))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()
# #




