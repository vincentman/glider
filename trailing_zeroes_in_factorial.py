def solution(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
    reverse_string = str(fact)[::-1]
    print(reverse_string)
    for i, char in enumerate(reverse_string):
        if char != '0':
            return i
    return 0

# print(solution(20))
print(solution(int('9')))