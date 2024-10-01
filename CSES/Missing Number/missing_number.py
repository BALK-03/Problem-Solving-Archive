# Main idea is to use the formula
# 1+ 2+ ... + n = n * (n + 1) / 2
# We look for k:
# k = n(n+1)/2 - (1+ 2+...+ k-1+ (k+1)+...+ n)

n = int(input())
line = input()

str_num = line.split(' ')
total = sum([int(val) for val in str_num])

output = n*(n+1)/2 - total
print(int(output))