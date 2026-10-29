import sys


def RUBIC_CUBE(A,N):
    A = [0] + A
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    stack = []
    for i in range(1,N+1):
        while stack and A[stack[-1]] > A[i]:
            stack.pop()
        if not stack:
            L[i] = 1
        else:
            L[i] = stack[-1] + 1
        stack.append(i)
    stack = []
    for i in range(N,0,-1):
        while stack and A[stack[-1]] > A[i]:
            stack.pop()
        if not stack:
            R[i] = N
        else:
            R[i] = stack[-1] - 1
        stack.append(i)
    for i in range(1,N+1):
        print(L[i],R[i])


def gr():
    V = sys.stdin.read().split()
    N = int(V[0])
    A = [int(x) for x in V[1:]]
    RUBIC_CUBE(A,N)


if __name__ == '__main__':
    gr()