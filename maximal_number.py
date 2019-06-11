string = '132'
print('original string:', string)

int_list = [int(c) for c in string]
print('integer list:', int_list)

sorted_list = []
while len(int_list)!=0:
    sorted_list.append(int_list.pop(int_list.index(max(int_list))))
print('sorted integers:', sorted_list)

print(''.join('%s' % i for i in sorted_list))