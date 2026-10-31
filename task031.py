import sys


def creating_tree(N, A):
    tree = [0] * (2 ** 20 + 5)
    list_of_answers = []
    index_dict = {}
    for element in A:
        cursor = 1
        while cursor in index_dict:
            if element > index_dict[cursor]:
                cursor = cursor * 2 + 1
            else:
                cursor = cursor * 2
        index_dict[cursor] = element
        list_of_answers.append(cursor)


    last_list = [str(x) for x in list_of_answers] + [' ']
    print(' '.join(last_list))


def solve():
    data_enter = sys.stdin.read().split()
    N = int(data_enter[0])
    A = [int(x) for x in data_enter[1:]]
    creating_tree(N, A)


if __name__ == '__main__':
    solve()
