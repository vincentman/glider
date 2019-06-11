n = 8
# string = 'aaabbbcd'
string = 'sxkalxjiqowwrytghjbczm'

for i, char in enumerate(string):
    count = 0
    keep_array = list(string)
    keep_array.pop(i)
    for j in keep_array:
        if j > char:
            count += 1
    print(count)
