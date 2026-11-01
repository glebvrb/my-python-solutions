import sys
from collections import deque


def determination_of_book_number(N,P):
    queue = deque()
    list_of_deleted_items = []
    number_of_book = 1
    for operation in P:
        if operation == 1:
            queue.appendleft(number_of_book)
            number_of_book += 1
        elif operation == 2:
            queue.append(number_of_book)
            number_of_book += 1
        elif operation == 3:
            if queue:
                list_of_deleted_items.append(queue.popleft())
            else:
                list_of_deleted_items.append(-1)
        else:
            if queue:
                list_of_deleted_items.append(queue.pop())
            else:
                list_of_deleted_items.append(-1)
    return list_of_deleted_items


def main():
    enter = sys.stdin.read().split()
    N = int(enter[0])
    P = [int(x) for x in enter[1:]]
    print(*determination_of_book_number(N,P))


if __name__ == "__main__":
    main()