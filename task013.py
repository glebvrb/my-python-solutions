import sys
def NA(N):
    w=0
    L = N; R = 10**60
    while L<=R:
        M = (L+R)//2
        if M//17+M//13-M//221 == M-N:
            W=M; R = M-1
        elif M//17+M//13-M//221 < M-N:
            R = M-1
        else:
            L = M+1
    return W
def gr():
    N = int(sys.stdin.readline())
    so=[]
    so.append(str(NA(N)))
    sys.stdout.write(' '.join(so)+'\n')
if __name__ == '__main__':
    gr()



