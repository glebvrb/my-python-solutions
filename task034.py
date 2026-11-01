import sys


def calculate_the_area(H,N):
    stack = []
    left_edge = [0]*(N+1)
    right_edge = [0] * (N+1)
    for i in range(0,N):
        while stack and H[stack[-1]] >= H[i]:
                stack.pop()
        if not stack:
            left_edge[i] = 1
            stack.append(i)
        else:
            left_edge[i] = stack[-1]+2
            stack.append(i)
    stack = []
    for i in range(N-1,-1,-1):
        while stack and H[stack[-1]] >= H[i]:
            stack.pop()
        if not stack:
            right_edge[i] = N
            stack.append(i)
        else:
            right_edge[i] = stack[-1]
            stack.append(i)
    areas = []
    for i in range(0,len(left_edge)-1):
        areas.append((right_edge[i]-left_edge[i]+1) * (H[i]))
    return max(areas)


def solve():
    enter = sys.stdin.read().split()
    N = int(enter[0])
    H = [int(x) for x in enter[1:] ]
    print(calculate_the_area(H,N))


if __name__ == "__main__":
    solve()
