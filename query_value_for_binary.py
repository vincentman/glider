'''
https://app.glider.ai/practice/problem/basic-programming/queries-for-decimal-values-of-binary-subarrays/problem
'''


n = 4
q = 1
arr = [1, 0, 0, 0]
lr = [(0, 3)]
# n = 5
# q = 2
# arr = [1, 0, 1, 1, 0]
# lr = [(0, 2), (2, 4)]


def solution(arr, l, r, n):
    string = ''.join(map(str, arr[l:r+1]))
    return int(string, 2)


for i in range(len(lr)):
    l, r = lr[i]
    print(solution(arr, l, r, n))