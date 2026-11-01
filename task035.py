import sys


def decoding(S):
    stack = [S[0]]
    for i in range(1,len(S)):
        if not stack:
            stack.append(S[i])
        elif stack[-1] != S[i]:
            stack.append(S[i])
        else:
            stack.pop()
    return ''.join(stack)


def solve():
    enter = str(sys.stdin.readline().strip())
    S = [str(x) for x in enter]
    print(decoding(S))


if __name__ == "__main__":
    solve()
