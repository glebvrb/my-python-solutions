import sys

def DETERMINATION_OF_THE_POWER_OF_TWO(N):
    K=1
    while K<N:
        K*=2
    return K


def solve2():
    ENTER = sys.stdin.read().split()
    cursor = 0
    N = int(ENTER[cursor]); cursor += 1
    A = [int(x) for x in ENTER[cursor:cursor+N]]; cursor += N
    pos = int(ENTER[cursor]); cursor += 1
    B = int(ENTER[cursor])
    K = DETERMINATION_OF_THE_POWER_OF_TWO(N)
    BINARY_TREE_1 = [0] * (2*K)
    for i in range(N):
        BINARY_TREE_1[K+i] = A[i]
    for j in range(K-1,0,-1):
        BINARY_TREE_1[j] = max(BINARY_TREE_1[j*2], BINARY_TREE_1[j*2+1])
    print(' '.join(str(x) for x in BINARY_TREE_1[1:])+' ')
    correct_pos = pos+K
    BINARY_TREE_1[correct_pos] = B
    correct_pos //= 2
    while correct_pos > 0:
        BINARY_TREE_1[correct_pos] = max(BINARY_TREE_1[correct_pos*2], BINARY_TREE_1[correct_pos*2+1])
        correct_pos //= 2
    print(' '.join(str(x) for x in BINARY_TREE_1[1:]) + ' ')



if __name__ == "__main__":
    solve2()

