import sys
from collections import deque


def SEARCHING_FOR_THE_MINIMUM_NUMBER_OF_KAYAKS(N, D, A):
    queue = deque(A)
    cnt = 0
    while queue:
        if len(queue) == 1:
            cnt += 1
            queue.pop()
            break
        if queue[0] + queue[-1] <= D:
            queue.popleft()
        cnt += 1
        queue.pop()
    print(cnt)


def main():
    INPUT = sys.stdin.read().split()
    cursor = 0
    N = int(INPUT[cursor]); cursor += 1
    D = int(INPUT[cursor]); cursor += 1
    A = [int(x) for x in INPUT[cursor:]]
    SEARCHING_FOR_THE_MINIMUM_NUMBER_OF_KAYAKS(N, D, A)


if __name__ == '__main__':
    main()