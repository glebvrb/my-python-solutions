import sys


def heap_sifting_up(heap):
    for element in range((len(heap)-1)//2,0,-1):
        main_check = False
        current = element
        while not main_check and current * 2 < len(heap):
            index_need_son = current * 2
            if index_need_son + 1 < len(heap):
                if heap[index_need_son + 1] < heap[index_need_son]:
                    index_need_son = index_need_son + 1
            if heap[current] <= heap[index_need_son]:
                main_check = True
            else:
                heap[index_need_son], heap[current] = heap[current], heap[index_need_son]
                current = index_need_son
    return heap


def heap_sifting_down(heap):
    first = heap[1]
    heap[1] = heap.pop()
    i=1
    main_check = False
    while not main_check and i * 2 < len(heap):
        index_down = i * 2
        if index_down + 1 < len(heap):
            if heap[index_down + 1] < heap[index_down]:
                index_down = index_down + 1
        if heap[i] <= heap[index_down]:
            main_check = True
        else:
            heap[i], heap[index_down] = heap[index_down], heap[i]
            i = index_down
    return first, heap


def get_up(heap):
    idx_last = len(heap) - 1
    while idx_last > 1:
        last_element = heap[idx_last]
        if heap[idx_last//2] > heap[idx_last]:
            heap[idx_last] = heap[idx_last//2]
            heap[idx_last//2] = last_element
            idx_last = idx_last//2
        else:
            break
    return heap


def determination_of_the_minimum_amount(N,heap):
    cnt=0
    heap = heap_sifting_up(heap)
    while len(heap)>=4:
        A, heap = heap_sifting_down(heap)
        B, heap = heap_sifting_down(heap)
        S = A + B
        cnt += S
        heap.append(S)
        heap = get_up(heap)
    cnt += heap[1]
    cnt += heap[2]
    return cnt




def main():
    enter = sys.stdin.read().split()
    N = int(enter[0])
    heap = ['0'] + [int(x) for x in enter[1:]]
    print(determination_of_the_minimum_amount(N,heap))


if __name__ == '__main__':
    main()







