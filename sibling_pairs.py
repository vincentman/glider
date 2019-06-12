from itertools import combinations


def create_dict(array):
    idx_array = {}
    for i, integer in enumerate(array):
        idx_array[i + 1] = list(range(1, integer + 1))
    return idx_array


def solve(array, n):
    # Write your code here
    idx_array = create_dict(array)
    com_list = list(combinations(range(1, n + 1), 2))
    count = 0
    for i, j in com_list:
        # print('i:', i, ', idx_array[j]:', idx_array[j], ', j:', j, ', idx_array[i]:', idx_array[i])
        if i in idx_array[j] and j in idx_array[i]:
            count += 1
            # print('count:', count)
    print(count)


def limit_max(k):
    return int(k) if int(k) <= 100000 else 100000


# n = int('10')
# array = list(map(limit_max,
#                  '1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000'.split(
#                      ' ')))
n = int('8')
array = list(map(int, '7 2 6 6 5 1 4 9'.split(' ')))
solve(array, n)
