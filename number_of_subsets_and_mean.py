from itertools import combinations

n = 5
input_string = '3 4 2 3 4'
# input = '3 1 2 3 4'

max_means = []
min_means = []
means = []
for i in range(1, n+1):
    com_str_list = list(combinations(input_string.split(), i))
    com_int_list = [list(map(int, i)) for i in com_str_list]
    # print('com_int_list:\n', com_int_list)
    for j in com_int_list:
        mean = sum(j)/len(j)
        mean %= (10^9+7)
        means.append(mean)
# print('means:\n', means)
reverse_sorted_means = sorted(means, reverse=True)
sorted_means = sorted(means, reverse=False)

# print('reverse_sorted_means:', reverse_sorted_means)
# print('sorted_means:', sorted_means)

count_max = 1
for i in range(1, len(reverse_sorted_means)):
    if reverse_sorted_means[i] != reverse_sorted_means[0]:
        count_max = i
        break

count_min = 1
for i in range(1, len(sorted_means)):
    if sorted_means[i] != sorted_means[0]:
        count_min = i
        break

print(count_max, count_min)
