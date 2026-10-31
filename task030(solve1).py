import sys


def DETERMINATION_OF_THE_POWER_OF_TWO(N):
    K=0
    while 2**K<N:
        K+=1
    return 2**K



def BUILDING_A_BINARY_TREE(A,pos,B,N):
    K = DETERMINATION_OF_THE_POWER_OF_TWO(N)
    BINARY_TREE_1 = [0]*(K-N) + A[::-1]
    cursor = 0
    while cursor+1<len(BINARY_TREE_1):
        actual_1, actual_2 = BINARY_TREE_1[cursor], BINARY_TREE_1[cursor+1]
        BINARY_TREE_1.append(max(actual_1, actual_2))
        cursor += 2
    BINARY_TREE_1.reverse()
    A_NEW = A.copy()

    A_NEW[pos] = B
    BINARY_TREE_2 = [0]*(K-N) + A_NEW[::-1]
    cursor = 0
    while cursor+1<len(BINARY_TREE_2):
        now1, now2 = BINARY_TREE_2[cursor], BINARY_TREE_2[cursor+1]
        BINARY_TREE_2.append(max(now1, now2))
        cursor += 2
    BINARY_TREE_2.reverse()

    out1 = " ".join(str(int(x)) for x in BINARY_TREE_1)
    out2 = " ".join(str(int(x)) for x in BINARY_TREE_2)

    print(out1 + ' ')
    print(out2, end=" ")


def main():
    ENTRY = sys.stdin.read().split()
    cursor = 0
    N = int(ENTRY[cursor]); cursor += 1
    A = [int(x) for x in ENTRY[cursor:cursor + N]]; cursor += N
    pos, B = int(ENTRY[cursor]), int(ENTRY[cursor + 1])
    BUILDING_A_BINARY_TREE(A,pos,B,N)


if __name__ == '__main__':
    main()
