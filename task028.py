import sys


N = int(sys.stdin.readline())


def OUTPUT_OF_ANCESTORS(N):
    almost_the_final_list = [1]
    final_list = [-1]*N
    visited = {1}
    pointer = 0
    while pointer < len(almost_the_final_list):
        actual = almost_the_final_list[pointer]
        pointer += 1
        for e in (2, 3, 5):
            nxt = (e * actual) % N
            if nxt not in visited:
                visited.add(nxt)
                almost_the_final_list.append(nxt)
                final_list[nxt] = actual
    print(*(final_list[i] for i in range(N)))


if __name__ == "__main__":
    OUTPUT_OF_ANCESTORS(N)
