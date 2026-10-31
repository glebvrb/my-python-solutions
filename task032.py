import sys


def remove_max_element(N,heap):
    for n in range(N-1):
        heap = remove_element(heap)


def solve():
    data_enter = sys.stdin.read().split()
    N = int(data_enter[0])
    heap = [' ']+[int(x) for x in data_enter[1:]]
    remove_max_element(N,heap)


def remove_element(heap):
    result = heap[1]
    heap[1] = heap.pop()
    i = 1
    main_check = False
    while not main_check and 2*i < len(heap):
        index_of_needed_child = 2*i
        if 2*i+1 < len(heap):
            if heap[index_of_needed_child+1] > heap[index_of_needed_child]:
                index_of_needed_child = index_of_needed_child + 1
        if heap[index_of_needed_child] <= heap[i]:
            main_check = True
        else:
            heap[index_of_needed_child], heap[i] = heap[i], heap[index_of_needed_child]
            i = index_of_needed_child
    answer = [i, result]
    print(*answer)
    return heap


if __name__ == '__main__':
    solve()



