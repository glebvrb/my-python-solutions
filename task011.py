# put your python code here
import sys
def BP(E,K):
    N = len(E)
    L,R,ot = 1,10**7+50000,0
    while L<=R:
        k=0
        T = (L+R)//2
        for p in E:
            k+=p//T
        if k>=K:
            ot=T; L = T+1
        else:
            R = T-1
    return ot


def gr():
    so=[]
    V = sys.stdin.read().split()
    u=0
    N = int(V[u]); u+=1
    K = int(V[u]); u+=1
    L = [int(x) for x in V[u:u+N]]
    so.append(str(BP(L,K)))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()



