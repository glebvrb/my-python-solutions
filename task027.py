import sys


N = int(sys.stdin.readline())


def CREATING_THE_CORRECT_SEQUENCE(N):
    set_of_visited = {1}
    final_list = [1]
    indicator = 0

    while indicator < len(final_list):
        current = final_list[indicator]
        indicator += 1
        for e in (2, 3, 5):
            nxt = current * e
            if nxt not in set_of_visited and nxt <= N:
                set_of_visited.add(nxt)
                final_list.append(nxt)
    print(*final_list)


if __name__ == '__main__':
    CREATING_THE_CORRECT_SEQUENCE(N)